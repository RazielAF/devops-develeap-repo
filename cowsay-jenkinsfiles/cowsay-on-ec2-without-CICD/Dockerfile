FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update -y \
        && apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) \
       stable"
RUN apt-get update  -y && apt-get -y install docker-ce
RUN usermod -aG docker jenkins
ARG  HOST_DOCKER_GID
RUN  groupmod -g $HOST_DOCKER_GID docker
USER jenkins

