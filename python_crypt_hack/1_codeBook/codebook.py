import codeBookPackage.enc
import codeBookPackage.dec

def makeCodeBook():
    encbook = {'a' : '1', 'b':'2', 'm':'3', 'i':'5', 'n':'*','o':'@','g':'%'}

    decbook = {}

    for i in encbook:
        val = encbook[i]
        decbook[val] = i

    return encbook, decbook

if __name__ == '__main__':
    h = open('C:/Users/sleep/Desktop/prac/prac_repo/python_crypt_hack/1_codeBook/plain.txt', 'rt')
    text =h.read()
    h.close

    encbook, decbook = makeCodeBook()
    ciperText = codeBookPackage.enc.encrypt(text, encbook)
    print("show ciper text : " + ciperText)
    decText = codeBookPackage.dec.decrypt(ciperText, decbook)
    print("show original text : " + decText)