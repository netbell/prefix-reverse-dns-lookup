from unittest.mock import patch
import prefix_reverse_dns_lookup
import socket

def test_reverse_dns_successful():
    with patch('socket.gethostbyaddr', return_value=("one.one.one.one", [], ["1.1.1.1"])):
        result = prefix_reverse_dns_lookup.reverse_dns("1.1.1.1")
        assert result == "one.one.one.one"

def test_reverse_dns_unsuccessful():
    with patch('socket.gethostbyaddr', side_effect=socket.herror):
        result = prefix_reverse_dns_lookup.reverse_dns("192.0.2.2")
        assert result is None

def test_validate_prefix_valid_ipv4():
    assert prefix_reverse_dns_lookup.validate_prefix("192.0.2.0/24")

def test_validate_prefix_valid_ipv6():
    assert prefix_reverse_dns_lookup.validate_prefix("2001:0db8::/32")

def test_validate_prefix_invalid():
    assert not prefix_reverse_dns_lookup.validate_prefix("192.0.2.256/24")

def test_reverse_dns_for_prefix():
    with patch("builtins.print") as mock_print:
        # Mocking the reverse_dns function
        with patch('prefix_reverse_dns_lookup.reverse_dns', return_value="one.one.one.one"):
            prefix_reverse_dns_lookup.reverse_dns_for_prefix("1.1.1.0/30", True)
            mock_print.assert_any_call("1.1.1.1         -> one.one.one.one")