from setuptools import setup, find_packages

setup(
    name='hydrop_sharepointsync',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-dotenv',
    ],
)
