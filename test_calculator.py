import pytest


class TestCalculator:
    """Test cases for calculator functionality"""
    
    def test_addition(self):
        """Test addition operation"""
        result = 5 + 3
        assert result == 8, "Addition failed"
    
    def test_subtraction(self):
        """Test subtraction operation"""
        result = 10 - 4
        assert result == 6, "Subtraction failed"
    
    def test_multiplication(self):
        """Test multiplication operation"""
        result = 7 * 6
        assert result == 42, "Multiplication failed"
    
    def test_division(self):
        """Test division operation"""
        result = 20 / 4
        assert result == 5, "Division failed"
    
    def test_division_by_zero(self):
        """Test that division by zero raises an error"""
        with pytest.raises(ZeroDivisionError):
            result = 10 / 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
