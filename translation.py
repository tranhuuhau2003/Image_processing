import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Xác định toạ độ tâm và lấy màu tại tâm
center_x, center_y = w // 2, h // 2

# Dịch chuyển ảnh
translation_x = 100  # Dịch sang phải 50 pixel
translation_y = 50  # Dịch xuống 30 pixel

# Tạo ma trận dịch chuyển
translation_matrix = np.float32([[1, 0, translation_x], [0, 1, translation_y]])

# Áp dụng dịch chuyển
translated_img = cv2.warpAffine(img, translation_matrix, (w, h))

# Hiển thị ảnh gốc và ảnh đã dịch chuyển
cv2.imshow("Ảnh gốc", img)
cv2.moveWindow("Ảnh gốc", 200, 100)  # Đặt vị trí cửa sổ ảnh gốc

cv2.imshow("Ảnh đã dịch chuyển", translated_img)
cv2.moveWindow("Ảnh đã dịch chuyển", 800, 100)  # Đặt vị trí cửa sổ ảnh đã dịch chuyển

cv2.waitKey(0)
cv2.destroyAllWindows()
