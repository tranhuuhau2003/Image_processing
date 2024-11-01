import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread('cachua.jpg')
(B, G, R) = cv2.split(img)

# Erode các kênh màu
for i in range(0, 5):
    eroded_B = cv2.erode(B.copy(), None, iterations=i + 1)
    eroded_G = cv2.erode(G.copy(), None, iterations=i + 1)
    eroded_R = cv2.erode(R.copy(), None, iterations=i + 1)

# Ghép các kênh màu lại với nhau
new_img = cv2.merge([eroded_B, eroded_G, eroded_R])

# Ghép hai ảnh lại với nhau
combined_img = np.hstack((img, new_img))

# Hiển thị ảnh gốc và ảnh đã xử lý trên cùng một màn hình
cv2.imshow("Anh goc và Anh phuc hoi", combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
