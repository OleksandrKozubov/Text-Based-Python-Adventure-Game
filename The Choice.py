import time as t
import random as r
import turtle
from turtle import *

def shot3():
   print("As he shoots he hits all of you...")
   t.sleep(0.5)
   print("Now you are all dead...")
   t.sleep(0.5)
   print("Game over!")
   t.sleep(0.5)

def shot2():
   print("As he shoots he did shot one of your crewmates...")
   t.sleep(0.5)
   print("That was the one with the most money...")
   t.sleep(0.5)
   print("You manage to get to the shelter but you have lost your mate and lost a lot of money...")
   t.sleep(0.5)

def shot1():
   print("As he shoots he did not shot anyone and you all escape!")
   t.sleep(0.5)
   print("Congratulations, you win!!!")
   t.sleep(0.5)

def run():
   print("You have decided to run forward with the rest of the team.")
   t.sleep(0.5)
   print("As you run you hear the cop behind!")
   t.sleep(0.5)
   print("He is far but he points the gun on you three!")
   t.sleep(0.5)
   print("You run as fast as you can and he starts to shoot!...")
   t.sleep(2)

def hop():
   print("You have decideed to hop on the train.")
   t.sleep(0.5)
   print("You get on it and think that all the danger is behind...")
   t.sleep(0.5)
   print("But unexpectedly your crewmate takes the pistol out of his pocket and points and you!")
   t.sleep(0.5)
   print("He says [I do not want to do it, but I have to...]")
   t.sleep(0.5)
   print("It turned out that he was an impostor and he shoots you and takes the money you have stolen...")
   t.sleep(0.5)
   print("Game over!")
   t.sleep(0.5)

def station():
   print("You have decided to go to the train station!")
   t.sleep(0.5)
   print("Near the station you get in police spikes!")
   t.sleep(0.5)
   print("Now you must run with the bags full of money through the railways!")
   t.sleep(0.5)
   print("You see the train that departs and one of your crewmates hops on it and tells you to go with him!")
   t.sleep(0.5)
   print("While the rest of the crew tells you to run with them!")
   t.sleep(0.5)
   print("Now you can hop on the train or run...")
   t.sleep(0.5)

def mate_slow():
   print("Your mate chose to go the slow way.")
   t.sleep(0.5)
   print("You are going to the narrow street.")
   t.sleep(0.5)
   print("But your mate does not know this road very well...")
   t.sleep(0.5)
   print("He drives extremely slow so the cops are blocking your way.")
   t.sleep(0.5)
   print("They have arrested you!")
   t.sleep(0.5)
   print("Game over!")
   t.sleep(0.5)

def mate_fast():
   print("Your mate chose to go the fast way.")
   t.sleep(0.5)
   print("He drives through the highway like a real recer!")
   t.sleep(0.5)
   print("You arrive to the shelter and meet up with the rest of the crew!")
   t.sleep(0.5)
   print("Congratulations, you win!!!")
   t.sleep(0.5)

def mate():
   print("Crewmate drives!")
   t.sleep(0.5)
   print("You get in the car and drive from the parking.")
   t.sleep(0.5)
   print("Now your mate has to decide which way to go, fast or slow...")
   t.sleep(1)

def you_slow():
   print("You chose to go the slow way.")
   t.sleep(0.5)
   print("You are going to the narrow street.")
   t.sleep(0.5)
   print("You manage to go through it safely!")
   t.sleep(0.5)
   print("You arrive to the shelter and meet up with the rest of the crew!")
   t.sleep(0.5)
   print("Congratulations, you win!!!")
   t.sleep(0.5)

def you_fast():
   print("You chose to go the fast way.")
   t.sleep(0.5)
   print("You enter the highway and going over 200km/h...")
   t.sleep(0.5)
   print("Sudenly you lost the control over the car!")
   t.sleep(0.5)
   print("You crash on the high speed and die with your crewmate...")
   t.sleep(0.5)
   print("Game over!")
   t.sleep(0.5)

def you():
   print("You drive!")
   t.sleep(0.5)
   print("You get in the car and drive from the parking.")
   t.sleep(0.5)
   print("Now you have two choices, to go faster but more dangerous way or to go slower but safer way...")
   t.sleep(0.5)

def lot():
   print("You have dicided to drive to the parking!")
   t.sleep(0.5)
   print("You have arrived on the spot you with your crewmate get out of the car.")
   t.sleep(0.5)
   print("You got to steal the car for you two...")
   t.sleep(0.5)
   print("You see a really fast sperts car and decide to steal it...")
   t.sleep(0.5)
   print("With your professional skills you do it really fast.")
   t.sleep(0.5)
   print("Now you need to decide who will be the driver, you or your crewmate...")
   t.sleep(0.5)

def r1():
   print("The robbery was successful!")
   t.sleep(0.5)
   print("You get in the car with your crew.")
   t.sleep(0.5)
   print("But then you hear the siren of police cars!")
   t.sleep(0.5)
   print("The pursuit beggins...")
   t.sleep(0.5)
   print("Now you have two choices, drive to the parking or to the train station...")
   t.sleep(0.5)

def emerald_escape():
   print("You chose to escape...")
   t.sleep(0.5)
   print("As you walk from the dungeon you hear a loud sound!")
   t.sleep(0.5)
   print("The floor have fallen in that room, it was a trap...")
   t.sleep(0.5)
   print("But fortunately you are safe!")
   t.sleep(0.5)

def emerald_take():
   print("You chose to take the emerald...")
   t.sleep(0.5)
   print("As you took it, you feel vibrations all over the place...")
   t.sleep(0.5)
   print("It was a trap!!!")
   t.sleep(0.5)
   print("The floor fell under you and you have died...")
   t.sleep(0.5)
   print("Game over!")
   t.sleep(0.5)

def tunnel_left():
   print("You chose to go left...")
   t.sleep(0.5)
   print("You appear in little room with the stend in the middle of it.")
   t.sleep(0.5)
   print("The stand has an beutiful emerald on it, but it is something about this stone that makes you doubt...")
   t.sleep(0.5)
   print("Will you take it or will you escape with no treasure?")
   t.sleep(0.5)
   print("[Take] or [Escape]:")
   t.sleep(0.5)

def ending_after_game():
   print("Now you are able to open the chest!!!")
   t.sleep(0.5)
   print("In the chest you find a giant ruby, then you are escaping the dungeon.")
   t.sleep(0.5)
   print("Congratulations, you win!!!")
   t.sleep(0.5)

def number_game():
   number = r.randint(1,10)
   print("Now guess the number between 1 and 10!")
   answer = int(input("Guess the number!:\n"))
   while answer != number:
     if answer > number:
         print("Your number is too big!")
         answer = int(input("Try again!:"))
     elif answer < number:
         print("Your number is too small!")
         answer = int(input("Try again!:"))
     else:
         break
   if answer == number:
     print("You win!")
     t.sleep(0.5)

def tunnel_right():
   print("You chose to go right...")
   t.sleep(0.5)
   print("You appear in beautiful room...")
   t.sleep(0.5)
   print("Then you find a chest!")
   t.sleep(0.5)
   print("But it has a sign on it that says:")
   print("[In order to open the chest you need to beat the game called [Number guesser]...]")
   t.sleep(0.5)
   print("Do you want to play the game and get a treasure?:")
   t.sleep(0.5)

def door_3():
   print("You have chosen the door...")
   t.sleep(0.5)
   print("As you go forward you fall into the water!")
   t.sleep(0.5)
   print("You see two tunnels, where should you go?...")
   t.sleep(0.5)

def door_2():
   print("You have chosen the door...")
   t.sleep(0.5)
   print("You have managed to escape the dungeon but without any treasure...")
   t.sleep(0.5)

def door_1():
   print("You have chosen the door...")
   t.sleep(0.5)
   print("But unfortunately you fall into the trap and die!")
   t.sleep(0.5)
   print("Game Over!")
   t.sleep(0.5)

def t1_2():
   print("As you are going down the staircase you hear a loud sound!")
   t.sleep(0.5)
   print("It was the door that closed behind!...")
   t.sleep(0.5)
   print("But you are going forward and find the room with 3 doors.")
   t.sleep(0.5)
   print("Choose the door [1],[2] or [3]:")
   t.sleep(0.5)

def t1_1_fight():
    print("You chose to fight!")
    t.sleep(1)
    print("You manage to kill the zombie with you torch!")
    t.sleep(0.5)
    print("But now you do not see anything, as you have broken the torch...")
    t.sleep(0.5)
    print("Now you are really scared and you run forward as fast as you can...")
    t.sleep(0.5)
    print("But little did you know that there is a spider nets all ahead!")
    t.sleep(0.5)
    print("You stuck in the nets and were eaten by hundreds of tiny spiders...")
    t.sleep(0.5)
    print("Game Over!")
    t.sleep(0.5)

def t1_1_run():
    print("You chose to run!")
    t.sleep(1)
    print("As you run forward you see that the entrance to the next room is full of spider nets...")
    t.sleep(0.5)
    print("But it was not a problem!")
    t.sleep(0.5)
    print("You managed to burn down all the nets!")
    t.sleep(0.5)
    print("You close the door behind you, and you appear in the room with the golden cup full of golden coins!!!")
    t.sleep(0.5)
    print("You grab the treasure and manage to escape the dungeon!!!")
    t.sleep(1)
    print("Congratulations, you win!!!")
    t.sleep(0.5)

def t1_1():
    print("As you are going forward with the torch you hear that the door behind you have closed!")
    t.sleep(0.5)
    print("You find the torch and manage to light it up! Now you have light.")
    t.sleep(0.5)
    print("All of the sudden you find a dead body. And you tried to check it...")
    t.sleep(0.5)
    print("It was a walking dead!")
    t.sleep(0.5)

def heart():
 turtle.title("Heart")
 color("red")
 bgcolor('black')
 begin_fill()
 pensize(3)
 left(50)
 forward(133)
 circle(50,200)
 right(140)
 circle(50,200)
 forward(133)
 t.sleep(5)
 end_fill()

def t1():
    print("You enter the dungeon through the secret entrance.")
    t.sleep(0.5)
    print("Everything seems fine until you fall into the trap!")
    t.sleep(0.5)
    print("You apear in the room with two doors, one goes upstairs, another goes downstairs, you should choose where to go...")
    t.sleep(0.5)

def menu():
    print("Welcome to my game [The Choice]!")
    t.sleep(1)
    print("Please, choose the character you want to play as.")
    t.sleep(0.5)
    print("Enter [Traveler] to play as traveler.")
    t.sleep(0.5)
    print("Enter [Robber] to play as robber.")
    t.sleep(0.5)

def beginning_t():
    print("You are the treveler - explorer and you went to Columbia to the dungeon that was locked for hundreds of years...")
    t.sleep(0.5)
    print("It is told that there are many treasures inside, but it is very dangerous...")
    t.sleep(0.5)
    print("But you were brave enough to explore it!")
    t.sleep(0.5)

def no_c():
   print("There is no such choice.\nTry again!")
   t.sleep(0.5)
   exit()

def no_d():
   print("There is no such direction.\nTry again!")
   t.sleep(0.5)
   exit()

def beginning_r():
    print("You are professional robber from Los Angeles.")
    t.sleep(0.5)
    print("You and your crew have decided to rob the bank.")
    t.sleep(0.5)
    print("You have a perfect plan and it goes well...")
    t.sleep(0.5)




#Main Program
repeating = "Yes"
menu()
while repeating == "Yes" or repeating == "yes" or repeating == "Y" or repeating == "y":
    character = (input("Enter to name of the character:\n"))
    if character == "Traveler" or character == "traveler" or character == "t":
     print("You chose to play as a Traveler!")
     t.sleep(1)
     beginning_t()
     t1()
     print("Choose the door ([Up] or [Down]):")
     door = input("")
     t.sleep(1)
     if door == "Up" or door == "up" or door == "u":
         print("You chose to go upstairs...")
         t.sleep(1)
         t1_1()
         print("You have two choices run, or fight it ([Run] to run, [Fight] to fight): ")
         choice_t1 = input("")
         if choice_t1 == "Run" or choice_t1 == "run" or choice_t1 == "r":
             t.sleep(1)
             t1_1_run()
         elif choice_t1 == "Fight" or choice_t1 == "fight" or choice_t1 == "f":
             t.sleep(1)
             t1_1_fight()
         else: no_c()
     elif door == "Down" or door == "down" or door == "d":
         print("You chose to go downstairs")
         t.sleep(1)
         t1_2()
         random_door = (input(""))
         if random_door == "1":
            door_1()
         elif random_door == "2":
            door_2()
         elif random_door == "3":
            door_3()
            print("[Right] to go right and [Left] to go left:")
            tunnel = input("")
            if tunnel == "Right" or tunnel == "right" or tunnel == "r":
               tunnel_right()
               choice_treasure = input("")
               if choice_treasure == "Yes" or choice_treasure == "yes" or choice_treasure == "y":
                  t.sleep(1)
                  number_game()
                  t.sleep(1)
                  ending_after_game()
               elif choice_treasure == "No" or choice_treasure == "no" or choice_treasure == "n":
                  print("You chose not to take the treasure!")
                  t.sleep(0.5)
                  print("You managed to escape! But did not obtain any treasure...")
               else: no_c()
            elif tunnel == "Left" or tunnel == "left" or tunnel == "l":
               tunnel_left()
               emerald = input("")
               if emerald == "Take" or emerald == "take" or emerald == "t":
                  emerald_take()
               elif emerald == "Escape" or emerald == "escape" or emerald == "e":
                  emerald_escape()
               else: no_c()
         else: no_c()
     else: 
         no_d()
    elif character == "Robber" or character == "robber" or character == "r":
     print("You chose to play as a Robber!")
     t.sleep(1)
     beginning_r()
     r1()
     t.sleep(0.5)
     print("Choose the direction [Parking] or [Station]:")
     direction = input("")
     if direction == "Parking" or direction == "parking" or direction == "p":
        lot()
        t.sleep(0.5)
        print("Choose the driver [You] or [Mate]:")
        driver = input("")
        if driver == "You" or driver == "you" or driver == "y":
           you()
           t.sleep(0.5)
           print("Choose which way to go [Fast] or [Slow]:")
           way_you = input("")
           if way_you == "Fast" or way_you == "fast" or way_you == "f":
            you_fast()
           elif way_you == "Slow" or way_you == "slow" or way_you == "s":
            you_slow()
           else: 
              no_c()
        elif driver == "Mate" or driver == "mate" or driver == "m":
           mate()
           mate_choice = r.randint(1,2)
           if mate_choice == 1: 
              mate_fast()
           elif mate_choice == 2:
              mate_slow()
        else: no_c()
     elif direction == "Station" or "station" or "s":
        station()
        print("Choose [Hop] or [Run]:")
        choice_rob = input("")
        if choice_rob == "Hop" or choice_rob == "hop" or choice_rob == "h":
           hop()
        elif choice_rob == "Run" or  choice_rob == "run" or choice_rob == "r":
           run()
           shot = r.randint(1,3)
           if shot == 1:
              shot1()
           elif shot == 2:
              shot2()
           elif shot == 3:
              shot3()
        else:
           no_c()
     else: 
        no_d()
    elif character == "Heart":
     heart()
    else: no_c()
    print("Do you want to play again? ([Yes] or [No])")
    repeating = input("")
print("Thank you for playing, goodbye!")