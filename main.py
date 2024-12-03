from flask import Flask

api = Flask(__name__)

@api.route('/')
def home():
    return 'Hey there!'

@api.route('/cheaper')
def getCheaper():
    return

if __name__ == '__main__':
    api.run(debug=True)