from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password
#
#     def __repr__(self):
#         return f'<User: {self.username}>'


# users = []
# users.append(User(id=1, username='Anthony', password='password'))
# users.append(User(id=2, username='Becca', password='secret'))
# users.append(User(id=3, username='Carlos', password='somethingsimple'))

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'


@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        # user = [x for x in users if x.id == session['user_id']][0]
        g.user = session['user']


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile')
def profile():
    if g.user:
        # return redirect(url_for('login'))
        return render_template('profile.html', user=session['user'])

    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)