class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, n in enumerate(arr):
            currentArr=arr[i+1:len(arr)]
            if currentArr == []:
                continue
            maxRight = max(currentArr)
            arr[i]= maxRight
        
        arr[-1] = -1
        return arr
            
