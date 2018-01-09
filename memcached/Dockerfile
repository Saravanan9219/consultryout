FROM memcached:alpine
ADD "https://releases.hashicorp.com/consul/1.0.2/consul_1.0.2_linux_amd64.zip" "/tmp/"
WORKDIR "/tmp/"
USER "root"
# install consul
RUN unzip ./consul_1.0.2_linux_amd64.zip; \
    mv consul /usr/local/bin
# create config files
RUN mkdir /etc/consul.d && \
    echo '{"service": {"name": "memcached", "port": 11211}}' \
    >> /etc/consul.d/memcached.json
     
RUN apk update
RUN apk add supervisor
COPY supervisord.conf /etc/
ENTRYPOINT ["supervisord"] 
CMD ["-n", "-c",  "/etc/supervisord.conf"]
