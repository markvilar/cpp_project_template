#include <mylib/say_hello.hpp>

int main(const int argc, const char** argv)
{
    auto message = mylib::say_hello("world");
    mylib::print(message);
    return 0;
}
