class StableSelection:
    
    def __init__(self, arrayA, arrayB):
        self.arrayA = arrayA
        self.arrayB = arrayB
        return

    def selectionSort(self):

        for i in range(len(self.arrayA)):

            minPosition = i

            for j in range(i+1, len(self.arrayA)):
                if self.arrayA[minPosition] > self.arrayA[j]:
                    minPosition = j
                        
            temp = self.arrayA[i]
            self.arrayA[i] = self.arrayA[minPosition]
            self.arrayA[minPosition] = temp

            temp = self.arrayB[i]
            self.arrayB[i] = self.arrayB[minPosition]
            self.arrayB[minPosition] = temp

        return self.arrayA, self.arrayB