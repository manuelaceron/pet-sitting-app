class Config:
    SECRET_KEY = 'secret-key'  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"