import statistics
import random
lst = []
for i in range(0, 5):
    ele = random.randint(0,100)
    lst.append(ele)
print("Marks in subject are:\n",lst)
pr = (statistics.mean(lst))
print("Your percentage is:",pr)
if(pr<50):
    print("Grade is F")
elif(pr>=50 or pr<60):
    print("Grade is D")
elif(pr>=60 or pr<70):
    print("Grade is C")
elif(pr>=70 or pr<80):
    print("Grade is B")
elif(pr>=80 or pr<90):
    print("Grade is A")
else:
    print("Grade is A+")