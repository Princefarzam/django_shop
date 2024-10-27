import re

# Function to validate Iranian or English name
def is_valid_name(name):
    # Check if the name is in the correct format
    pattern = re.compile(r'^[a-zA-Z\u0600-\u06FF\s]+$')
    # Check if the name matches the pattern
    return bool(pattern.match(name))

# Example usage
print(is_valid_name("محمد مهربان"))  # Replace with actual name for testing
