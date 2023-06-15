import numpy as np

def find_outliers(data):
    # Step 1: Sort the data in ascending order
    sorted_data = np.sort(data)
    
    # Step 2: Calculate the first quartile (Q1)
    q1 = np.percentile(sorted_data, 25)
    
    # Step 3: Calculate the third quartile (Q3)
    q3 = np.percentile(sorted_data, 75)
    
    # Step 4: Compute the IQR
    iqr = q3 - q1
    
    # Step 5: Define the outlier threshold
    lower_threshold = q1 - 1.5 * iqr
    upper_threshold = q3 + 1.5 * iqr
    
    # Step 6: Identify the outliers
    outliers = [x for x in data if x < lower_threshold or x > upper_threshold]
    
    return outliers

# Example usage:
data = [12, 15, 18, 20, 22, 25, 27, 30, 35, 100]
outliers = find_outliers(data)
print("Outliers:", outliers)
