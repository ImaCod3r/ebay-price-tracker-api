from flask import Flask, request, jsonify
from scrapper import get_data
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

api = Flask(__name__)

@api.route('/')
def home():
    return 'Hey there!'

@api.route('/search', methods=['GET','POST'])
def search():
    query = request.args.get('q')
    
    if not query:
        logging.warning("Query parameter 'q' is missing.")
        return jsonify({
            'error': True, 
            'message': 'Query parameter is required.', 
            'code': 400
            })
    try:
        data = get_data(query)
        if data:
            return jsonify(data)
        else:
            logging.info(f"No data found for query: {query}")
            return jsonify({
                'error': True,
                'message': 'No data found.',
                'code': 404
            })
            
    except Exception as e:
        logging.error(f"Error occured while fetching data: {str(e)}")
        return jsonify({
            'error': True,
            'message': 'An error occurred while processing your request.',
            'code': 500
        })
    
if __name__ == '__main__':
    api.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')