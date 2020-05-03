import os
import random

def generatepassword ():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        return password
    
if os.geteuid()==0:
  print("Running as root. Continuing")
else:
  print ("User is not root, aborting")
  exit()

domainName = ""
userName = ""
sqlpassword = generatepassword()

while len(domainName) == 0:
    domainName = input("Enter the domain name to your website: ")
while len(userName) == 0:
    userName = input("Enter a username: ")
    
print("Generating Config Files")

script_dir = os.path.dirname(os.path.realpath(__file__))
fin = open(os.path.join(script_dir, "configs/nginx.conf"), "rt")

data = fin.read()
data = data.replace('<targetusername>', userName)
fin.close()
fin = open(os.path.normpath("/etc/nginx/nginx.conf"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/www.conf"), "rt")

data = fin.read()
data = data.replace('<targetusername>', userName)
fin.close()
fin = open(os.path.normpath("/etc/php/7.4/fpm/pool.d/www.conf"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/vhostsample.conf"), "rt")

data = fin.read()
data = data.replace('<targetusername>', userName)
data = data.replace('<domain>', domainName)
fin.close()
fin = open(os.path.normpath("/etc/nginx/conf.d/" + domainName + ".conf"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/dbcreation.sql"), "rt")

data = fin.read()
data = data.replace('<password>', sqlpassword)
fin.close()
fin = open(os.path.join(script_dir, "dbcreation.sql"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/backupdatabase.sh"), "rt")

data = fin.read()
data = data.replace('<password>', sqlpassword)
data = data.replace('<username>', userName)
fin.close()
fin = open(os.path.join(script_dir, "backupdatabase.sh"), "wt")
fin.write(data)
fin.close()
os.chdir(script_dir)

print("Setting host nmae")
os.system("hostname " + domainName)

if os.path.exists():
    print("User Exists, skipping user creation")
else:
    print("Creating user " + userName)
    os.system("adduser " + userName)
    os.system("usermod -aG sudo " + userName)
    
print("Copying SSH Keys")
os.system("cp -R ~/.ssh /home/" + userName)
os.system("chown " + userName + ":" + userName + " .ssh -R")

print("Creating database for Wordpress")
print("Enter the root password for MySQL to continue.")
os.system("cat dbcreation.sql | mysql -u root -p")

print("Restarting Services")
os.system("service php7.4-fpm restart");
os.system("service nginx restart");

print("Downloading and installing Wordpress files")
os.system("wget https://wordpress.org/latest.zip");
os.system("unzip latest.zip")
os.system("mv wordpress /home/"+ userName + "/www")
os.system("chown " + userName + ":" + userName + " /home/" + userName + "/www -R")

print("Done. Set up WordPress and view your site at http://" + domainName)
print("Use the following database information to setup WordPress:")
print("Database: wordpress")
print("Database Username: wordpress")
print("Database Password: " + sqlpassword)

