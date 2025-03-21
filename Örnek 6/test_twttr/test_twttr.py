def main():
    word=input("Input : ")
    print("Output :",shorten(word))



def shorten(word):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in word if char not in vowels])
    return result
def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("12345") == "12345"
    assert shorten("!@#$%") == "!@#$%"
    assert shorten("TwItTeR") == "TwtTR"

if __name__ == "__main__":
    main()


