import cv2
import os

TEST_IMAGES = r"./data/test"

def load_image(image_id: int):

    # image_path = f"{TEST_IMAGES}/000000.png"
    image_path = os.path.join(TEST_IMAGES, f"{image_id:06d}.png")
    image = cv2.imread(image_path)

    return image

image = load_image(13)

# Visualize the image
cv2.imshow("Chest X-Ray", image) 
cv2.waitKey(0)  
cv2.destroyAllWindows() 