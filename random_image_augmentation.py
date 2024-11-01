import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import os

# Load an image
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]

# Define augmentation functions
def translate(img, prob=0.5):
    if random.random() < prob:
        x = random.randint(-w // 4, w // 4)
        y = random.randint(-h // 4, h // 4)
        M = np.float32([[1, 0, x], [0, 1, y]])
        img = cv2.warpAffine(img, M, (w, h))
        return img, f"Translate({x}, {y})"
    return img, None

def rotate(img, prob=0.5):
    if random.random() < prob:
        angle = random.uniform(-30, 30)
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
        img = cv2.warpAffine(img, M, (w, h))
        return img, f"Rotate({angle:.2f})"
    return img, None

def resize(img, prob=0.5):
    if random.random() < prob:
        scale = random.uniform(0.9, 1.1)  # Giảm mức độ thay đổi kích thước
        new_w, new_h = int(w * scale), int(h * scale)
        img = cv2.resize(img, (new_w, new_h))
        img = cv2.resize(img, (w, h))  # Resize back to original dimensions
        return img, f"Resize({scale:.2f})"
    return img, None

def flip(img, prob=0.5):
    if random.random() < prob:
        flip_code = random.choice([-1, 0, 1])
        img = cv2.flip(img, flip_code)
        flip_dir = "Horizontal" if flip_code == 1 else "Vertical" if flip_code == 0 else "Both"
        return img, f"Flip({flip_dir})"
    return img, None

def crop(img, prob=0.5):
    if random.random() < prob:
        start_x, start_y = w // 8, h // 8  # Cắt nhỏ hơn để giữ nhiều phần của ảnh
        end_x, end_y = w * 7 // 8, h * 7 // 8
        img = img[start_y:end_y, start_x:end_x]
        img = cv2.resize(img, (w, h))  # Resize back to original dimensions
        return img, "Crop"
    return img, None

# Apply random transformations
def random_transform(img, probabilities):
    transformations = [translate, rotate, resize, flip, crop]
    applied_transforms = []
    transformed_img = img.copy()
    
    for func, prob in zip(transformations, probabilities):
        transformed_img, desc = func(transformed_img, prob)
        if desc:
            applied_transforms.append(desc)
    
    return transformed_img, applied_transforms

# Save and display augmented images
def display_image(img, transformations):
    plt.figure(figsize=(5, 5))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Applied Transformations:\n" + "\n".join(transformations), fontsize=12)
    plt.axis("off")
    plt.show()

# Set transformation probabilities
probabilities = [0.5, 0.5, 0.3, 0.3, 0.3]  # Giảm xác suất biến đổi

# Display images with keyboard interaction
num_iterations = 20  # Số lần hiển thị hình ảnh biến đổi

for _ in range(num_iterations):
    augmented_img, transformations = random_transform(img, probabilities)
    display_image(augmented_img, transformations)

    print("Press any key to see a new transformation.")

    # Chờ người dùng nhấn phím
    key = cv2.waitKey(0)  # Chờ một phím nhấn

cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ của OpenCV 
