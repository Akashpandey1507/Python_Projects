
import numpy as np

def identify_outliers(data):
    mean = np.mean(data)
    std = np.std(data)
    threshold = 3  # Z-score threshold for identifying outliers
    
    outliers = []
    
    for value in data:
        z_score = (value - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(value)
    
    return outliers

# Example usage
data = [1, 2, 3, 4, 5, 20]  # Sample dataset
outliers = identify_outliers(data)
print("Outliers:", outliers)
