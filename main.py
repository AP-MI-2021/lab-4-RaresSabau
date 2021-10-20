def minim_ultima_cifra(lst, n):
    '''
    Returneaza numarul cel mai mic din lista initiala care are ultima cifra egala cu un numar citit de la tastatura
    :param lst:
    :return:
    '''
    minim = None
    for el in lst:
        if el % 10 == n:
            if minim == None or el < minim:
                minim = el
    return minim

def test_minim_ultima_cifra():
    assert minim_ultima_cifra([1, 2, 6553, 85434, 453], 3) == 453
    assert minim_ultima_cifra([875423, 3, 5432, 2], 2) == 2


def lst_nr_negative(lst):
    '''
    Returneaza lista numerelor negative din lista initiala
    :param lst:
    :return:
    '''
    ok = 0
    lst_neg = []
    for nr in lst:
        if nr < 0:
            lst_neg.append(nr)
            ok = ok + 1
    if ok != 0:
        return lst_neg
    elif ok == 0:
        return None

def test_lst_nr_negative():
    assert lst_nr_negative([-1, 2, 3, -10, 9]) == [-1, -10]
    assert lst_nr_negative([2, 3, 4, 5]) == None
    assert lst_nr_negative([-1, -34243, 67654, 874232]) == [-1, -34243]

def lst_int_numbers():
    '''
    Citeste o lista de numere intregi
    :return:
    '''

    lst_str = input("Introduceti numerele intregi: ").split(" ")
    lst_int = []
    for nr in lst_str:
        lst_int.append(int(nr))
    return lst_int


def show_menu():
    '''
    Printare meniu
    :return:
    '''

    print ('''
    1. Citire numere intregi in lista
    2. Afișarea tuturor numerelor negative nenule din listă
    3. Afișarea celui mai mic număr care are ultima cifră egală cu o 
    cifră citită de la tastatură.
    4. Afișarea tuturor numerelor din listă care sunt superprime.
    5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    x. Iesire
    ''')

def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Introduceti comanda: ")
        if cmd == '1':
            lst = lst_int_numbers()
        elif cmd == '2':
            print (lst_nr_negative(lst))
        elif cmd == '3':
            n = int (input ("Introduceti cifra dorita: "))
            mini = (minim_ultima_cifra(lst, n))
            print (mini)
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == 'x':
            break
        else:
            print ("Comanda invalida")

def run_tests():
    test_lst_nr_negative()
    test_minim_ultima_cifra()

if __name__ == '__main__':
    run_tests()
    main()