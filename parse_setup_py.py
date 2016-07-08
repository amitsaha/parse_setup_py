import ast
import sys
import re

def get_package_name(path):
    """
    Return the name of this package specified via "name="

    path: path to a setup.py file
    """
    with open(path) as f:
        parsed_setup_py = ast.parse(f.read())

    # find the call to setup()
    for body in parsed_setup_py.body:
        if hasattr(body, 'value') and isinstance(body.value, ast.Call):
            # this is a call object, but setup() can be called either as:
            # setuptools.setup(), 
            # or
            # from setuptools import setup
            # setup()
            if (getattr(body.value.func, 'attr', None) and body.value.func.attr == 'setup') or \
                    (getattr(body.value.func, 'id', None) and body.value.func.id == 'setup'):
                        setup_call_object = body.value
                        break
    for kw in setup_call_object.keywords:
        if kw.arg == 'name':
            # .replace() for python package names to debian
            # package names
            return kw.value.s

    raise 'No name found'


def get_package_dep_names(path):
    """
    Parse install_requires keyword argument and return just the
    package_names

    path: path to a setup.py file

    """
    req_spec = re.compile('^[a-zA-Z0-9-_]+')
    with open(path) as f:
        parsed_setup_py = ast.parse(f.read())

    # find the call to setup()
    setup_call_object = None
    for body in parsed_setup_py.body:
        if hasattr(body, 'value') and isinstance(body.value, ast.Call):
            # this is a call object, but setup() can be called either as:
            # setuptools.setup(),
            # or
            # from setuptools import setup
            # setup()
            if (getattr(body.value.func, 'attr', None) and body.value.func.attr == 'setup') or \
                    (getattr(body.value.func, 'id', None) and body.value.func.id == 'setup'):
                        setup_call_object = body.value
                        break
    # Find install_requires and iterate through the list of deps
    deps = []
    if setup_call_object:
        for kw in setup_call_object.keywords:
            if kw.arg == 'install_requires':
                for dep in kw.value.elts: # elts: https://docs.python.org/2/library/ast.html
                    # dep.s is of the form package_name  >= 0.1, we just need the
                    # package_name
                    group = re.match(req_spec, dep.s)
                    if group:
                        deps.append(group.group())
                    else:
                        sys.exit('Could not parse %s' % dep.s)
    return deps
