import list_statistics
# Mean

def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Median

def calculate_median(numbers):
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

# Range

def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

# Sum
def calculate_sum(numbers):
    return sum(numbers)

test_list = [10, 20, 30, 40, 50]
print("Mean:", calculate_mean(test_list))
print("Median:", calculate_median(test_list))
print("Range:", calculate_range(test_list))
print("Sum:", calculate_sum(test_list))