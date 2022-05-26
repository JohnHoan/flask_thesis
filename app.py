from turtle import speed
from flask import Flask, request, jsonify
app = Flask(__name__)
import utils

@app.route('/predict')
def predict():
    score_1 = float(request.values.get('score_1'))
    package_1 = float(request.values.get('package_1'))
    score_2 = float(request.values.get('score_2'))
    package_2 = float(request.values.get('package_2'))
    score_3 = float(request.values.get('score_3'))
    package_3 = float(request.values.get('package_3'))
    speed = float(request.values.get('speed'))
    satisfied_level = float(request.values.get('satisfied_level'))
    output = utils.get_estimated_package(score_1,package_1,score_2,package_2,score_3,package_3,speed,satisfied_level)
    return jsonify([output])
    
if __name__ == "__main__":
    print("Starting Python Flask Server...")
    utils.load_saved_artifacts()
    app.run()