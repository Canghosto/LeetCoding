class ProductOfNumbers:

    def __init__(self):
        self.ponMap = []
        self.size = 0
        

    def add(self, num: int) -> None:
        if len(self.ponMap) > 0 and num != 1:
            self.ponMap = list(map(lambda x: x * num, self.ponMap))
        self.ponMap.append(num)
        self.size = self.size + 1



    def getProduct(self, k: int) -> int:
        return self.ponMap[self.size - k]