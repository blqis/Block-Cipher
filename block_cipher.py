cle = (2, 5)
k0 = cle[0]
k1 = cle[1]
S = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]


def round(msg, souscle):

    t = msg ^ souscle
    return S[t]


def enc(msg, cle):

    c = round(msg, cle[0])
    c = round(c, cle[1])

    return c


def back_round(c, souscle):

    return S.index(c) ^ souscle


def dec(c, cle):

    return back_round(back_round(c, cle[1]), cle[0])


### Test

# print(enc(6, cle))

# print(round(6, cle[0]))
# print(back_round(round(6, cle[0]), cle[0]))

# print(enc(15, cle)) # donne 6
# print(dec (6, cle)) # redonne bien 15




"""************ Exercice 2 ************"""


def enc_byte(octet, cle):

    return (enc(octet >> 4, cle) << 4) + enc(octet & 15, cle)


def dec_byte(c, cle):

    return (dec(c >> 4, cle) << 4) + dec(c & 15, cle)


### Test

# print(chr(dec_byte(enc_byte(ord('6'), cle), cle)))
# print(chr(dec_byte(enc_byte(ord('A'), cle), cle)))


### 4.


def enc_file(file, cle):
    
    f = open(file, "rb")
    T = f.read()
    tab = []

    for octet in T:
        tab.append(enc_byte(octet, cle))

    f.close()

    g = open((file + ".enc"), "wb")
    g.write(bytes(tab))
    g.close()

    return

def dec_file(file, cle):

    f = open(file, "rb")
    T = f.read()
    tab = []

    for octet in T:
        tab.append(dec_byte(octet, cle))

    f.close()

    g = open(file + ".dec", "wb")
    g.write(bytes(tab))
    g.close()

    return



enc_file("msg", cle)
dec_file("msg.enc", cle)


# enc_file("coucou", (9, 0))


vecteur = 172

def enc_file_cbc(file, cle, vecteur):


    f = open(file, "rb")
    T = f.read()
    tab = []

    for octet in T:
        tab.append(enc_byte((octet ^ vecteur), cle))
        vecteur = tab[-1]

    f.close()

    g = open((file + ".enc"), "wb")
    g.write(bytes(tab))
    g.close()

    return


def dec_file_cbc(file, cle, vecteur):
    
    f = open(file, "rb")
    T = f.read()
    tab = []

    for octet in T:
        
        tab.append(dec_byte((octet), cle) ^ vecteur)
        vecteur = octet

    f.close()

    g = open(file + ".dec", "wb")
    g.write(bytes(tab))
    g.close()

    return

enc_file_cbc("coucou", cle, vecteur)
dec_file_cbc("coucou.enc", cle, vecteur)
