#Input: A string Text and an integer k
#Output: All most frequent k-mers in Text, in a list

# Algorithm
#FrequencyTable(Text, k)     function that generates a frequency table with keys being k-mers, and values being the number of times the k-mer appeared in the text
#     freqMap ← empty map
#     n ← |Text|
#     for i ← 0 to n − k
#         Pattern ← Text(i, k)
#         if freqMap[Pattern] doesn't exist
#             freqMap[Pattern]← 1
#         else
#            freqMap[pattern] ←freqMap[pattern]+1 
#     return freqMap
#Example: text=AGGCTA k=2

#function that generates a frequency table with keys being k-mers, and values being the number of times the k-mer appeared in the text
#faster since only takes one pass through the text
def frequencyTable(text: str, k: int) -> dict:
    freqMap = {}
    n = len(text)
    for i in range(0,n-k+1):
        pattern = text[i:i+k]
        if pattern in freqMap:
            freqMap[pattern] = freqMap[pattern] +1
        else:
            freqMap[pattern] = 1
    return freqMap

#function MaxMap() that takes a map of str patterns to int numebr times appeared in Text; returns the maximum value of this map as output
def MaxMap(my_dict) -> int:
    MaxCount = 0
    for value in my_dict.values():
        if value > MaxCount:
            MaxCount = value
    return MaxCount

# BetterFrequentWords(Text, k)
#     FrequentPatterns ← an array of strings of length 0
#     freqMap ← FrequencyTable(Text, k)
#     max ← MaxMap(freqMap)
#     for all strings Pattern in freqMap
#         if freqMap[pattern] = max
#             append Pattern to frequentPatterns
#     return frequentPatterns

#given Input: A string Text and an integer k; Output: All most frequent k-mers in Text in a list
def frequent_words(text: str, k: int) -> list[str]:
    frequentPatterns = []
    freqMap = frequencyTable(text,k)
    max = MaxMap(freqMap)
    
    for pattern in freqMap:
        if freqMap[pattern] == max:
            frequentPatterns.append(pattern)
    return frequentPatterns

# output = frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)
# print(output)

str = "ACT"
print(str[0])
print(str[0:1])
