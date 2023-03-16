
# The most simple Flask  app to render mobile site
# David Howe Kingston 2023 March.


from flask import Flask,  render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('mypage.html')



@app.route('/newflags')
def newflags():
    return render_template('newflags.html')


@app.route('/kastone')
def links():
    return render_template('kastone.html')
