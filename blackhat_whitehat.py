import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\img\\bien_so_xe.jpg")

# Kiểm tra xem hình ảnh đã được tải hay chưa
if img is None:
    print("Không thể tải hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Tạo kernel (phần tử cấu trúc) để áp dụng các phép toán hình thái học
    kernel = np.ones((5, 5), np.uint8)
    
    # Áp dụng phép toán White Hat (Top Hat)
    white_hat = cv2.morphologyEx(gray_img, cv2.MORPH_TOPHAT, kernel)
    
    # Áp dụng phép toán Black Hat
    black_hat = cv2.morphologyEx(gray_img, cv2.MORPH_BLACKHAT, kernel)

    # Hiển thị ảnh gốc, ảnh White Hat và ảnh Black Hat bằng matplotlib
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh gốc
    plt.title("Hình ảnh gốc")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(white_hat, cmap="gray")  # Hiển thị ảnh White Hat
    plt.title("Ảnh White Hat")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(black_hat, cmap="gray")  # Hiển thị ảnh Black Hat
    plt.title("Ảnh Black Hat")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
