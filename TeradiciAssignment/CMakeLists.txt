cmake_minimum_required(VERSION 3.5)

project(TeradiciAssignment LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(TeradiciAssignment main.cpp
    grid16x16.h
    grid16x16.cpp
    utils.h
    utils.cpp
    grid16x16_test.h
    grid16x16_test.cpp)
