# Display the vowals in using if else

alpha = str(input("Enter any Character: "))
alpha = alpha.casefold()
if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
    print("It is Vowal")
else:
    print("It is consonent")