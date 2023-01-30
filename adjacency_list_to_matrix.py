def convert_to_matrix(adj_list):
    # Look for the highest number in all arrays, protects against cases
    # where there are more vertices than accounted for.
    n = max(map(max, adj_list)) + 1

    # Construct the matrix, initialize with 0s
    matrix = [[0]*n for i in range(n)]

    # Iterate through adjacency list
    for arr in adj_list:
        vert = arr[0]  # Get current vertex
        for ele in arr:
            if ele == vert:
                continue  # This, in effect, skips the first element of the line
            matrix[vert][ele] = 1  # For each number on this line, set the corresponding 0 on the matrix to 1
    return matrix


def print_matrix(mat):
    string = ''  # Empty string
    for arr in mat:
        for ele in arr[:-1]:  # We will handle the last element separately...
            string += str(ele) + ' '
        string += str(arr[-1]) + '\n'  # ...to have a new line instead of a space
    print(string)


# Test cases
adj1 = [[0,1,3], [1,2], [2,3]]
adj2 = [[0,1,4], [1,0,2,3,4], [2,1,3], [3,1,2,4], [4,0,1,3]]
print_matrix(convert_to_matrix(adj1))
print_matrix(convert_to_matrix(adj2))
