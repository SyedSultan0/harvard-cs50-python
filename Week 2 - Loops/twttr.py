a = input("Input: ")
b = ""
for letters in a:
    if letters.lower() in ["a","e","i","o","u"]:
        b += letters.replace(letters,"")
    else:
        b += letters
print(f"Output: {b}")
