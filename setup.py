import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-10minutemail",
    version="0.0.4",
    description="Python wrapper for 10minutemail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SauravKanchan/10minutemail",
    author="Saurav Kanchan",
    author_email="sauravnk30@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    py_modules= ["minutemail", "endpoints"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    entry_points={},
)
