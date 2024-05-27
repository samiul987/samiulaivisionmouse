Features
Hand Tracking: Utilizes the cvzone library's HandDetector module to track hand movements in real-time.
Cursor Control: Move the mouse cursor using your index finger.
Click Actions: Perform click actions by pinching with your thumb and index finger.
Smooth Motion: Includes a smoothening algorithm to provide a fluid cursor movement experience.
Frame Rate Display: Displays the current frame rate to monitor performance.
Installation
You can install samiulaivisionmouse using pip:

bash
Copy code
pip install samiulaivisionmouse
Usage
Here is a basic example of how to use the samiulaivisionmouse package:

python
Copy code
from samiulaivisionmouse import HandTrackingMouseControl

htmc = HandTrackingMouseControl()
htmc.run()
How It Works
Initialization: The HandTrackingMouseControl class initializes the webcam, sets up the hand detector, and determines the screen dimensions.
Hand Detection: Continuously captures frames from the webcam and detects hands using the HandDetector module.
Cursor Movement: Maps the position of the index finger to the screen coordinates and moves the cursor accordingly.
Click Detection: Measures the distance between the index finger and the middle finger to detect a click gesture.
Smoothening: Applies a smoothening algorithm to reduce the jitter and provide a fluid cursor movement.
Frame Rate Calculation: Calculates and displays the frame rate to monitor performance.
Example Code
Here's a more detailed example of how to run the hand tracking mouse control:

python
Copy code
import samiulaivisionmouse

# Create an instance of the HandTrackingMouseControl class
htmc = samiulaivisionmouse.HandTrackingMouseControl()

# Run the hand tracking mouse control
htmc.run()
Requirements
Python 3.6 or higher
opencv-python
numpy
cvzone
pyautogui
You can install the dependencies using:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Developed by [Your Name].

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

Support
For any issues or questions, please open an issue on the GitHub repository.

This description provides a comprehensive overview of the project, including its features, usage instructions, and additional information. Feel free to modify it to better suit your specific project details and preferences.
