class FrequencyTracker:

    def __init__(self):
        # self.map_ = {}
        # self.freq = {}
        self.count = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        # if number in self.map_ :
        #     self.map_[number] +=1
        #     ## should update the self.freq but how?

        #     return
        # self.map_[number] = 1
        old = self.count[number]

        if old > 0:
            self.freq[old] -= 1

        self.count[number] += 1
        new = self.count[number]

        self.freq[new] += 1 


    def deleteOne(self, number: int) -> None:
        # if number in self.map_ :
        #     if self.map_[number] ==1:
        #         self.map_.pop(number)
        #     else:
        #         self.map_[number] -=1
        #     return
        old = self.count[number]

        if old > 0:
            self.freq[old] -= 1
            self.count[number] -= 1
            new = self.count[number]

            if new > 0:
                self.freq[new] += 1
            
    def hasFrequency(self, frequency: int) -> bool:
         return self.freq[frequency] > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
