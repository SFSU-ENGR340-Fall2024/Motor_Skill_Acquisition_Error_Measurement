import MeasurmentClass
import DataClassTemp



# Load and process the image
image = cv2.imread(image_path)
processor = ImageProcess(image)

# Collect calibration points
processor.measurementcollect()
processor.calibration()
processor.errormeasurment()

# Clean up and exit
cv2.destroyAllWindows()