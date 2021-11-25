# Fibonacci series
n=int(input("Enter number of terms upto where you print the seroes: "))    # Reading number for nterms
a=0
b=1
c=0
print("Fibonacci series upto ",n,"terms are:")
if(n<=0):
    print("Please enter positive number\n")
else:
    while(c<n):                     
        print(a)
        s=a+b                    # Logic for Fibonacci series
        a=b
        b=s
        c=c+1
