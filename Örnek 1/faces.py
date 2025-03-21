def faces(a):


    return a.replace(':)', '🙂').replace(':(', '🙁')

def main():

    text = input("Lütfen dönüştürmek istediğiniz metni girin: ")
    result = faces(text)
    print(result)

    main()
