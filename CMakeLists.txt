cmake_minimum_required (VERSION 2.8.8)
project (pcgen)
add_executable(pcgen main.cpp lsystem.cpp turtle.cpp)
#TODO make produce lib which can be linked in the tests

#########################
# Testing
#########################
# TODO refactor to have one source list and use gtest variables
# enabled in gtest project
enable_testing()
add_subdirectory(gtest-1.7.0)
include_directories(gtest-1.7.0/include)
add_executable(utests tests.cpp  lsystem.cpp turtle.cpp)
target_link_libraries(utests gtest pthread)
add_test(NAME ltests COMMAND utests)
