##################################################################################
#  /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$  #
# | $$__  $$|_  $$_/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  | $$| $$__  $$ #
# | $$  \ $$  | $$  | $$  \__/| $$  \__/| $$  \ $$| $$  \__/| $$  | $$| $$  \ $$ #
# | $$  | $$  | $$  |  $$$$$$ | $$      | $$  | $$|  $$$$$$ | $$  | $$| $$$$$$$  #
# | $$  | $$  | $$   \____  $$| $$      | $$  | $$ \____  $$| $$  | $$| $$__  $$ #
# | $$  | $$  | $$   /$$  \ $$| $$   /$$| $$  | $$ /$$  \ $$| $$  | $$| $$  \ $$ #
# | $$$$$$$/ /$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$$/ #
# |_______/ |______/ \______/  \______/  \______/  \______/  \______/ |_______/  #
#                                                                                #
# discosub 0.3.0                                                                 #
# author: 4383 (Hervé Beraud)                                                    #
# url: https://github.com/4383/discosub                                          #
##################################################################################

FROM python:3-onbuild
WORKDIR /usr/src/app/
RUN python setup.py install
ENV TARGET=google.com
CMD discosub run $TARGET
