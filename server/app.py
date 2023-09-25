from flask import Flask, request, jsonify
from inference import query

app = Flask(__name__)


@app.route('/classify_email', methods=['POST'])
def classify_email():
    # print(request)
    # query_param = request.args.get('text')
    query_param = request.json.get('text')
    # response = f"Received query: {query_param}"
    if query_param:
        result = query(query_param)
    else:
        result = "No text received"

    return jsonify({'message': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
