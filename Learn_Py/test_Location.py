import pytest

def testlogin():
    print("Login Success")

@pytest.mark.sanity
def testassert():
    assert 2+2 == 6