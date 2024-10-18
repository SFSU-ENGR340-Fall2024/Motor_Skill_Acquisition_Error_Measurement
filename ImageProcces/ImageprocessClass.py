import cv2

ImageDisplayWidth = 800
ImageDisplayHeight = 600
<<<<<<< HEAD
#image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\calimage.JPG'
=======
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\calimage.JPG'
>>>>>>> 933a85e861c6b64673cfc027154ccc04a5738e32

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
        cv2.imshow('Measurement Collection', self.imageresized)

    # Method to draw a line between two points on the image
    def drawline(self, point1, point2):
        cv2.line(self.imageresized, point1, point2, (0, 255, 0), 1)
        # Show the updated image in the 'Test Image' window
        cv2.imshow('Test Image', self.imageresized)

    # Method to collect calibration points from the user
    def measurementcollect(self):
        cv2.namedWindow('Measurement Collection')  # Create the window
        cv2.setMouseCallback('Measurement Collection', self.checkclicks)

        while True:
            cv2.imshow('Measurement Collection', self.imageresized)
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

# Load an image
image = cv2.imread(image_path)

if image is not None:  # Ensure the image loaded successfully
    # Create an instance of the ImageProcess class
    img_process = ImageProcess(image, ImageDisplayWidth, ImageDisplayHeight)
    
    # Collect points for calibration
    img_process.measurementcollect()

    # Add a short wait to ensure the window is properly closed
    cv2.waitKey(1)  # Wait briefly before resetting the image
    # reset the image
    img_process.reset()

    # Redraw the points on the image
    if len(img_process.points) >= 2:  # Ensure there are at least two points
        for point in img_process.points:
            img_process.drawcircle(point[0], point[1])
    
        # Draw a line between the two points
        img_process.drawline(img_process.points[0], img_process.points[1])

        # Display the image
        cv2.imshow('Test Image', img_process.imageresized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Not enough points selected for drawing lines.")

else:
    print("Error: Image could not be loaded. Please check the file path.")
