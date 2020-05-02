#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "You must be root to run this script"
		exit 1
else
	echo "Installing required packages"
	dnf install wget unzip -y
	echo "Setting up nginx"
	dnf install nginx -y
	systemctl enable nginx
	systemctl start nginx
	firewall-cmd --permanent --add-service=http
	firewall-cmd --permanent --zone=public --add-service=https
	firewall-cmd --reload
	
	echo "Setting up MariaDB"
	dnf install mariadb-server -y
	sudo systemctl enable mariadb
	systemctl start mariadb
	mysql_secure_installation
	
	echo "setting up PHP"
	dnf install php-fpm php-mysqlnd php-json php-gd php-xml php-mbstring tar curl -y
	wget https://raw.githubusercontent.com/chikorita157/WordpressVPSSetupScripts/master/www.conf?token=AABHLH37FBXZZ5DQYTJ7NBC6VXEGO
	mv www.conf /etc/php-fpm.d
	sudo systemctl enable php-fpm
	systemctl start php-fpm
	
	echo "Restarting nginx"

	exit 0
fi