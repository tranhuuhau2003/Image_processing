import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\z5989234620386_19b6325f9d6bb67a9c17f08c8aee78ad.jpg")

# Kiểm tra xem hình ảnh đã được tải hay chưa
if img is None:
    print("Không thể tải hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng bảng màu cho ảnh xám
    img_color = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)

    # Tạo một kernel (mô hình) hình chữ nhật
    kernel = np.ones((5, 5), np.uint8)  # Kích thước kernel có thể thay đổi

    # Thực hiện phép xói mòn 3 lần bằng vòng lặp
    eroded_img = gray_img.copy()
    for _ in range(3):  # Lặp 3 lần
        eroded_img = cv2.erode(eroded_img, kernel, iterations=1)

    # Hiển thị ảnh gốc, ảnh màu đã áp dụng bảng màu, ảnh xám, ảnh xói mòn 1 lần và ảnh xói mòn 3 lần
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh gốc
    plt.title("Hình ảnh gốc")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh màu đã áp dụng bảng màu
    plt.title("Hình ảnh sau áp dụng màu")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(gray_img, cmap='gray')  # Hiển thị ảnh xám
    plt.title("Hình ảnh xám")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(eroded_img, cmap='gray')  # Hiển thị ảnh xói mòn 3 lần
    plt.title("Hình ảnh xói mòn 3 lần")
    plt.axis("off")

    plt.tight_layout()  # Điều chỉnh khoảng cách giữa các subplot
    plt.show()
