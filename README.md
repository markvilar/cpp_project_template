# C++ Project Template

[![Build](https://github.com/markvilar/cpp_project_template/actions/workflows/build-linux.yml/badge.svg)](https://github.com/markvilar/cpp_project_template/actions/workflows/build-linux.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Template project for C++ with CMake and Conan 2.0 support.

## Supported tools

- CMake (3.19+)
- Conan (2.0.0+)

## Conan workflow

The project workflow for Conan 2.0 is listed below. For more comprehensive details, check out the Conan documentation: [https://docs.conan.io/2/index.html](https://docs.conan.io/2/index.html)
See the `conan/profiles` directory for a set of pre-generated profiles.

```sh
# Install conan with pip
pip install --user conan

# Create a profile by detecting installed build systems and compilers
conan profile detect

# Install the project dependencies
conan install . --profile <path/to/profile> --build missing

# Build the project package
conan build . --profile <path/to/profile> --build missing

# Create the project package
conan create . --profile <path/to/profile> --build missing
```
