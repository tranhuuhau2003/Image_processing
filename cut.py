import cv2

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Xác định toạ độ tâm và lấy màu tại tâm
center_x, center_y = w // 2, h // 2
(b, g, r) = img[center_y, center_x]  # Sửa lại chỉ số
print("Pixel tại tâm ({}, {}) - Đỏ: {}, Xanh lá: {}, Xanh dương: {}".format(center_x, center_y, r, g, b))

# Đổi màu tâm ảnh thành màu đen
img[center_y, center_x] = (0, 0, 0)
(b, g, r) = img[center_y, center_x]  # Sửa lại chỉ số
print("Pixel tại tâm ({}, {}) - Đỏ: {}, Xanh lá: {}, Xanh dương: {}".format(center_x, center_y, r, g, b))

# Cắt ảnh thành 4 phần
top_left = img[0:center_y, 0:center_x]  # Góc trên bên trái
top_right = img[0:center_y, center_x:w]  # Góc trên bên phải
bottom_left = img[center_y:h, 0:center_x]  # Góc dưới bên trái
bottom_right = img[center_y:h, center_x:w]  # Góc dưới bên phải

# Hiển thị các phần cắt
cv2.imshow("Top Left", top_left)
cv2.imshow("Top Right", top_right)
cv2.imshow("Bottom Left", bottom_left)
cv2.imshow("Bottom Right", bottom_right)

cv2.waitKey(0)
cv2.destroyAllWindows()
