**Invisibility Cloak using OpenCV**

This project demonstrates the creation of an invisibility cloak effect using Python and OpenCV. By detecting a specific color on a cloak (such as red, blue, green, etc.), the system replaces it with the static background, giving the illusion of invisibility.

# Features:
- Real-time background replacement.
- Supports multiple cloak colors (Red, Blue, Green, Yellow, Purple).
- Interactive color selection.
- Refined masking using morphological operations.

# Technologies Used:
- Python
- OpenCV
- NumPy

# How It Works:
1. The program captures a few frames initially to set the static background.
2. It detects the chosen color using HSV color segmentation.
3. The cloak region is then masked, and the background replaces it.
4. The modified frame is displayed in real-time to simulate invisibility.

# Setup & Usage:
1. Install the necessary dependencies:

   ```bash
   pip install opencv-python numpy
   ```

2. Run the script:

   ```bash
   python cloak.py
   ```

3. Follow the on-screen prompt:
   - Enter the color of your cloak (Red, Blue, Green, Yellow, Purple).
   - Stay still for a few seconds while the background is captured.
   - Enjoy the invisibility effect!
   
4. Press 'q' to quit.

#Project Structure:
```
cloak.py       # Main Python script
README.md      # Project documentation
```

# Concepts Applied:
- HSV color space and masking.
- Morphological operations (open, dilate).
- Bitwise operations for image blending.
- Real-time video processing.
