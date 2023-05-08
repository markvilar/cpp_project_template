# C++ Project Template

[![Build](https://github.com/markvilar/cpp_project_template/actions/workflows/build-linux.yml/badge.svg)](https://github.com/markvilar/cpp_project_template/actions/workflows/build-linux.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Template project for C++ with CMake and Conan support.

## Supported tools

CMake (3.17+)
Conan (2.0.0+)

## Usage

```sh
# TODO: Figure out how to configure CC/CXX in the profile
conan profile detect --name <profile>

# Install the dependencies
conan install .

# Build the package
conan build .
```
