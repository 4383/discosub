import configparser
import os.path


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOCAL_STORAGE_DIR = os.path.join(BASE_DIR, "../.microservice")
PROFIL = os.path.join(LOCAL_STORAGE_DIR, 'config')


def exist():
    if not os.path.isfile(PROFIL):
        print('Config unavailable...')
        return False
    return True


def load():
    if not exist():
        return
    profil = configparser.ConfigParser()
    profil.read(PROFIL)
    return profil
