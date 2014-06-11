from flask import Flask, render_template, url_for, jsonify
app = Flask(__name__)

categories = ['music','reading', 'watching', 'food','other']

@app.route('/')
def hello_world():
    return render_template('index.html',categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
