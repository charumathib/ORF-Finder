def restOfORF(DNA):
    cod = ""
    for i in range(0, len(DNA)-2, 3):
        cod = DNA[i:(i+3)]
        if cod in ["TAG", "TAA", "TGA"]:
            return DNA[:i]
    return DNA

def oneFrame(DNA):
    l = []
    string = ""
    for i in range(0, len(DNA)):
        triple = DNA[i:i+3]
        if(triple == "ATG"):
            string = restOfORF(DNA[i:])
            l.append(string)
    return l

def longestORF(DNA):
    outList = oneFrame(DNA)
    longest = ""
    for element in outList:
        if(len(element) > len(longest)):
            longest = element
    return longest








        