import numpy as np
import re

'''
# Q1
import re
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

# Q2
def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result ** 0.5
    return result


a_arr = np.random.randn(20, 20)
b_arr = np.random.randn(20, 20)
print(len(np.reshape(b_arr, (20 * 20))))
print(l2_dist(np.reshape(a_arr, (20 * 20)), np.reshape(b_arr, (20 * 20, 1))))
print(l2_dist(a_arr, b_arr))
print(l2_dist(np.reshape(a_arr, (20 * 20)), np.reshape(b_arr, (20 * 20))))
print(l2_dist(a_arr.T, b_arr.T))

# Q3
a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1, 4, 4)
print(a1, a2, a3, a4, a5, sep='\n\n', end='\n--------\n')
print(a1.ndim, a2.ndim, a3.ndim, a4.ndim, a5.ndim, sep='\n\n', end='\n--------\n')
print(a1.shape, a2.shape, a3.shape, a4.shape, a5.shape, sep='\n\n', end='\n--------\n')

# Q4
old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0
print(old)

# Q5
arr = np.arange(36).reshape((6, 6))
print(arr[[2, 4], [2, 4]])
print(arr[2:3, 2:3])
print(arr[2:4, 2:4])
print(arr[[2, 3], [2, 3]])

# Q6
s = 'ACBCAC'
t = 'CABACBC'
print(re.findall(r'^AC', t))

# Q7
s = 'ACAABAACAAAB'
result = re.findall('A{1,2}', s)
res = re.finditer('A{1,2}', s)
for r in res:
    print(r)
print(len(result))

# Q8
s = """Office of Research Administration: (734) 647-6333 | 4325 North Quad
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
Office of the Dean: (734) 647-3576 | 4322 North Quad
UMSI Engagement Center: (734) 763-1251 | 777 North University
Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad"""
print(re.findall(r'[(]\d{3}[)]\s\d{3}[-]\d{4}', s))

# Q9
s = 'I refer to https://google.com and ' \
    'I never refer http://www.baidu.com if I have to search anything'
print(re.findall(r'(?<=[https]:\/\/)([A-Za-z0-9.]*)', s))
print(re.findall(r'(?<=https:\/\/)([.]*)', s))
print(re.findall(r'(?<=https:\/\/)([A-Za-z0-9]*)', s))
print(re.findall(r'(?<=https:\/\/)([A-Za-z0-9.]*)', s))

# Q10
text = r"""Everyone has the following fundamental freedoms:
(a) freedom of conscience and religion;
(b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
(c) freedom of peaceful assembly; and
(d) freedom of association.
"""

print(len(re.findall(r'[(][a-z][)]', text)))
print(len(re.findall(r'\(.\) ', text)))'''

