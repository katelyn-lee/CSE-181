# Implement RandomizedMotifSearch().

# Input: Integers k and t, followed by a space-separated collection of strings Dna.
# Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times and 
# taking the best scoring ending motifs over all these runs of the algorithm. Remember to use pseudocounts!
import random
#--------------------------------------------------------------------------------------------------------------------------
def random_number(a:int) -> int:
    return random.randint(0,a)
#--------------------------------------------------------------------------------------------------------------------------
def random_motif_set(dna:list[str],k:int) -> list[str]:
    n = len(dna[0])

    random_motifs = []
    for string in dna:
        start_position = random.randint(0,n-k)
        rand_kmer = string[start_position:start_position+k]
        random_motifs.append(rand_kmer)
    return random_motifs
#--------------------------------------------------------------------------------------------------------------------------
def freq_profile(motifs:list[str],k:int) -> list[dict[str,float]]:
    profile = []
    t = len(motifs)
    for i in range(0,k):
        column = {}
        count_A,count_C,count_G,count_T = 0,0,0,0
        for motif in motifs:    #check ith char of each motif for char type, and update counts
            if motif[i] == "A": count_A+=1
            elif motif[i] == "C": count_C+=1
            elif motif[i] == "G": count_G+=1
            else: count_T+=1
        #after counts for a col is updated, add freq for each base to col dict
        column['A'] = ((count_A + 1)/(t+4))
        column['C'] = ((count_C + 1)/(t+4))
        column['G'] = ((count_G + 1)/(t+4))
        column['T'] = ((count_T + 1)/(t+4))
        profile.append(column)
    return profile
        
# motifs = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
# print(freq_profile(motifs,8))
#--------------------------------------------------------------------------------------------------------------------------
def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """

    maxProb = -1
    most_probable_kmer = ''
    n = len(text)
    for i in range(n-k+1):
        kmer = text[i:i+k]
        prob = 1
        #calc prob of the kmer based on profile matrix
        for j in range(0,k):
            prob = prob * profile[j][kmer[j]]

        if maxProb < prob:
            maxProb = prob
            most_probable_kmer = kmer

    return most_probable_kmer

def generate_motifs(profile:list[dict[str,float]],dna: list[str],k:int) -> list[str]:
    motifs = []
    for string in dna:
        string_motif = profile_most_probable_kmer(string,k,profile)
        motifs.append(string_motif)
    return motifs

# profile = [{'A': 0.5, 'C': 0.125, 'G': 0.25, 'T': 0.125}, {'A': 0.375, 'C': 0.25, 'G': 0.125, 'T': 0.25}, {'A': 0.125, 'C': 0.25, 'G': 0.375, 'T': 0.25}, {'A': 0.375, 'C': 0.25, 'G': 0.25, 'T': 0.125}, {'A': 0.25, 'C': 0.25, 'G': 0.125, 'T': 0.375}]
# dna = ['ATTGCATCGA','TACATAAGAT','GTCTCGACCG','CATGCGCAAC']
# print(generate_motifs(profile,dna,5))
#--------------------------------------------------------------------------------------------------------------------------
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    counter = 0
    n = len(p)
    for i in range(0,n):
        if p[i] != q[i]:
            counter += 1
    return counter

def stringKmers(string:str,k:int) -> list[str]:
    #generates a list of kmers for each given string
    dnaStringKmers = []
    n = len(string)
    for i in range(n-k+1):
        dnaStringKmers.append(string[i:i+k])
    return dnaStringKmers

# print(stringKmers("ACGT",3))

def distance_between_pattern_and_strings(pattern: str, dna: list[str]) -> int:
    """Returns the sum of the Hamming distances between pattern and each string in dna."""
    k = len(pattern)

    #generate dictionary hashmap of each dna string with its kmers
    dnaStringKmers = {}
    for string in dna:
        oneStringKmers = stringKmers(string,k)
        dnaStringKmers[string] = oneStringKmers
        
    sumDistance = 0
    for string in dna:
        HammingDistance = float('inf')
        kmers = dnaStringKmers[string]
        for kmer in kmers:                          #for each dna string, find kmer with least hd btw Pattern, and add that hd to sumDistance
            hd = hamming_distance(pattern,kmer)
            if HammingDistance > hd:
                HammingDistance = hd
        sumDistance += HammingDistance              #for each string, you find the smallest hd of a kmer, add it to sumDistance
    
    return sumDistance

def find_consensus_motif(profile: list[dict[str, float]]) -> str:
    probKmer = ''

    for column in profile:
        maxFreq = float('-inf')
        maxBase = ''
        for base, freq in column.items():
            if maxFreq < freq:
                maxFreq = freq
                maxBase = base
        probKmer = probKmer + maxBase
    
    return probKmer

def score(motifs:list[str],profile: list[dict[str, float]]):
    consensus_string = find_consensus_motif(profile)
    score = distance_between_pattern_and_strings(consensus_string, motifs)
    return score

# profile = [{'A': 0.5, 'C': 0.125, 'G': 0.25, 'T': 0.125}, {'A': 0.375, 'C': 0.25, 'G': 0.125, 'T': 0.25}, {'A': 0.125, 'C': 0.25, 'G': 0.375, 'T': 0.25}, {'A': 0.375, 'C': 0.25, 'G': 0.25, 'T': 0.125}, {'A': 0.25, 'C': 0.25, 'G': 0.125, 'T': 0.375}]
# motifs = ['ATTGC', 'AAGAT', 'TCGAC', 'ATGCG']
# print(score(motifs,profile))
#--------------------------------------------------------------------------------------------------------------------------
# For each dna string, randomly find start position and grab that kmer
# Return list of motifs

# RandomizedMotifSearch(Dna, k, t)
#     randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
#     BestMotifs ← Motifs
#     while forever
#         Profile ← Profile(Motifs)
#         Motifs ← Motifs(Profile, Dna)
#         if Score(Motifs) < Score(BestMotifs)
#             BestMotifs ← Motifs
#         else
#             return BestMotifs

def rand_motif_search(dna: list[str], k: int) :
    """Implements the RandomizedMotifSearch algorithm with pseudocounts."""
    motifs = random_motif_set(dna,k)
    best_motifs = motifs
    while True:
        profile = freq_profile(motifs,k)
        motifs = generate_motifs(profile,dna,k)

        motif_score = score(motifs,profile)
        best_motif_score = score(best_motifs,profile)

        if motif_score < best_motif_score:
            best_motifs = motifs
        else: 
            return best_motif_score, best_motifs

#--------------------------------------------------------------------------------------------------------------------------
def randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Runs the RandomizedMotifSearch algorithm 1000 times, and returns best MotifSet."""
    motif_sets = {}
    score = 0
    motifs = []
    # run RandomizedMotifSearch 1000 times 
    for i in range(1000):
        score, motifs = rand_motif_search(dna,k)
        motif_sets[score] = motifs

    # find best motif set w lowest score
    sorted_motif_scores = sorted(motif_sets.keys())
    return motif_sets[sorted_motif_scores[0]]

hello = randomized_motif_search(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 
                                 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 
                                 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 
                                 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 
                                 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'],8,5)
print(hello)
