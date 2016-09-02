FROM python:3-onbuild

RUN apt-get update
RUN apt-get -y install tor && \
    apt-get -y install proxychains && \
    apt-get -y install polipo

WORKDIR /usr/src/app/
RUN python setup.py install

ENV TARGET=google.com

CMD \
    service tor start && \
    service polipo start && \
    proxychains discosub run $TARGET
