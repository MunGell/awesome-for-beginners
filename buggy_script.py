#!/usr/bin/env python3
"""
A buggy Python script for testing Greptile's bug detection capabilities.
This script contains various types of bugs that should be caught.
"""

import os
import sys
import json
from typing import List, Dict

def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

def process_data(data: Dict) -> str:
    """Process some data and return a result."""
    if 'name' not in data:
        return "No name found"
    
    # Bug: This will cause a KeyError if 'age' doesn't exist
    age = data['age']
    
    # Bug: This will cause a TypeError if age is not a number
    if age > 18:
        return f"{data['name']} is an adult"
    else:
        return f"{data['name']} is a minor"

def read_config_file(filename: str) -> Dict:
    """Read and parse a JSON configuration file."""
    # Bug: No error handling for file not found
    with open(filename, 'r') as f:
        config = json.load(f)
    return config

def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers."""
    # Bug: No check for division by zero
    return a / b

def find_maximum(numbers: List[int]) -> int:
    """Find the maximum number in a list."""
    if not numbers:
        return 0  # Bug: Should probably return None or raise an exception
    
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

def validate_email(email: str) -> bool:
    """Validate an email address."""
    # Bug: Very basic validation, will accept invalid emails
    return '@' in email and '.' in email

def main():
    """Main function with various buggy operations."""
    # Test data with missing 'age' field
    test_data = {
        'name': 'John Doe'
        # Missing 'age' field - will cause KeyError
    }
    
    # This will cause a KeyError
    result = process_data(test_data)
    print(result)
    
    # This will cause division by zero
    result = divide_numbers(10, 0)
    print(f"10 / 0 = {result}")
    
    # This will cause a FileNotFoundError
    config = read_config_file('nonexistent_config.json')
    print(config)
    
    # This will work but return 0 for empty list (questionable behavior)
    max_num = find_maximum([])
    print(f"Maximum of empty list: {max_num}")
    
    # This will accept invalid emails
    invalid_emails = ['not-an-email', 'test@', '@domain.com']
    for email in invalid_emails:
        is_valid = validate_email(email)
        print(f"{email} is valid: {is_valid}")

if __name__ == "__main__":
    main()
