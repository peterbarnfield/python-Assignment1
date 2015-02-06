score=0
while True:
    name=input("What is your name? ")
    if name=="":
        print("You didn't type anything. Please try again")
    else:
        break
print("Welcome "+name+" to the computing quiz")
print("Question 1")
while True:
    q1=input("What does RAM stand for, A-Read Access Memory, B-Randomly accused Memory,\nor C- Random Access Memory: ")
    q1=q1.lower()
    if q1=='c':
        score=score+1
        break
    elif q1=='a' or q1=='b':
        break
    else:
        print("You didn't eneter A, B or C, please try again")
print("Question 2")
while True:
    q2=input("What does ROM stand for, A-Read Only Memory, B-Randomly owned memory,\nor C- Random Only Memory: ")
    q2=q2.lower()
    if q2=='a':
        score=score+1
        break
    elif q1=='c' or q1=='b':
        break
    else:
        print("You didn't eneter A, B or C, please try again")
