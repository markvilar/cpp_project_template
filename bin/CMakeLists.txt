# -----------------------------------------------------------------------------
# Hello world
# -----------------------------------------------------------------------------

add_executable(hello_world hello_world.cpp)

target_compile_features(hello_world PRIVATE cxx_std_17)
target_compile_options(hello_world PRIVATE -std=c++17)
target_compile_definitions(hello_world PRIVATE)

target_link_libraries(hello_world PRIVATE myproject::cpptemp)

set_target_properties(hello_world 
    PROPERTIES 
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
)
