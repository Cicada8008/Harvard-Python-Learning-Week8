from jar import Jar

def test_init():
    # Test for correct initialization
    jar = Jar()
    assert jar.capacity == 12  # Default capacity
    assert jar.size == 0  # No cookies initially
    jar = Jar(5)
    assert jar.capacity == 5  # Custom capacity
    assert jar.size == 0  # No cookies initially

    # Test invalid capacity
    try:
        Jar(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative capacity"

    try:
        Jar("string")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid capacity type"

def test_str():
    # Test string representation of the jar
    jar = Jar()
    assert str(jar) == ""  # No cookies initially
    jar.deposit(1)
    assert str(jar) == "🍪"  # One cookie
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # 12 cookies, full jar

def test_deposit():
    # Test depositing cookies
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5  # 5 cookies in the jar
    jar.deposit(3)
    assert jar.size == 8  # 8 cookies in the jar
    try:
        jar.deposit(5)  # Exceeds capacity
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for exceeding capacity"

    try:
        jar.deposit(-1)  # Invalid deposit
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative deposit"

def test_withdraw():
    # Test withdrawing cookies
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5  # 5 cookies remain in the jar
    jar.withdraw(5)
    assert jar.size == 0  # All cookies withdrawn

    try:
        jar.withdraw(1)  # No cookies to withdraw
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for insufficient cookies"

    try:
        jar.withdraw(-1)  # Invalid withdrawal
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative withdrawal"

def test_capacity_property():
    # Test the capacity property
    jar = Jar(15)
    assert jar.capacity == 15
    jar.capacity = 20
    assert jar.capacity == 20  # Updated capacity
    try:
        jar.capacity = -5  # Invalid capacity
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid capacity"
