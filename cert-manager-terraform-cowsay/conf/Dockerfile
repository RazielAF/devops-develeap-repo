FROM nginx:1.23.1
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./index.js /usr/share/nginx/html/index.js
COPY ./cert.pem /etc/nginx/ssl/cert.pem
COPY ./key_uncrypted.pem /etc/nginx/ssl/key.pem
RUN apt-get -y update 
RUN apt-get -y install python3 pip 
RUN pip3 install pip --upgrade
RUN pip3 install certbot-nginx
RUN apt-get -y install certbot