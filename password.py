import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self):
        self.length = 12
        self.complexity = "Medium"

    def set_length(self, length):
        self.length = length

    def set_complexity(self, complexity):
        self.complexity = complexity

    def generate_password(self):
        try:
            if self.complexity == "Low":
                characters = string.ascii_letters + string.digits
            elif self.complexity == "Medium":
                characters = string.ascii_letters + string.digits + string.punctuation
            elif self.complexity == "High":
                characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation

            password = ''.join(random.choice(characters) for _ in range(self.length))
            return password
        except ValueError:
            return "Error: Invalid password length or complexity."

    def copy_to_clipboard(self, password):
        pyperclip.copy(password)
        return "Password copied to clipboard!"

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.set_length(12)  
    password_generator.set_complexity("Medium")

    generated_password = password_generator.generate_password()
    print("Generated Password:", generated_password)

    copy_message = password_generator.copy_to_clipboard(generated_password)
    print(copy_message)
