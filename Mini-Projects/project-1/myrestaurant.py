menu = {
    'pizza' : 100,
    'Barger' : 60,
    'Pasta' : 40,
    'Chilli Patato' : 60,
    'Chaominn' : 30,
    };

print("Welcome to my restaurant")
o = 1
amount = 0

while o<=5:
    i = input("Please order me:")
    if menu == i:
        print("Anything else sir")
        if o == i:
         break
    elif i != menu:
        print("Sorry Sir Your order item is not avalable in menu")
        break
    else:
        print("please try again")
else:
    print("Thankyou sir")