class InPlaceArrange:
    """
    Rearrange the given array such that arr[i] = arr[arr[i]] without using additional memory
    """
    def __init__(self, input):
        self.input = input
        self.length = len(self.input)

    def arrange(self):
        #Based on property, provided X and Y is less than Z, (X + Y*Z)/Z = Y and (X + Y*Z)%Z = X
        #Increase each element by (arr[arr[i]] % len) * len to reduce it to the above mentioned property
        #The use of %len is to make sure that arr[arr[i]] is less than len for the property to hold good
        for i in range(0, self.length):
            self.input[i] += (self.input[self.input[i]] % self.length) * self.length

        #Divide each element by len to get the required value
        for i in range(0, self.length):
            self.input[i] /= self.length
        print self.input

#Test code
input = [3,2,0,1]
inPlaceArrange = InPlaceArrange(input)
inPlaceArrange.arrange()