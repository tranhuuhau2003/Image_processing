import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread('D:/Xu-li-anh/AI.jpg')  # Thay thế đường dẫn bằng đường dẫn ảnh của bạn
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Chuyển sang RGB để hiển thị màu đúng

# Chuyển sang ảnh xám
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tạo kernel cho các phép biến đổi
kernel = np.ones((5, 5), np.uint8)

# Áp dụng phép giãn (dilation)
img_dilated = cv2.dilate(img_gray, kernel, iterations=1)

# Áp dụng phép xói mòn (erosion)
img_eroded = cv2.erode(img_gray, kernel, iterations=1)

# Tính gradient hình thái học
img_gradient = cv2.morphologyEx(img_gray, cv2.MORPH_GRADIENT, kernel)

# Hiển thị ảnh gốc và các ảnh kết quả
plt.figure(figsize=(15, 8))

# Hiển thị ảnh gốc (màu)
plt.subplot(1, 5, 1)
plt.title('Color Image')
plt.imshow(img_rgb)
plt.axis('off')

# Hiển thị ảnh xám
plt.subplot(1, 5, 2)
plt.title('Gray Image')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

# Hiển thị ảnh giãn (dilation)
plt.subplot(1, 5, 3)
plt.title('Dilated Image')
plt.imshow(img_dilated, cmap='gray')
plt.axis('off')

# Hiển thị ảnh xói mòn (erosion)
plt.subplot(1, 5, 4)
plt.title('Eroded Image')
plt.imshow(img_eroded, cmap='gray')
plt.axis('off')

# Hiển thị gradient hình thái học
plt.subplot(1, 5, 5)
plt.title('Morphological Gradient')
plt.imshow(img_gradient, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
