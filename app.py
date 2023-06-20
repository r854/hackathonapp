from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import query as query
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(username, password)
        if username=="admin" and password=="admin":
            return render_template('data.html')
        else:
            return render_template('index.html')
        

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query')

    # Call the query.py function with the search query
    results = query.search_data(search_query)

    return render_template('data.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
