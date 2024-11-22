class Jar:
    def __init__(self, capacity=12):
        # Ensure the capacity is a non-negative integer.
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity  # Set the capacity of the jar
        self.cookies = 0  # Start with no cookies in the jar

    def __str__(self):
        # Return a string representation of the number of cookies in the jar
        return "🍪" * self.cookies

    def deposit(self, n):
        # Add n cookies to the jar if there's enough space
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self.cookies + n > self.capacity:
            raise ValueError("Not enough space in the jar.")
        self.cookies += n  # Add cookies to the jar

    def withdraw(self, n):
        # Remove n cookies from the jar if there are enough cookies
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self.cookies < n:
            raise ValueError("Not enough cookies to withdraw.")
        self.cookies -= n  # Remove cookies from the jar

    @property
    def capacity(self):
        # Return the jar's capacity
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        # Set the capacity and ensure it's a non-negative integer
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value

    @property
    def size(self):
        # Return the number of cookies in the jar
        return self.cookies

