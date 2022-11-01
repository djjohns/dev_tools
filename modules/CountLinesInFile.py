
def count_lines_in_file(filename=None):
    '''
    ### Count the number of lines in the given file.
    ### Kwargs:
    filename (str): File name or path to the file to count the lines of.
    ### Returns:
    number_of_lines (int): Number of lines in the given file.
    ### Example Usage:
    ```
    file = "some_file.txt"
    num_of_lines_in_some_file = count_lines_in_file(filename="some_file.txt")
    print(f"Total number of lines in {file}: {num_of_lines_in_some_file} ")
    ```
    '''
    number_of_lines = sum(1 for line in open(filename))
    return number_of_lines


if __name__ == '__main__':
    file = "some_file.txt"
    num_of_lines_in_some_file = count_lines_in_file(filename="some_file.txt")
    print(f"Total number of lines in {file}: {num_of_lines_in_some_file} ")