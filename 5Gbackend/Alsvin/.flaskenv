FLASK_ENV=development
FLASK_APP=Alsvin-5GAPI.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:///Alsvin-5GAPI.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
