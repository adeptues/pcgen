cmake_minimum_required (VERSION 2.8.8)
project (pcgen)
add_executable(pcgen main.cpp lsystem.cpp turtle.cpp)
# Linkable library for unit tests
add_library(pcg lsystem.cpp turtle.cpp)


#########################
# Testing
#########################
# TODO refactor  use gtest variables
# enabled in gtest project
enable_testing()
add_subdirectory(gtest-1.7.0)
include_directories(gtest-1.7.0/include)
add_executable(utests tests.cpp)
target_link_libraries(utests gtest pthread pcg)
add_test(NAME ltests COMMAND utests)
