lst = []
start = int(input("Enter the starting number of the series: "))
end = int(input("Enter the ending number of the series: "))
n = int(start/3)
for i in range(0,n+1):
    ele = start - (3*i)
    if(ele<=end):
        break
    lst.append(ele)
print("The series generated is:\n",lst)