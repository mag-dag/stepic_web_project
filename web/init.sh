sudo ln -s /home/box/web/etc/test.conf /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/test.conf /etc/nginx/sites-available/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/defaul
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo cp /home/box/web/gunicorn-* /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start gunicorn-hello.service
sudo systemctl start gunicron-django.service
sudo systemctl status gunicorn-hello.service
sudo systemctl status gunicron-django.service
sudo /etc/init.d/mysql start
