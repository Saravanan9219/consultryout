FROM alpine:latest
ADD "https://releases.hashicorp.com/consul/1.0.2/consul_1.0.2_linux_amd64.zip" "/tmp/"
WORKDIR "/tmp/"
# install consul
RUN unzip ./consul_1.0.2_linux_amd64.zip; \
    mv consul /usr/local/bin
ENTRYPOINT ["/bin/sh"]
WORKDIR "/"
CMD ["-c", "/usr/local/bin/consul agent -server -data-dir=/tmp/consul -node=consul_server -enable-script-checks=true -bootstrap-expect=1 -client='{{ GetPrivateIPs }}' -dns-port=53"]
