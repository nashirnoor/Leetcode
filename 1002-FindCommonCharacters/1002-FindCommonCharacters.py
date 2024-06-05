    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        nums = []
        g = words[0]
        arr = [ d for d in g]
        k = 0
        for i in range(len(arr)):
            for j in range(1,len(words)):
                if arr[i] in words[j]:
                    words[j] = words[j].replace(arr[i], "*", 1)
                    k+=1
            if k==len(words)-1:
                nums.append(arr[i])
            k = 0
        return nums


["bella","label","roller"]
