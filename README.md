### Parse setup.py

Parse a Python package's ``setup.py`` to return:

- the package name
- the dependency names (not the versions)

See ``parse_setup_py.py`` and ``tests``.

### Notes

Some things I learned along the way:

``pip`` uses the following shim to basically invoke ``python setup.py <arg>``:

```
# Shim to wrap setup.py invocation with setuptools
SETUPTOOLS_SHIM = (
    "import setuptools, tokenize;__file__=%r;"
    "exec(compile(getattr(tokenize, 'open', open)(__file__).read()"
    ".replace('\\r\\n', '\\n'), __file__, 'exec'))"

)
```

``setup()`` function is defined in ``distutils.core``.
