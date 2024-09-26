import os
from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import judoscale

app = Flask(__name__)
judoscale.init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = get_response(message)
    return jsonify({'response': response})

@app.route('/report')
def report():
    # This is a placeholder for generating a report
    # You would typically gather data from your chatbot usage here
    chat_count = 100  # Example data
    unique_users = 50  # Example data
    return render_template('report.html', chat_count=chat_count, unique_users=unique_users)

if __name__ == '__main__':
    app.run(debug=True)
