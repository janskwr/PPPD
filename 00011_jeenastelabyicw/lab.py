class Matrix:
    __slots__ = ["nrow", "ncol", "__data", "__shape"]

    def __init__(self, nrow, ncol, data):
        self.nrow = nrow
        self.ncol = ncol
        self.__shape = [nrow, ncol]
        # self.__data = data # ZLE! to jest płytkie kopiowanie, to jest kopiowanie referencji
        # po pierwsze chcemy płaską listę, a tu będzie pojedyncza liczba lub lista list,
        # a po drugie wtedy jak ktoś na zewnątrz zmieni zawartość listy list to nam też się tutaj zmieni
        if type(data) is list:
            self.__data = [0] * (nrow * ncol)
            for row in range(nrow):
                for col in range(ncol):
                    self.__data[row * ncol + col] = data[row][col]
        else:
            self.__data = [data for _ in range(nrow * ncol)]

        def __repr__(self):
            # Matrix([[1, 2, 3], [4, 5, 6]])
            # ŻADNEGO PRINTA !!!!!!!!!
            result = "Matrix(["

            for row in range(self.nrow):
                result += "["
                for col in range(self.ncol):
                    result += str(self.__data[row * self.ncol + col])
                    if col < self.ncol - 1:
                        result += ", "
                result += "]"
                if row < self.nrow - 1:
                    result += ", "

            result += "])"
            return result
