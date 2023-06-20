from flask import Flask, redirect, render_template, request, url_for, jsonify
from datetime import datetime, timedelta
import TF_IDF.query100 as query

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
        
    print(username, password)
    if username == "admin" and password == "admin":
        return redirect(url_for('problems'))
    else:
        return render_template('index.html')

@app.route('/problems')
def problems():
    return render_template('problems.html')

@app.route('/search')
def search():
    return render_template('data.html')



@app.route('/query', methods=['POST'])
def search_query():
    search_data = request.get_json()
    search_query = search_data['query']
    print(search_query)

    # Call the query.py function with the search query
    results = query.return_search_result(search_query)
    if len(results) == 0:
        return jsonify({'message': 'No results found'})
    else:
        return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

