from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This is coming to you from SKDSAN003 and GBRADD001'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
