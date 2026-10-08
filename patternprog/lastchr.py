n =int(input("enter no of rows: " ))

for i in range(n):
    if i == 0 or i==n-1:
     print(" "*(n-i+1), end=" ")
    else:
       print(" ") 

    for j in range(2*i+1):
        if j == 0 or j == 2*i:
         print(chr(65+j), end = " ")
        else :
           print(" ")
          
    
    print()