<h1 align="center">🧮 Mean-Variance-Standard Deviation Calculator</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/freeCodeCamp-0A0A23?style=for-the-badge&logo=freecodecamp&logoColor=white" alt="freeCodeCamp">
</div>

<br>

## 📝 Overview
This is the first project of the **Data Analysis with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/). The core objective is to utilize **NumPy** to perform complex matrix operations and generate a comprehensive statistical summary from a simple list of numbers.

## ⚙️ Functionality
The core of this project is the `calculate()` function. It takes a list of 9 digits, converts it into a `3x3` NumPy array, and calculates the mean, variance, standard deviation, max, min, and sum across three different perspectives:
* **Axis 0 (Columns):** Calculations running vertically down the columns.
* **Axis 1 (Rows):** Calculations running horizontally across the rows.
* **Flattened:** Calculations considering all 9 elements of the matrix as a single dataset.

## 🛠️ Implementation Details
1. **Input Validation:** The script strictly enforces that the input list contains exactly 9 elements. If not, it gracefully raises a `ValueError` with the message: *"List must contain nine numbers."*
2. **Reshaping:** Converts the 1D flat list into a 2D `3x3` matrix using `np.reshape()`.
3. **Statistical Computations:** Heavily relies on NumPy's optimized mathematical functions (`np.mean`, `np.var`, `np.std`, `np.max`, `np.min`, `np.sum`).
4. **Data Formatting:** Ensures full compatibility with standard Python data structures by converting the resulting NumPy arrays back into standard Python lists using `.tolist()` before packaging them into the final dictionary.

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/LyNhutMinh/Mean-Variance-Standard-Deviation-Calculator.git](https://github.com/LyNhutMinh/Mean-Variance-Standard-Deviation-Calculator.git)
