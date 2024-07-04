import random
import string

def generate_password(length, complexity):
    
    # Define character sets based on complexity
    char_sets = [
        string.ascii_lowercase,
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase + string.ascii_uppercase + string.digits,
        string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    ]
    
    if complexity < 1 or complexity > 4:
        raise ValueError("Complexity level must be between 1 and 4")
    
    # Select the character set based on complexity
    characters = char_sets[complexity - 1]
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Ask user for the length and complexity of the password
    try:
        length = int(input("Enter the length of the password: "))
        complexity = int(input("Enter the complexity level (1-4): "))
        
        # Generate the password
        password = generate_password(length, complexity)
        
        # Display the generated password
        print("Generated password:", password)
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()