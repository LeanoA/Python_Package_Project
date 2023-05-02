import numpy as np


def get_data_as_numpy_array(clean_data_file_path, num_columns):
    """ Get the contents of the data file as a numpy array

    Args:
        clean_data_file_path(str): Path to the clean data file
        num_columns(int): Number of columns in the data file

    Raises:
        ValueError: Badly formatted data file
        ValueError: Data file has wrong number of columns

    Returns:
        numpy.ndarray(int) : Numpy array of data from the file
    """
    result = np.empty((0, num_columns))
    with open(clean_data_file_path, "r") as f:
        rows = f.readlines()
        for row_num in range(len(rows)):
            try:
                row = np.array([rows[row_num].rstrip(
                    "\n").split("\t")], dtype=float)
            except ValueError:
                raise ValueError("Line {0} of {1} is badly formatted".format(
                    row_num + 1, clean_data_file_path))
            else:
                if row.shape != (1, num_columns):
                    raise ValueError("Line {0} of {1} does not have {2} columns".format(row_num + 1,
                                                                                        clean_data_file_path,
                                                                                        num_columns
                                                                                        )
                                     )
            result = np.append(result, row, axis=0)
    return result
