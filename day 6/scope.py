# a=10

# def number():
#     a=11
#     print(a)
# number()
# print(a)

# a=10
# def number():
#     a=11
#     print(a)
# number()
# print(a)

a=10
def outer():
    a=11
    def inner():
        global a
        a=12
        print('inner sees a as',a)
    inner()
    print('outer sees a as',a)
print('main sees a as'a)
outer()    



# loop conditional functional,scope
#list append()
# user register and login

# a=[1,2,3]
# print(a)
# a.append()
# print(a)