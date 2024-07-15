# Chuyển đổi ảnh màu - ảnh xám
# Đọc ảnh
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

img = mpimg.imread('D:\2. STUDY\1. AIO 2024\MODULE 2\Week 1\Numpy_ImageProcessing_TableSQL\dog.jpeg')

# Cách 1


def color2grayscale(vector):
    return np.max(vector)*0.5+np.min(vector)*0.5


gray_img_01 = np.apply_along_axis(color2grayscale,
                                  axis=2,
                                  arr=img)
print(gray_img_01[0, 0])

plt.imshow(gray_img_01, cmap=plt.get_cmap('gray'))
plt.show()

# Cách 2


def color2grayscale2(vector):
    return np.sum(vector)/3


gray_img_02 = np.apply_along_axis(color2grayscale2,
                                  axis=2,
                                  arr=img)
print(gray_img_02[0, 0])

plt.imshow(gray_img_02, cmap=plt.get_cmap('gray'))
plt.show()

# Cách 3


def color2grayscale3(vector):
    return vector[0]*0.21+vector[1]*0.72+vector[2]*0.07


gray_img_03 = np.apply_along_axis(color2grayscale3,
                                  axis=2,
                                  arr=img)
print(gray_img_03[0, 0])

plt.imshow(gray_img_03, cmap=plt.get_cmap('gray'))
plt.show()
