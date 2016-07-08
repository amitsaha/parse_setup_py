from setuptools import setup, find_packages
setup(name="mypackagename", 
      author="author@gmail.com",
      description="My awesome package",
      packages=find_packages(exclude=["tests.*", "tests"]),
      include_package_data=True,
      install_requires=[
           'enum34==1.0.4', 'Flask >=0.9, <0.10',
           'Flask-Script==0.6.2',]
      )
