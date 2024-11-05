import os
import cv2

def preprocess_images(input_dir, output_dir, img_size=(224, 224)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, img_size)
            img = img / 255.0  # Normalize pixel values to [0, 1]
            cv2.imwrite(os.path.join(output_dir, filename), img * 255)
    
    print("Images preprocessed and saved in:", output_dir)

#runing the function with my directories
preprocess_images(
    'part1',  #input directory for raw images
    'UTKFace_resized'  #output directory for preprocessed images
)

