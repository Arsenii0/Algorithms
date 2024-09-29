#pragma once

#include "grid16x16.h"

#include <fstream>

namespace Utils {
Point byteToPoint(unsigned char byte);

std::vector<Point> convertBytesToPoints(const std::vector<char> &bytes);

std::vector<char> readBytesFromFile(const std::string &file_path);
} // namespace Utils
