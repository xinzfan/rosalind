import re
import collections
import numpy as np
from operator import mul
import operator



myFilename = "/Users/siakhnin/Downloads/dataset_40_9.txt"


f = open(myFilename, 'r')
inputstr = f.read()

'''

inputstr = """12 25
GATGGACCGGGCCATACATGGTGACACGCATCAGAAAGCTGTCCCCGTGCCTTATGCGCTGTCTGTTAGTACATCTCTCTCAATGGCCGTATTTTCAGAACAAGTATCACTTGGATCATCATCTACTCGACGGAGGGCGCGCAAGTGGGTATCTCG
TAAAAAGGTATAAGGGAGTCATATCCGCAGTCCTAGTGACCTTTCCCGGCCCTAGCAGTGCTCCGATAGCCCATGGATGAGACGTAACTCGGCTACTGTTTGTGACTCAAGATAGTTGCCGTCGATATCTCGGATTCTGCTTATCGTGTTACGAGC
AACCACGAGTACCTCTGTCGTGGTCCTTCACCAGGACTCGAAATTTGGCTCACGCCCAACGCCAAGATTACGTCGATCGTTCCTGTTGATATCTCGCCGCATATCAGGTTTATACTGATCGGCTCAGTGATTGTTAATCATCGGCGCGGGTTGTCA
TGTCATGTGCGGATACAGTGGTGACACCAGGTCACCTCCGACCTAAAAGCGTTCAAGGTATGGCCCGAAGAGGTAGGTATCTCTTGTGCCCGCTGCTGCTATCACTCCCTGTGAGCCCCGACACGAATGTTAAACCAGTTTATATTCGCTCGTCAT
AACCTAAACCCTTGCTTCCCACCATCCCTGCGAAGCAACCTTATCCGTAGTTCAGTCGCGCTGAACTCGGAAAGTGCGCTCACGAGATTCTAACTTACACTTGTTTAAGTACCACGTCCGGTGGATATCGCTGGCGTTGAAGGATAGTTCTGGTTA
GTGCCCGATATGCCCGTCAGGGTTGAAGTCTGGGAAGTCGTTATCCCAAACGAAATACCCCGTTCGCAGGCGTGATGTATATCCTGATTAGTACCGCGTATAATATTAGTTTCGCACAGGAGCGTGCTTGTTTTGGGTCATGGATTGGGTACAGCA
TAGTCTTCGAGGCATCTACCTGCGACCGAGCTTGCGATCCAAAAGCATACCCATGAAGTTTGCAAATCTTTCTTAGAGCTACAGGTAGATATCCCTGGGCCGGTAACTAGTAATATGTACAGTTTAGTTGTCCTGTACAATACTGATTGGAGTCAG
AGGAGACGTGTTTGGTAGGCGCTCGACCCTTACCCCCCTATCTCGACTGGCATTGGACGTCCTCAGACTGGTGGATTTGACCTAGTGGTTATCACGCACATGGGAGAACCCGGTCAGAATACATCCTGTTACAGTCAGACGCCGGGTCATTCGCAA
TGTGGGGATCGTCTGATTCATCGACGTCATGGAAACGGGGACGGGCCAGTGGTTATCCCATGCTGCCTTTTAGGAATTCTAGGAGGCGTTCCTAAATAGCTCGCCCGACGATATCCTACTTGATTGTGGCGGTATACCTTGCTGAACCTCGCAGTA
CGCAGTGCACTAGTGGCTATCGCCTTTCTATCCCTGAGGCGTTTGCGTTATAAGATCACTCTGTCGGTGTGAAACCACTGAGTCACACTGACCGGTCGACTGGCCCGTCATATGCAAGTTGAAACGCTTACTGCCGGGTATCGCTCTAAGCTCGAC
TACTCGTAACTTCAAAATCTCGTAGGGTCTGCAGAGTAAGAATCCCGGATACTTCAACATTATCGATTCGTCAAGACGTGCGGAGTGGATATCCCTTATTCCTATACGTCACAAGCCGCGGTCAAGTCGCTTACGCACGGTAGAGCGGGAAACCCT
GCTCTAGTACGCCACAGTGCCAGTACATGACCTCACGAGCCGCCACTTACGTTGATATGTTATAAATCACTAGTTTCGTTGGTACAAACAATAAGTGAGAAGCAATGAGCAACTTATCTCATAAAAAGTGTGGTCGTTATCACACATGACATAAAC
GAGACGGTCGTAGAAATTTGCGCTTGCTCGTATCTCAGTATCCTTCAAAGATTGAACCGGATCGCGGCGGCTAATATTGAAATCCTTAGACTTAACGTTGGTATCACTTTAGAATTTCTGACTTGAGGGTAGTGACTAGACAATCATGATGGAAGA
GATCGGTGGCAGTTGAATTAAGACTAGTTATCCCCTGCTTACACTTTTTCCGCCCGGACACGTGTGACGGTAGTTGATATCTCTCAAGTATCCCGACTTCACGTACGATGCCACCCATCTCCGGCAAACACACTTCTATAATATCGTGGAGCCGAA
GTAGGTATCACCAGAGTTCTCTCGGTATGTGGCGCTAAAACCTCTTAGAGTATGAAGGGTGAAGACCAAGCTCATACCACCCCTATATAGGGCTAATTAATTCCACATCCAGGCAAGATGTCACCCTACAGGTCGCTCACTTGTGGAGAACATCAC
GTGGCTATCGCTGTGATCCGTCACACAAAATCAACTTTGTAGTATTTTGGGTAGTCGGGATAACGCGTGGTCTAAGGTGAGCTGCCTTTGATCCGTTGGGTGGCTACCTTGCAAGTTACCGGCTTGTCACTAGATATAACCGGAAGTCTCTGCAAA
TGAGCAGACCCGACAAAGGCCATGACTTCAAAACCGGTTGTGCAGCGACAGGTACTTTAAGTACGGCACCATTAATATCGCTATACTTACGAGTTAGTGGGTATCTCATGCAAACAAACTGCTACTAGGAACTTAGACGAACTTACCAGGAGGATT
AGTGATCTGAGCATAGTATACTGAGAACGTGTGTGTGACCCCTCCAGCGTCCCCGGCTACTGTTCCAGATCCTAACTAATTACTGCTAGCGATCTGGTCGATATCGCTACGGAACGAAGCCGTACAATCGCCCAGAAGCGGTTAGTCAAGGGCGTT
CAAAATGGGAGTACTTCTCGTAGAATAATTCGTCTGTAATTCCTAGGTTCCATAGATAGGCCTCGATAGTGAAATTCCTTCATGCCCCGAGGTGGCGTTGATATCTCCTTTCTAAGCGGTACCCTTAAGAGTACTCGCGATGGGCTTATCCTCCTC
GTTGGTATCACCCCCAATCCTCTTAGTTTACACTGTAAGATTAACGTCAGGGTGTTGTGGATGGCTTTTCTAATTTAGGTCCTCGGGATGCTCAGGTGTTACTATCGGACTGAGTGAATGTAAGTCCGGGTATCAGCCATGAAACCACTGGAGATC
CCTCGGAAAACGTCGTAAGTGGTATCACAATCCACTAGTCACGGAGGGCGGTGAGTGTCTCGATGCTCAACCCCCAACCCTCAGATGAGGCTATCTGTAGGTATCACTTACGTCACTACGGGGAACAGCTCGCCTTAAGTGTAGGCTAGGTATATG
GGCGGCTCCATCCGATGTGACGGATTTCATGAGGCACAAGCGCTTCACTCCCTATTTGGCTCGTGACAAAGTTCAACGGCTTTGCAGATATCCATGGTCGTTATCCCGGTGGTGAACCTACCGTCAAGTCTCTACAGTGCGCGAAGTGTCCCGGGC
TACTAGTATAAGTTCCGAGCCAAATGGATGGCCCAGGCGCACTAGTGTTAGAAGGATTCGGGCTGTAGGTACATCAAGCTCGAATTTGTCCCACGTCATTCTGGGCCACCCGGACCACAGAAGACCTCTCTCTGTGCCGACGGTGTGGTTATCACG
GTGGTTATCACCGGGATCGAATACAGATACGTCTGGTACATGCCTTGTCATTATTCATACGCCCCCTGGGCCAACAATCCTTTGTCAACCGCGGTCAAAAAGGTAACTAGGATCGGCTTGATCTCTAATTCCGGACTGTTCACCACGGGTCGACCG
CATCACGCAATGCGAACGACTGAAGAAGGCAAGGACAGTTACGCAACCTATCATGCGTAGATCAAGGTAATCGGGACCGGTCTGGAATTTAGGAGTGTTGTTATCGCAACCTGCGATCATAACATCCTCTTATTGCCTATAAACCGACCCTGACCG"""

inputstr =  """3 5
     GGCGTTCAGGCA
     AAGAATCAGTCA
     CAAGGAGTTCGC
     CACGTCAATCAC
     CAATAATATTCG"""
'''   
inputlist = [x.strip() for x in inputstr.split("\n") if len(x) > 0]
param = inputlist[0].split(" ")
k = int(param[0].strip())
t = int(param[1].strip())

dna_strings = inputlist[1:]

nuc_to_col_mapping = {"A":0, "C":1, "G":2, "T":3}
col_to_nuc_mapping = {0:"A", 1:"C", 2:"G", 3:"T"}

ne = operator.ne

def getHammingDistance(str1,str2):
    return sum(map(ne,str1, str2))

# Yield all kmers of string my_str
def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]
            
# Return tuple (my_dna_str, prob) where prob is the probability of generating my_dna_str under profile
def profileProbabilityOf(my_dna_str,profile):
    return (my_dna_str,reduce(mul,[profile[c[0]][nuc_to_col_mapping[c[1]]] for c in enumerate(my_dna_str)],1))
            
def bestKmer(dna_str, profile, k):
    return max([profileProbabilityOf(my_str, profile) for my_str in allKmersOf(dna_str,k)], key=lambda x: x[1])[0]

def generateInitialMotifList():
    return [dna_string[0:k] for dna_string in dna_strings]

def createProfile(dna_strings, withPseudoCounts):
    profile = np.zeros((len(dna_strings[0]),4))
    x = np.array([list(dna_str) for dna_str in dna_strings])
    
    total_samples = len(dna_strings)
    if withPseudoCounts:
        total_samples += 4
    
    counters = [collections.Counter(x[:,i]) for i in range(len(dna_strings[0]))]
    for i,c in enumerate(counters):
        for ch in 'ACGT':
            current_count = float(c[ch])
            if withPseudoCounts:
                current_count += 1
            profile[i][nuc_to_col_mapping[ch]] = current_count / total_samples
        
    return profile

def buildConsensusString(motifs):
    current_profile = createProfile(motifs, withPseudoCounts=True)
    cons_str = ""
    for val in current_profile.argmax(axis=1):
        cons_str += col_to_nuc_mapping[val]
    
    return cons_str

def getMotifScore(motifs):
    consensus_string = buildConsensusString(motifs)
    motif_score = 0
    for motif in motifs:
        motif_score += getHammingDistance(motif, consensus_string)
    return motif_score

def greedyMotifSearch(dna_str,k,t):
    best_motifs = generateInitialMotifList()
    my_motifs = []
    for kmer in allKmersOf(dna_str[0], k):
        my_motifs = []
        my_motifs.append(kmer)
        for i in range(1,t):
            current_profile = createProfile(my_motifs, withPseudoCounts=True)
            ith_motif = bestKmer(dna_str[i],current_profile, k)
            my_motifs.append(ith_motif)
        if getMotifScore(my_motifs) < getMotifScore(best_motifs):
            best_motifs = my_motifs
            
    return best_motifs

print("\n".join(greedyMotifSearch(dna_strings,k,t)))