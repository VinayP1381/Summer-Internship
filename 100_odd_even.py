def isEven(n):
     
    # n&1 is 1, then odd, else even
    return (not(n & 1))
     
# Driver code
n = 101;
print("Even" if isEven(n) else "Odd")