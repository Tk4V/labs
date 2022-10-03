from merge import merge_sort


input_array = []
  
# number of elements as input
t = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, t):
    ele = int(input())
  
    input_array.append(ele)


n = len(input_array)
merge_sort(input_array, 0, n-1)
print("\n\nSorted array is: ")
for i in range(n):
    print("%d" % input_array[i],end=" ")