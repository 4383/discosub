FROM python:3-onbuild

WORKDIR /usr/src/app/
RUN python setup.py install

ENV TARGET=google.com

RUN apt-get update
RUN apt-get -y install tor && \
    apt-get -y install proxychains && \
    apt-get -y install polipo

CMD \
    service tor start && \
    service polipo start && \
    proxychains discosub run $TARGET
