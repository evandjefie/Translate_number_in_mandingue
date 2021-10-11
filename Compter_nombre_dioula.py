'''
    TRANSCRIT UN NOMBRE ENTIER EN LANGUE MANDINGUE
'''

def dico_diou(num):
    d = { 1 : 'kilin', 2 : 'fula', 3 : 'saba', 4 : 'naani', 5 : 'luulu',
          6 : 'wooro', 7 : 'worowula', 8 : 'sey', 9 : 'kononto', 10 : 'taŋ',
          11 : 'taŋ niŋ kiliŋ', 12 : 'taŋ niŋ fula', 13 : 'taŋ niŋ saba', 14 : 'taŋ niŋ naani',
          15 : 'taŋ niŋ luulu', 16 : 'taŋ niŋ wooro', 17 : 'taŋ niŋ worowula', 18 : 'taŋ niŋ sey',
          19 : 'taŋ niŋ kononto', 20 : 'muwaŋ',
          30 : 'taŋ saba', 40 : 'taŋ naani', 50 : 'taŋ luulu', 60 : 'taŋ wooro',
          70 : 'taŋ worowula', 80 : 'taŋ sey', 90 : 'taŋ kononto' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' niŋ ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return 'keme ' + d[num // 100]
        else: return d[num // 100] + ' keme niŋ ' + dico_diou(num % 100)

    if (num < m):
        if num % k == 0: return 'wuli ' + dico_diou(num // k)
        else: return 'wuli ' + dico_diou(num // k) + " niŋ " + dico_diou(num % k)

    if (num < b):
        if (num % m) == 0: return 'miliyoŋ ' + dico_diou(num // m)
        else: return 'miliyoŋ' +dico_diou(num // m) + 'niŋ' + dico_diou(num % m)

    if (num < t):
        if (num % b) == 0: return dico_diou(num // b) + ' miliyar'
        else: return 'miliyar ' + dico_diou(num // b) + ' niŋ ' + dico_diou(num % b)


if __name__ == '__main__':
    entree = input("Écrire un nombre : ")
    taille = len(entree)
    entier = int(entree)

    try:
        assert(0 <= entier)
        t = dico_diou(entier)
        print("Signifie: ",t)
    except AssertionError as msg:
        print(msg, "Le mot n\'existe pas en mandingue")
