from parse_setup_py import get_package_dep_names


def test_get_package_dep_names():

    expected_deps = ['enum34', 'Flask', 'Flask-Script']
    assert expected_deps == get_package_dep_names('./setup_test.py')
