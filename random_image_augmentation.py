import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import os

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]  # Lấy chiều cao (h) và chiều rộng (w) của hình ảnh

# Định nghĩa các hàm tăng cường hình ảnh
def translate(img, prob=0.5):
    # Dịch chuyển hình ảnh theo chiều ngang và chiều dọc
    if random.random() < prob:  # Kiểm tra xác suất
        x = random.randint(-w // 4, w // 4)  # Dịch chuyển ngẫu nhiên theo chiều ngang
        y = random.randint(-h // 4, h // 4)  # Dịch chuyển ngẫu nhiên theo chiều dọc
        M = np.float32([[1, 0, x], [0, 1, y]])  # Ma trận dịch chuyển
        img = cv2.warpAffine(img, M, (w, h))  # Áp dụng dịch chuyển
        return img, f"Translate({x}, {y})"  # Trả về hình ảnh đã dịch và mô tả
    return img, None  # Không thay đổi nếu không áp dụng dịch

def rotate(img, prob=0.5):
    # Xoay hình ảnh
    if random.random() < prob:
        angle = random.uniform(-30, 30)  # Chọn góc xoay ngẫu nhiên
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)  # Tạo ma trận xoay
        img = cv2.warpAffine(img, M, (w, h))  # Áp dụng xoay
        return img, f"Rotate({angle:.2f})"  # Trả về hình ảnh đã xoay và mô tả
    return img, None  # Không thay đổi nếu không áp dụng xoay

def resize(img, prob=0.5):
    # Thay đổi kích thước hình ảnh
    if random.random() < prob:
        scale = random.uniform(0.9, 1.1)  # Tạo tỷ lệ thay đổi kích thước ngẫu nhiên
        new_w, new_h = int(w * scale), int(h * scale)  # Tính toán kích thước mới
        img = cv2.resize(img, (new_w, new_h))  # Thay đổi kích thước
        img = cv2.resize(img, (w, h))  # Trả về kích thước gốc
        return img, f"Resize({scale:.2f})"  # Trả về hình ảnh đã thay đổi kích thước và mô tả
    return img, None  # Không thay đổi nếu không áp dụng thay đổi kích thước

def flip(img, prob=0.5):
    # Lật hình ảnh theo chiều ngang, dọc hoặc cả hai
    if random.random() < prob:
        flip_code = random.choice([-1, 0, 1])  # Chọn kiểu lật ngẫu nhiên
        img = cv2.flip(img, flip_code)  # Áp dụng lật
        flip_dir = "Horizontal" if flip_code == 1 else "Vertical" if flip_code == 0 else "Both"
        return img, f"Flip({flip_dir})"  # Trả về hình ảnh đã lật và mô tả
    return img, None  # Không thay đổi nếu không áp dụng lật

def crop(img, prob=0.5):
    # Cắt hình ảnh
    if random.random() < prob:
        # Giảm kích thước cắt để giữ lại nhiều hơn phần ảnh gốc
        margin_x = w // 10  # Tính toán kích thước lề theo chiều ngang
        margin_y = h // 10  # Tính toán kích thước lề theo chiều dọc
        start_x, start_y = margin_x, margin_y  # Điểm bắt đầu cắt
        end_x, end_y = w - margin_x, h - margin_y  # Điểm kết thúc cắt
        img = img[start_y:end_y, start_x:end_x]  # Cắt hình ảnh
        img = cv2.resize(img, (w, h))  # Trả về kích thước gốc
        return img, "Crop"  # Trả về hình ảnh đã cắt và mô tả
    return img, None  # Không thay đổi nếu không áp dụng cắt

# Áp dụng các biến đổi ngẫu nhiên
def random_transform(img, probabilities):
    transformations = [translate, rotate, resize, flip, crop]  # Danh sách các hàm biến đổi
    applied_transforms = []  # Lưu trữ các biến đổi đã áp dụng
    transformed_img = img.copy()  # Tạo bản sao của hình ảnh gốc để biến đổi
    
    # Chọn ngẫu nhiên 3 hàm từ danh sách
    selected_transforms = random.sample(transformations, 3)  
    
    for func in selected_transforms:
        prob = probabilities[transformations.index(func)]  # Lấy xác suất tương ứng
        transformed_img, desc = func(transformed_img, prob)  # Áp dụng biến đổi
        if desc:  # Nếu có biến đổi đã áp dụng
            applied_transforms.append(desc)  # Thêm mô tả vào danh sách
    
    return transformed_img, applied_transforms  # Trả về hình ảnh đã biến đổi và mô tả

# Lưu và hiển thị hình ảnh đã biến đổi
def display_images(images_with_text):
    num_images = len(images_with_text)  # Số lượng hình ảnh

    # Thiết lập kích thước khung hình để chứa nhiều hình ảnh
    plt.figure(figsize=(15, 15))
    
    for i, (img, transformations) in enumerate(images_with_text):
        # Thêm văn bản vào từng hình ảnh
        for j, text in enumerate(transformations):
            cv2.putText(img, text, (10, 30 + j * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

        plt.subplot(5, 4, i + 1)  # Sắp xếp thành 5 hàng, 4 cột
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Hiển thị hình ảnh
        plt.axis("off")  # Tắt trục
        plt.title(f"Image {i + 1}", fontsize=12)  # Tiêu đề cho mỗi hình ảnh
    
    plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Điều chỉnh khoảng cách giữa các hình ảnh
    plt.show()  # Hiển thị tất cả các hình ảnh

# Đặt xác suất cho các biến đổi
probabilities = [0.5, 0.5, 0.3, 0.3, 0.3]  # Giảm xác suất biến đổi

# Lưu tất cả hình ảnh đã biến đổi
augmented_images = []

# Số lần hiển thị hình ảnh biến đổi
num_iterations = 20  

# Thực hiện tăng cường hình ảnh nhiều lần
for _ in range(num_iterations):
    augmented_img, transformations = random_transform(img, probabilities)  # Áp dụng biến đổi ngẫu nhiên
    augmented_images.append((augmented_img, transformations))  # Thêm hình ảnh đã biến đổi vào danh sách

# Hiện thị tất cả các hình ảnh biến đổi
display_images(augmented_images)

cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ của OpenCV
