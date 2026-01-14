import pytest


class TestLogin:
    """Test cases for user login functionality"""
    
    def test_valid_login(self):
        """Test valid user login with correct credentials"""
        username = "admin"
        password = "password123"
        
        # Simulate login validation
        is_valid = len(username) > 0 and len(password) > 0
        assert is_valid, "Login failed: invalid credentials"
    
    def test_empty_username(self):
        """Test login with empty username"""
        username = ""
        password = "password123"
        
        # Should fail with empty username
        is_valid = len(username) > 0
        assert not is_valid, "Login should fail with empty username"
    
    def test_password_length(self):
        """Test that password meets minimum length requirement"""
        password = "pass123"
        min_length = 8
        
        # Password should be at least 8 characters
        assert len(password) >= min_length, f"Password must be at least {min_length} characters"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
