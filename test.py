from fractionlib.Fraction import Fraction, simplification
from sys import argv

if __name__ == '__main__':
    x = Fraction(-2, -3)
    y = Fraction(2, 3)
    z = Fraction(5, 7)
    try:
        if argv[1].lower() == 'true':
            simplification(True)
        else:
            simplification(False)
    except:
        simplification(False)
    print(x + y)
    print(x + y + z)
    print(Fraction(3, 4) *  y)
    print(y * z)
    print(y - z)
    print(x * y - z)
    print(x == y)
    print(x != y)
    print(x > z)
    print(y <= z)
