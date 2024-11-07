from flask import Flask, request, jsonify
from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict')
def predict():
    """
    Predict the sentiment of a given text.
    """
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})
    
    sample = [sample]
    predictions = predict_pipeline(sample)

    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({'error': str(e)})
    
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
