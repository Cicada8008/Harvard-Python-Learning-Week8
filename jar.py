import logging

logging.basicConfig(
    filename='jar_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

class Jar:
    def __init__(self, capacity=12): # Ensure capacity is a non-negative int
        if not isinstance(capacity, int) or capacity < 0:
            logging.error("Failed to initialize Jar: Capacity must be a non-negative integer.")
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity # Set the capacity of the jar
        self.cookies = 0 # Start with no cookies in the jar
        logging.info(f"Jar initialized with capacity {self.capacity} and starting with {self.cookies} cookies.")

    def __str__(self):
        return "🍪" * self.cookies # Return number of cookies in the jar

    def deposit(self, n):# Add n cookies to the jar if there's enough space
        if n < 0:
            logging.error("Failed deposit: Cannot deposit a negative number of cookies.")
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self.cookies + n > self.capacity:
            logging.error(f"Failed deposit: Not enough space in the jar. Tried to deposit {n} cookies.")
            raise ValueError(f"Not enough space in the jar. Capacity is {self.capacity} and you tried to deposit {n} cookies.")
        self.cookies += n # Add cookies to the jar
        logging.info(f"Deposited {n} cookies. Current cookies: {self.cookies}/{self.capacity}.")
# add log entry of amout of cookies added


    def withdraw(self, n):# Remove n cookies from the jar if there are enough cookies to remove
        if n < 0:
            logging.error("Failed withdrawal: Cannot withdraw a negative number of cookies.")
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self.cookies < n:
            logging.error(f"Failed withdrawal: Not enough cookies to withdraw. Tried to withdraw {n} cookies.")
            raise ValueError("Not enough cookies to withdraw.")
        self.cookies -= n # Remove cookies from the jar & log how many cookies removed
        logging.info(f"Withdrew {n} cookies. Current cookies: {self.cookies}/{self.capacity}.")

    @property
    def capacity(self):
        # Return the jar's capacity
        return self._capacity

    @capacity.setter # Set the capacity and ensure it's a non-negative integer
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            logging.error("Failed to set capacity: Capacity must be a non-negative integer.")
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value
        logging.info(f"Capacity set to {self._capacity}.")

    @property
    def size(self):# Return the number of cookies in the jar
        return self.cookies
