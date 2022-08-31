#include "grid16x16.h"
#include "utils.h"

#include "grid16x16_test.h"

void check_tests() {
  bool passed{true};
  passed &= check_default_grid();
  passed &= check_example_from_assignment();

  if (passed) {
    std::cout << "All test cases passed!\n";
  } else {
    std::cout << "Test failed.\n";
  }
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    std::cerr << "Error: a single file path is expected\n";
    return 1;
  }

  Grid16x16 grid;

  const auto bytes_from_file = Utils::readBytesFromFile(argv[1]);
  for (const char byte : bytes_from_file) {
    grid.onSelect(Utils::byteToPoint(static_cast<unsigned char>(byte)));
  }

  std::cout << "Grid from file: \n";
  grid.print();
  std::cout << "Zeros: " << grid.countValues(ZERO) << "\n\n";

  // Also check tests
  check_tests();

  return 0;
}
