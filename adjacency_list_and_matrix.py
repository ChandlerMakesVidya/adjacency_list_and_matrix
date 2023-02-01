def convert_to_matrix(adj_list):
    # Look for the highest number in all arrays, protects against cases
    # where there are more vertices than accounted for.
    n = max(map(max, adj_list)) + 1

    # Construct the matrix, initialize with 0s
    adj_matrix = [[0]*n for i in range(n)]

    # Iterate through adjacency list
    for arr in adj_list:
        vert = arr[0]  # Get current vertex
        for ele in arr:
            if ele == vert:
                continue  # This, in effect, skips the first element of the line
            adj_matrix[vert][ele] = 1  # For each number on this line, set the corresponding 0 on the matrix to 1
    return adj_matrix


def convert_to_list(adj_matrix):
    # How many vertices?
    n = len(adj_matrix)

    # Initialize the list from 0 to n
    adj_list = [[i] for i in range(n)]

    # Iterate through the matrix
    # Using counters since Python doesn't want to give me any fucking indexes
    i = 0
    for arr in adj_matrix:
        j = 0
        for ele in arr:
            if ele == 1:
                adj_list[i].append(j)
            j += 1
        i += 1

    # Remove empty rows
    for arr in adj_list:
        if len(arr) == 1:
            adj_list.remove(arr)

    return adj_list


def print_arrays(array):
    string = ''  # Empty string
    for arr in array:
        for ele in arr[:-1]:  # We will handle the last element separately...
            string += str(ele) + ' '
        string += str(arr[-1]) + '\n'  # ...to have a new line instead of a space
    print(string)


# Test cases
list1 = [[0,1,3], [1,2], [2,3]]
list2 = [[0,1,4], [1,0,2,3,4], [2,1,3], [3,1,2,4], [4,0,1,3]]
print_arrays(convert_to_matrix(list1))
print_arrays(convert_to_matrix(list2))

matrix1 = [[0,1,0,1], [0,0,1,0], [0,0,0,1], [0,0,0,0]]
matrix3 = [[0,1,0,1], [0,0,1,0], [0,0,0,0], [0,0,1,0]]  # Test empty row removal
matrix2 = [[0,1,0,0,1], [1,0,1,1,1], [0,1,0,1,0], [0,1,1,0,1], [1,1,0,1,0]]
print_arrays(convert_to_list(matrix1))
print_arrays(convert_to_list(matrix3))
print_arrays(convert_to_list(matrix2))
