# Program 20: Print Factors of a Number
# Demonstrating number factorization

print("=" * 50)
print("Program 20: Factors of a Number")
print("=" * 50)

# Method 1: Basic factor finding
print("\nMethod 1: Basic Factor Finding")

def find_factors(n):
    """Find all factors of a number"""
    if n <= 0:
        return []
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Test numbers
test_numbers = [12, 20, 30, 100]
for num in test_numbers:
    factors = find_factors(num)
    print(f"Factors of {num}: {factors}")

# Method 2: Efficient factor finding (up to sqrt(n))
print("\nMethod 2: Efficient Method (optimized)")

def find_factors_efficient(n):
    """Find factors more efficiently"""
    if n <= 0:
        return []
    factors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                factors.append(n // i)
    
    return sorted(factors)

print("Using efficient method:")
for num in test_numbers:
    factors = find_factors_efficient(num)
    print(f"Factors of {num}: {factors}")

# Method 3: Detailed output with factor properties
print("\nMethod 3: Detailed Factor Analysis")

def factor_analysis(n):
    """Analyze factors of a number"""
    factors = find_factors_efficient(n)
    print(f"\nAnalysis of {n}:")
    print(f"Total factors: {len(factors)}")
    print(f"Factors: {factors}")
    print(f"Smallest factor: {min(factors)}")
    print(f"Largest factor: {max(factors)}")
    print(f"Sum of factors: {sum(factors)}")
    print(f"Average of factors: {sum(factors) / len(factors):.2f}")

for num in [24, 36]:
    factor_analysis(num)

# Method 4: Prime and composite factors
print("\nMethod 4: Prime Factors Only")

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_factors(n):
    """Find only prime factors"""
    factors = find_factors_efficient(n)
    prime_factors = [f for f in factors if is_prime(f)]
    return prime_factors

for num in [12, 30, 100]:
    prime_factors = find_prime_factors(num)
    print(f"Prime factors of {num}: {prime_factors}")

# Method 5: Factor pairs
print("\nMethod 5: Factor Pairs")

def find_factor_pairs(n):
    """Find factor pairs that multiply to n"""
    pairs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

for num in [12, 24, 100]:
    pairs = find_factor_pairs(num)
    print(f"Factor pairs of {num}: {pairs}")

# Method 6: Display in tabular format
print("\nMethod 6: Tabular Display")

def factors_table(n):
    """Display factors in table format"""
    factors = find_factors_efficient(n)
    print(f"\nFactors of {n}:")
    print(f"{'Factor':<10} {'Other Factor':<15} {'Product':<10}")
    print("-" * 35)
    for factor in factors:
        other = n // factor
        if factor <= other:
            print(f"{factor:<10} {other:<15} {factor} × {other} = {n}")

factors_table(60)

# Method 7: User input
print("\nMethod 7: User Input")

try:
    user_num = int(input("Enter a number to find factors: "))
    
    if user_num <= 0:
        print("Please enter a positive number!")
    else:
        factors = find_factors_efficient(user_num)
        print(f"\nFactors of {user_num}: {factors}")
        print(f"Total number of factors: {len(factors)}")
        print(f"Sum of all factors: {sum(factors)}")
except ValueError:
    print("Please enter a valid integer!")

# Method 8: Perfect number check
print("\n" + "=" * 50)
print("Method 8: Perfect Number Check")
print("(A perfect number equals sum of its proper divisors)")

def is_perfect_number(n):
    """Check if number is perfect"""
    if n <= 0:
        return False
    proper_divisors = [i for i in range(1, n) if n % i == 0]
    return sum(proper_divisors) == n

print("\nChecking perfect numbers:")
for num in [6, 28, 100, 496]:
    if is_perfect_number(num):
        print(f"{num} is a perfect number")
        factors = [i for i in range(1, num) if num % i == 0]
        print(f"  Proper divisors: {factors}")
        print(f"  Sum: {sum(factors)} = {num}")
    else:
        print(f"{num} is not a perfect number")
