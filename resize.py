import cv2

# Đọc ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966263488289_871d634a1742dd7d2ba9d0b0585b7ede.jpg")
(h, w) = img.shape[:2]
print('Chiều cao ảnh: ', h)
print('Chiều rộng ảnh: ', w)

# Xác định toạ độ tâm và lấy màu tại tâm
center_x, center_y = w // 2, h // 2

cv2.imshow("old image", img) 
cv2.moveWindow("old image", 200, 100)  # Đặt vị trí cửa sổ ảnh gốc

new_width = 100 
ratio = new_width /img.shape[1]
dim = (new_width, int(img.shape[0] * ratio))
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.moveWindow("Resized", 1000, 300)  # Đặt vị trí cửa sổ ảnh gốc

cv2.waitKey(0)
