currentpassword = int(input())
actualpassword = 4567
attemptscount=3
for i in range(3):
     
     if currentpassword == actualpassword:
         print("successfully logged in")
         break
     else:
        if attemptscount == 1:
            print("your account is blocked,try after 24 hours")
        else:
            print("incorrect password ,your left with",attemptscount - 1,"attempts")
     attemptscount -= 1
