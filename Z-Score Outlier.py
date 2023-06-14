import numpy as np

def find_outliers_z_score(data, threshold):
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std_dev = np.std(data)
    
    outliers = []
    
    # Calculate the Z-score for each data point
    for x in data:
        z_score = (x - mean) / std_dev
        
        # Check if the Z-score exceeds the threshold
        if abs(z_score) > threshold:
            outliers.append(x)
    
    return outliers

# Example usage
dataset = [2, 4, 6, 8, 10, 12, 14, 100,101]
threshold = 1

outliers = find_outliers_z_score(dataset, threshold)
print("Outliers:", outliers)
