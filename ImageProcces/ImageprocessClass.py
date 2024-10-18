import cv2

ImageDisplayWidth = 800
ImageDisplayHeight = 600
#image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\calimage.JPG'

# Class to process images
class Imageproccess:
    def __init__(self, image, width=800, height=600):
        self.image = image
        self.imageresized = cv2.resize(self.image, (width, height))
        self.points = []  # List to store clicked points

    # Method to check where the left mouse button is clicked
    def checkclicks(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Left mouse button clicked at:", x, y)
            self.drawcircle(x, y)
            self.points.append((x, y))  # Store the coordinates
            print("Points:", self.points)
            self.drawtext(f"Point {len(self.points)}")  # Display text

    # Method to draw a circle on the image
    def drawcircle(self, x, y):
        cv2.circle(self.imageresized, (x, y), 3, (255, 0, 0), 1)
        cv2.imshow('Calibration Image', self.imageresized)

    # Method to display text in the bottom-right corner of the image
    def drawtext(self, text):
        font = cv2.FONT_HERSHEY_SIMPLEX  # Choose a font
        font_scale = 0.6  # Font scale factor
        color = (255, 255, 255)  # White color
        thickness = 2  # Line thickness

        # Get the text size to calculate its position
        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate bottom-right corner position (with some padding)
        text_x = self.imageresized.shape[1] - text_width - 10  # 10 pixels from the right edge
        text_y = self.imageresized.shape[0] - 10  # 10 pixels from the bottom edge

        # Draw the text on the image at the calculated position
        cv2.putText(self.imageresized, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
        cv2.imshow('Calibration Image', self.imageresized)

    # Method to calibrate the pixel coordinates
    def calibrate(self):
        cv2.namedWindow('Calibration Image')  # Create the window outside of the loop
        cv2.setMouseCallback('Calibration Image', self.checkclicks)

        while True:
            cv2.imshow('Calibration Image', self.imageresized)
            # Exit the loop if two points have been selected
            if len(self.points) >= 2:  
                print("Calibration complete with points:", self.points)
                break
            # Wait for a short period to allow for window refresh
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break

        cv2.destroyAllWindows()  # Close the window

# Load an image
image = cv2.imread(image_path)

if image is not None:  # Ensure the image loaded successfully
    # Create an instance of the Imageproccess class
    img_process = Imageproccess(image, ImageDisplayWidth, ImageDisplayHeight)
    # Calibrate the image
    img_process.calibrate()
else:
    print("Error: Image could not be loaded. Please check the file path.")
