# Notes on Unit Testing

# UNIT TEST - test if a function works on its own.
# INTEGRATION TEST - test if a function works with other functions (possibly in a main section of code)

# simple interest function
#    simple interest formula is i = p * r * t
#    i = interest
#    p = principal
#    r = rate of return
#    t = time

def simple_interest(p, r, t):
	"""Calculates and returns simple interest given a principal dollars, rate as a decimal, and time in years"""
	i = p * r * t
	return i

# compound interest function
def compound_interest(p, r, t, n):
	"""Calculates and returns compound interest given the principal, interest rate,
		time in years, and number of times compounded per year"""
	a = p * (1 + r/n) ** (n * t)
	i = a - p
	return i  # could also return 'a if you wanted principal and interest

# when designing unit tests:
#        - test more than one thing
#        - test the upper and lower bounds
#        - consider unexpected cases (negatives, types, etc.)
# NOTE: you may have to deal with the imprecision of floating point values when testing numbers, 
#       in which case you want to test if the expected value is 'close enough'
#       (e.g., check if the difference is less than a small tolerance like 0.001 or 0.01)


# simple unit tests
print("Test 1: Simple Interest - Basic case")
print("Actual: ", simple_interest(100, .10, 2))
print("Expected: ", 20.0)
print("Pass test?", simple_interest(100, .10, 2) == 20.0)

print()
print("Test 2: Simple Interest - Larger values")
result = simple_interest(5500, .07, 5)
print("Actual:", result)
print("Expected:", 1925.0)
print("Pass test?", abs(result - 1925.0) < 0.001)

# Test edge cases - what happens with zeros?
print()
print("Test 3: Simple Interest - Edge case: zero principal")
result = simple_interest(0, .10, 2)
print("Actual:", result)
print("Expected:", 0.0)
print("Pass test?", result == 0.0)

print()
print("Test 4: Simple Interest - Edge case: zero interest rate")
result = simple_interest(1000, 0, 5)
print("Actual:", result)
print("Expected:", 0.0)
print("Pass test?", result == 0.0)

print()
print("Test 5: Simple Interest - Edge case: zero time")
result = simple_interest(1000, .10, 0)
print("Actual:", result)
print("Expected:", 0.0)
print("Pass test?", result == 0.0)

# compound interest unit tests
print()
print("Test 6: Compound Interest - Basic case")
result = compound_interest(1000, .10, 5, 4)
print("Actual:", result)
print("Expected:", 638.62)
# For floating point, check if close enough (within 0.01)
print("Pass test?", abs(result - 638.62) < 0.01)

print()
print("Test 7: Compound Interest - Different compounding frequency")
result = compound_interest(5000, .20, 4, 2)
print("Actual:", result)
print("Expected:", 5717.94)
print("Pass test?", abs(result - 5717.94) < 0.01)

# Test edge case for compound interest
print()
print("Test 8: Compound Interest - Edge case: zero principal")
result = compound_interest(0, .10, 5, 4)
print("Actual:", result)
print("Expected:", 0.0)
print("Pass test?", result == 0.0)
