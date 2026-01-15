import pytest
from datetime import datetime


class DatabaseValidator:
    """Validates database operations and queries"""
    
    @staticmethod
    def validate_table_name(name):
        """Check if table name is valid"""
        if not name:
            return False, "Table name cannot be empty"
        if not name[0].isalpha():
            return False, "Table name must start with a letter"
        if not all(c.isalnum() or c == '_' for c in name):
            return False, "Table name can only contain letters, numbers, and underscores"
        if len(name) > 64:
            return False, "Table name cannot exceed 64 characters"
        return True, "Table name is valid"
    
    @staticmethod
    def validate_column_name(name):
        """Check if column name is valid"""
        if not name:
            return False, "Column name cannot be empty"
        if not name[0].isalpha():
            return False, "Column name must start with a letter"
        if not all(c.isalnum() or c == '_' for c in name):
            return False, "Column name can only contain letters, numbers, and underscores"
        return True, "Column name is valid"
    
    @staticmethod
    def validate_email_column_value(email):
        """Check if email value is valid for database"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False, "Invalid email format"
        if len(email) > 255:
            return False, "Email exceeds maximum length of 255 characters"
        return True, "Email is valid"
    
    @staticmethod
    def validate_record_id(record_id):
        """Check if record ID is valid"""
        if not isinstance(record_id, int):
            return False, "Record ID must be an integer"
        if record_id <= 0:
            return False, "Record ID must be positive"
        return True, "Record ID is valid"
    
    @staticmethod
    def validate_date_format(date_string):
        """Check if date is in correct format"""
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True, "Date format is valid"
        except ValueError:
            return False, "Date must be in format YYYY-MM-DD"
    
    @staticmethod
    def validate_query_limit(limit):
        """Check if query limit is valid"""
        if not isinstance(limit, int):
            return False, "Limit must be an integer"
        if limit <= 0:
            return False, "Limit must be greater than 0"
        if limit > 10000:
            return False, "Limit cannot exceed 10000 records"
        return True, "Query limit is valid"
    
    @staticmethod
    def validate_query_offset(offset):
        """Check if query offset is valid"""
        if not isinstance(offset, int):
            return False, "Offset must be an integer"
        if offset < 0:
            return False, "Offset cannot be negative"
        return True, "Query offset is valid"


class TestDatabase:
    """Test cases for database operations"""
    
    def test_valid_table_name(self):
        """Test that valid table names are accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_table_name("users")
        assert is_valid, f"Valid table name should pass: {msg}"
    
    def test_valid_table_name_with_underscore(self):
        """Test that table names with underscores are accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_table_name("user_profiles")
        assert is_valid, "Table name with underscore should be valid"
    
    def test_invalid_table_name_starts_with_number(self):
        """Test that table names starting with numbers are rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_table_name("1users")
        assert not is_valid, "Table name starting with number should fail"
    
    def test_invalid_table_name_special_chars(self):
        """Test that table names with special characters are rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_table_name("user-profiles")
        assert not is_valid, "Table name with special characters should fail"
    
    def test_valid_column_name(self):
        """Test that valid column names are accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_column_name("first_name")
        assert is_valid, "Valid column name should pass"
    
    def test_invalid_column_name_empty(self):
        """Test that empty column names are rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_column_name("")
        assert not is_valid, "Empty column name should fail"
    
    def test_valid_email_in_database(self):
        """Test that valid emails are accepted for database"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_email_column_value("user@example.com")
        assert is_valid, "Valid email should pass"
    
    def test_invalid_email_format(self):
        """Test that invalid emails are rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_email_column_value("invalidemail")
        assert not is_valid, "Invalid email should fail"
    
    def test_valid_record_id(self):
        """Test that valid record IDs are accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_record_id(1)
        assert is_valid, "Valid record ID should pass"
    
    def test_invalid_record_id_zero(self):
        """Test that zero record ID is rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_record_id(0)
        assert not is_valid, "Record ID 0 should fail"
    
    def test_valid_date_format(self):
        """Test that valid date format is accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_date_format("2024-01-15")
        assert is_valid, "Valid date should pass"
    
    def test_invalid_date_format(self):
        """Test that invalid date format is rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_date_format("15/01/2024")
        assert not is_valid, "Invalid date format should fail"
    
    def test_valid_query_limit(self):
        """Test that valid query limits are accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_query_limit(100)
        assert is_valid, "Valid query limit should pass"
    
    def test_invalid_query_limit_too_large(self):
        """Test that query limits exceeding max are rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_query_limit(15000)
        assert not is_valid, "Query limit over 10000 should fail"
    
    def test_valid_query_offset(self):
        """Test that valid query offsets are accepted"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_query_offset(100)
        assert is_valid, "Valid query offset should pass"
    
    def test_invalid_query_offset_negative(self):
        """Test that negative offsets are rejected"""
        validator = DatabaseValidator()
        is_valid, msg = validator.validate_query_offset(-1)
        assert not is_valid, "Negative query offset should fail"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
