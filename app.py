from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, AI Running Coach!"

if __name__ == '__main__':
    app.run(debug=True)