import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\img\\contour.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Hàm Auto Canny để tính toán các ngưỡng tự động
def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(image, lower, upper)
    return edges

auto_canny_edges = auto_canny(blurred)

# Tìm các đường viền (contours)
contours, _ = cv2.findContours(auto_canny_edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tạo bản sao ảnh để vẽ các đường viền
copied_img = img.copy()

# Lặp qua các contour và tính toán thông tin
for i, contour in enumerate(contours):
    # Lọc các contour quá nhỏ hoặc rỗng
    area = cv2.contourArea(contour)
    if area < 100:  # Loại bỏ contour có diện tích quá nhỏ
        continue

    perimeter = cv2.arcLength(contour, True)

    # Tìm tâm (centroid) của contour
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    # In ra chu vi, diện tích và tọa độ tâm trên console
    print(f"Contour {i + 1}:")
    print(f" - Area: {area}")
    print(f" - Perimeter: {perimeter}")
    print(f" - Center: ({cX}, {cY})\n")

    # Vẽ tâm lên ảnh
    cv2.circle(copied_img, (cX, cY), 5, (0, 0, 255), -1)  # Chấm đỏ tại tâm mỗi contour

# Vẽ các đường viền lên ảnh
cv2.drawContours(copied_img, contours, -1, (255, 255, 0), 2)

# Hiển thị ảnh với các đường viền và tâm
cv2.imshow("Contours with Centroids", copied_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
