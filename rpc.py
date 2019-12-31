# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:36:39 2019

@author: cousi
"""
import random

def computer(player_computer):    
    if player_computer == 1:
        print("computer's choice is : ROCK")
    elif player_computer == 2:
        print("computer's choice is: PAPER")
    else:
        print("computer's choice is : SCEASOR")

def user(choice):
       
    if choice==1:
        print("your choice is: ROCK")
    elif choice==2:
        print("Your choice is: PAPER")
    else:
        print("your choice is: SCEASOR")

def result():
    print("1> ROCK 2> SCEASOR 3>PAPER")
    choice = int(input("please choose: "))
    if choice>=4 and choice<=0:
        print("enter valid input.")
        print("1> ROCK 2> PAPER 3>SCEASOR")
        choice = input("please choose: ")
   
    user(choice)
    player_computer = random.randint(1,3)
    computer(player_computer)
    if (player_computer==1 and choice ==2) or (player_computer==3 and choice ==1) or player_computer==2 and choice ==3:
        print("YOU WIN!!!!!!!!!")
    elif (player_computer==1 and choice ==3) or (player_computer==2 and choice ==1) or (player_computer==3 and choice ==2):
        print("COMPUTER WIN!!!!!!!!!")
    else:
        print("DRAW")
        print("COMPUTER AND YOU BOTH CHOOSE SAME")
result()
   
    
            
        