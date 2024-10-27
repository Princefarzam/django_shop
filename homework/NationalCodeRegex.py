import re

# Function to validate Iranian national code
def is_valid_iranian_national_code(code):
    # Check if the code is a 10-digit number
    if not re.match(r'^\d{10}$', code):         
        return False
    
    # Get the check digit
    check = int(code[9])                        
    
    # Calculate the sum of digits
    sum_digits = sum(int(code[i]) * (10 - i) for i in range(9)) % 11
    
    # Validate the check digit
    return (sum_digits < 2 and check == sum_digits) or (sum_digits >= 2 and check + sum_digits == 11) 

# Example usage
print(is_valid_iranian_national_code("1960412752"))  # Replace with actual code for testing
