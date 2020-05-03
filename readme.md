
# What is this?
These are a collection of scripts to easily setup a hosting enviroment for Wordpress. We intend to make the process more automated so that users do not need to copy or enter in commands. It's meant to make virtual private hosting not only more accessible to people, but also secure.

This script does the following:
* Disable Password Authentication and prefer SSH Key Authentication (optional, but strongly recommended)
* Installs nginx, PHP-FPM 7.4, and Mysql
* Configures nginx and PHP
* Creates the database for Wordpress
* Downloads and installs Wordpress
* Set up HTTPS via Lets Encrypt (optional)

## Server Requirements
* Ubuntu 20.04 or later
* Root Accesss
* SSH keys generated (strongly recommended)
