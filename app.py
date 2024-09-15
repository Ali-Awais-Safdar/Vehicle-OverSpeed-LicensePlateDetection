from flask import Flask, render_template, send_from_directory, jsonify
from speed_detector import trackMultipleObjects as trackMultipleObjectsMain
from speed_detector_isb import trackMultipleObjects as trackMultipleObjectsISB
from License_plate_recognition import *


app = Flask(__name__)

@app.route('/get_images', methods=['GET'])
def get_images():
    identified_folder = "offenders"

    # Get a list of identified image files in the folder
    identified_images = os.listdir(identified_folder)

    return jsonify(identified_images)

@app.route('/images/<filename>')
def images(filename):
    identified_folder = "offenders"

    # Serve the identified images from the folder
    return send_from_directory(identified_folder, filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_speed_detector')
def run_speed_detector_main():
    # Call the function from speed_detector.py
    trackMultipleObjectsMain()

    return "Speed Detector Script Executed"

@app.route('/run_own_speed_detector')
def run_speed_detector_isb():
    # Call the function from speed_detector_isb.py
    trackMultipleObjectsISB()

    return "Own Speed Detector Script Executed"

@app.route('/run_license_plate_recognition')
def run_license_plate_recognition():
    offenders_folder = "offenders"
    identified_folder = "offenders_identified"

    # Call the function to process offenders' images for license plate recognition
    process_offenders_folder(offenders_folder, identified_folder)

    return "License Plate Recognition Script Executed"

@app.route('/get_identified_images', methods=['GET'])
def get_identified_images():
    identified_folder = "offenders_identified"

    # Get a list of identified image files in the folder
    identified_images = os.listdir(identified_folder)

    return jsonify(identified_images)

@app.route('/identified_images/<filename>')
def identified_image(filename):
    identified_folder = "offenders_identified"

    # Serve the identified images from the folder
    return send_from_directory(identified_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
