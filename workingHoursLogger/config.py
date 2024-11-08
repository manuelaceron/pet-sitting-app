class Config:
    SECRET_KEY = 'secret-key'  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = "manuela.cv96@gmail.com"
    MAIL_PASSWORD = "set_password"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True