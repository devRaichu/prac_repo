def encrpyt(msg, num):

    #97~122 A~Z
    ciper = ""
    for k in msg:
        if ord(k) + num < 123:
            ciper = ciper + chr( ord(k) + num )
        else:
            ciper = ciper + chr( 122 - ord(k) + num + 96 )

    return ciper

def decrypt(msg, num):

    text = ""
    for k in msg:
        if ord(k) - num > 96:
            text = text + chr( ord(k) - num )
        else:
            text = text + chr( ord(k) - 97 + 123 - num )
    
    return text

if __name__ == '__main__':

    file = open('C:/Users/sleep/Desktop/prac/prac_repo/python_crypt_hack/2_caesarCode/plain.txt', 'rt')
    text = file.read()
    file.close()

    #ceaserNum = input("Enter Ceasar number : ")
    ceaserNum = 1

    ciper = encrpyt( text, ceaserNum )
    print("encrypt text : "+ciper)
    text = decrypt( ciper, ceaserNum)
    print("decrypt text : "+text)