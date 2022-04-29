import os

if os.environ.get('ENVIRONTMENT') != 'prod':
    from dotenv import load_dotenv
    load_dotenv()

# Postgresql conf
POSTGRESQL_USER = os.environ.get('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = os.environ.get('POSTGRESQL_PASSWORD')
POSTGRESQL_HOST = os.environ.get('POSTGRESQL_HOST')
POSTGRESQL_PORT = os.environ.get('POSTGRESQL_PORT')
POSTGRESQL_DATABASE = os.environ.get('POSTGRESQL_DATABASE')

# JWT conf
JWT_PREFIX = os.environ.get('JWT_PREFIX', 'Bearer')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30))

# Redis Conf
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_DB = int(os.environ.get('REDIS_DB'))

# CORS
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')