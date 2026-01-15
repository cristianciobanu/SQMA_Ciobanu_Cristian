import pytest


class Calculator:
    """Simple calculator with basic operations"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract two numbers"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def square_root(a):
        """Calculate square root"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5


class TestCalculator:
    """Test cases for calculator functionality"""
    
    def test_addition_positive_numbers(self):
        """Test addition with positive numbers"""
        calc = Calculator()
        assert calc.add(5, 3) == 8, "5 + 3 should equal 8"
    
    def test_addition_negative_numbers(self):
        """Test addition with negative numbers"""
        calc = Calculator()
        assert calc.add(-5, -3) == -8, "-5 + (-3) should equal -8"
    
    def test_subtraction(self):
        """Test subtraction operation"""
        calc = Calculator()
        assert calc.subtract(10, 4) == 6, "10 - 4 should equal 6"
    
    def test_multiplication_positive(self):
        """Test multiplication with positive numbers"""
        calc = Calculator()
        assert calc.multiply(7, 6) == 42, "7 * 6 should equal 42"
    
    def test_multiplication_by_zero(self):
        """Test multiplication by zero"""
        calc = Calculator()
        assert calc.multiply(100, 0) == 0, "Any number * 0 should equal 0"
    
    def test_division(self):
        """Test division operation"""
        calc = Calculator()
        assert calc.divide(20, 4) == 5, "20 / 4 should equal 5"
    
    def test_division_by_zero_raises_error(self):
        """Test that division by zero raises an error"""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
    
    def test_square_root_positive(self):
        """Test square root of positive number"""
        calc = Calculator()
        assert calc.square_root(16) == 4, "√16 should equal 4"
        assert calc.square_root(25) == 5, "√25 should equal 5"
    
    def test_square_root_negative_raises_error(self):
        """Test that square root of negative number raises error"""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot calculate square root of negative"):
            calc.square_root(-4)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
