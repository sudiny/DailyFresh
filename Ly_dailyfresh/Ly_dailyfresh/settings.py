"""
Django settings for Ly_dailyfresh project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 加入系统的路径,可以不在使用ａｐｐｓ前缀
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=4-q245qjua+a6ido$9nvc50+hj99n(e(@s3px#lc3w-!o9gd9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 自定义模块
    'apps.user',
    'apps.goods',
    'apps.cart',
    'apps.order',
    # 注册富文本编辑器应用
    'tinymce',
    # 全文搜索框架
    'haystack',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Ly_dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Ly_dailyfresh.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',
        'HOST':'192.168.99.99',# 数据库在本地
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD':'root',

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

# 富文本编辑器的默认配置
TINYMCE_DEFAULT_CONFIG = {
    'theme':'advanced',
    'width':600,
    'height':400,
}

# 指定django 的默认使用的认证模型类
AUTH_USER_MODEL = 'user.User'

# 配置发送邮件的信息
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = '17611223926@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'liyi939250'
#收件人看到的发件人
EMAIL_FROM = 'liyi<17611223926@163.com>'

# 配置ｃａｃｈｅ缓存到ｒｅｄｉｓ的2号数据库
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.211.55.4:6379/2",
        "OPTIONS": {
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 配置session的存储到缓存中，即　使用的redis数据库
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 指定没有登录的时候默认请求路径，会将当前访问的路径存入next变量传入
LOGIN_URL = '/user/login'



# 使用分布式文件系统和nginx协同配置
# 指定Django上传文件的存储类
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FDFSStorage'
# 指定fdfs的客户端的配置文件的路径
FDFS_CLIENT_CONF = './utils/fdfs/client.conf'

# 指定fdfs 服务器 nginx服务的地址

FDFS_NGINX_URL = 'http://10.211.55.4:8888/'



# 全文检索框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 控制全文检索显示的条数
HAYSTACK_SEARCH_RESULTS_PER_PAGE=1





