class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15
        arr = []
        f = celsius * 1.80 + 32.00
        arr.append(k)
        arr.append(f)
        return arr
        
3
