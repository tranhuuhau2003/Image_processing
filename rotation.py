import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Xác định toạ độ tâm
center_x, center_y = w // 2, h // 2

# Xoay ảnh
angle = 90  # Góc xoay (độ)
scale = 0.5  # Tỷ lệ phóng đại (1.0 là không thay đổi kích thước)

# Tạo ma trận xoay
rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, scale)

# Áp dụng xoay
rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

# Hiển thị ảnh gốc và ảnh đã xoay
cv2.imshow("Ảnh gốc", img)
cv2.moveWindow("Ảnh gốc", 200, 100)  # Đặt vị trí cửa sổ ảnh gốc

cv2.imshow("Ảnh đã xoay", rotated_img)
cv2.moveWindow("Ảnh đã xoay", 800, 100)  # Đặt vị trí cửa sổ ảnh đã dịch chuyển


cv2.waitKey(0)
cv2.destroyAllWindows()
