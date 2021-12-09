#try it yourself page89
#5.8Hello admin
#note that I put parts of code as comment so python will ignore that part

#users=["admin", "mimouni", "hadjadj", "lachab", "guest"]
#if users:
#    for user in users:
#        if user=="admin":
#            print("Hello admin, would you like to see a status report")
#        else:
#            print(f"Hello {user}, thanks for logging in again")
#else:
#    print(" we need to find some users")

#5.10 checking usernames

#current_users=["souad", "leila","Walid", "hachemi","moussadegh","DAlila"]
#new_users=["khalil", "raouf", "souad", "dalila"]
#for i in range(6):
#    current_users[i]=current_users[i].lower()
#print(f"current users: {current_users})")
#for user in new_users:
#    if user in current_users:
#        print(f"{user} already exists, please enter a new user")
#    else:
#        print(f"{user} this user name is available")
#        current_users.append(user.lower())
#print(current_users)

#5.11 Ordinal numbers

digits=[1,2,3,4,5,6,7,8,9]
for digit in digits:
    if digit == 1:
        print("1st")
    elif digit == 2:
        print("2nd")
    elif digit == 3:
        print("3rd")
    else:
        print(f"{digit}th")