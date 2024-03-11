#File: CS112_A1_T2_Game3_20230473.Py
#Purpose:This is a two-player mathematical game of strategy. It is played by two  
#people with a pile of coins (or other tokens) between them. The players take turns removing  
#coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …).  
#The player who removes the last coin wins.
#Author:Youmna Salah Abd El_hamid Ahmed
#ID:20230473
print("welcome to subtract a square game")
while True:
  print("A) random number")
  print("B) Enter a number")
  selection=input("Choose a selection")
  if selection.upper()=='A':
     import random
     excluded_squares=(i**2 for i in range(4,32))
     while True:
      Number =random.randint(10,1000)
      if Number not in excluded_squares:
        break
     print("A random number is ",Number)
     while Number>0:
      Player1_num = int(input("player1 enter a square number less than the random number "))
      square_root=Player1_num**0.5
      if square_root**2==Player1_num and square_root%1==0 and Player1_num<Number :
        Number-=Player1_num
        print(Number)
      
      else:
       print("This number is not square")
       continue
     
      if Number==0:
       print(" player1 is winner") 
       break
      while True:
       Player2_num = int(input("player2 enter a square number less than the random number"))
       square_root=Player2_num**0.5
       if square_root**2==Player2_num and square_root%1==0 and Player2_num<Number:
        Number-=Player2_num
        print(Number)
       else:
        print("This number is not square or bigger than the random number")
        continue
       if Number==0:
        print(" player2 is winner") 
       break

    
     
  elif selection.upper()=='B':
     Number=int(input("Enter a number "))
     while Number<=0:
      Number=int(input(" Please Enter a positive number "))
     while Number>0:
      Player1_num = int(input("player1 enter a square number less than and equal the number"))
      square_root=Player1_num**0.5
      if square_root**2==Player1_num and square_root%1==0 and Player1_num<=Number:
        Number-=Player1_num
        print(Number)
      else:
       print("This number is not square or bigger than or equal number")
       continue
     
      if Number==0:
       print(" player1 is winner") 
       break
      while True:
       Player2_num = int(input("player2 enter a square number less than and not equal number "))
       square_root=Player2_num**0.5
       if square_root**2==Player2_num and square_root%1==0 and Player1_num<=Number :
        Number-=Player2_num
        print(Number)
       else:
        print("This number is not square or bigger than the number or equal")
        continue
       if Number==0:
        print(" player2 is winner") 
       break
        
  else:
    print("Please choose a valid selection")
  
