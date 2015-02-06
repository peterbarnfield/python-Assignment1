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
        print("You didn't enter A, B or C, please try again")
print(score)
print(q1)
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
        print("You didn't enter A, B or C, please try again")
print("Question 3")
while True:
    q3=input("What does HTTP stand for, A-Hyper Text Transfer Protocol, B-Highly Transferable Text Pricipal,\nor C-Highly Transferable Text Protocol: ")
    q3=q3.lower()
    if q3=='a':
        score=score+1
        break
    elif q1=='c' or q1=='b':
        break
    else:
        print("You didn't enter A, B or C, please try again")
print("Question 4")
while True:
    q3=input("What does WWW. stand for, A-World Wide Web, B-Website World Wide,\nor C-Wireless World Website ")
    q3=q3.lower()
    if q3=='a':
        score=score+1
        break
    elif q1=='c' or q1=='b':
        break
    else:
        print("You didn't enter A, B or C, please try again")
print("Question 5")
while True:
    q3=input("What does FTP stand for, A-File Transfer Practice, B-Files Transfered Princible,\nor C-File Transfer Protocol: ")
    q3=q3.lower()
    if q3=='a':
        score=score+1
        break
    elif q1=='c' or q1=='b':
        break
    else:
        print("You didn't enter A, B or C, please try again")
print(name+" your score was "+score)
if score>=3:
    print("Well Done "*5)

