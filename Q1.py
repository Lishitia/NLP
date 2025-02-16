def dynamic_programming(x, y):
    m, n = len(x), len(y)
    # Create the dynamic programming table, T
    T = [[0] * (n + 1) for _ in range(m + 1)]

    # Define costs for insertion, deletion, and substitution
    def Ins(c):
        return 1

    def Del(c):
        return 1

    def Sub(a, b):
        return 0 if a == b else 2  # Substitution cost is 2 if characters are different

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

    # Join alignments into strings
    final_alignment_x = ' '.join(alignment_x)
    final_alignment_y = ' '.join(alignment_y)

    return T[m][n], final_alignment_x, final_alignment_y

def main():
    x = input("Enter the first string: ")
    y = input("Enter the second string: ")
    cost, align_x, align_y = dynamic_programming(x, y)
    print("The cost is:", cost)
    print("A possible alignment is:")
    print(align_x)
    print('| ' * len(align_x.split()))
    print(align_y)

if __name__ == "__main__":
    main()