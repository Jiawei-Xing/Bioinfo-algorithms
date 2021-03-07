#calculate the number of breakpoints
def breakpoints(seq1, seq2):
    bp=[]
    for i in range(0, len(seq1)-1):
        if abs(seq2.index(seq1[i]) - seq2.index(seq1[i+1])) != 1:
            bp.append(i+1)
    if seq1[0] != seq2[0]:
        bp.insert(0, 0)
    if seq1[-1] != seq2[-1]:
        bp.append(len(seq1))
    return bp

#return reservals with the smallest breakpoints
def rev_dis(seq1, seq2, k=0):
    reversal=[]
    new_bp=[]
    for s1 in seq1:
        bp = breakpoints(s1, seq2)
        if len(bp) == 0:
            return k
        for i in range(0, len(bp)-1):
            for j in range(i+1, len(bp)):
                rev = s1[:bp[i]] + s1[bp[i]:bp[j]][::-1] + s1[bp[j]:]
                reversal.append(rev)
                new_bp.append(len(breakpoints(rev, seq2)))
    min_i = [i for i, x in enumerate(new_bp) if x == min(new_bp)]
    seq1=[]
    for i in min_i:
        seq1.append(reversal[i])
    k+=1
    return rev_dis(seq1, seq2, k)

#input seqs
seqs=[]
with open('rosalind_rear.txt') as f1:
    for line in f1:
        seqs.append(line.strip().split())

for i in range(0, 13, 3):
    print(rev_dis([seqs[i]], seqs[i+1]))


# ~ def performReversal(sequence, start_index, end_index):
    # ~ prefix = sequence[:start_index]
    # ~ reversed_subsequence = sequence[start_index:end_index][::-1]
    # ~ suffix = sequence[end_index:]
    # ~ return prefix + reversed_subsequence + suffix

# ~ def findBreakpoints(sequence, target_sequence):
    # ~ breakpoints = []
    # ~ for index in range(len(sequence)-1):
        # ~ current_element = sequence[index]
        # ~ adjacent_element = sequence[index+1]
        # ~ if abs(target_sequence.index(current_element) - target_sequence.index(adjacent_element)) != 1:
            # ~ breakpoints.append(index+1)
    # ~ return breakpoints

# ~ def findMinimumBreakpointReversals(sequences, target_sequence):
    # ~ reversals = []
    # ~ for sequence in sequences:
        # ~ breakpoints = findBreakpoints(sequence, target_sequence)
        # ~ for start_index_i in range(len(breakpoints)-1):
            # ~ for end_index_i in range(start_index_i+1, len(breakpoints)):
                # ~ reversals.append(performReversal(sequence, breakpoints[start_index_i], breakpoints[end_index_i]))
    # ~ min_bp = len(target_sequence)
    # ~ minimum_reversals = []
    # ~ for reversal in reversals:
        # ~ num_breakpoints = len(findBreakpoints(reversal, target_sequence))
        # ~ if num_breakpoints < min_bp:
            # ~ min_bp = num_breakpoints
            # ~ minimum_reversals = [reversal]
        # ~ elif num_breakpoints == min_bp:
            # ~ minimum_reversals.append(reversal)
    # ~ return minimum_reversals

# ~ def getReversalDistance(sequence, target_sequence):
    # ~ sequence = ["-"] + sequence + ["+"]
    # ~ target_sequence = ["-"] + target_sequence + ["+"]
    # ~ reversals = 0
    # ~ current_sequences = [sequence]
    # ~ while target_sequence not in current_sequences:
        # ~ current_sequences = findMinimumBreakpointReversals(current_sequences, target_sequence)
        # ~ reversals += 1
    # ~ return reversals

# ~ if __name__ == "__main__":

    # ~ sequence = '3 10 8 2 5 4 7 1 6 9'.split()
    # ~ target_sequence = '5 2 3 1 7 4 10 8 6 9'.split()
    
    # ~ print(getReversalDistance(sequence, target_sequence))
