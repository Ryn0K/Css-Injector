from flask import Flask,render_template,request,redirect,make_response
import os
import uuid

app = Flask(__name__,static_url_path='/')

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
def generate_random_nonce():
    return uuid.uuid4().hex

@app.get('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('private-cookie',str(generate_random_nonce()))
    return resp
@app.get('/challenge-1')
def challenge_1():
    if not request.args.get('msg'):
        return redirect('/challenge-1?msg=Welcome to this website.')
    msg = request.args.get('msg')
    return render_template('challenge1.html',msg = msg)

@app.get('/mitigate-1')
def mitigate_1():
    if not request.args.get('msg'):
        return redirect('/mitigate-1?msg=Welcome to this website.')
    msg = request.args.get('msg')
    return render_template('mitigate1.html',msg = msg,nonce=generate_random_nonce())

@app.get('/challenge-2')
def challenge_2():
    return render_template('challenge2.html')

@app.get('/mitigate-2')
def mitigate_2():
    return render_template('mitigate2.html',nonce=generate_random_nonce())

if __name__ == "__main__":
    app.run()
