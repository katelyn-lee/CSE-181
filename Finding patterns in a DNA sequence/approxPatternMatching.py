# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

# Input: Strings Pattern and Text along with an integer d.
# Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    counter = 0
    n = len(p)
    for i in range(0,n):
        if p[i] != q[i]:
            counter += 1
    return counter

# generate hash map of all kmers in text of size k, with its starting position
def startPosMap(text: str, k: int) -> dict:
    startMap = {}
    n = len(text)
    for i in range(0,n-k+1):
        pattern = text[i:i+k]
        if pattern in startMap:
            startMap[pattern].append(i)
        else:
            startMap[pattern] = [i]
    return startMap

def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    """Find all starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    # Map not for freq, but for all kmers in the text with list of starting positions (to add all duplicates' start pos into hash w unique keys)
    # check each kmer, if it matches the pattern with at most d mismatches, add its starting position(s) to output list
    patternStartPositions = []
    startMap = startPosMap(text,len(pattern))        #map with all kmers and starting positions
    for kmer in startMap:
        hd = hamming_distance(kmer,pattern)
        if hd <= d:
            patternStartPositions = patternStartPositions + startMap[kmer]
    return patternStartPositions

# print(approximate_pattern_matching('ATA','CGATCGAGTACCATAAG',1))

def approximate_pattern_count(text: str, pattern: str, d: int) -> int:
    """Count the occurrences of a pattern in a text, allowing for up to d mismatches."""
    c = 0
    n = len(text)
    np = len(pattern)
    for i in range(0,n-np+1):
        kmer = text[i:i+np]
        if hamming_distance(kmer,pattern) <= d:
            c += 1
    return c
    
print(approximate_pattern_count('CCACCT','CCA',0))
