#!/usr/bin/bash

find ${PWD}/bin/ -iname "*.hpp" -o -iname "*.cpp" \
    | xargs clang-format -style=file -i -fallback-style=none

find ${PWD}/example/ -iname "*.hpp" -o -iname "*.cpp" \
    | xargs clang-format -style=file -i -fallback-style=none

find ${PWD}/src/ -iname "*.hpp" -o -iname "*.cpp" \
    | xargs clang-format -style=file -i -fallback-style=none

find ${PWD}/test/ -iname "*.hpp" -o -iname "*.cpp" \
    | xargs clang-format -style=file -i -fallback-style=none

exit 0
