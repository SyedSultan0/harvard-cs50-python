def convert(text):
    newmsg = text.replace(":)","🙂").replace(":(","🙁")
    return newmsg

def main():
    msg = input("Type:")
    print(convert(msg))

main()
