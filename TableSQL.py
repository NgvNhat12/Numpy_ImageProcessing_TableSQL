import pandas as pd
import numpy as np

#đọc tệp CSV vào pandas Data Frame
df = pd.read_csv('D:\2. STUDY\1. AIO 2024\MODULE 2\Week 1\Numpy_ImageProcessing_TableSQL\advertising.csv')

data = df.to_numpy()
print(data)

#Câu 15
sale_data = data[:,3]
sale_max = np.max(sale_data)
sale_index = np.argmax(sale_data)
sale_max, sale_index

#Câu 16
tv_mean = np.mean(data[:,0])
tv_mean

#Câu 17
sale_counter = np.sum(data[:,3]>=20)
sale_counter

#Câu 18
sale_cond = data[:,3]>15
radio_data = data[:,1]
radio_cond = radio_data * sale_cond
radio_mean = np.sum(radio_cond)/np.sum(sale_cond)
radio_mean

#Câu 19
newspaper_data = data[:,2]
newspaper_mean = np.mean(newspaper_data)
newspaper_cond = newspaper_data > newspaper_mean
sale_data = data[:,3]
sale_cond = sale_data * newspaper_cond
sale_sum = np.sum(sale_cond)
sale_sum

#Câu 20
sale_data = data[:,3]
A = np.mean(sale_data)

score_sale = np.where(
    sale_data > A, "Good",
    np.where(sale_data == A, "Average", "Bad")
  )
score_sale

#Câu 21
sale_data = data[:,3]
A = np.mean(sale_data)
sub_mean = sale_data - A
sub_abs = abs(sub_mean)
average_idx = np.argmin(sub_abs)
#average_idx
sale_average = sale_data[average_idx]
#sale_average
score_sale = np.where(
    sale_data > sale_average, "Good",
    np.where(sale_data == sale_average, "Average", "Bad")
  )
score_sale
