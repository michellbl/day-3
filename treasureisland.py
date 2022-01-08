print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
def line():
  print("*" * 60)

print("Welcome to Treasure Island.")
line()
print("Your mission is to find the treasure.") 
line()
name = ("Chose your name, adveturer: ")
# game start here
print("you awake in a beach, you can see a skull, a old rusty sword and a bucket. You can can carry only one item.")
line()
print("Choose wisely!")
line()

# the player chose his first item
first_item = input("Write the item... sword, bucket or skull. ")

if first_item == "sword":
    print("The sworld is to old, cant cut anything more, but you take it")
    line()
    print("You to the horizon and see a cave, to your left is an boat, to your right your see sea, what you chose")
    line()
# if sword is chosen as first item, the player must chose a way to continue the adventure
    first_choice = input("cave, boat or sea? ")
    line()
    if first_choice == "cave":
        print("inside is a troll, you use the sword, but it cant resist the troll attack... the world is sooo violent, what is that light...")
        line()
        print("Game Over")
        line()
        print('''

             ..............
   ::::::::::::::::::
  :::::::::::::::
 :::`::::::: :::     :
 :::: ::::: :::::    :
 :`   :::::;     :..~~
 :   ::  :::.     :::.
 :...`:, :::::...:::
::::::.  :::::::::'
 ::::::::|::::::::  !
 :;;;;;;;;;;;;;;;;']}
 ;--.--.--.--.--.-
  \/ \/ \/ \/ \/ \/
     :::       ::::
      :::      ::
     :\:      ::
   /\::    /\:::
 ^.:^:.^^^::`::
 ::::::::.::::
  .::::::::::
        
        ''')
    if first_choice == "sea":
        print("You start to swim, you realise no treasure is too good to risk your life.")
        line()
        print("Game Over!")
        line()
        print('''

                                                                            ..%%%%%
                                                          ...    .%%%%%%""
                                                       .%%%%%%%/%%%%%"
                                     .....           .%%%%%%%%%%%%%%\
                                ..:::::::::::..      :;""  {_}\%%/%%%%%%..
                              .:::::::::::::::::.            {_}/{_}%%%%%%%
                             :::::::::::::::::::::            \\//    """\::
                            :::::::::::::::::::::::           \\//
---____-----__---------_____----....-----..--.....~-----_____-\\//---_____-
-----___---___----____--__--_.----...----...----..---__--_-___\\//--___--__
--____----__-___-----____----_...-----..--..---..___-------__\\//_-----____
___----____------____---__--___..--..-..----....___-----___--\\//_---__----
---___--___--__---__----___---___..----------._---____-----__\\//___---__--
--___---_-___-------______------___--___----___--__------___-\\//__--__----
____------____----_________------__                         \\//
--_____--__--____                              '            \\//  _
__---                 @            ,                  "          {_}
             .                            '                            cgmm

        ''')
    if first_choice == 'boat':
        print("Its too good to be real, the boat is sicking....bloooo, glooop.... bloooog.... .....")
        line()
        print("Game Over!")
        line()      
        print('''
        
          ..............
   ::::::::::::::::::
  :::::::::::::::
 :::`::::::: :::     :
 :::: ::::: :::::    :
 :`   :::::;     :..~~
 :   ::  :::.     :::.
 :...`:, :::::...:::
::::::.  :::::::::'
 ::::::::|::::::::  !
 :;;;;;;;;;;;;;;;;']}
 ;--.--.--.--.--.-
  \/ \/ \/ \/ \/ \/
     :::       ::::
      :::      ::
     :\:      ::
   /\::    /\:::
 ^.:^:.^^^::`::
 ::::::::.::::
  .::::::::::


        ''')
# if player chose the skull, the game ending
elif first_item == "skull":
    print("Oh no, its a trap... you can smell an acid air... the lights start to become.... very bluuuury")
    line()
    print("Game Over!")
    line()
    print('''

         ..............
   ::::::::::::::::::
  :::::::::::::::
 :::`::::::: :::     :
 :::: ::::: :::::    :
 :`   :::::;     :..~~
 :   ::  :::.     :::.
 :...`:, :::::...:::
::::::.  :::::::::'
 ::::::::|::::::::  !
 :;;;;;;;;;;;;;;;;']}
 ;--.--.--.--.--.-
  \/ \/ \/ \/ \/ \/
     :::       ::::
      :::      ::
     :\:      ::
   /\::    /\:::
 ^.:^:.^^^::`::
 ::::::::.::::
  .::::::::::
   
    ''')
# the player chose the bucket
else:
    print("You look inside the bucket, there is the key...what for that is the question...")
    line()
    print("you decide looking around...")
    line()
    print("there is a palm tree....")
    line()
    print("Near it you find a chest")
    line()
    open_chest = input("Should you open the chest? YES or NO ")
    if open_chest == "YES":
        print("Now you find the TREASURE... SHIIIINEEE!")
        line()
        print("Now is Game Over, thanks for play.... wait for or next DLC... Bye!!!")
        line()
    else:
        print("You decide not to open the chest, your soul is lost forever in the eternal beach, waiting for the Forbiden One for wake up!")
        line()
        print("GAME OVER...")
        line()
