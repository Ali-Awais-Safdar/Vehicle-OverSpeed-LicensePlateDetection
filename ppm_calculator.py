import cv2
import numpy as np

# Read image
image = cv2.imread('speed_detector_isb_ppm_calculations.png')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use canny edge detection with a lower threshold
edges = cv2.Canny(gray, 30, 100, apertureSize=3)

# Apply HoughLinesP method to
# directly obtain line end points
lines_list = []
lines = cv2.HoughLinesP(
    edges,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 180,  # Angle resolution in radians
    threshold=50,  # Min number of votes for valid line
    minLineLength=5,  # Min allowed length of line
    maxLineGap=10  # Max allowed gap between line for joining them
)

# Iterate over points
for points in lines:
    # Extracted points nested in the list
    x1, y1, x2, y2 = points[0]

    # Calculate the average intensity along the line
    intensity = np.mean(gray[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)])

    # Filter lines based on intensity (adjust the threshold as needed)
    
    if intensity < 200: #150 for chinese video and 200 for isb video
        # Draw the lines joining the points on the original image
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 2)
        # Maintain a simple lookup list for points
        lines_list.append([(x1, y1), (x2, y2)])
        # Display the number of pixels in each line drawn on the image
        cv2.putText(image, str(abs(x2 - x1)), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# Save the result image
cv2.imshow('detectedLines.png', image)
cv2.waitKey(0)
