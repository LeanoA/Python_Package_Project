import numpy as np
from scipy.stats import linregress


def split_into_training_and_testing_sets(data_array):
    """ Split data array into training and testing sets, returning both

    Args:
        data_array (int): Numpy array containing clean data

    Raises:
        ValueError: Argument data_array must be two dimensional.
        ValueError: Argument data_array must have at least 2 rows.

    Returns:
        tuple: Tuple containing:
            training_set (int): Portion of data_array used for training
            testing_set (int): Portion of data_array used for testing
    """
    dim = data_array.ndim
    if dim != 2:
        raise ValueError(
            "Argument data_array must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        raise ValueError(
            "Argument data_array must have at least 2 rows, it actually has just {0}".format(num_rows))
    num_training = int(0.75 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]


def model_test(testing_set, slope, intercept):
    """Test the model with testing set and compute the R^2 value

    Args:
        testing_set (ndarray (int)): Clean data of actual values of area and prices.
        slope (int): slope of the linear regression model 
        intercept (int): intercept of the linear regression model

    Raises:
        ValueError: Argument testing_set must be two dimensional.

    Returns:
        int : R^2 value
    """
    dim = testing_set.ndim
    if dim != 2:
        raise ValueError(
            "Argument testing_set must be two dimensional. Got {0} dimensional array instead!".format(
                dim)
        )
    actual_price = testing_set[:, 1]
    predicted_price = slope*testing_set[:, 0] + intercept
    residual_sum_of_squares = np.sum(
        np.square(predicted_price - actual_price)) / testing_set.shape[0]
    return 1 - residual_sum_of_squares / np.var(actual_price)


def train_model(training_set):
    """Train the model with training set and return the slope and intercept

    Args:
        training_set (numpy.ndarray(int)): Clean data of area and prices.

    Raises:
        ValueError: Argument training_set must be two dimensional.
        ValueError: Argument training_set must have at least 2 rows for linear regression to work.

    Returns:
        tuple: Tuple containing:
            slope (int): slope of the linear regression model. 

            intercept (int): intercept of the linear regression model
    """
    dim = training_set.ndim
    if dim != 2:
        raise ValueError(
            "Argument training_set must be two dimensional. Got {0} dimensional array instead!".format(
                dim)
        )
    num_rows = training_set.shape[0]
    if num_rows < 2:
        raise ValueError("Argument training_set must have at least 2 rows for linear regression to work, "
                         "it actually has just {0}".format(num_rows)
                         )
    num_cols = training_set.shape[1]

    slope, intercept, _, _, _ = linregress(
        training_set[:, 0], training_set[:, 1])
    return slope, intercept
