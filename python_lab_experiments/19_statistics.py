# Program 19: Statistics - Average, Mean, Median, Standard Deviation
# Demonstrating statistical calculations

import math

print("=" * 50)
print("Program 19: Statistical Calculations")
print("=" * 50)

# Method 1: Using manual calculations
print("\nMethod 1: Manual Calculations")

def calculate_mean(data):
    """Calculate mean/average"""
    return sum(data) / len(data)

def calculate_median(data):
    """Calculate median"""
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def calculate_std_dev(data):
    """Calculate standard deviation"""
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Test data
marks = [75, 80, 85, 90, 88, 92, 78]
print(f"Marks: {marks}")
print(f"Average/Mean: {calculate_mean(marks):.2f}")
print(f"Median: {calculate_median(marks):.2f}")
print(f"Standard Deviation: {calculate_std_dev(marks):.2f}")

# Method 2: Using statistics module
print("\n" + "=" * 50)
print("Method 2: Using Statistics Module")

import statistics

data = [10, 12, 15, 18, 20, 22, 25]
print(f"Data: {data}")
print(f"Mean: {statistics.mean(data):.2f}")
print(f"Median: {statistics.median(data):.2f}")
print(f"Mode: {statistics.mode(data) if len(set(data)) < len(data) else 'No mode'}")
print(f"Std Dev (sample): {statistics.stdev(data):.2f}")
print(f"Std Dev (population): {statistics.pstdev(data):.2f}")

# Method 3: Detailed statistics function
print("\nMethod 3: Complete Statistics Report")

def statistics_report(dataset, name="Data"):
    """Generate complete statistics report"""
    print(f"\n{name} Statistics Report:")
    print(f"Values: {dataset}")
    print(f"Count: {len(dataset)}")
    print(f"Sum: {sum(dataset)}")
    print(f"Average: {statistics.mean(dataset):.2f}")
    print(f"Median: {statistics.median(dataset):.2f}")
    print(f"Min: {min(dataset)}")
    print(f"Max: {max(dataset)}")
    print(f"Range: {max(dataset) - min(dataset)}")
    print(f"Standard Deviation: {statistics.stdev(dataset):.2f}")

# Example datasets
students_marks = [65, 70, 75, 80, 85, 90]
statistics_report(students_marks, "Students' Marks")

test_scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
statistics_report(test_scores, "Test Scores")

# Method 4: Multiple datasets comparison
print("\n" + "=" * 50)
print("Method 4: Comparing Multiple Datasets")

class_a = [70, 75, 80, 85, 88]
class_b = [65, 78, 82, 90, 95]

print(f"\nClass A: {class_a}")
print(f"Class B: {class_b}")
print(f"\n{'Metric':<20} {'Class A':<15} {'Class B':<15}")
print("-" * 50)
print(f"{'Mean':<20} {statistics.mean(class_a):<15.2f} {statistics.mean(class_b):<15.2f}")
print(f"{'Median':<20} {statistics.median(class_a):<15.2f} {statistics.median(class_b):<15.2f}")
print(f"{'Min':<20} {min(class_a):<15} {min(class_b):<15}")
print(f"{'Max':<20} {max(class_a):<15} {max(class_b):<15}")
print(f"{'Std Dev':<20} {statistics.stdev(class_a):<15.2f} {statistics.stdev(class_b):<15.2f}")

# Method 5: User input
print("\n" + "=" * 50)
print("Method 5: User Input for Statistics")

try:
    input_str = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, input_str.split()))
    
    if len(numbers) > 0:
        print(f"\nStatistics for entered numbers:")
        print(f"Count: {len(numbers)}")
        print(f"Sum: {sum(numbers):.2f}")
        print(f"Average: {statistics.mean(numbers):.2f}")
        print(f"Median: {statistics.median(numbers):.2f}")
        print(f"Min: {min(numbers):.2f}")
        print(f"Max: {max(numbers):.2f}")
        if len(numbers) > 1:
            print(f"Std Dev: {statistics.stdev(numbers):.2f}")
    else:
        print("No numbers entered!")
except ValueError:
    print("Please enter valid numbers!")

# Method 6: Visual representation
print("\n" + "=" * 50)
print("Method 6: Understanding Median and Mean")

sample_data = [10, 15, 20, 25, 30]
print(f"\nData: {sample_data}")
print(f"Mean: {statistics.mean(sample_data)}")
print(f"Median: {statistics.median(sample_data)}")
print("\nMean vs Median:")
print("- Mean: Average of all values")
print("- Median: Middle value when sorted")

# Skewed data example
skewed_data = [10, 15, 20, 25, 100]
print(f"\nSkewed Data: {skewed_data}")
print(f"Mean: {statistics.mean(skewed_data):.2f} (affected by outlier)")
print(f"Median: {statistics.median(skewed_data)} (not affected by outlier)")

# Method 7: Frequency distribution
print("\n" + "=" * 50)
print("Method 7: Frequency Distribution")

scores = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(f"Scores: {scores}")
print("\nFrequency Distribution:")
print(f"{'Score':<10} {'Frequency':<15} {'Percentage':<15}")
print("-" * 40)
for score in sorted(set(scores)):
    freq = scores.count(score)
    percentage = (freq / len(scores)) * 100
    print(f"{score:<10} {freq:<15} {percentage:<15.2f}%")
