FROM       ubuntu:20.04
MAINTAINER arknell@yonsei.ac.kr

# update pacakge
RUN apt update

# install python 3
RUN apt install -y python3
RUN apt install -y python3-pip

# install library
RUN pip3 install flask

# copy source
COPY . /usr/src/app

# move to source
WORKDIR /usr/src/app

# start server
EXPOSE 8998
CMD    nohup python3 serve.py > log 2>&1 &
