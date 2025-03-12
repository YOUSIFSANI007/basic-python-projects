import random
import string
import argparse
import sys

class PasswordGenerator:
    def __init__(self):
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    def generate_password(self, length=12, use_lowercase=True, use_uppercase=True, 
                          use_digits=True, use_special=True, min_of_each=1):
        """
        Generate a random password with specified complexity requirements.
        
        Args:
            length (int): Length of the password to generate
            use_lowercase (bool): Include lowercase letters
            use_uppercase (bool): Include uppercase letters
            use_digits (bool): Include numbers
            use_special (bool): Include special characters
            min_of_each (int): Minimum count of each selected character type
            
        Returns:
            str: Generated password
        """
        # Validate inputs
        if length < 4 and (use_lowercase + use_uppercase + use_digits + use_special) * min_of_each > length:
            raise ValueError("Password length too short to satisfy minimum character requirements")
            
        if not any([use_lowercase, use_uppercase, use_digits, use_special]):
            raise ValueError("At least one character type must be selected")
        
        # Prepare character pool
        char_pool = ""
        if use_lowercase:
            char_pool += self.lowercase_letters
        if use_uppercase:
            char_pool += self.uppercase_letters
        if use_digits:
            char_pool += self.digits
        if use_special:
            char_pool += self.special_chars
            
        # Generate initial password with required minimums
        password = []
        
        # Add minimum characters from each selected type
        if use_lowercase and min_of_each > 0:
            password.extend(random.sample(self.lowercase_letters, min_of_each))
        if use_uppercase and min_of_each > 0:
            password.extend(random.sample(self.uppercase_letters, min_of_each))
        if use_digits and min_of_each > 0:
            password.extend(random.sample(self.digits, min_of_each))
        if use_special and min_of_each > 0:
            password.extend(random.sample(self.special_chars, min_of_each))
            
        # Fill remaining length with random characters from the pool
        remaining_length = length - len(password)
        if remaining_length > 0:
            password.extend(random.choices(char_pool, k=remaining_length))
            
        # Shuffle the password to avoid predictable patterns
        random.shuffle(password)
        
        return ''.join(password)
    
    def check_password_strength(self, password):
        """
        Evaluate the strength of a password.
        
        Args:
            password (str): Password to evaluate
            
        Returns:
            tuple: (score, message) where score is 1-5 and message is feedback
        """
        score = 0
        feedback = []
        
        # Length check
        if len(password) < 8:
            score += 1
            feedback.append("Password is too short")
        elif len(password) < 12:
            score += 2
            feedback.append("Good length")
        else:
            score += 3
            feedback.append("Excellent length")
            
        # Character variety checks
        has_lower = any(c in self.lowercase_letters for c in password)
        has_upper = any(c in self.uppercase_letters for c in password)
        has_digit = any(c in self.digits for c in password)
        has_special = any(c in self.special_chars for c in password)
        
        variety_score = has_lower + has_upper + has_digit + has_special
        score += variety_score
        
        if variety_score < 2:
            feedback.append("Add more types of characters")
        elif variety_score < 4:
            feedback.append("Good character variety")
        else:
            feedback.append("Excellent character variety")
            
        # Normalize score to 1-5 range
        final_score = min(5, max(1, score // 2))
        
        strength_labels = {
            1: "Very Weak",
            2: "Weak",
            3: "Moderate",
            4: "Strong",
            5: "Very Strong"
        }
        
        result_message = f"Strength: {strength_labels[final_score]} ({final_score}/5)\nFeedback: {' | '.join(feedback)}"
        
        return final_score, result_message

def main():
    # Command-line interface
    parser = argparse.ArgumentParser(description="Generate secure random passwords")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")
    parser.add_argument("-m", "--min-each", type=int, default=1, help="Minimum of each char type (default: 1)")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
    
    # Interactive mode if no arguments provided
    if len(sys.argv) == 1:
        return interactive_mode()
    
    args = parser.parse_args()
    
    # Ensure at least one character type is selected
    if args.no_lowercase and args.no_uppercase and args.no_digits and args.no_special:
        print("Error: At least one character type must be enabled")
        return
    
    generator = PasswordGenerator()
    for i in range(args.count):
        try:
            password = generator.generate_password(
                length=args.length,
                use_lowercase=not args.no_lowercase,
                use_uppercase=not args.no_uppercase,
                use_digits=not args.no_digits,
                use_special=not args.no_special,
                min_of_each=args.min_each
            )
            
            strength, message = generator.check_password_strength(password)
            print(f"\nPassword {i+1}:\n{password}")
            print(message)
            
        except ValueError as e:
            print(f"Error: {e}")
            return

def interactive_mode():
    """Run the password generator in interactive mode with a menu interface"""
    generator = PasswordGenerator()
    
    while True:
        print("\n===== PASSWORD GENERATOR =====")
        print("1. Generate a password")
        print("2. Check password strength")
        print("3. Password generation options")
        print("4. Exit")
        print("==============================")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Get saved options or use defaults
            options = getattr(interactive_mode, 'options', {
                'length': 12,
                'use_lowercase': True,
                'use_uppercase': True,
                'use_digits': True,
                'use_special': True,
                'min_of_each': 1
            })
            
            try:
                password = generator.generate_password(**options)
                strength, message = generator.check_password_strength(password)
                
                print("\n----- Generated Password -----")
                print(password)
                print("-----------------------------")
                print(message)
                print("-----------------------------")
                
                save = input("Save this password to file? (y/n): ").lower()
                if save == 'y':
                    with open("saved_passwords.txt", "a") as f:
                        f.write(f"{password} - {message}\n")
                    print("Password saved to 'saved_passwords.txt'")
            
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            password = input("Enter password to check: ")
            strength, message = generator.check_password_strength(password)
            print("\n----- Password Strength -----")
            print(message)
            print("-----------------------------")
        
        elif choice == '3':
            options = getattr(interactive_mode, 'options', {
                'length': 12,
                'use_lowercase': True,
                'use_uppercase': True,
                'use_digits': True,
                'use_special': True,
                'min_of_each': 1
            })
            
            print("\n----- Password Options -----")
            print(f"Current settings:")
            print(f"- Length: {options['length']}")
            print(f"- Lowercase letters: {'Yes' if options['use_lowercase'] else 'No'}")
            print(f"- Uppercase letters: {'Yes' if options['use_uppercase'] else 'No'}")
            print(f"- Numbers: {'Yes' if options['use_digits'] else 'No'}")
            print(f"- Special characters: {'Yes' if options['use_special'] else 'No'}")
            print(f"- Minimum of each type: {options['min_of_each']}")
            print("---------------------------")
            
            try:
                length = int(input("Enter password length (4-100): "))
                if length < 4 or length > 100:
                    print("Invalid length. Using default (12)")
                    length = 12
                
                use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
                use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
                use_digits = input("Include numbers? (y/n): ").lower() == 'y'
                use_special = input("Include special characters? (y/n): ").lower() == 'y'
                
                if not any([use_lower, use_upper, use_digits, use_special]):
                    print("At least one character type must be selected. Using all types.")
                    use_lower = use_upper = use_digits = use_special = True
                
                min_each = int(input("Minimum of each selected type (0-5): "))
                if min_each < 0 or min_each > 5:
                    print("Invalid minimum. Using default (1)")
                    min_each = 1
                
                # Save options for future use
                interactive_mode.options = {
                    'length': length,
                    'use_lowercase': use_lower,
                    'use_uppercase': use_upper,
                    'use_digits': use_digits,
                    'use_special': use_special,
                    'min_of_each': min_each
                }
                
                print("Options saved successfully!")
                
            except ValueError:
                print("Invalid input. Please enter a number when requested.")
        
        elif choice == '4':
            print("Thank you for using Password Generator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
