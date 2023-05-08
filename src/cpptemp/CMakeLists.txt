# Add library with alias
add_library(cpptemp)
add_library(myproject::cpptemp ALIAS cpptemp)

# -----------------------------------------------------------------------------
# Library options
# -----------------------------------------------------------------------------

option(CPPTEMP_PCH_ENABLED "Enable precompiled headers." OFF)

# -----------------------------------------------------------------------------
# Library sources and includes
# -----------------------------------------------------------------------------

target_sources(cpptemp
    PUBLIC
        include/cpptemp/say_hello.hpp
    PRIVATE
        src/say_hello.cpp
)

if(CPPTEMP_PCH_ENABLED)
    target_precompile_headers(cpptemp)
endif()

target_include_directories(cpptemp
    PUBLIC
        include
    PRIVATE
        src
)

# -----------------------------------------------------------------------------
# Library dependency linkage
# -----------------------------------------------------------------------------

find_package(fmt CONFIG REQUIRED)

target_link_libraries(cpptemp
    PUBLIC
    PRIVATE
        fmt::fmt
)

# -----------------------------------------------------------------------------
# Library settings - Definitions / features / options
# -----------------------------------------------------------------------------

target_compile_definitions(cpptemp
    PUBLIC
        $<$<CONFIG:Debug>:CPPTEMP_DEBUG_DEFINITION>
        $<$<CONFIG:Release>:CPPTEMP_RELEASE_DEFINITION>
    PRIVATE
)

target_compile_features(cpptemp
    PUBLIC
        cxx_std_17
    PRIVATE
)
target_compile_options(cpptemp
    PUBLIC
        -std=c++17
    PRIVATE
)

# -----------------------------------------------------------------------------
# Library output and installation
# -----------------------------------------------------------------------------

set_target_properties(cpptemp 
    PROPERTIES
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/lib"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/lib"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/bin"
)

# Install include directory to install location
install(DIRECTORY "include/cpptemp" TYPE INCLUDE FILES_MATCHING PATTERN "*.hpp")
