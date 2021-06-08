"""
Local settings
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'job_board_scrapper',
        'USER': 'root',
        'PASSWORD': 'ufeltfvec',
        'HOST': 'localhost:8000',
        'PORT': '3306',
    }
}
