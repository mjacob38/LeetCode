# Question: First Bad Version
"""
Your code is stored in a version control system, which numbers all versions sequentially.
You see a bug in your code, and you know it wasn't there before.
Write a function to find the revision that introduced the bug.
"""

# Input is sequential, so sorted
# Expected I/O?
# Size of inputs
# Data types, all ints?
# Function just finds a boolean bug or no bug
# Assume you have access to a function: is_bad(int version)
# What's the known bad version? What's the known good version? - Given parameters

# OPTIMAL SOLUTION - BINARY SEARCH
# Because the input is sorted and if we find a bug, then the following versions cannot have a bug

# Here is a typical binary search implementation:
def binary_search(input: list) -> int:
  low = 0
  high = len(input) - 1
  while low <= high:
    mid = (low + high // 2)
    if is_bad(input[mid]):
      high = mid - 1
    else:
      low = mid + 1

  return low

# Answer:
def is_bad(versions: list):
  # This is a given function
  pass

# Assumption, known_good and known_bad are bounds of our actual list
  def find_bad_revision(known_good: int, known_bad: int) -> int:
    # If we haven't narrowed the problematic code to one version
    # keep searching for the change-over point
    while known_bad - known_good > 1:
      mid = int(known_bad + known_good) / 2
      if is_bad(known_good + mid):
        known_bad = known_good + mid
      else:
        known_good = known_good + mid

      return known_bad

# Test case:
# [123,...,545]
# 123 is known_good and 545 is known_bad

# Edge cases:
# Only one good, one bad
# All bad

# Runtime analysis:
# O(1) for operations such as finding midpoint and checking is_bad
# O(log(n)) because each iteration discards half the data