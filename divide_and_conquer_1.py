Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def divide_and_conquer(nums: list[int])->list[int]:
...     nums_a = []
...     nums_b = []
...     final_list = []
... 
... 
...     for num in nums:
...         if num < 500:
...             nums_a.append(num)
...         else:
...             nums_b.append(num)
... 
...     for i in range(len(nums_a)):
...         for j in range(0, len(nums_a)-1):
...             if nums_a[j] > nums_a[j+1]:
...                 nums_a[j], nums_a[j+1] = nums_a[j+1], nums_a[j]
...             
...     for b in range(len(nums_b)):
...         for c in range(0, len(nums_b)-1):
...             if nums_b[c] > nums_b[c+1]:
...                 nums_b[c], nums_b[c+1] = nums_b[c+1], nums_b[c]
...             
...             
...     final_list = nums_a + nums_b
...             
