FROM ubuntu:20.04

LABEL maintainer="kevincho9029@gmail.com"

RUN ln -s /usr/bin/* /usr/sbin/ -f

RUN mkdir paimon
WORKDIR /paimon
COPY main.py ./main.py
RUN chmod 774 main.py

RUN apt update
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN pip3 install genshinstats


ENV LTOKEN=yourLTOKEN
ENV LTUID=yourLTUID

ENTRYPOINT ["python3", "./main.py"]`

