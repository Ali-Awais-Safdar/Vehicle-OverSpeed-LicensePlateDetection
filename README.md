# Vehicle Overspeed Detection and Number Plate Recognition
This project combines vehicle overspeed detection with number plate recognition using two separate Python scripts.

## License_plate_recognition.py
This script focuses on number plate recognition. It uses the EasyOCR library for text detection and extraction from images. The process involves preprocessing the image, detecting the license plate, and saving the processed image with the identified license plate.

## Usage:
Make sure to adjust the input and output folders as needed. The identified images will be saved in the specified output folder.

This script focuses on vehicle overspeed detection. It uses the OpenCV and dlib libraries to detect and track vehicles in a video stream. The estimated speed of each vehicle is calculated and displayed on the video feed. Additionally, images of speeding cars are saved to the "offenders" folder. You can run it in the terminal using:

```
python speed_detector.py
```

Make sure to provide the correct video file path by changing the line:

```
video = cv2.VideoCapture("your_video_filename.mp4")
```

Several test videos are provided in the "videos" folder, and you can use them by changing the filename in the above line.

The processed video, including speed information, will be saved as "ProcessedVideo.avi." Images of speeding cars will be saved to the "offenders" folder.

## Dependencies:
Ensure that you have the required dependencies installed:

- OpenCV
- dlib
- easyocr
- numpy
- Pillow
You can install these dependencies using the following:

```
pip install opencv-python dlib easyocr numpy Pillow
```
## User Interface
We have also provided a GUI using Flask where you can add a video and run the both scripts accordingly.
You can run this by using:
```
python app.py
```

## Notes:
- Adjust the script parameters, such as file paths and detection parameters, based on your specific use case.
- Both scripts can be run independently for their respective functionalities.
- The overspeed detection script saves images of speeding cars in the "offenders" folder.
- Make sure to have the required classifier file ("car.xml") for vehicle detection.
