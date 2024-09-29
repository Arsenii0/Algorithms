#include "utils.h"

namespace Utils {
Point byteToPoint(unsigned char byte) {
  const unsigned char low = byte & 0x0F;
  const unsigned char high = (byte >> 4) & 0x0F;

  return Point{static_cast<int>(high), static_cast<int>(low)};
}

std::vector<Point> convertBytesToPoints(const std::vector<char> &bytes) {
  std::vector<Point> points;
  points.reserve(bytes.size());

  for (const unsigned char byte : bytes) {
    points.push_back(byteToPoint(byte));
  }

  return points;
}

std::vector<char> readBytesFromFile(const std::string &file_path) {
  std::ifstream inFile(file_path, std::ios_base::binary);

  if (!inFile) {
    std::cerr << "File opening error: " << file_path;
    return {};
  }

  inFile.seekg(0, std::ios_base::end);
  size_t length = inFile.tellg();
  inFile.seekg(0, std::ios_base::beg);

  std::vector<char> buffer;
  buffer.reserve(length);
  std::copy(std::istreambuf_iterator<char>(inFile),
            std::istreambuf_iterator<char>(), std::back_inserter(buffer));

  inFile.close();

  return buffer;
}

} // namespace Utils
