from parse_setup_py import get_package_name


def test_get_package_name():

    assert 'mypackagename' == get_package_name('./setup_test.py')
