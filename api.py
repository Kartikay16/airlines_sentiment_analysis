from flask import Flask,jsonify
import Inference_pipeline.inference_main as inference_main

app = Flask(__name__)

@app.route('/hareKrishna')
def hello():
    return "Hare Krishna"

@app.route('/gettweetanalytics')
def trigger_pipeline():
    predictions_dict = inference_main.InferMain().get_inference()
    return jsonify(predictions_dict)


if __name__ == '__main__':
    app.run(debug=True)