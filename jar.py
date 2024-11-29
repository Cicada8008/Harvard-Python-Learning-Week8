import logging
import time

logging.basicConfig(
    filename='jar_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

class Cookie:
    TYPES = [
        "Chocolate Chip",
        "Oatmeal Raisin",
        "White Chocolate",
        "Peanut Butter",
        "Sugar"
    ]
    
    _last_cookie_id = 0

    def __init__(self, cookie_type):
        if cookie_type not in self.TYPES:
            logging.error(f"Failed to create cookie: Invalid cookie type. Must be one of {self.TYPES}")
            raise ValueError(f"Cookie type must be one of {self.TYPES}")
        
        Cookie._last_cookie_id += 1
        self._id = f"{int(time.time() * 1000)}_{Cookie._last_cookie_id}"
        self._type = cookie_type
        logging.info(f"Created new {self._type} cookie. ID: {self._id}")

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    def __str__(self):
        return f"{self._type} cookie (ID: {self._id[-5:]})"

    def __repr__(self):
        return f"Cookie(type='{self._type}', id='{self._id}')"


class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            logging.error("Failed to initialize Jar: Capacity must be a non-negative integer.")
            raise ValueError("Capacity must be a non-negative integer.")
        
        self.capacity = capacity
        self.cookies = 0
        self._cookie_types = {cookie_type: 0 for cookie_type in Cookie.TYPES}
        self._cookie_collection = []
        logging.info(f"Jar initialized with capacity {self.capacity} and starting with {self.cookies} cookies.")

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, cookie):
        if not isinstance(cookie, Cookie):
            logging.error("Failed deposit: Can only deposit Cookie objects.")
            raise ValueError("Can only deposit Cookie objects.")
        
        if self.cookies + 1 > self.capacity:
            logging.error(f"Failed deposit: Not enough space in the jar. Tried to deposit {cookie.type} cookie.")
            raise ValueError(f"Not enough space in the jar. Capacity is {self.capacity}")
        
        self.cookies += 1
        self._cookie_types[cookie.type] += 1
        self._cookie_collection.append(cookie)
        
        logging.info(f"Deposited {cookie.type} cookie. Current cookies: {self.cookies}/{self.capacity}")
        return self

    def withdraw(self, cookie_type=None):
        if self.cookies == 0:
            logging.error("Failed withdrawal: No cookies in the jar.")
            raise ValueError("No cookies to withdraw.")
        
        if cookie_type is None:
            last_cookie = self._cookie_collection.pop()
            self.cookies -= 1
            self._cookie_types[last_cookie.type] -= 1
            logging.info(f"Withdrew {last_cookie}. Current cookies: {self.cookies}/{self.capacity}")
            return last_cookie
        
        if cookie_type not in Cookie.TYPES:
            logging.error(f"Failed withdrawal: Invalid cookie type {cookie_type}")
            raise ValueError(f"Invalid cookie type. Must be one of {Cookie.TYPES}")
        
        if self._cookie_types[cookie_type] == 0:
            logging.error(f"Failed withdrawal: No {cookie_type} cookies in the jar.")
            raise ValueError(f"No {cookie_type} cookies in the jar.")
        
        for i, cookie in enumerate(self._cookie_collection):
            if cookie.type == cookie_type:
                withdrawn_cookie = self._cookie_collection.pop(i)
                self.cookies -= 1
                self._cookie_types[cookie_type] -= 1
                logging.info(f"Withdrew {withdrawn_cookie}. Current cookies: {self.cookies}/{self.capacity}")
                return withdrawn_cookie

    def cookie_counts(self):
        return self._cookie_types.copy()

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            logging.error("Failed to set capacity: Capacity must be a non-negative integer.")
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value
        logging.info(f"Capacity set to {self._capacity}.")

    @property
    def size(self):
        return self.cookies

    

if __name__ == "__main__":
    try:
        cookie_jar = Jar(12)

        choc_chip_1 = Cookie("Chocolate Chip")
        white_choc = Cookie("White Chocolate")
        oatmeal = Cookie("Oatmeal Raisin")
        peanut_butter = Cookie("Peanut Butter")
        sugar = Cookie("Sugar")
        
        while True:
            user_input = input("\n           What flavour cookies would you like to add ?\n"
                               "\n🍪 🍪 Chocolate Chip, White Chocolate, Oatmeal Raisin, Peanut Butter, Sugar 🍪 🍪?\n" 
                               "\n            Type 'done' when finished adding cookies: ").title().strip()

            if user_input == "Done":  
                print("Exiting.......")
                break

            if user_input == "Chocolate Chip":
                cookie_jar.deposit(choc_chip_1)
            elif user_input == "White Chocolate":
                cookie_jar.deposit(white_choc)
            elif user_input == "Oatmeal Raisin":
                cookie_jar.deposit(oatmeal)
            elif user_input == "Peanut Butter":
                cookie_jar.deposit(peanut_butter)
            elif user_input == "Sugar":
                cookie_jar.deposit(sugar)
            else:
                print(f"Invalid cookie type: {user_input}") 

        for cookie_type, count in cookie_jar.cookie_counts().items():
            emoji_list = "🍪" * count  
            print(f"{emoji_list} : {cookie_type} : {count}")

        print(f"Total Cookies: {cookie_jar}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"Error: {e}")
