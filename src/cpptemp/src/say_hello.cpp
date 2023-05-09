#include "cpptemp/say_hello.hpp"

#include <fmt/core.h>

namespace mylib {

void print(const std::string_view text)
{
    fmt::print(text);
}

std::string say_hello(const std::string_view subject)
{
    return fmt::format("Hello {}!\n", subject);
}

} // namespace mylib
