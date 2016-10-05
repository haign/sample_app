from flask import Flask, render_template
app = Flask(__name__)

#defined index functions needs to be right undernath @app.route('/')

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)