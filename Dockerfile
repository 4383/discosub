FROM python:3-onbuild
WORKDIR /usr/src/app/
RUN python setup.py install
ENV TARGET=google.com
CMD discosub run $TARGET
