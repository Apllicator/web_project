sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/wsgi.examle
sudo /etc/init.d/gunicorn restart
