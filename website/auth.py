# this file will have bunch of routes inside 
# all route urls
from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return '<p>This is logout</p>'

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif len(password1) < 7:
            flash('Password must be atlest 6 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        else:
            flash('Account created', category='success')


    return render_template('sign_up.html')