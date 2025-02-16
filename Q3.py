def compute_edit_distance(s1, s2):
    # Create a table to store results of subproblems
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp[][] in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Min. operations = j (insertions)
            elif j == 0:
                dp[i][j] = i  # Min. operations = i (deletions)
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No cost if characters are the same
            else:
                # Substitution cost is 2, insertion and deletion costs are 1
                dp[i][j] = min(dp[i - 1][j - 1] + 2,  # Replace
                               dp[i][j - 1] + 1,  # Insert
                               dp[i - 1][j] + 1)  # Remove
    return dp[m][n]


def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Process lines to separate references and hypotheses
    reference = None
    results = []

    for line in lines:
        line = line.strip()
        if line:
            typ, word = line.split(maxsplit=1)
            if typ == 'R':
                reference = word
                results.append(f'R {word}')
            elif typ == 'H' and reference is not None:
                edit_distance = compute_edit_distance(reference, word)
                results.append(f'H {word} {edit_distance}')

    # Write results to the output file
    with open(output_file, 'w') as file:
        for result in results:
            file.write(result + '\n')


# Call the process_file function
input_filename = 'word_corpus.txt'
output_filename = 'word_edit_distance.txt'
process_file(input_filename, output_filename)