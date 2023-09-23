from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def query():
    query_param = request.args.get('q', '')
    response = f"Received query: {query_param}"
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
