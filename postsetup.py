import os

if os.geteuid()==0:
  print("Running as root. Continuing")
else:
  print ()"User is not root, aborting")
  exit()

domainName = ""
userName = ""
sqlpassword = ""

while len(domainName) == 0:
    domainName = input("Enter the domain name to your website: ")
while len(userName) == 0:
    userName = input("Enter a username: ")
while len(sqlpassword) == 0:
    sqlpassword = input("Enter a secure database password: ")
    
print("Generating Config Files")

script_dir = os.path.dirname(os.path.realpath(__file__))
fin = open(os.path.join(script_dir, "configs/nginx.conf"), "rt")

data = fin.read()
data = data.replace('<targetusername>', userName)
fin.close()
fin = open(os.path.join(script_dir, "nginx.conf"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/www.conf"), "rt")

data = fin.read()
data = data.replace('<targetusername>', userName)
fin.close()
fin = open(os.path.join(script_dir, "www.conf"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/vhostsample.conf"), "rt")

data = fin.read()
data = data.replace('<targetusername>', userName)
data = data.replace('<domaib>', domainName)
fin.close()
fin = open(os.path.join(script_dir, domainName + ".conf"), "wt")
fin.write(data)
fin.close()

fin = open(os.path.join(script_dir, "configs/dbcreation.sql"), "rt")

data = fin.read()
data = data.replace('<password>', sqlpassword)
fin.close()
fin = open(os.path.join(script_dir, "dbcreation.sql"), "wt")
fin.write(data)
fin.close()

print("Creating user " + userName)
os.system("adduser" + userName)
os.system("cp -R ~/.ssh /home/" + userName)
os.system("chown " + userName + ":" + userName + " .ssh -R")
print("Copying configs")
os.system("cp " + script_dir + "nginx.conf /etc/nginx/");
os.system("cp " + script_dir + domainName + ".conf /etc/nginx/conf.d");
os.system("cp " + script_dir + "www.conf /etc/php/7.4/fpm/pool.d/conf.d");
print("Creating database for Wordpress")
os.system("mysql -u root –p < dbcreation.sql"
print("Restarting Services")
os.system("service php7.4-fpm restart");
os.system("service nginx restart");

os.system("wget https://wordpress.org/latest.zip");
os.system("unzip latest.zip")
os.system("mv wordpress /home/"+ userName + "/www")
os.system("chown " + userName + ":" + username + " /home/" + userName + "/www -R")
print("Done. View your site at http://" + domainName)
