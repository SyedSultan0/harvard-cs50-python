from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("SYED") == "SYD"
    assert shorten("@$%!%123^E") == "@$%!%123^"

if __name__ =="__main__":
    main()
