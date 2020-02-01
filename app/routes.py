from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('login.html', title='CELF Login', form=form)
