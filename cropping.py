import cv2

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Xác định vùng cắt (cắt từ (x1, y1) đến (x2, y2))
x1, y1 = 100, 100  # Tọa độ góc trên bên trái
x2, y2 = 300, 300  # Tọa độ góc dưới bên phải

# Cắt ảnh
cropped_img = img[y1:y2, x1:x2]

# Hiển thị ảnh gốc và ảnh đã cắt
cv2.imshow("Ảnh gốc", img)
cv2.imshow("Ảnh đã cắt", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
