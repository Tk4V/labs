import sorting_methods


def run(start_index = 0, end_index = 0, sorting_type = 'bubble'):
  random_array = [1,10,3,8,4,14,2,2]
  print ( '-->>> Last index is ' + str(len(random_array)))
  start_index = start_index
  end_index = len(random_array) if end_index == 0 else end_index

  random_array = random_array[start_index:end_index]
  sorting_methods.print_sorted(random_array, sorting_type)



#run(start_index = 0, end_index = 0, sorting_type= 'bubble')
run(start_index = 0, end_index = 0, sorting_type= 'insert')
sorting_methods.insertion_sort([1,10,3,8,4,14,2,2])
# run(0,3, 'insert')
# run(0,3, 'selection')