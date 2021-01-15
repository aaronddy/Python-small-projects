import numpy as np

a = np.array([[2,3], [4, 2]])
print("a 크기:", a.shape)
print("a 타입:", a.dtype)
print(a)

b = np.array([['grape', 'banana'], [4, 2]])
print("b 크기:", b.shape)
print("b 타입:", b.dtype)
print(b)

c = np.array(['rainbow', 'umbrella', 'rain'])
print("c 크기:", c.shape)
print("c 타입:", c.dtype)
print(c)


' numpy 함수 '

zeros = np.zeros((3, 5))
print(zeros.shape)
print(zeros)

ones = np.ones((2, 9))
print(ones.shape)
print(ones)

arange1 = np.arange(5)                        # 0부터 5 이전까지
arange2 = np.arange(5, 10)                    # 5부터 10 이전까지
arange3 = np.arange(5, 15, 4)                 # 5부터 15 이전까지 4 간격으로
print("arange1:", arange1, "type", arange1.dtype)
print("arange2:", arange2)
print("arange3:", arange3)


trans = np.zeros((2, 8))
print(trans)

transs = np.transpose(trans)
print(transs)


''' 
 numpy array 사칙 연산 
 * 행렬과 다른 연산 방식 주의 *
'''

print("======")
arr1 = np.array([[2, 4, 10], [33, 8, 0.9]])
print("arr1", arr1.shape)
arr2 = np.array([[21, 2, 7], [4, 0.3, 7]])
print("arr2", arr2.shape)
print("======")

print("======")
print("+", arr1[0]+arr1[1])
print("*", arr1*arr2)
print("/", arr2[0]/arr1[1])
print("======")

print("===broadcasting===")
arr3 = np.array([5, 41, 20])
print("arr3", arr3.shape)
print("arr1+arr3", arr1+arr3)
print("arr1[1]+arr3", arr1[1]+arr3)
print("======")

print("===not working===")
arr4 = np.arange(10)
# print(arr4.shape)
# print("arr1+arr4", arr1+arr4)   error
# print(arr3+arr4)                error
print("======")






