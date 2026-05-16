# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs
        
        # middle index
        m = (s + e) // 2      # // rounds down

        self.mergeSortHelper(pairs, s, m) # left
        self.mergeSortHelper(pairs, m+1, e) # right

        self.merge(pairs, s, m, e) # merge, technically don't need to pass m but its ok

        return pairs

    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        L = arr[s: m + 1] # allocates for left array
        R = arr[m + 1: e + 1] # allocates for right aaray

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge two sorted halfs into OG array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key: # Stable <= !
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        

