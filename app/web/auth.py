from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import web
from app.forms.auth import RegisterForm, LoginForm, ResetPasswordForm, EmailForm, \
    ChangePasswordForm
from app.models.user import User
from app.models import db
from app.libs.email import send_email

__author__ = 'JOJO'


# DONE
@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, False)
        return redirect(url_for('web.index'))
    return render_template('auth/register.html', form=form)


# DONE
# 登录
@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            #  用login_user登录，并记住用户
            login_user(user, remember=True)
            #  获取用户登陆之前访问的地址，这个访问信息在next中
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误', category='login_error')
    return render_template('auth/login.html', form=form)


# DONE
# 发送邮箱，重置密码
@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    if request.method == 'POST':
        form = EmailForm(request.form)
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            send_email(form.email.data, '重置你的密码',
                       'email/reset_password', user=user,
                       token=user.generate_token())
            flash('一封邮件已发送到邮箱' + account_email + '，请及时查收')
            return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html')


# 收到邮件，用邮件中的token重置密码
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    if not current_user.is_anonymous:
        return redirect(url_for('web.index'))
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        result = User.reset_password(token, form.password1.data)
        if result:
            flash('你的密码已更新,请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            return redirect(url_for('web.index'))
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        current_user.password = form.new_password1.data
        db.session.commit()
        flash('密码已更新成功')
        return redirect(url_for('web.personal'))
    return render_template('auth/change_password.html', form=form)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        form = RegisterForm()
        form.validate()
        user = User(form.nickname.data,
                    form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, False)
        g.status = True
        flash('一封激活邮件已发送至您的邮箱，请快完成验证', 'confirm')
        # 由于发送的是ajax请求，所以redirect是无效的
        return 'go to index'
