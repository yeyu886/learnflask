# -*- coding:utf-8 -*-
from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login:username=%s, remember_me=%s' % (form.openId.data,str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',title="Sign in",form=form,providers=app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
def index():
    user  = {"nickname":"fengzi"}
    posts = [{"author":"fz","body":"hehe"},{"author":"laji","body":"haha"}]
    return render_template('index.html',title="home",user=user,posts=posts)