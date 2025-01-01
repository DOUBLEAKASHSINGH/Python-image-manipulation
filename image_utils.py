import cv2 
from matplotlib import pyplot as plt

# Read the image
image_file = "D:\\Disk\\Albert.jpeg" 
img = cv2.imread(image_file)

# Check if the image was loaded successfully
if img is not None: 
    cv2.imshow('original image', img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
else:
    print("Error: Could not read the image.")


# Inverted Images
inverted_image = cv2.bitwise_not(img)
cv2.imwrite("D:\\Disk\\Inverted_Image.jpg", inverted_image)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Load a grayscale image
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv2.imwrite("D:\\Disk\\gray.jpg", gray_image)
cv2.imshow("gray_image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Thresholding
thresh, im_bw = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
cv2.imwrite("D:\\Disk\\bw.jpg", im_bw)
cv2.imshow("bw_image", im_bw)
cv2.waitKey(0)