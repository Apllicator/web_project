sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/apllicator/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/apllicator/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
