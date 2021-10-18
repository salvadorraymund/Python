from array import array
"""i at the beginning means you are going to use integer data type"""
arr1 = array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(arr1)
arr2 = array('i', [elem * 2 for elem in arr1])
print(arr2)
