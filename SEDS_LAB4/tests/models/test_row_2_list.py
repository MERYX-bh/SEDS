import pytest

def row_to_list(s):
 return list(s.split())
def test_row_to_list():
 assert row_to_list("2,081\t314,942\n") == ["2,081","314,942"]
