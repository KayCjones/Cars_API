# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--89p9$#^(6ji$!e86jfy=5*3%(iz5cij#p_p4!$88i-zh^0bzw'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '1123581321',
    }
}