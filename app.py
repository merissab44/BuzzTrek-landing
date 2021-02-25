from flask import Flask, request, render_template
from flask_split import split

app = Flask(__name__)
app.register_blueprint(split)

@app.route('/')
def displayHomePage():
    return render_template('index.html')

@app.route('/about.html')
def displayAboutPage():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)