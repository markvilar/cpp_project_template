#! /usr/bin/bash

SOURCE_DIR=${PWD}
PROFILE=${SOURCE_DIR}/profiles/linux_clang

# Create default and custom profile
conan profile detect
conan profile detect --name ${PROFILE}
   
# Install package dependencies
conan install ${SOURCE_DIR} --profile=${PROFILE} -g Ninja

# Build package
conan build ${SOURCE_DIR} --profile ${PROFILE} --build missing -g Ninja

# Create and, optionally, upload the package
conan create ${SOURCE_DIR} --profile ${PROFILE} -g Ninja
