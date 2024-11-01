import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread('Xu-li-anh\z5989234620386_19b6325f9d6bb67a9c17f08c8aee78ad.jpg')

# Chuyển ảnh sang không gian màu HSV để dễ dàng phân tách màu
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Định nghĩa khoảng màu cho cà chua (HSV)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Tạo mặt nạ cho cà chua
mask1 = cv2.inRange(hsv, lower_red, upper_red)

# Định nghĩa khoảng màu cho cà chua đỏ (phạm vi khác)
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Kết hợp hai mặt nạ
mask = mask1 | mask2

# Tạo mặt nạ ngược để bảo vệ phần cà chua
mask_inv = cv2.bitwise_not(mask)

# Tách các kênh màu
(B, G, R) = cv2.split(img)

# Xử lý với phép co lại 5 lần trên các kênh màu nền
eroded_B = B.copy()
eroded_G = G.copy()
eroded_R = R.copy()

for i in range(5):
    eroded_B = cv2.erode(eroded_B, None, iterations=1)
    eroded_G = cv2.erode(eroded_G, None, iterations=1)
    eroded_R = cv2.erode(eroded_R, None, iterations=1)

# Kết hợp các kênh đã xử lý với mặt nạ
new_B = cv2.bitwise_and(eroded_B, eroded_B, mask=mask_inv)
new_G = cv2.bitwise_and(eroded_G, eroded_G, mask=mask_inv)
new_R = cv2.bitwise_and(eroded_R, eroded_R, mask=mask_inv)

# Kết hợp lại các kênh màu
new_img = cv2.merge([new_B + cv2.bitwise_and(B, B, mask=mask),
                      new_G + cv2.bitwise_and(G, G, mask=mask),
                      new_R + cv2.bitwise_and(R, R, mask=mask)])

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow("Anh goc", img)
cv2.imshow("Anh phuc hoi", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()