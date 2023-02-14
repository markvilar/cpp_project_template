#pragma once

#include <string>
#include <string_view>

namespace mylib {

void print(const std::string_view text);
std::string say_hello(const std::string_view subject);

} // namespace mylib
