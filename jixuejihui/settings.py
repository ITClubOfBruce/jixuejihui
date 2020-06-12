import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mjlrn&jv&-&yttxncqf7e9c)+ldr@0w(d5vvv7msm%v@c2-w01'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'course',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'corsheaders',
    'captcha'
]
# 使用自定义的user类
AUTH_USER_MODEL = 'users.UserProfile'
# 自定义可以通过 邮箱或（or）mobile登录
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CORS
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:5500']  # 配置IP白名单
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
CORS_ORIGIN_ALLOW_ALL = False  # 不能允许所有的主机都可以请求你的API

ROOT_URLCONF = 'jixuejihui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jixuejihui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bwonline_db',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': '12345678',      #密码
        'HOST': '127.0.0.1',    #IP
        'PORT': '3306',                   #端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 25
EMAIL_HOST_USER  = "1046244623@qq.com"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
EMAIL_FROM = "1046244623@qq.com"








