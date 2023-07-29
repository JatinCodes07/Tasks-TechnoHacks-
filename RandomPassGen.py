import random
import string

def gen_pass(len):
    # Define the characters to be used in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(chars) for _ in range(len))
    return password

def main():
    # Prompt the user for the desired password length
    len = int(input("Enter the desired password length: "))

    # Generate the password
    password = gen_pass(len)

    # Display the generated password
    print("Generated password:", password)

# Run the main function
if __name__ == "__main__":
    main()
