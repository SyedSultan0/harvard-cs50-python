a = input("Camel Case: ")
snake_case =""
for letters in a:
    if letters == letters.upper():
        snake_case += letters.replace(letters,f'_{letters.lower()}')
    else:
        snake_case += letters
print("snake_case: "+snake_case)
