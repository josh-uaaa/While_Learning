import random
import string

class Robot:
    existing_names = set()

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        while True:
            generated_name = random.choices(string.ascii_uppercase, k=2)
            generated_name += random.choices(string.digits, k=3)
            generated_name = "".join(generated_name)
            if generated_name not in Robot.existing_names:
                Robot.existing_names.add(generated_name)
                return generated_name

    def reset(self):
        self.name = self.generate_name()