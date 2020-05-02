#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "You must be root to run this script"
		exit 1
else
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
	wget 
	sudo systemctl enable php-fpm
	systemctl start php-fpm
	
	echo "Restarting nginx"

	exit 0
fi