#include <cpptemp/say_hello.hpp>

int main([[maybe_unused]] const int argc, [[maybe_unused]] const char** argv)
{
    auto message = mylib::say_hello("world");
    mylib::print(message);
    return 0;
}
