import re

# Function to validate Iranian phone number
def is_valid_iranian_phone_number(phone_number):
    # Check if the phone number is in the correct format    
    pattern = re.compile(r'^(0|0098|\+98)?9\d{9}$')
    # Check if the phone number matches the pattern 
    return bool(pattern.match(phone_number))

# Example usage
print(is_valid_iranian_phone_number("+989121326389"))  # Replace with actual phone number for testing
