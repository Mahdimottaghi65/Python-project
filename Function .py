# Function  تابع ها

# با تابع میتوانیم از تکرار عملیات دلخواه جلوگیری کنیم
# موارد موردنظر را داخل ان تعریف کرده و در زمان دلخواه استفاده میکنیم
# ... مثل عملیات ریاصی و یا ربات های تلگرام و 
# در واقع کدها را داخل یک بلاک میگذاریم و در زمان معین صدا کنیم
# بدین وسیله از تکرار کدها جلوگیری میکنیم
# تمام آنها قابل استفاده محدد هستن در زمان فراخوان


#def say_hello () :
#    print ("Salam")
#    print ("Khoosh amadin")
#    print ("Che komamki mitoonam bokonam")
    
#say_hello()
# اگر چندبار بنویسیم  به همان مقدار تکرار میشود
 
 
 
 
# فانکشن ها میتوانند همچین پارامتر هایی زا دزیافت کنند که مقادیری را برمیگرداند
# اینکار به وسیله انجام میشود RETURN


#def get_two() :
#    print(2) 
 
    
#get_two()
# هرچندباری که تکرار کنیم عدد 2 نمایش داده میشود

#get_two() + 2 
# چیزی نمایش داده نمیشود و علامت جمع انجام نمیشود
# صرفا برای نمایش 2 است این کد


# برای اینکه بتونیم محاسبه انجام دهیم اینگونه عمل میکنیم 
 
# def get_two() :
# print (2)
 
#def get_two() :
#    return 2

#print ( get_two() + 2) = 4
#print ( get_two() * 3) = 6

#به این طزیق عملیات انجام میشود 


#def sum (x,y) :
#    z = x+y
#    return z

#sum (2 , 8)   = جوابی نداریم در این قسمت
#print (sum(1 , 2))   = 3
#print (sum(2.5 , 5)) = 7.5

 
#def sum ( x , y ) :
#    z = x + y
#    return z

#print (sum( 4 , 2 ))   = 6
#print (sum( 5 , 3 ))   = 8

# فانکشن یک سری آرگومان را دریافت کرده و عملیات را اعمال میکند 



#def sum ( x , y , z ) :
#    p = x+z+y
#    return p

#print (sum( 2 , 5 , 7 ))     = 14
#print (sum( 40 , 53 , 90 ))  = 183



#def sum ( a , b , c , d ) :
#    q = a+b+c+d
#    return q

#print (sum( 23 , 40 , 54 , 89 ))    = 206
#print (sum( 23 , 60 , 79 , 309 ))   = 471



#def average ( a , b ) :
#    z = (a+b)/2
#    return z

#print (average ( 10 , 20 ))   = 15
#print (average ( 120 , 160 )) = 140



#def gold(price_dollar) :
#    price_toman = price_dollar * 53000
#    return price_toman

#print ( gold(60000) )   = 3180000000
#print ( gold(90000) )   = 4770000000

#print ( f"gheymat barabar ast ba {gold(6000)} toman " )
#print ( f"gheymat barabar ast ba {gold(90000)} toman" )
# به این طریق کل جمله نمایش داده میشود

#def oil ( price_dollar ) :
#    price_toman = price_dollar * 53000
#    return price_toman

#print (oil(5000))   = 265000000
#print (oil(85000))  = 4505000000

#print ( f"gheymat barabar ast ba {oil(5000)} toman " )
# با اف استیرسنگ می توانیم این جمله را با قیمت نمایش دهیم 
# با اف شروع میکنیم و عبارت را داخل اکولاد میگذاریم


#def tavan_two (x) :
#    return x*x

#print (tavan_two (3))   = 9
#print (tavan_two (24))  = 576

#z = tavan_two(5) + 4
#print (z)  = 29



#def mahsahat_dayere (r) :
#    return 3.14 * r**2

#print ( mahsahat_dayere (3))   = 28.26
#print ( mahsahat_dayere (9))   = 254.34



#def masahat_mostatil ( x , y ) :
#    return x * y

#print ( masahat_mostatil ( 4 , 5 ))   = 20
#print ( masahat_mostatil ( 10 , 20 )) = 200


#def masahat_mosalas ( a , b ) :
#    return (a  * b ) / 2

#print ( masahat_mosalas ( 3 , 4 ))
#print ( masahat_mosalas ( 20 , 30 ))



#def jam_tafrigh_adad ( a , b , c , e , f ) :
    
#    natije = a+b-c+e-f
#    return natije

#print (jam_tafrigh_adad ( 2,5,9,7,3) )


#def zarb_taghsim_adad ( a , b , c , d ) :
    
#    natije = a * c / b * d
#    return natije

#print ( zarb_taghsim_adad ( 2 , 3 , 4 , 5 ))



#def zarb_jam_list ( a , b , c , d ) :
    
#    natije = a + b * c + d
#    return natije

#print (zarb_jam_list ( 2 , 4 , 6 , 8 ))




#def tavan_three (x) :
#    return x * x * x

#print ( tavan_three ( 3 ))


#def masahat_moraba ( x ) :
    
    #return x * x

#print ( masahat_moraba ( 4 ))














