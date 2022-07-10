from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello word'

if __name__ == '__main__':
    app.run(port = 5000, debug = True)