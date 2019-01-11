from aminoAcids import *
from orf import *
from load import *

def compBase(N):
    N = N.toupper()
    if(N == "A"):
        return "T"
    elif(N == "T"):
        return "A"
    elif(N == "C"):
        return "G"
    elif(N == "G"):
        return "C"

def revString(s):
    string = ""
    for n in range(0, len(s)):
        string += s[len(s)-1-n] 
    return string

def reverseComplement(DNA):
    string = revString(DNA)
    newString = ""
    for i in string:
        newString += compBase(i)
    return newString

def amino(codon):
    for i in range (0, len(codons)):
        for triple in codons[i]:
            if(codon == triple):
                return aa[i]

def codingStrandToAA(DNA):
    finalSeq = ""
    codon = ""
    for i in range(0, len(DNA), 3):
        codon = DNA[i:i+3]
        if(amino(codon) != None):
            finalSeq += amino(codon)
    return finalSeq

