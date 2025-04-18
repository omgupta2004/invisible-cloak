import cv2
import numpy as np

def get_color_range(color_name):
    """
    Define HSV color ranges for different colors
    """
    color_ranges = {
        'red': [
            (np.array([0, 100, 50]), np.array([10, 255, 255])),
            (np.array([160, 100, 50]), np.array([180, 255, 255]))
        ],
        'blue': [
            (np.array([100, 100, 50]), np.array([140, 255, 255]))
        ],
        'green': [
            (np.array([40, 100, 50]), np.array([80, 255, 255]))
        ],
        'yellow': [
            (np.array([20, 100, 50]), np.array([35, 255, 255]))
        ],
        'purple': [
            (np.array([130, 100, 50]), np.array([160, 255, 255]))
        ]
    }
    return color_ranges.get(color_name.lower(), color_ranges['red'])

def create_invisibility_cloak():
    
    print("Available colors: Red, Blue, Green, Yellow, Purple")
    chosen_color = input("What color is your cloak/object? ").strip()

    color_ranges = get_color_range(chosen_color)

 
    cap = cv2.VideoCapture(0)

  
    print("🎥 Setting up background. Please stay still...")
    for i in range(30):
        ret, background = cap.read()

    print(f"🔮 Invisibility cloak activated for {chosen_color}! Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        
      
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        
        masks = [cv2.inRange(hsv, lower, upper) for lower, upper in color_ranges]
        
       
        mask = masks[0]
        for m in masks[1:]:
            mask = cv2.bitwise_or(mask, m)
        
        # Refine the mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
        
      
        mask_inv = cv2.bitwise_not(mask)
  
        background_part = cv2.bitwise_and(background, background, mask=mask)
        
       
        frame_part = cv2.bitwise_and(frame, frame, mask=mask_inv)
        
       
        result = cv2.add(background_part, frame_part)
        
        
        cv2.imshow("Invisibility Cloak", result)
        cv2.imshow("Color Mask", mask)  
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_invisibility_cloak()
