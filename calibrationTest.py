import cv2
import numpy as np

# Load the image
calibration_image = cv2.imread(r'C:\Users\milto\OneDrive\Desktop\340 test System\.venv\data\calimage.JPG')

# Check if the image was loaded successfully
if calibration_image is None:
    print("Error: Image not found or failed to load.")
else:
    # Resize the image
    height, width = calibration_image.shape[:2]
    scale_percent = 50  # Resize to 50% of the original size
    new_dimensions = (int(width * scale_percent / 100), int(height * scale_percent / 100))
    resized_image = cv2.resize(calibration_image, new_dimensions, interpolation=cv2.INTER_AREA)

    # List to store clicked points
    points = []

    # Define the mouse callback function for Calibrating the image
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(points) < 2:  # Only accept two points
                points.append((x, y))
                print(f"Point clicked: ({x}, {y})")  # Print the clicked point
                # Draw a hollow circle (outline only) on the image
                cv2.circle(resized_image, (x, y), 3, (255, 0, 0), 1)  # Smaller hollow circle
                cv2.imshow('Calibration Image', resized_image)  # Update the image to show the circle

            if len(points) == 2:  # If two points are clicked
                print("Two points have been selected.")
                # Draw a line between the two points
                cv2.line(resized_image, points[0], points[1], (255, 0, 0), 4)  # Draw line in blue
                cv2.imshow('Calibration Image', resized_image)  # Update the image to show the line

    
    # Display the resized image in a window
    cv2.imshow('Calibration Image', resized_image)

    # Set the mouse callback function
    cv2.setMouseCallback('Calibration Image', click_event)

    # Wait for 10 seconds (10,000 milliseconds) and check for events
    for _ in range(100):
        if cv2.waitKey(100) & 0xFF == ord('q'):  # Check for 'q' to exit early
            break
        if len(points) >= 2:  # Exit the loop if two points have been selected
            break

    # Print the points that were clicked
    print("Clicked points:", points)

    # Prompt the user for the real-world distance
    real_world_distance = float(input("Enter the real-world distance corresponding to the clicked points (in cm): "))

    if len(points) == 2:
        # Calculate the pixel distance between the two points
        pixel_distance = np.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2)

        # Calculate the scaling factor (real-world distance per pixel)
        scaling_factor = real_world_distance / pixel_distance if pixel_distance > 0 else 0

        # Prepare the text to display
        result_text = f"Pixel distance: {pixel_distance:.2f} pixels"
        scaling_text = f"Scaling factor: {scaling_factor:.2f} cm/pixel"

        # Define the position for the text
        text_position = (10, 30)
        scaling_position = (10, 60)

        # Draw a gray rectangle behind the text for better visibility
        cv2.rectangle(resized_image, (5, 15), (400, 50), (200, 200, 200), -1)  # Background for result_text
        cv2.rectangle(resized_image, (5, 45), (400, 80), (200, 200, 200), -1)  # Background for scaling_text

        # Put the text on the image
        cv2.putText(resized_image, result_text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(resized_image, scaling_text, scaling_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

        # Show the updated image with the results
        cv2.imshow('Calibration Image', resized_image)

    # Keep the window open until the user decides to close it
    cv2.waitKey(0)  # Wait indefinitely until a key is pressed
    cv2.destroyAllWindows()  # Close the window
