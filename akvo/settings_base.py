# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module. 
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

# Django settings for akvo project.
# settings_base.py contains non-server specific settings and
# is imported into settings.py.

# Alphabetically ordered (more or less...)

# Accounts not activated in a week get purged. Used by registration app.
ACCOUNT_ACTIVATION_DAYS = 7

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/rsr/media/admin/'

ADMINS = (
     ('Gabriel von Heijne', 'gabriel@akvo.org'),
)

SUPPORT_EMAIL = ADMINS[0][1]

#Additional information about a User
AUTH_PROFILE_MODULE = 'rsr.userprofile'

#Memcached settings
#CACHE_MIDDLEWARE_SECONDS = 300 # 5 minutes
#CACHE_MIDDLEWARE_KEY_PREFIX = 'rsr' #not needed but mandatory setting
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True # Only non-logged in
 
#Use memcached for sessions with write-through to DB
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

#DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = '/var/dev/akvo/data/akvo.sqlite' # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

#DEBUG = True

#DEFAULT_FROM_EMAIL = 'noreply@akvo.og'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.webdesign',
    #'feedjack', #maybe later...
    # not used here, used for GraphViz on the Mac 'extensions', #django-command-extensions see http://code.google.com/p/django-command-extensions
    'akvo.rsr',
    'akvo.gateway',
    'template_utils',
    'registration', #see http://code.google.com/p/django-registration/
    #'django_granular_permissions',
    #'akvo.status',
    'paypal.standard.ipn',
    'sorl.thumbnail',
    'rosetta',
    'django_counter',
    'mollie.ideal',
    'django_sorting',
    'pagination',
    'oembed',
    'django_markup',
    'notification',
    'permissions',
    'workflows',
    'tastypie',
)

#INTERNAL_IPS = (
#    '87.227.60.54', '125.27.250.14', '192.168.38.68',
#)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

gettext = lambda s: s

LANGUAGES = (
    #('de', gettext('German')),
    ('en', gettext('English')),
    #('nl', gettext('Dutch')),
    #('es', gettext('Spanish')),
    #('fr', gettext('French')),
    #('sv', gettext('Swedish')),
)

LOGIN_URL = '/rsr/signin/'
LOGIN_REDIRECT_URL = '/rsr/'

MANAGERS = ADMINS

#MEDIA_ROOT = '/var/dev/akvo/mediaroot/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = 'http://dev.akvo.org:8080/rsr/media/'

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django_sorting.middleware.SortingMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

# PAUL
# PAYPAL_RECEIVER_EMAIL = 'noreply@akvo.org'

# Is this the pvw-rsr?
PVW_RSR = False 

ROOT_URLCONF = 'akvo.urls'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^qd@tv7*d96zt(6c%ouy-hql0(+5ess^kpqsqwtbn+=)13a^+^'

SEND_BROKEN_LINK_EMAILS = True

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "akvo.rsr.context_processors.extra_context",
)

#TEMPLATE_DEBUG = DEBUG

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

import os.path
if PVW_RSR:
    TEMPLATE_LEAF_DIR = 'dws'
else:
    TEMPLATE_LEAF_DIR = 'akvo'
    
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates/%s' % TEMPLATE_LEAF_DIR).replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'templates/core').replace('\\','/'),
)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Stockholm'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'verbose_request': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s %(request)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        #'special': {
        #    '()': 'project.logging.SpecialFilter',
        #    'foo': 'bar',
        #},
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'akvo.log').replace('\\','/'),
            #'filename': '/var/log/apache2/iati-test/akvo_rsr.log',
            'maxBytes': 1024*1024,
            'backupCount': 4,
            'formatter': 'verbose',
        },
        'request_to_console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose_request',
        },
        'request_to_file':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'akvo.log').replace('\\','/'),
            #'filename': '/var/log/apache2/iati-test/akvo_rsr.log',
            'maxBytes': 1024*1024,
            'backupCount': 4,
            'formatter': 'verbose_request',
        },
        #'mail_admins': {
        #    'level': 'ERROR',
        #    'class': 'django.utils.log.AdminEmailHandler',
        #    'filters': ['special']
        #},
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        #'django.request': {
        #    'handlers': ['mail_admins'],
        #    'level': 'ERROR',
        #    'propagate': False,
        #},
        'django.request': {
            'handlers': ['request_to_file', ], #'request_to_console',],
            'level': 'DEBUG',
            'propagate': False,
        },
        'akvo.rsr': {
            'handlers': ['file', ], #'console', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
