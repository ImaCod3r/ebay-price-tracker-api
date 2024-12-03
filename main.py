from flask import Flask, request, jsonify
from scrapper import getData

api = Flask(__name__)

@api.route('/')
def home():
    return 'Hey there!'

@api.route('/search', methods=['GET','POST'])
def search():
    query = request.args.get('q')
    data = getData(query)
    
    if data:
        return jsonify(data) 
    return '<h2>Nao foi possivel obter dados</h2>'

if __name__ == '__main__':
    api.run(debug=True)