cmake_minimum_required (VERSION 2.8.8)
project (pcgen)
# Configure project variables
set(EXECUTABLE_NAME "pcgen")
set(SRCS lsystem.cpp turtle.cpp  display.cpp)
# Configure third part cmake find modules
#set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake_modules"
#${CMAKE_MODULE_PATH})
# check sfml installed
#find_package(SFML 2 REQUIRED system window graphics network audio)

add_executable(${EXECUTABLE_NAME} app.cpp ${SRCS})
#target_link_libraries(${EXECUTABLE_NAME} ${SFML_LIBRARIES})

# Linkable library for unit tests
add_library(pcg ${SRCS})


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
