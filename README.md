# rock-paper-scissor-
game code
print("Lets Start the Game.........")
while True:
com = random.randint(1, 5)
     user = int(input("Enter the Number : "))
     if (com == user):
         print("You Win the Game")
     else:
         print("Com Win the Game")

     print("Computers Number : ",com)
     pg=input("Play Again (Yes/No): ")
     if pg=='Yes' or pg=='yes':
       continue
     else:
        break