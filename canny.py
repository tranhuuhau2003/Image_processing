import cv2
import numpy as np
import matplotlib.pyplot as plt

def auto_canny(image, sigma=1):
    """
    Hàm auto_canny tự động xác định ngưỡng thấp và ngưỡng cao cho bộ lọc Canny.
    
    Tham số:
    - image: Ảnh xám đầu vào (grayscale image).
    - sigma: Tỷ lệ để điều chỉnh ngưỡng dựa trên độ lệch chuẩn (mặc định là 0.5).
    
    Trả về:
    - edges: Ảnh sau khi phát hiện cạnh bằng phương pháp Canny.
    """
    # Tính độ lệch chuẩn của ảnh
    std_dev = np.std(image)
    
    # Xác định ngưỡng thấp và ngưỡng cao dựa trên độ lệch chuẩn và sigma
    lower = int(std_dev * sigma)  # Ngưỡng thấp
    upper = int(std_dev * (8 * sigma))  # Ngưỡng cao
    
    # Áp dụng Canny với các ngưỡng tự động
    edges = cv2.Canny(image, lower, upper)
    return edges, lower, upper

# Tải hình ảnh từ đường dẫn đã cho
img = cv2.imread("L:\\NNLT_Python\\Xu-li-anh\\img\\bien_so_xe.jpg")

# Kiểm tra xem hình ảnh đã được tải hay chưa
if img is None:
    print("Không thể tải hình ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    # Chuyển đổi sang ảnh xám
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Làm mờ ảnh để giảm nhiễu
    blured_img = cv2.GaussianBlur(gray_img, (5,5), 0)
    
    # Áp dụng hàm auto_canny để phát hiện cạnh
    edges, low_threshold, high_threshold = auto_canny(blured_img)
    
    # Hiển thị kết quả
    plt.figure(figsize=(10, 8))

    # Ảnh gốc
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Ảnh Gốc')
    plt.axis('off')

    # Ảnh Canny với ngưỡng tự động
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title(f'Canny (Low: {low_threshold}, High: {high_threshold})')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
