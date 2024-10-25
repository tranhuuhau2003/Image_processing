import cv2

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Xác định toạ độ tâm và lấy màu tại tâm
center_x, center_y = w // 2, h // 2
(b, g, r) = img[center_y, center_x]  # Lấy màu pixel tại tâm
print("Màu tại tâm ({}, {}) - Đỏ: {}, Xanh lá: {}, Xanh dương: {}".format(center_x, center_y, r, g, b))

# Lật ảnh theo chiều ngang
flipped_horizontal = cv2.flip(img, 1)  # 1: lật theo chiều ngang

# Lật ảnh theo chiều dọc
flipped_vertical = cv2.flip(img, 0)    # 0: lật theo chiều dọc

# Lật ảnh theo cả hai chiều
flipped_both = cv2.flip(img, -1)       # -1: lật cả hai chiều

# Hiển thị ảnh gốc và các ảnh đã lật
cv2.imshow("Ảnh gốc", img)
cv2.imshow("Lật theo chiều ngang", flipped_horizontal)
cv2.imshow("Lật theo chiều dọc", flipped_vertical)
cv2.imshow("Lật cả hai chiều", flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
