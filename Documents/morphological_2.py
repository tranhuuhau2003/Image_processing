import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\z5989234620386_19b6325f9d6bb67a9c17f08c8aee78ad.jpg")

# Kiểm tra xem hình ảnh đã được tải hay chưa
if img is None:
    print("Không thể tải hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Tách ảnh thành 3 kênh màu R, G, B
    b, g, r = cv2.split(img)  # OpenCV đọc ảnh theo thứ tự BGR

    # Tạo một kernel (mô hình) hình chữ nhật
    kernel = np.ones((5,5), np.uint8)  # Kích thước kernel có thể thay đổi

    # Thực hiện phép xói mòn 5 lần cho từng kênh
    eroded_r = r.copy()
    eroded_g = g.copy()
    eroded_b = b.copy()

    for _ in range(3):  # Lặp 5 lần
        eroded_r = cv2.erode(eroded_r, kernel, iterations=1)
        eroded_g = cv2.erode(eroded_g, kernel, iterations=1)
        eroded_b = cv2.erode(eroded_b, kernel, iterations=1)

    # Hợp nhất các kênh màu lại với nhau
    merged_img = cv2.merge((eroded_b, eroded_g, eroded_r))  # Thứ tự là BGR

    # Hiển thị tất cả ảnh trong một frame
    plt.figure(figsize=(10, 5))

    # Hiển thị ảnh gốc
    plt.subplot(2, 4, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh gốc
    plt.title("Hình ảnh gốc")
    plt.axis("off")

    # Hiển thị các kênh màu
    plt.subplot(2, 4, 2)
    plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))  # Hiển thị kênh màu B
    plt.title("Kênh màu B")
    plt.axis("off")

    plt.subplot(2, 4, 3)
    plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))  # Hiển thị kênh màu G
    plt.title("Kênh màu G")
    plt.axis("off")

    plt.subplot(2, 4, 4)
    plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))  # Hiển thị kênh màu R
    plt.title("Kênh màu R")
    plt.axis("off")

    # Hiển thị các kênh màu đã xói mòn
    plt.subplot(2, 4, 5)
    plt.imshow(cv2.cvtColor(eroded_b, cv2.COLOR_BGR2RGB))  # Hiển thị kênh màu B đã xói mòn
    plt.title("Kênh B sau xói mòn")
    plt.axis("off")

    plt.subplot(2, 4, 6)
    plt.imshow(cv2.cvtColor(eroded_g, cv2.COLOR_BGR2RGB))  # Hiển thị kênh màu G đã xói mòn
    plt.title("Kênh G sau xói mòn")
    plt.axis("off")

    plt.subplot(2, 4, 7)
    plt.imshow(cv2.cvtColor(eroded_r, cv2.COLOR_BGR2RGB))  # Hiển thị kênh màu R đã xói mòn
    plt.title("Kênh R sau xói mòn")
    plt.axis("off")

    # Hiển thị ảnh đã hợp nhất
    plt.subplot(2, 4, 8)
    plt.imshow(cv2.cvtColor(merged_img, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh đã hợp nhất
    plt.title("Hình ảnh sau khi hợp nhất")
    plt.axis("off")

    plt.tight_layout()  # Điều chỉnh khoảng cách giữa các subplot
    plt.show()
