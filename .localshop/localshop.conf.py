import os
import herokuify

LOCALSHOP_DISTRIBUTION_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

SECRET_KEY = os.environ['LOCALSHOP_SECRET_KEY']

from herokuify.common import *  # NOQA
from herokuify.aws import *  # NOQA

DATABASES = herokuify.get_db_config()   # Database config
CACHES = herokuify.get_cache_config()   # Memcache config for Memcache/MemCachier
