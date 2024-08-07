# Display the Generate the electronic bill on unit Consumed and minimum amount include 100rs.

cons = int(input("Enter the unit consumed: "))

if cons <= 200:
    amount = cons*1.20
elif cons <=399:
    amount = cons*1.50
elif cons <=599:
    amount = cons*1.80
else:
    amount = cons*2.0

if amount <= 100:
    amount = 100

print(amount)

