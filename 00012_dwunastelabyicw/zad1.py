import copy
class Wielomian:
    __slots__ = ["coefs"]
    def __init__(self, coefs):
        self.coefs = copy.copy(coefs)
    def __repr__(self):
        napis = ""
        for i in range(len(self.coefs)):
            if i == len(self.coefs)-1:
                napis += f"{self.coefs[-i-1]}x^{len(self.coefs) - i-1}"
            else:
                napis += f"{self.coefs[-i-1]}x^{len(self.coefs)-i-1}+"
        return napis
def main():
    coefs = [1, 2,3]
    w1 = Wielomian(coefs)
    print(w1)
    coefs[1] = 4
    w2 = Wielomian(coefs)
    print(w1)
    print(w2)
if __name__ == '__main__':
    main()