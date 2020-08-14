from app import app
from .admin import admin
from .visitor import visitor

# 拼装高达~~~
app.register_blueprint(visitor, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')