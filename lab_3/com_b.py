#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#with repetitions
def a_n_k(n,k):
  if k >= n:
    return 'invalid' 
  return factorial(n)//(factorial(n-k))

#without repetitions
def _a_n_k(n,k):
  return n**k

#combination
def C(n,k):
  return factorial(n)//(factorial(k)*factorial(n-k))

#combination without repetitions
def _C(n,k):
  return factorial(n + k -1)//(factorial(k)*factorial(n-1))


def Gen_perm(A):
    f = open("permutations.txt", "w")
    for i in range(factorial(len(A))):        
        f.write(str(i+1) + ': ' + str(A) + "\n")   
        p = len(A)-1

        while (p > 0) and (A[p-1] > A[p]):        
            p=p-1
        A[p:] = reversed(A[p:]) 
        if p > 0: 
            q = p 
            while A[p-1] > A[q]:   
                q=q+1
        A[p-1],A[q]=A[q],A[p-1]

    f.close()
    print("look at permutations.txt to find permutations")
        


def gen_comb(arr, k):
    n = len(arr)
    index = 0
    for i in range(k-1, -1, -1):
        if arr[i] != n - k + i + 1:
            index = i
            break
    arr[index] += 1
    for i in range(index, k):

        arr[i+1] = arr[i]+1

def GenComb(n, k):
    f = open("combinations.txt", "w")
    arr = list(range(1, n+1))
    arr.sort()
    for i in range(C(len(arr), k)):
        f.write(str(i+1) + ': ' + str(tuple(arr[:k])) + "\n")   
        print(tuple(arr[:k]))
        gen_comb(arr, k)
    f.close()

