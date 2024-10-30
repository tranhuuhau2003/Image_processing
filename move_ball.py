import cv2
import numpy as np

# Đọc hình ảnh
img = cv2.imread("L:/NNLT_Python/Xu-li-anh/z5966644918373_7b172cc8fbab770b830f303be22d9a71.jpg")

# Tọa độ và bán kính của quả bóng (giả định)
x, y, r = 812, 218, 60  # Tọa độ tâm và bán kính

# Cắt vùng chứa quả bóng (hình vuông bao quanh quả bóng)
circle_roi = img[y-r:y+r, x-r:x+r]

# Tạo mặt nạ hình tròn
mask = np.zeros((2*r, 2*r), dtype=np.uint8)  # Kích thước của mặt nạ
cv2.circle(mask, (r, r), r, (255), -1)  # Vẽ hình tròn vào mặt nạ

# Áp dụng mặt nạ hình tròn vào vùng quả bóng
circle_with_mask = cv2.bitwise_and(circle_roi, circle_roi, mask=mask)

# Chọn vị trí mới để dán quả bóng (chỉ dán vùng tròn)
new_x, new_y = 400, 200
new_img = img.copy()

# Dán quả bóng vào vị trí mới (chỉ lấy phần hình tròn)
for c in range(0, 3):  # Lặp qua 3 kênh màu (BGR)
    new_img[new_y-r:new_y+r, new_x-r:new_x+r, c] = np.where(mask == 255, circle_with_mask[:, :, c], new_img[new_y-r:new_y+r, new_x-r:new_x+r, c])

# Hiển thị kết quả
cv2.imshow("Result", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
