import cv2
import os
import easyocr
import numpy as np

def preprocess_image(image):
    # Convert the image to binary
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # # Use a morphological transformation (opening) to enhance characters
    # kernel = np.ones((2, 2), np.uint8)
    # closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("closed", gray)
    cv2.waitKey(0)
    
    return gray

def detect_license_plate(image):
    # Preprocess the image
    # processed_image = preprocess_image(image)
    processed_image = image

    # Use EasyOCR for text detection
    reader = easyocr.Reader(['ch_sim','en'])
    results = reader.readtext(processed_image,detail = 0)

    # Get the last five element of the list
    license_plate_text = results[0][-5:]
    
    # Join all the characters in the list to get a string
    license_plate_text = ''.join(license_plate_text)

    return license_plate_text

def process_offenders_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # Read the image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            # Detect license plate
            license_plate_text = detect_license_plate(image)

            # Adjust font size according to the image and write the license plate number on the image
            font_size = max(0.5, min(image.shape[0] / 500, image.shape[1] / 500))
            cv2.putText(image, f"License Plate: {license_plate_text}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 255, 0), 1)

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, f"identified_{filename}")
            cv2.imwrite(output_path, image)

            print(f"Detected License Plate: {license_plate_text} in {filename}. Processed image saved to {output_path}")

if __name__ == "__main__":
    offenders_folder = "offenders"
    identified_folder = "offenders_identified"

    process_offenders_folder(offenders_folder, identified_folder)
