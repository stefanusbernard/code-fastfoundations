def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)