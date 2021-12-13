from Alsvin-5GAPI.app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("Alsvin-5GAPI.tasks.example",)
