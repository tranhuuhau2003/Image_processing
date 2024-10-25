import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Tạo mặt nạ giống như ảnh gốc
mask = np.zeros_like(img)  # Tạo mặt nạ có cùng kích thước với ảnh gốc

# Định nghĩa tọa độ và bán kính hình tròn
center = (w // 2, h // 2)  # Tọa độ tâm hình tròn
radius = 150  # Bán kính hình tròn

# Vẽ hình tròn lên mặt nạ
cv2.circle(mask, center, radius, (255, 255, 255), -1)  # Màu trắng (255) và độ dày -1 để làm đầy

# Áp dụng mặt nạ lên ảnh gốc
masked_img = cv2.bitwise_and(img, mask)

# Hiển thị ảnh gốc, mặt nạ và ảnh đã áp dụng mặt nạ
cv2.imshow("Ảnh gốc", img)
cv2.imshow("Mặt nạ", mask)
cv2.imshow("Hình tròn trên ảnh", masked_img)


# Chỉnh vị trí của các cửa sổ
cv2.moveWindow("Ảnh gốc", 0, 100)        # Đặt vị trí cửa sổ Ảnh gốc
cv2.moveWindow("Mặt nạ", 520, 100)         # Đặt vị trí cửa sổ Mặt nạ
cv2.moveWindow("Hình tròn trên ảnh", 1040, 100)  # Đặt vị trí cửa sổ Hình tròn trên ảnh

cv2.waitKey(0)
cv2.destroyAllWindows()
