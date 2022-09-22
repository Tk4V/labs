start = True
#i = lambda:n-1


try: 
    n = int(input('Enter n: ')) 
except ValueError: 
    print("Wrong input") 
    start = False 


if start: 

  for i in (range(1, n+1)[::-1]): 
      print(([g for g in range(1, i+1)]))

  for i in reversed(range(1, n+1)[::-1]): 
    print(([g for g in range(1, i+1)])) 