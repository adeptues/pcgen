#!/bin/bash

echo 'making tests ...'
g++ -I /home/adeptues/workspace/pcgen/gtest-1.7.0/include -L /home/adeptues/workspace/pcgen/gtest-1.7.0/ tests.cpp lsystem.cpp -lgtest -lpthread  -o utests
