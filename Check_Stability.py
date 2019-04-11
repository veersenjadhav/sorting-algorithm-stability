from Stable import *

class CheckStable:

    def __init__(self):
        self.A = [8,2,5,2,5]
        self.B = ['A', 'B', 'C', 'D', 'E']
        return

    def main(self):
        SS = StableSelection(self.A, self.B)
        A, B = SS.selectionSort()
        print(A)
        print(B)
        return


if __name__ == "__main__":
    CS = CheckStable()
    CS.main()