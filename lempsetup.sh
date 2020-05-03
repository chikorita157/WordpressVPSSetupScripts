#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "You must be root to run this script"
		exit 1
else
while true; do
    read -p "Disable Password Authentication and use SSH keys only to make your server more secure?" yn
    case $yn in
        [Yy]* ) echo "Disabling Password Authentication"; sudo grep -q "ChallengeResponseAuthentication" /etc/ssh/sshd_config && sed -i "/^[^#]*ChallengeResponseAuthentication[[:space:]]yes.*/c\ChallengeResponseAuthentication no" /etc/ssh/sshd_config || echo "ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config; sudo grep -q "^[^#]*PasswordAuthentication" /etc/ssh/sshd_config && sed -i "/^[^#]*PasswordAuthentication[[:space:]]yes/c\PasswordAuthentication no" /etc/ssh/sshd_config || echo "PasswordAuthentication no" >> /etc/ssh/sshd_config; sudo service ssh restart; break;;
        [Nn]* ) echo "Not disabling password authentication"; break;;
        * ) echo "Please answer yes or no.";;
    esac
done
	
	apt update
	echo "Installing required packages"
	apt install wget unzip -y
	echo "Setting up nginx"
	apt install nginx -y
	systemctl enable nginx
	service nginx start
	ufw allow 'Nginx Full'
	
	echo "Setting up MariaDB"
	apt install mysql-server -y
	sudo systemctl enable mysql
	service mysql start
	mysql_secure_installation
	
	echo "setting up PHP"
	apt install php-fpm php-mysql php-json php-gd php-xml php-mbstring tar curl -y
	systemctl enable php7.4-fpm
	service php7.4-fpm start
	
	echo "Restarting nginx"
	systemctl restart nginx
 
    echo "Running Post Setup"
    python3 ./postsetup.py
    
    while true; do
        read -p "Install SSL Certificates with Lets Encrypt to enable HTTPS support?" yn
        case $yn in
            [Yy]* ) echo 'export PATH=$PATH:/snap/bin' >> ~/.bashrc; snap install --beta --classic certbot; certbot --nginx; break;;
            [Nn]* ) break;;
            * ) echo "Please answer yes or no.";;
        esac
    done
	exit 0
fi
