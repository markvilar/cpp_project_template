cmake_minimum_required(VERSION 3.16)
project(cpp_project VERSION 0.0.1 LANGUAGES CXX)

# Common project settings and utilities
include(cmake/project_settings.cmake)
include(cmake/prevent_in_source_build.cmake)

# -----------------------------------------------------------------------------
# Project options
# -----------------------------------------------------------------------------

option(PROJECT_BUILD_SHARED "Build shared library." ON)
option(PROJECT_CONAN_ENABLED "Enable Conan for package management." ON)
option(PROJECT_WARNINGS_ENABLED "Enable compiler warnings." ON)
option(PROJECT_EXAMPLES_ENABLED "Enable project examples." ON)
option(PROJECT_TESTS_ENABLED "Enable project tests." ON)

# -----------------------------------------------------------------------------
# Package management
# -----------------------------------------------------------------------------

if(PROJECT_CONAN_ENABLED)
    set(PROJECT_CONAN_INSTALL_DIR "${CMAKE_CURRENT_BINARY_DIR}/conan_install")
    set(PROJECT_CONAN_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/conan_output")
    if(CONAN_EXPORTED)
        include(conanbuildinfo.cmake)
        conan_basic_setup()
    else()
        include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/conan.cmake")
        conan_cmake_autodetect(PROJECT_CONAN_SETTINGS)
        conan_cmake_install(
            PATH_OR_REFERENCE "${CMAKE_CURRENT_SOURCE_DIR}/conanfile.py"
            REMOTE conancenter
            BUILD missing
            SETTINGS "${PROJECT_CONAN_SETTINGS}"
            # Directory to put generator files (i.e. conanbuildinfo.txt)
            INSTALL_FOLDER "${PROJECT_CONAN_INSTALL_DIR}"
            # Root directory for generated and build files
            OUTPUT_FOLDER "${PROJECT_CONAN_OUTPUT_DIR}"
            # TODO: add support for conan profiles
            # PROFILE "${PROJECT_CONAN_PROFILE}"
        )
        # Add build directory to module path to find Conans' CMake config files.
        list(APPEND CMAKE_PREFIX_PATH "${PROJECT_CONAN_INSTALL_DIR}")
        list(APPEND CMAKE_MODULE_PATH "${PROJECT_CONAN_INSTALL_DIR}")
    endif()
endif()

# -----------------------------------------------------------------------------
# Settings - Warnings / sanitizers / analyzers
# -----------------------------------------------------------------------------

# Interface library for options
add_library(options INTERFACE)
add_library(project::options ALIAS options)
target_compile_features(options INTERFACE cxx_std_17)

# Interface library for warnings
add_library(warnings INTERFACE)
add_library(project::warnings ALIAS warnings)

# Enable cache system.
include(cmake/cache.cmake)

# Standard compiler warnings.
include(cmake/compiler_warning.cmake)
set_project_warnings(warnings)

# Sanitizer options if supported by compiler.
include(cmake/sanitizers.cmake)
enable_sanitizers(options)

# Allow static analysis options.
include(cmake/static_analyzers.cmake)

# Enable doxygen
include(cmake/doxygen.cmake)
enable_doxygen()

# -----------------------------------------------------------------------------
# Source - Libraries / executables / examples / tests
# -----------------------------------------------------------------------------

# Add project source code
add_subdirectory(src)

# Add executables
add_subdirectory(bin)

# Add examples
if(PROJECT_EXAMPLES_ENABLED)
    add_subdirectory(example)
endif()

# Add tests
if(PROJECT_TESTS_ENABLED)
    add_subdirectory(test)
endif()
