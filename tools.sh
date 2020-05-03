#!/bin/bash
    while true; do
        read -p “Select an option“ 12345
		echo “1. Install Lets Encrypt Certificates”
		echo “2. Renew all Lets Encrypt Certificates”
		echo “3. Backup Database”
        echo "4. Update wordpressvpssetup scripts"
		echo “5. Exit”
        case $12345 in
            [1]* ) echo 'export PATH=$PATH:/snap/bin' >> ~/.bashrc; snap install --beta --classic certbot; certbot --nginx; break;;
		    [2]* ) echo 'export PATH=$PATH:/snap/bin' >> ~/.bashrc; certbot renew; break;;
			[3]* ) chmod 755 backupdatabase.sh; ./backupdatabase.sh; break;;
            [3]* ) git pull; break;;
            [4]* ) break;;
            * ) echo "Please enter a valid option.”;;
        esac
    done
