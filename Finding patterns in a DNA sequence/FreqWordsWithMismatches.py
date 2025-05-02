# 1.11 Generating Neighborhood of a String
# Code Challenge: Implement Neighbors() to find the d-neighborhood of a string.

# Input: A string Pattern and an integer d.
# Output: The collection of strings Neighbors(Pattern, d).

def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    if d==0: return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    
    neighborhood = []
    
    sPrefix = s[0]
    sSuffix = suffix(s)
    suffixNeighbors = neighbors(sSuffix,d)

    for text in suffixNeighbors:
        if hamming_distance(sSuffix,text) == d:
            neighborhood.append(sPrefix + text)
        else:
            for nucleotide in ['A','T','C','G']:
                neighborhood.append(nucleotide + text)

    return neighborhood

def suffix(s) -> str:
    return s[1:len(s)]

# print(neighbors('AAA',1))

# -------------------------------------------

# Code Challenge: Solve the Frequent Words with Mismatches Problem.

# Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
# Output: All most frequent k-mers with up to d mismatches in Text.


def MaxMap(my_dict) -> int:
    MaxCount = 0
    for value in my_dict.values():
        if value > MaxCount:
            MaxCount = value
    return MaxCount

def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    counter = 0
    n = len(p)
    for i in range(0,n):
        if p[i] != q[i]:
            counter += 1
    return counter

def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text."""
    patterns = []

    freqMap = {}
    n = len(text)

    for i in range(0,n-k+1):
        kmer = text[i:i+k]
        neighborhood = neighbors(kmer,d)
        nn = len(neighborhood)
        for j in range(0,nn):
            neighbor = neighborhood[j]
            if neighbor in freqMap:
                freqMap[neighbor] = freqMap[neighbor] + 1
            else:
                freqMap[neighbor] = 1
    
# max frequency is m, only words with m freq are added to returned patterns list
    m = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns

print(frequent_words_with_mismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT',4,1))


