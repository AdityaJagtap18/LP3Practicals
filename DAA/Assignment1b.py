# Python program to display the Fibonacci sequence
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 7
# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
            print(recur_fibo(i))
"""
Output:

PS C:\Users\tejas> & C:/Users/tejas/AppData/Local/Microsoft/WindowsApps/python3.11.exe e:/JAVA/Assignment2.py
Fibonacci sequence:
0
1
1
2
3
5
8
"""