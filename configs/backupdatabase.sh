#!/bin/bash
cd /home/<username>/backups
if [ ! -d wordpressbackups ]
then
mkdir -p wordpressbackups
fi

cd wordpressbackups

DATE=`date +%Y-%m-%d-%T`
mysqldump --max_allowed_packet=512M -u backupservice -p<password> wordpress | gzip > /home/<username>/backups/wordpressbackups/wordpress_$DATE.sql.gz