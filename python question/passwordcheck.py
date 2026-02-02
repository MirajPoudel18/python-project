#1. Password Strength Checker
# Create a function that checks password strength based on:

# Minimum 8 characters
# Contains uppercase, lowercase, digits, and special characters
# Returns "Weak", "Medium", or "Strong"

def check(password):
    
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    min_length = len(password) >= 8
    score = sum([has_upper, has_lower, has_digit, has_special, min_length])
    
    # Determine strength
    if score == 5:
        return "Strong"
    elif score >= 3 and min_length:
        return "Medium"
    else:
        return "Weak"



password= input("Enter your password")
result=check(password)
print(f"Your password is {result}")
