def merge(input_array, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    #Створення масивів
    for i in range(0, n1):
        L[i] = input_array[l + i]
 
    for j in range(0, n2):
        R[j] = input_array[m + 1 + j]
 
    
    i = 0     #ініціалізуємо індекси
    j = 0     #ініціалізуємо індекси
    k = l     #передаємо значення
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            input_array[k] = L[i]
            i += 1
        else:
            input_array[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        input_array[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        input_array[k] = R[j]
        j += 1
        k += 1

def merge_sort(input_array, l, r):
    if l < r:
        m = l+(r-l)//2 #формула
        ######################
        merge_sort(input_array, l, m)
        merge_sort(input_array, m+1, r)
        merge(input_array, l, m, r)

