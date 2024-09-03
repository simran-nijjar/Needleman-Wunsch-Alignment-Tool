# needleman_wunsch_algorithm.py

def needleman_wunsch(seq1, seq2, match, mismatch, gap):
    len1 = len(seq1)
    len2 = len(seq2)

    # Initialize the score matrix
    score_matrix = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]

    # Initialize first row and column with the gap penalties
    for i in range(1, len1 + 1):
        score_matrix[i][0] = score_matrix[i - 1][0] + gap
    for j in range(1, len2 + 1):
        score_matrix[0][j] = score_matrix[0][j - 1] + gap

    # Fill the score matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score = match
            else:
                score = mismatch
            score_matrix[i][j] = max(
                score_matrix[i - 1][j - 1] + score,
                score_matrix[i - 1][j] + gap,
                score_matrix[i][j - 1] + gap
            )

    # Create display matrix with proper formatting
    display_matrix = []

    header = "   " + "   ".join(seq1)
    display_matrix.append(f"    -{header}")

    # First row with the initial gap penalties
    first_row = ["-"] + [f"{score_matrix[0][j]:2}" for j in range(len2 + 1)]
    display_matrix.append("  ".join(first_row))

    # Remaining rows with seq2 on the left and score matrix values
    for i in range(1, len1 + 1):
        row = [seq2[i - 1]] + [f"{score_matrix[i][j]:2}" for j in range(len2 + 1)]
        display_matrix.append("  ".join(row))

    # Backtrace to find the optimal alignment
    align1 = []
    align2 = []
    i, j = len1, len2

    while i > 0 and j > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i - 1][j - 1]
        up_score = score_matrix[i - 1][j]
        left_score = score_matrix[i][j - 1]

        if seq1[i - 1] == seq2[j - 1]:
            score = match
        else:
            score = mismatch

        if current_score == diagonal_score + score:
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif current_score == up_score + gap:
            align1.append(seq1[i - 1])
            align2.append("-")
            i -= 1
        elif current_score == left_score + gap:
            align1.append("-")
            align2.append(seq2[j - 1])
            j -= 1

    # Handle remaining characters
    while i > 0:
        align1.append(seq1[i - 1])
        align2.append("-")
        i -= 1
    while j > 0:
        align1.append("-")
        align2.append(seq2[j - 1])
        j -= 1

    return ''.join(align1[::-1]), ''.join(align2[::-1]), score_matrix[len1][len2], display_matrix

