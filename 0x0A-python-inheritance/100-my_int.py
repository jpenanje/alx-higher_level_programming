#!/usr/bin/python3
"""class MyInt that inherits from int."""


class MyInt(int):
    """swap int operators == and !=."""

    def __eq__(self, value):
        """== operator has != behavior."""
        return self.real != value

    def __ne__(self, value):
        """!= operator has == behavior."""
        return self.real == value
