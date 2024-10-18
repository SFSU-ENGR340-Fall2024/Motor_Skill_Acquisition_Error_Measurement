import cv2

ImageDisplayWidth = 800
ImageDisplayHeight = 600
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\calimage.JPG'

# Class to process images
class ImageProcess:
    def __init__(self, image, width=800, height=600):
        self.image = image
        self.imageresized = cv2.resize(self.image, (width, height))
        self.original_image = self.imageresized.copy()  # Store a copy of the original image
        self.points = []  # List to store clicked points

    # Method to check where the left mouse button is clicked
    def checkclicks(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Left mouse button clicked at:", x, y)
            self.drawcircle(x, y)
            self.points.append((x, y))  # Store the coordinates
            print("Points:", self.points)

    # Method to draw a circle on the image
    def drawcircle(self, x, y):
        cv2.circle(self.imageresized, (x, y), 3, (255, 0, 0), 1)
        cv2.imshow('Test Image', self.imageresized)

    # Method to draw a line between two points on the image
    def drawline(self, point1, point2):
        cv2.line(self.imageresized, point1, point2, (0, 255, 0), 1)
        # Show the updated image in the 'Test Image' window
        cv2.imshow('Test Image', self.imageresized)

    # Method to collect calibration points from the user
    def measurementcollect(self):
        cv2.namedWindow('Test Image')  # Create the window
        cv2.setMouseCallback('Test Image', self.checkclicks)

        while True:
            cv2.imshow('Test Image', self.imageresized)
            # Exit the loop if two points have been selected
            if len(self.points) >= 2:
                print("Calibration complete with points:", self.points)
                break
            # Wait for a short period to allow for window refresh
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break

        # Short delay to ensure proper window closure
        cv2.waitKey(1)  
        cv2.destroyAllWindows()  # Close the window

    # Method to reset the image 
    # This method removes all drawn points, text, and lines from the image
    # input: None
    # output: None
    def reset(self):
        self.imageresized = self.original_image.copy()  # Reset to the original image
        print("Image and points reset.")

    # Method to display a text in the middle of the image with a gray background
    def displaytextmiddle(self, text):
        # Set font and size for the text
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)  # White text
        thickness = 2
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate the position for the text (centered)
        text_x = (self.imageresized.shape[1] - text_size[0]) // 2
        text_y = (self.imageresized.shape[0] + text_size[1]) // 2

        # Draw a gray background rectangle behind the text
        background_color = (128, 128, 128)  # Gray background
        rectangle_top_left = (text_x - 10, text_y - text_size[1] - 10)  # Some padding
        rectangle_bottom_right = (text_x + text_size[0] + 10, text_y + 10)
        cv2.rectangle(self.imageresized, rectangle_top_left, rectangle_bottom_right, background_color, cv2.FILLED)

        # Put the text on the image
        cv2.putText(self.imageresized, text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Show the updated image with the text in the middle
        cv2.imshow('Test Image', self.imageresized)


# Load an image
image = cv2.imread(image_path)


img_process = ImageProcess(image, ImageDisplayWidth, ImageDisplayHeight)

# Collect points for calibration
img_process.measurementcollect()

# Reset the image to its original state
img_process.reset()
cv2.waitKey(1)  # Optional, but ensures smoothness in some environments
# Reopen the 'Measurement Collection' window with the reset image

for point in img_process.points:
    img_process.drawcircle(point[0], point[1])

# Draw a line between the two points
img_process.drawline(img_process.points[0], img_process.points[1])

# Display the image
cv2.imshow('Test Image', img_process.imageresized)

# 

cv2.waitKey(10000)  # Wait 9s before proceeding