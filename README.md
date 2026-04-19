# Mean-Variance-Standard Deviation Calculator

This is the first project of the **Data Analysis with Python** certification from freeCodeCamp. It demonstrates the use of **NumPy** to perform matrix operations and statistical calculations.

## Project Description

The goal of this project is to create a function named `calculate()` that uses NumPy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The function takes a list of 9 digits as input and returns a dictionary containing the following statistics across three different perspectives:
* **Axis 1**: Calculations along the columns.
* **Axis 2**: Calculations along the rows.
* **Flattened**: Calculations for the entire matrix.

## Technologies Used
* **Python 3.x**
* **NumPy**: For high-performance multidimensional array processing and mathematical functions.

## Implementation Details
1.  **Input Validation**: Checks if the input list contains exactly 9 elements, otherwise raises a `ValueError`.
2.  **Reshaping**: Converts the 1D list into a 3x3 NumPy array.
3.  **Statistical Functions**: Utilizes `np.mean()`, `np.var()`, `np.std()`, `np.max()`, `np.min()`, and `np.sum()`.
4.  **Data Formatting**: Converts NumPy arrays back to standard Python lists using `.tolist()` to ensure compatibility with the required output format.

## How to Run
1.  Make sure you have NumPy installed:
    ```bash
    pip install numpy
    ```
2.  Clone the repository:
    ```bash
    git clone [https://github.com/LyNhutMinh/Mean-Variance-Standard-Deviation-Calculator.git](https://github.com/LyNhutMinh/Mean-Variance-Standard-Deviation-Calculator.git)
    ```
3.  Run the script:
    ```bash
    python mean_var_std.py
    ```

## Example Output
For an input list `[0,1,2,3,4,5,6,7,8]`, the function returns:
```json
{
  "mean": [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  "variance": [[6.0, 6.0, 6.0], [0.6666, 0.6666, 0.6666], 6.6666],
  ...
}
