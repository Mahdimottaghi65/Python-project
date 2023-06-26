# Random Player

import random

print ( ' Sang ..... ' )
print ( ' Kaghaz ..... ' )
print ( ' Gheychi ..... ' )
print ( '' )

player1 = input ( ' player1 , lotfan harekat khod ra entekhab konid ... : ' ) .lower()

randomnumber = random.randint(1 , 3)
print (randomnumber)

if randomnumber == 1 :
    player2 = 'sang'
elif randomnumber == 2 :
    player2 = 'kaghaz'
elif randomnumber == 3 :
    player2 = 'gheychi'
    
print (player2)

if player1 == player2 :
    print ( ' Mosavi/draw ' ) 
elif player1 == 'sang'  and  player2 == 'kaghaz' :
     print ( ' player2 winnnn ')
elif player1 == 'sang'  and  player2 == 'gheychi' :
    print ( ' player1 winnnn ' )
     
elif player1 == 'kaghaz'  and  player2 == 'sang' :
    print ( ' player1 winnnn ' )
elif player1 == 'kaghaz'  and  player2 == 'gheychi' :
    print ( ' player2 winnnn ' ) 
    
elif player1 == 'gheychi'  and  player2 == 'sang' :
    print ( ' player2 winnnn ' )
elif player1 == 'gheychi'  and  player2 == 'kaghaz' :
    print ( ' player1 winnnn ' )
    
else :
    print ( ' yek chizi eshtebah ast ' )
           
     