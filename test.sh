#!/bin/bash

echo 'making tests ...'
g++ -I ./gtest-1.7.0/include -L ./gtest-1.7.0/ tests.cpp lsystem.cpp -lgtest -lpthread  -o utests
