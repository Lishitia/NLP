def dynamic_programming_sentences(sentence1, sentence2):
    # Split the sentences into words
    x = sentence1.split()
    y = sentence2.split()
    m, n = len(x), len(y)

    # Create the dynamic programming table, T
    T = [[0] * (n + 1) for _ in range(m + 1)]

    # Define costs for insertion, deletion, and substitution
    def Ins(c):
        return 1

    def Del(c):
        return 1

    def Sub(a, b):
        return 0 if a == b else 2  # Substitution cost is 2 if words are different

    # Initialize the DP table
    for i in range(1, m + 1):
        T[i][0] = T[i - 1][0] + Del(x[i - 1])
    for j in range(1, n + 1):
        T[0][j] = T[0][j - 1] + Ins(y[j - 1])

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[i][j] = min(T[i - 1][j - 1] + Sub(x[i - 1], y[j - 1]),
                          T[i - 1][j] + Del(x[i - 1]),
                          T[i][j - 1] + Ins(y[j - 1]))

    # Traceback to find the alignment
    alignment_x, alignment_y = [], []
    i, j = m, n
    while i > 0 and j > 0:
        if T[i][j] == T[i - 1][j - 1] + Sub(x[i - 1], y[j - 1]):
            alignment_x.append(x[i - 1])
            alignment_y.append(y[j - 1])
            i, j = i - 1, j - 1
        elif T[i][j] == T[i - 1][j] + Del(x[i - 1]):
            alignment_x.append(x[i - 1])
            alignment_y.append('-')
            i -= 1
        else:
            alignment_x.append('-')
            alignment_y.append(y[j - 1])
            j -= 1

    while i > 0:
        alignment_x.append(x[i - 1])
        alignment_y.append('-')
        i -= 1
    while j > 0:
        alignment_x.append('-')
        alignment_y.append(y[j - 1])
        j -= 1

    # Reverse the alignments as we've built them backwards
    alignment_x.reverse()
    alignment_y.reverse()

    # Format the output to match the maximum word length
    max_length_per_column = [max(len(a), len(b)) for a, b in zip(alignment_x, alignment_y)]
    formatted_x = ' '.join(word.ljust(max_length_per_column[i]) for i, word in enumerate(alignment_x))
    formatted_y = ' '.join(word.ljust(max_length_per_column[i]) for i, word in enumerate(alignment_y))
    vertical_bars = ' '.join('|'.center(max_length_per_column[i]) if ax != '-' or ay != '-' else ' '.center(max_length_per_column[i]) for i, (ax, ay) in enumerate(zip(alignment_x, alignment_y)))

    return T[m][n], formatted_x, vertical_bars, formatted_y

def main():
    sentence1 = input("Enter the first sentence: ")
    sentence2 = input("Enter the second sentence: ")
    cost, formatted_x, vertical_bars, formatted_y = dynamic_programming_sentences(sentence1, sentence2)
    print("The cost is:", cost)
    print("A possible alignment is:")
    print(formatted_x)
    print(vertical_bars)
    print(formatted_y)

if __name__ == "__main__":
    main()