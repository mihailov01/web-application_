import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# CURRENT_USER='admin'   #  админ
# CURRENT_USER='ivan'  #  оператор
# CURRENT_USER='artem' #  пользователь
# CURRENT_USER='masha' #  пользователь
CURRENT_USER='lena'  #  пользователь

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
UPLOAD_FOLDER = "C:\\Users\\XayLoad\\PycharmProjects\\nikak\\app\\static"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

THREADS_PER_PAGE = 8

SQLALCHEMY_TRACK_MODIFICATIONS = False
