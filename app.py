from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask web server is running on port 7001!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001)
