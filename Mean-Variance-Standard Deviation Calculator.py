import numpy as np

def calculate(list):
    # 1. Kiểm tra số lượng phần tử
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Chuyển list thành Numpy array 3x3
    matrix = np.array(list).reshape(3, 3)

    # 3. Tính toán các chỉ số
    # Lưu ý: .tolist() được dùng để chuyển Numpy array về List thuần túy của Python
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), # Axis 1 (cột)
            matrix.mean(axis=1).tolist(), # Axis 2 (hàng)
            matrix.mean().tolist()        # Flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations