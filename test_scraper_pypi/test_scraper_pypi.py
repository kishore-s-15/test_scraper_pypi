"""Main module."""
from typing import Optional

class TestScraperPypi:
    """Main class."""

    def __init__(self, name: Optional[str] = None):
        self.name = name

    def main(self):
        """Main function."""
        return self.return_greet_message()

    def return_greet_message(self):
        """Return a greeting message."""

        message = "Hello "
        message += self.name if self.name is not None else "World"
        message += "!"

        return message