from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField
from wtforms import IntegerField,StringField,PasswordField
from wtforms.validators import Required,Length

# 定义表单
class LoginForm(FlaskForm):
    id = IntegerField(label='输入id', validators=[Required,Length(min=6,max=10,message='id长度有问题')])
    password = PasswordField(label='输入密码', validators=[Required,Length(min=6,message='密码长度至少六位')])
    submit = SubmitField('提交')
