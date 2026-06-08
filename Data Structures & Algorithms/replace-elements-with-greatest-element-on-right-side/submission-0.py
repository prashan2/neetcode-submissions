class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        self.elements = []
        self.greatest = arr[0]
        self.temp = arr.copy()
        #print(f'temp is {temp}')
        #print(f'max of temp:{max(temp)}')
        self.length =len(arr)
        for i in range(self.length - 1):
            #print(f'temp[i:len(arr)] :{temp[i:len(arr)]}')
            del self.temp[0]
            #print(temp)
            self.greatest = max(self.temp)
            self.elements.append(self.greatest)

        self.elements.append(-1)
        return self.elements


