#1.4clumpFindingProblem

#Clump Finding Problem: Find patterns forming clumps in a string.

# Input: A string Genome, and integers k, L, and t, representing length of kmer, length of windo, and min number of patterns in the window
# Output: All distinct k-mers forming (L, t)-clumps in Genome.

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

def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    """Find patterns forming clumps in a genome."""
    patterns = []
    n = len(genome)
    for i in range(0,n-l+1):
        window = genome[i:i+l]

        freqMap = frequencyTable(window,k)
        for key in freqMap:
            if freqMap[key] >= t:
                if key not in patterns:
                    patterns.append(key)
    return patterns


# print(find_clumps('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',5,50,4))

with open('/Users/katelynlee/UCSD/BENG181CodingChallenges/genome.txt') as file_object:
    contents = file_object.read()
    patterns = find_clumps(contents,9,500,3)    #search e coli genome for 9mers clumping in 500 base window, repeating at least 3 times
    # print('different 9mers forming (500,3)-clumps in e coli genome: ')
    # print(patterns)
    print('num of different 9mers forming (500,3)-clumps in e coli genome: ')
    print(len(patterns))

