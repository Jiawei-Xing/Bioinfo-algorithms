# ~ #calculate the number of breakpoints
# ~ def breakpoints(seq1, seq2):
    # ~ bp=[]
    # ~ for i in range(0, len(seq1)-1):
        # ~ if abs(seq2.index(seq1[i]) - seq2.index(seq1[i+1])) != 1:
            # ~ bp.append(i+1)
    # ~ if seq1[0] != seq2[0]:
        # ~ bp.insert(0, 0)
    # ~ if seq1[-1] != seq2[-1]:
        # ~ bp.append(len(seq1))
    # ~ return bp

# ~ #return reservals with the smallest breakpoints
# ~ def rev_dis(seq1, seq2, k=0):
    # ~ reversal={}
    # ~ new_bp={}
    # ~ for q1 in seq1.values():
        # ~ for s1 in q1:
            # ~ reversal[str(s1)]=[]
            # ~ new_bp[str(s1)]=[]
            # ~ bp = breakpoints(s1, seq2)
            # ~ if len(bp) == 0:
                # ~ return k, seq1.index(s1)
            # ~ for i in range(0, len(bp)-1):
                # ~ for j in range(i+1, len(bp)):
                    # ~ rev = s1[:bp[i]] + s1[bp[i]:bp[j]][::-1] + s1[bp[j]:]
                    # ~ reversal[str(s1)].append(rev)
                    # ~ new_bp[str(s1)].append(len(breakpoints(rev, seq2)))
    # ~ min_i={}
    # ~ seq1={}
    # ~ for n in new_bp.keys():
        # ~ min_i[n] = [i for i, x in enumerate(new_bp[n]) if x == min(new_bp[n])]
        # ~ seq1[n] = []
        # ~ for i in min_i[n]:
            # ~ seq1[n].append(reversal[n][i])
    # ~ k+=1
    # ~ print(seq1)
    # ~ return rev_dis(seq1, seq2, k)

# ~ #input seqs
# ~ seq1 = '3 1 9 5 4 2 6 8 10 7'.split()
# ~ seq2 = '4 1 5 2 7 9 10 6 3 8'.split()
# ~ print(rev_dis({0:[[seq1]]}, seq2))


def performReversal(sequence, start_index, end_index):
    prefix = sequence[:start_index]
    reversed_subsequence = sequence[start_index:end_index][::-1]
    suffix = sequence[end_index:]
    return prefix + reversed_subsequence + suffix

def findBreakpoints(sequence, target_sequence):
    breakpoints = []
    for index in range(len(sequence)-1):
        current_element = sequence[index]
        adjacent_element = sequence[index+1]
        if abs(target_sequence.index(current_element) - target_sequence.index(adjacent_element)) != 1:
            breakpoints.append(index+1)
    return breakpoints

def findMinimumBreakpointReversals(sequences, target_sequence):
    reversals = []
    for sequence in sequences:
        breakpoints = findBreakpoints(sequence[0], target_sequence)
        for start_index_i in range(len(breakpoints)-1):
            for end_index_i in range(start_index_i+1, len(breakpoints)):
                reversals.append((performReversal(sequence[0], breakpoints[start_index_i], breakpoints[end_index_i]), sequence[1] + [(breakpoints[start_index_i]-1, breakpoints[end_index_i]-1)]))
    min_bp = len(target_sequence)
    minimum_reversals = []
    for reversal in reversals:
        num_breakpoints = len(findBreakpoints(reversal[0], target_sequence))
        if num_breakpoints < min_bp:
            min_bp = num_breakpoints
            minimum_reversals = [reversal]
        elif num_breakpoints == min_bp:
            minimum_reversals.append(reversal)
    return minimum_reversals

def getReversalDistanceWithHistories(sequence, target_sequence):
    sequence = ["-"] + sequence + ["+"]
    target_sequence = ["-"] + target_sequence + ["+"]
    reversals = 0
    current_sequences = [(sequence, [])]
    while target_sequence not in [current_sequence[0] for current_sequence in current_sequences]:
        current_sequences = findMinimumBreakpointReversals(current_sequences, target_sequence)
        reversals += 1
    return reversals, current_sequences

def buildSequencesFromHistory(sequence, reversal_history):
    sequence_history = [sequence]
    reversal_sorting = []
    for reversal_start, reversal_end in reversal_history:
        sequence_history.append(performReversal(sequence_history[-1], reversal_start, reversal_end))
        reversal_sorting.append([reversal_start+1, reversal_end])
    return sequence_history, reversal_sorting

if __name__ == "__main__":

    sequence = [6, 8, 5, 2, 9, 1, 4, 10, 3, 7]
    target_sequence = [10, 1, 3, 2, 8, 9, 4, 5, 7, 6]
    
    rev_distance, histories = getReversalDistanceWithHistories(sequence, target_sequence)
    for history in histories:
        sequences_from_history, reversal_sorting  = buildSequencesFromHistory(sequence, history[1])
        print("Sequence:", sequence)
        print("Target:", target_sequence)
        print("Distance:", rev_distance)
        for s in sequences_from_history:
            print(s)
        print(reversal_sorting)
        print("\n")
