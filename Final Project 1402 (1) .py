#  Final Project 1402
#  Ostad Arjmandnia
#  بازی سنگ / کاغذ / قیچی به همراه لاگ این 




#username == 1401123078
#password == "0020082101"

import random

name = input ( " Lotfan name karbari khod ra vared konid : " )
password = input ( " Lotfan ramze oboor khod ra vared konid : " )


name = 1401123078 and password == "0020082101"
while name != 1401123078 and password != "0020082101" :
     print ( " Lotfan name karbari va ramze oboor sahih ra vared konid " )
     print ( " Yek ja Eshtebahi Rokh Dade Astt " ) 

     password = print ( input ( " Lotfan Name Khod Ra Vared Konid : " ) )
     name = print ( input ( " Lotfan Ramze Khod Ra Vared Konid : " ) )

     if name == 1401123078 and  password == "0020082101" :
          break

print ( " Shoma Vared System Shodid " )
print ( " Khosh Amadid " )

emtiaze_player1 = 0
emtiaze_player2 = 0
while emtiaze_player1 <= 3 or emtiaze_player2 <= 3 :
    
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
     print('Mosavi/Draw')

    elif player1 == 'sang'  and  player2 == 'kaghaz' :
     print ( 'player2 winnnn' )
     emtiaze_player2 += 1
    elif player1 == 'sang'  and  player2 == 'gheychi' :
     print ( 'player1 winnnn' )
     emtiaze_player1 += 1
    elif player1 == 'kaghaz'  and  player2 == 'sang' :
     print ( 'player1 winnnn' )
     emtiaze_player1 += 1
    elif player1 == 'kaghaz'  and  player2 == 'gheychi' :
     print ( 'player2 winnnn' )
     emtiaze_player2 += 1
        
    elif player1 == 'gheychi'  and  player2 == 'sang' :
     print ( 'player2 winnnn' )
     emtiaze_player2 += 1
    elif player1 == 'gheychi'  and  player2 == 'kaghaz' :
     print ( 'player1 winnnn' )
     emtiaze_player1 += 1

    else :
     print ( 'yek chizi eshtebah asttt , lotfan harekat dorost ra entekhab konid' )
     
     
     
    print ( " \n ")
    print ( f" emtiaze player1 : {emtiaze_player1 } " )
    print ( f" emtiaze player2 : {emtiaze_player2 } " )
    print ( "....................." ) 
    
    if emtiaze_player1 > 2 or emtiaze_player2 > 2 :
       break


print ( "  ")
print ( " Khaste Nabashid " )       
print ( " Bazi Be Etmam Resid " )
print ( " Be Omide Didar " )
print ( " ..................... " )
