a = input("Greeting:").lower().strip()
if "hello" in a:
    print("$0")
elif a.startswith("h"):
    print("$20")
else:
    print("$100")
