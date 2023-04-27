# بازی سنگ - کاغذ - قیچی

print ( "Sang ...." )
print ( "Kaghaz ..." )
print ("Gheychi ..." )
print ("")

player1 = input ( 'player1 , Lotfan harekate khor ra entekhab konid ..... :' ).lower()
player2 = input ( 'player2 , lotfan harekate khod ra entekhab konid ..... :' ).lower()

if player1 == player2 :
    print('Mosavi/Draw')

elif player1 == 'sang'  and  player2 == 'kaghaz' :
    print ( 'player2 winnnn' )
elif player1 == 'sang'  and  player2 == 'gheychi' :
    print ( 'player1 winnnn' )
    
elif player1 == 'kaghaz'  and  player2 == 'sang' :
    print ( 'player1 winnnn' )
elif player1 == 'kaghaz'  and  player2 == 'gheychi' :
    print ( 'player1 winnnn' ) 
    
elif player1 == 'gheychi'  and  player2 == 'sang' :
    print ( 'player2 winnnn' )
elif player1 == 'gheychi'  and  player2 == 'kaghaz' :
    print ( 'player1 winnnn' )
    
else :
    print ( 'yek chizi eshtebah asttt , lotfan harekat dorost ra entekhab konid' )
    