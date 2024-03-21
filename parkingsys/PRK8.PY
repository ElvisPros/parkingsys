import cv2
import numpy as np

# Load the image (replace "parking_lot.jpg" with the actual image file)
image_path = r"C:\Users\ELVIS PROS\Desktop\computer vision projects\parkingsys\parking6.jpg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection (Canny)
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize empty and occupied parking spaces lists
empty_spaces = []
occupied_spaces = []

# Define a threshold area for parking spaces (adjust as needed)
min_area = 100

# Iterate over each contour
for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_area:
        # Draw a bounding rectangle around the parking space
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green for empty
        empty_spaces.append((x, y, w, h))
    else:
        # Draw a bounding rectangle around the car
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red for occupied
        occupied_spaces.append((x, y, w, h))

# Save the output image (replace "output_parking_lot.jpg" with the desired output file name)
output_path = "output_parking_lot.jpg"
cv2.imwrite(output_path, image)

# Print the number of empty and occupied parking spaces
print(f"Number of empty parking spaces: {len(empty_spaces)}")
print(f"Number of occupied parking spaces: {len(occupied_spaces)}")
