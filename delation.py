import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\z5989404464457_9d96419ccaf336e300573682d6f30433.jpg")

# Kiểm tra xem hình ảnh đã được tải hay chưa
if img is None:
    print("Không thể tải hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Tạo một kernel cho phép dilation và erosion
    kernel = np.ones((3,3), np.uint8)  # Kích thước kernel có thể thay đổi

    # Thực hiện phép dilation 3 lần
    dilated_img = gray_img.copy()
    for i in range(3):
        dilated_img = cv2.dilate(dilated_img, kernel, iterations=1)

    # Thực hiện phép erosion 3 lần
    eroded_img = dilated_img.copy()
    for i in range(3):
        eroded_img = cv2.erode(eroded_img, kernel, iterations=1)

    # Hiển thị tất cả ảnh trong một frame
    plt.figure(figsize=(15, 5))

    # Hiển thị ảnh gốc
    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Hiển thị ảnh gốc
    plt.title("Hình ảnh gốc")
    plt.axis("off")

    # Hiển thị ảnh xám
    plt.subplot(1, 4, 2)
    plt.imshow(gray_img, cmap='gray')  # Hiển thị ảnh xám
    plt.title("Hình ảnh xám")
    plt.axis("off")

    # Hiển thị ảnh sau phép dilation
    plt.subplot(1, 4, 3)
    plt.imshow(dilated_img, cmap='gray')  # Hiển thị ảnh đã mở rộng
    plt.title("Hình ảnh sau Dilation")
    plt.axis("off")

    # Hiển thị ảnh sau phép erosion
    plt.subplot(1, 4, 4)
    plt.imshow(eroded_img, cmap='gray')  # Hiển thị ảnh đã xói mòn
    plt.title("Hình ảnh sau Erosion")
    plt.axis("off")

    plt.tight_layout()  # Điều chỉnh khoảng cách giữa các subplot
    plt.show()
