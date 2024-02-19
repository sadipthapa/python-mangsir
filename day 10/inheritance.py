class Grandfather:
    house="luxury"
    
class Grandmother:
    jewellary="sunn wala diamond"
    
class Father(Grandfather,Grandmother):
    car="Mercedez"
class Son(Father):
    console='PS5'
    
son=Son()
print(son.jewellary)
    

grandfather=Grandfather()
print(grandfather.house)    
father=Father()
print(father.jewellary) 

print(isinstance(son,Grandfather))


