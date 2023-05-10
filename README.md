# C++ Project Template

[![Build](https://github.com/markvilar/cpp_project_template/actions/workflows/build-linux.yml/badge.svg)](https://github.com/markvilar/cpp_project_template/actions/workflows/build-linux.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Template project for C++ with CMake and Conan 2.0 support.

## Supported tools

- CMake (3.19+)
- Conan (2.0.0+)

## Conan workflow

The project workflow for Conan 2.0 is listed below. See the `conan/profiles`
directory for a set of pre-generated profiles.

```sh
# Create a default profile
conan profile detect

# Install the dependencies
conan install . --profile <path/to/profile> --build missing

# Build the package
conan build . --profile <path/to/profile> --build missing

# Create the package
conan create . --profile <path/to/profile> --build missing
```
