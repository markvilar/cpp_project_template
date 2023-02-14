# Add library with alias
add_library(mylib)
add_library(myproject::mylib ALIAS mylib)

# -----------------------------------------------------------------------------
# Library options
# -----------------------------------------------------------------------------

option(MYLIB_PCH_ENABLED "Enable precompiled headers." OFF)

# -----------------------------------------------------------------------------
# Library sources and includes
# -----------------------------------------------------------------------------

target_sources(mylib
    PUBLIC
        include/mylib/say_hello.hpp
    PRIVATE
        src/say_hello.cpp
)

if(MYLIB_PCH_ENABLED)
    target_precompile_headers(mylib)
endif()

target_include_directories(mylib
    PUBLIC
        include
    PRIVATE
        src
)

# -----------------------------------------------------------------------------
# Library dependency linkage
# -----------------------------------------------------------------------------

find_package(fmt CONFIG REQUIRED)

target_link_libraries(mylib
    PUBLIC
    PRIVATE
        fmt::fmt
)

# -----------------------------------------------------------------------------
# Library settings - Definitions / features / options
# -----------------------------------------------------------------------------

target_compile_definitions(mylib
    PUBLIC
        $<$<CONFIG:Debug>:MYLIB_DEBUG_DEFINITION>
        $<$<CONFIG:Release>:MYLIB_RELEASE_DEFINITION>
    PRIVATE
)

target_compile_features(mylib
    PUBLIC
        cxx_std_17
    PRIVATE
)
target_compile_options(mylib
    PUBLIC
        -std=c++17
    PRIVATE
)

# -----------------------------------------------------------------------------
# Library output and installation
# -----------------------------------------------------------------------------

set_target_properties(mylib 
    PROPERTIES
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/lib"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/lib"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/bin"
)

# Install include directory to install location
install(DIRECTORY "include/mylib" TYPE INCLUDE FILES_MATCHING PATTERN "*.hpp")
