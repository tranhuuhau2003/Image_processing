import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\img\\leaf.jpg")

# Kiểm tra xem hình ảnh đã được tải hay chưa
if img is None:
    print("Không thể tải hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Áp dụng ngưỡng đảo (THRESH_BINARY_INV) để chuyển sang ảnh nhị phân
    _, binary_inv_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)

    # Áp dụng toán tử gradient
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(binary_inv_img, cv2.MORPH_GRADIENT, kernel)

    # Hiển thị ảnh gốc, ảnh nhị phân đảo và ảnh gradient bằng matplotlib
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh gốc
    plt.title("Hình ảnh gốc")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(binary_inv_img, cmap="gray")  # Hiển thị ảnh nhị phân đảo
    plt.title("Ảnh nhị phân đảo")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(gradient, cmap="gray")  # Hiển thị ảnh gradient
    plt.title("Ảnh Gradient")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
