#  Final Project 1402
#  Ostad Arjmandnia
#  بازی گل یا پوچ به همراه لاگ این
 
 
 
 
#username == 1401123078
#password == "0020082101"



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


import random

emtiaze_player1 = 0
emtiaze_player2 = 0

while emtiaze_player1 <= 2   and   emtiaze_player2 <= 2 :
    
    

    print ( ' Gol ...... ' )
    print ( ' Poch ...... ' )
    print ('')


    player1 = input ( 'player1 , lotfan entekhab khod ra vared konid : ' ) .lower()

    randomnumber = random.randint( 1 , 2 )
    print (randomnumber)

    if randomnumber == 1 :
       player2 = 'gol'
    elif randomnumber == 2 :
       player2 = 'poch'

    print (player2)

    if player1 == player2 :
       print ( ' Mosaviiiii ' )
    elif player1 == 'gol'   and   player2 == 'poch' :
       print ( ' player1  winnnn ' )
       emtiaze_player1 += 1
    elif player1 == 'poch'   and   player2 == 'gol' :
       print ( ' Player2  winnn ' )
       emtiaze_player2 += 1
    else :
       print ( ' yek chizi eshtebah ast ' )





    print ( " \n ")
    print ( f" emtiaze player1 : {emtiaze_player1 } " )
    print ( f" emtiaze player2 : {emtiaze_player2 } " )
    print ( "....................." )
    
    
    if emtiaze_player1 > 1   or   emtiaze_player2 > 1 :
        break
    
    
print ( "  ")
print ( " Khaste Nabashid " )       
print ( " Bazi Be Etmam Resid " )
print ( " Be Omide Didar " )
print ( " ..................... " )