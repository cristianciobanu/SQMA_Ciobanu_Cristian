import pytest


class APIValidator:
    """Validates API requests and responses"""
    
    @staticmethod
    def validate_endpoint(endpoint):
        """Check if endpoint URL is valid"""
        if not endpoint:
            return False, "Endpoint cannot be empty"
        if not endpoint.startswith(('http://', 'https://')):
            return False, "Endpoint must start with http:// or https://"
        if ' ' in endpoint:
            return False, "Endpoint cannot contain spaces"
        return True, "Endpoint is valid"
    
    @staticmethod
    def validate_http_method(method):
        """Check if HTTP method is valid"""
        valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
        if method not in valid_methods:
            return False, f"Invalid HTTP method. Must be one of: {', '.join(valid_methods)}"
        return True, "HTTP method is valid"
    
    @staticmethod
    def validate_status_code(code):
        """Check if HTTP status code is valid"""
        if not isinstance(code, int):
            return False, "Status code must be an integer"
        if code < 100 or code > 599:
            return False, "Status code must be between 100 and 599"
        return True, "Status code is valid"
    
    @staticmethod
    def validate_response_time(response_time, max_time=5000):
        """Check if response time is acceptable (in milliseconds)"""
        if response_time < 0:
            return False, "Response time cannot be negative"
        if response_time > max_time:
            return False, f"Response time {response_time}ms exceeds maximum {max_time}ms"
        return True, f"Response time acceptable ({response_time}ms)"
    
    @staticmethod
    def categorize_status_code(code):
        """Categorize HTTP status code"""
        if 200 <= code < 300:
            return "Success"
        elif 300 <= code < 400:
            return "Redirect"
        elif 400 <= code < 500:
            return "Client Error"
        elif 500 <= code < 600:
            return "Server Error"
        else:
            return "Unknown"


class TestAPI:
    """Test cases for API validation"""
    
    def test_valid_http_endpoint(self):
        """Test that valid HTTP endpoints are accepted"""
        validator = APIValidator()
        is_valid, msg = validator.validate_endpoint("https://api.example.com/users")
        assert is_valid, f"Valid endpoint should pass: {msg}"
    
    def test_invalid_endpoint_no_protocol(self):
        """Test that endpoints without protocol are rejected"""
        validator = APIValidator()
        is_valid, msg = validator.validate_endpoint("api.example.com/users")
        assert not is_valid, "Endpoint without protocol should fail"
    
    def test_invalid_endpoint_with_spaces(self):
        """Test that endpoints with spaces are rejected"""
        validator = APIValidator()
        is_valid, msg = validator.validate_endpoint("https://api.example.com/user name")
        assert not is_valid, "Endpoint with spaces should fail"
    
    def test_valid_http_methods(self):
        """Test that valid HTTP methods are accepted"""
        validator = APIValidator()
        methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
        for method in methods:
            is_valid, msg = validator.validate_http_method(method)
            assert is_valid, f"Method {method} should be valid"
    
    def test_invalid_http_method(self):
        """Test that invalid HTTP methods are rejected"""
        validator = APIValidator()
        is_valid, msg = validator.validate_http_method("INVALID")
        assert not is_valid, "Invalid HTTP method should fail"
    
    def test_valid_status_codes(self):
        """Test that valid status codes are accepted"""
        validator = APIValidator()
        codes = [200, 201, 400, 404, 500]
        for code in codes:
            is_valid, msg = validator.validate_status_code(code)
            assert is_valid, f"Status code {code} should be valid"
    
    def test_invalid_status_code_out_of_range(self):
        """Test that status codes outside valid range are rejected"""
        validator = APIValidator()
        is_valid, msg = validator.validate_status_code(999)
        assert not is_valid, "Status code 999 should fail"
    
    def test_valid_response_time(self):
        """Test that acceptable response times are valid"""
        validator = APIValidator()
        is_valid, msg = validator.validate_response_time(1000)
        assert is_valid, "Response time 1000ms should be valid"
    
    def test_slow_response_time(self):
        """Test that slow response times are rejected"""
        validator = APIValidator()
        is_valid, msg = validator.validate_response_time(6000)
        assert not is_valid, "Response time 6000ms should fail"
    
    def test_status_code_categorization_success(self):
        """Test that 2xx codes are categorized as success"""
        validator = APIValidator()
        category = validator.categorize_status_code(200)
        assert category == "Success", "200 should be categorized as Success"
    
    def test_status_code_categorization_error(self):
        """Test that 5xx codes are categorized as server error"""
        validator = APIValidator()
        category = validator.categorize_status_code(500)
        assert category == "Server Error", "500 should be categorized as Server Error"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
