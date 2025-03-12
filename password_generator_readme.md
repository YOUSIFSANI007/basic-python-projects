# Password Generator

A versatile and secure random password generator with customizable complexity options and password strength evaluation.

## Features

- **Customizable Password Generation**:
  - Adjust password length
  - Include/exclude character types (lowercase, uppercase, digits, special characters)
  - Set minimum requirements for each character type
  - Generate multiple passwords at once

- **Password Strength Checker**:
  - Evaluate the strength of any password
  - Get detailed feedback on password quality
  - Score passwords on a 5-point scale

- **Multiple Usage Modes**:
  - Interactive menu-driven interface
  - Command-line arguments for scripting/automation
  - Password saving capability

## Skills Practiced

- **Random Module**: Secure random number generation for unpredictable passwords
- **String Manipulation**: Character set management and password composition
- **Loops and Conditionals**: Logic flow for password creation and validation
- **Command-Line Argument Parsing**: Flexible user interfaces
- **Object-Oriented Programming**: Modular, reusable code structure
- **Input Validation**: Robust error handling

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. Run the application:
   ```
   python password_generator.py
   ```

## Usage

### Interactive Mode

Simply run the program without arguments to enter interactive mode:

```
python password_generator.py
```

This will present a menu with the following options:
1. Generate a password
2. Check password strength
3. Password generation options
4. Exit

### Command-Line Arguments

For automation or quick password generation, use command-line arguments:

```
python password_generator.py [-h] [-l LENGTH] [--no-lowercase] [--no-uppercase] 
                            [--no-digits] [--no-special] [-m MIN_EACH] [-c COUNT]
```

Arguments:
- `-l, --length`: Password length (default: 12)
- `--no-lowercase`: Exclude lowercase letters
- `--no-uppercase`: Exclude uppercase letters
- `--no-digits`: Exclude numbers
- `--no-special`: Exclude special characters
- `-m, --min-each`: Minimum of each character type (default: 1)
- `-c, --count`: Number of passwords to generate (default: 1)

Examples:
```
# Generate a 16-character password
python password_generator.py -l 16

# Generate a password with only letters and numbers
python password_generator.py --no-special

# Generate 5 different passwords
python password_generator.py -c 5

# Generate a password with at least 2 of each character type
python password_generator.py -m 2
```

## Password Strength Criteria

Passwords are evaluated based on:
1. **Length**: Longer passwords score higher
2. **Character Variety**: Using multiple character types improves score
3. **Distribution**: Having a minimum of each character type

Strength ratings:
- **Very Weak** (1/5): Short with minimal character variety
- **Weak** (2/5): Either short or lacking character variety
- **Moderate** (3/5): Decent length with some character variety
- **Strong** (4/5): Good length with good character variety
- **Very Strong** (5/5): Excellent length with all character types

## Security Notes

- This generator uses Python's `random` module, which is suitable for most purposes but not for cryptographically sensitive applications
- Generated passwords are displayed in the console - be aware of your surroundings when generating passwords
- If you save passwords to a file, ensure appropriate file system security

## Future Enhancements

Possible improvements for future versions:
- Use `secrets` module instead of `random` for cryptographically secure passwords
- Add GUI interface option
- Implement password generation based on memorable patterns or phrases
- Add password manager integration
- Include pronounceable password option

## License

[MIT License](LICENSE)

## Author

[Your Name]

---

Feel free to contribute to this project by submitting issues or pull requests!
