import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\img\\hand.jpg")

# Chuyển đổi ảnh sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Chuyển ảnh xám sang nhị phân
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Khởi tạo kernel cho phép mở
kernel = np.ones((3,3), np.uint8)

# Thực hiện phép mở
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Hiển thị kết quả
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title('Hình gốc')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Hình nhị phân')
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Kết quả phép mở')
plt.imshow(opening, cmap='gray')
plt.axis('off')

plt.show()
