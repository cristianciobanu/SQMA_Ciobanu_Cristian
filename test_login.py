import pytest
import re


class UserValidator:
    """Validates user credentials"""
    
    @staticmethod
    def validate_email(email):
        """Check if email format is valid"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_password_strength(password):
        """Check if password is strong enough"""
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter"
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit"
        return True, "Password is strong"
    
    @staticmethod
    def validate_username(username):
        """Check if username is valid"""
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        if not username.isalnum():
            return False, "Username must contain only letters and numbers"
        return True, "Username is valid"


class TestLogin:
    """Test cases for user login and validation"""
    
    def test_valid_email_format(self):
        """Test that valid email addresses are accepted"""
        validator = UserValidator()
        assert validator.validate_email("user@example.com"), "Valid email should pass"
        assert validator.validate_email("john.doe@company.co.uk"), "Email with dot should pass"
    
    def test_invalid_email_format(self):
        """Test that invalid email addresses are rejected"""
        validator = UserValidator()
        assert not validator.validate_email("invalidemail"), "Email without @ should fail"
        assert not validator.validate_email("user@nodomain"), "Email without domain extension should fail"
    
    def test_strong_password_requirement(self):
        """Test that passwords must be strong"""
        validator = UserValidator()
        is_valid, msg = validator.validate_password_strength("Password123")
        assert is_valid, f"Strong password should pass: {msg}"
    
    def test_weak_password_too_short(self):
        """Test that short passwords are rejected"""
        validator = UserValidator()
        is_valid, msg = validator.validate_password_strength("Pass1")
        assert not is_valid, "Short password should fail"
        assert "8 characters" in msg, "Error message should mention length requirement"
    
    def test_weak_password_no_uppercase(self):
        """Test that passwords need uppercase letters"""
        validator = UserValidator()
        is_valid, msg = validator.validate_password_strength("password123")
        assert not is_valid, "Password without uppercase should fail"
    
    def test_valid_username(self):
        """Test that valid usernames are accepted"""
        validator = UserValidator()
        is_valid, msg = validator.validate_username("john123")
        assert is_valid, "Valid username should pass"
    
    def test_invalid_username_too_short(self):
        """Test that usernames must be at least 3 characters"""
        validator = UserValidator()
        is_valid, msg = validator.validate_username("ab")
        assert not is_valid, "Username too short should fail"
    
    def test_invalid_username_special_chars(self):
        """Test that usernames cannot contain special characters"""
        validator = UserValidator()
        is_valid, msg = validator.validate_username("user@name")
        assert not is_valid, "Username with special chars should fail"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
