user_1=input('Enter your name')
user_2=input('enter your name')
i=0
s1=0
s2=0
while i!=6:
    user1_input=input("""ENTER YOUR CHOICE
1. Enter 1 for stone
2. ENTER 2 FOR SCISSOR
3.Enter 3 for paper
4. Enter anything else to exit""")
    user2_input=input("""ENTER YOUR CHOICE
1. Enter 1 for stone
2. ENTER 2 FOR SCISSOR
3.Enter 3 for paper
4. Enter anything else to exit""")
    if user1_input=='1' and user2_input=='2':
        s1 = s1 + 1
        i = i + 1

    elif (user1_input =='2' and user2_input=='3'):
        s1 = s1 + 1
        i = i + 1
    elif (user1_input=='3' and user2_input=='1'):
        s1 = s1 + 1
        i = i + 1
    elif user1_input=='2' and user2_input=='1' :
        s2=s2+1
        i=i+1
    elif user1_input=='3' and user2_input=='2' :
        s2 = s2 + 1
        i = i + 1
    elif  user1_input=='1' and user2_input=='3' :
        s2 = s2 + 1
        i = i + 1
    else:
        print("byeee")
        break

if(s1>s2):

    print(user_1,'wins')
elif(s2>s1):
    print(user_2,'wins')
else:
    print('draw match')
