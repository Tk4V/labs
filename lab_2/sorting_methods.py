# SortBubble
def bubble_sort(input_array, start_index = 0, end_index = -1 ):
    length = len(input_array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j]
                input_array[j] = input_array[j + 1]
                input_array[j + 1] = temp
    return input_array

#Сортування вставкою
def insertion_sort(input_array):
  for i in range(1, len(input_array)):
    key = input_array[i]
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >=0 and key < input_array[j] :
            input_array[j+1] = input_array[j]
            j -= 1
    input_array[j+1] = key

  return input_array


# #Сортування вибором
def selection_sort(input_array):
    size = len(input_array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if input_array[i] < input_array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (input_array[step], input_array[min_idx]) = (input_array[min_idx], input_array[step])

    return input_array


def print_sorted(array, sorting_type = ''):
  if sorting_type in ['selection', 'insert', 'bubble']:
    print('Sorted by ' + sorting_type +':')
  if sorting_type == 'bubble':
    print(bubble_sort(array))
  elif sorting_type == 'insert' :
    print(insertion_sort(array))
  elif sorting_type == 'selection':
    print(selection_sort(array))

  elif sorting_type not in ['selection', 'insert', 'bubble']:
    print('Sorted by all types:')
    print(selection_sort(array))
    print(insertion_sort(array))
    print(bubble_sort(array))

