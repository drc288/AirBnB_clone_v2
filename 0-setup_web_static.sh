#!/usr/bin/env bash
# This script configure the web static in the server, using nginx
# ###############################################################
# #                     Deply Web Static                        #
# ###############################################################
#
# First install nginx if not exists and update the sistem
sudo apt-get update -y
sudo apt-get install nginx -y
# Create the folder if not exists
# Dir 1
if [ ! -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/;
fi;
# Dir 2
if [ ! -d /data/web_static/shared/ ]; then
    sudo mkdir -p /data/web_statci/shared/;
fi;
# Create the file with the basic html
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# Create a symlink 
sudo ln -sfn /data/web_static/releases/test /data/web_static/current
# Set the user and group
sudo chown ubuntu. -R /data
# Update the data
sudo sed -i '35ilocation /hbnb_static/ {' /etc/nginx/sites-available/default
sudo sed -i '36ialias /data/web_static/current/;' /etc/nginx/sites-available/default
sudo sed -i '37iautoindex off;' /etc/nginx/sites-available/default
sudo sed -i '38i}' /etc/nginx/sites-available/default
# Restart the nginx
sudo service nginx restart
