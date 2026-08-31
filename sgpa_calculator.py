#finding sgpa
print("KTU SGPA calculator")
n=int(input("enter your sub number"))
total_credits=0
total_points=0

for i in range(n):
    print(f"\nsubject{i+1}:")
    grade=input("grade(o,A+,A,B+,B,C,P,F)")
    credit=int(input("enter credits"))

#KTU gade point
if grade=="o":
    point=10
elif grade=="A+":
    point=9
elif grade=="A":
    point=8.5
elif grade=="B+":
    point=7
elif grade=="c":
    point=6
elif grade=="P":
    point=5
else:
    point=0

total_points+=point*credit
total_credits+=credit

sgpa=total_points/total_credits
print(f"sgpa:{sgpa:2f}")
if sgpa>=8:
    print("worth it CJ!! grove street proud!")
else:
    print("try on next sem dude")
    
