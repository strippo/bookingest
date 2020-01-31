DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'pdz.base.urls'
SITE_ID = 1

AUTH_USER_MODEL = 'user.User'

ALLOWED_HOSTS = ['localhost', ]

INSTALLED_APPS = (
    'pdz.admin',
    'bootstrap_admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    "django_select2",
    "dbbackup",
    'tinymce',
    'sorl.thumbnail',
    'south',
    'smart_selects',
    'pdz.user',
#    "cns.areas",
    "pdz.base",
#    "cns.calls",
#    "cns.courses",
    "pdz.workers",
#    "cns.relations",
    "pdz.users",
    "pdz_import",
    'pdz.events',
    "pdz.enum",
    "pdz.warehouse",
    "pdz.appointments",
#    "cns.practices",
#    "cns.supportpaths",
    "admin_menu",
    "protected_filefield",
    "overextends"
)



MEDIA_URL = '/media/'
STATIC_URL = '/static/'

PUBLIC_ROOT = "public/"

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'it_IT'

DATABASES = {
'default':
                 {
                 'ENGINE': 'django.db.backends.mysql',
                 'NAME': 'pandizucchero2',
                 'HOST': '127.0.0.1',
                 'USER': 'cns',
                 'PASSWORD': 'cns'
                }
            }

DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i:s'



DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y', # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y', # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y', # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)
USE_I18N = True
USE_L10N = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.static',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_FROM = 'newsletter@brokerconsult.it'

#TINYMCE_JS_ROOT = '/media/js/tiny_mce/'
#TINYMCE_JS_URL = os.path.join(MEDIA_URL, "tiny_mce/tiny_mce_src.js")
#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,spellchecker,paste,searchreplace",
#    'theme': "advanced",
#}
#TINYMCE_SPELLCHECKER = True

STATIC_ROOT = '/static/'
STATIC_URL = '/static/'

TINYMCE_JS_URL = STATIC_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_ROOT + 'js/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,fullscreen",
    'theme': "advanced",
    'width': '430px',
    'height': '300px',
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_buttons1': "bold,italic,separator,link,unlink,separator,bullist,separator,justifyleft,justifyfull,separator,formatselect",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_blockformats': "p,h1,h2",
}


# import locale
# locale.setlocale(locale.LC_ALL,'it_IT.UTF-8')

#db backup
DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_FILESYSTEM_DIRECTORY = './dbbackup'
DBBACKUP_CLEANUP_KEEP = 31
# DBBACKUP_STORAGE = 'cns.base.dbbackup.ftp_storage'
# DBBACKUP_FTP_HOST = '192.168.1.251'
# DBBACKUP_FTP_USER = 'ucipemusr'
# DBBACKUP_FTP_PASSWORD = 'uc1p3mftpusrpwd.2016'
# DBBACKUP_FTP_PATH = 'ucipem/backups'
# DBBACKUP_MEDIA_PATH = 'private/'
# DBBACKUP_CLEANUP_KEEP = 31
