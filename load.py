#The length of the sequence is 2055

def loadSeq(fileName):
    f = open(fileName) # open the file
    linesList = f.readlines() # read in the file as a list of its lines
    f.close() # close the file
    sequence = ""
    for i in linesList:
        sequence += i
    return sequence

salSeq = loadSeq("U81861.txt")
