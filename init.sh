sudo ln -s /home/box/web/etc/test.conf /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/test.conf /etc/nginx/sites-available/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
