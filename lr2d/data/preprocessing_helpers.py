

def convert_to_int(integer_string_with_commas):
    """Converts a string containing commas to an int.

    Args:
        integer_string_with_commas ( str ): String version of an integer number

    Returns:
        int: The integer represented by integer_string_with_commas,
    """
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 3:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    except ValueError:
        return None


def row_to_list(row):
    """Converts a string containing tab separated values to a list of strings.

    Args:
        row ( str ): String containing tab separated values

    Returns:
        list : List of strings containing the values in row
    """
    row = row.rstrip("\n")
    separated_entries = row.split("\t")
    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries
    return None


def preprocess(raw_data_file_path, clean_data_file_path):
    """Reads in a raw data file and outputs a preprocessed data file.

    Args:
        raw_data_file_path ( file ): Path to the raw data file to read in
        clean_data_file_path ( file ): Path to the file to output the preprocessed data.
    """
    # Try to open the file at raw_data_file_path for reading
    # If that fails, print an error message and return False
    # If that succeeds, read in the rows of the file into a list
    # Iterate over the rows, preprocess each row, and write it out to the file at clean_data_file_path

    try:
        with open(raw_data_file_path, "r") as input_file:
            rows = input_file.readlines()
    except FileNotFoundError:
        print("File not found")
        return False

    with open(clean_data_file_path, "w") as output_file:
        for row in rows:
            row_as_list = row_to_list(row)

            if row_as_list is None:
                continue

            area = convert_to_int(row_as_list[0])
            price = convert_to_int(row_as_list[1])

            if area is None or price is None:
                continue
            output_file.write("{0}\t{1}\n".format(area, price))
