#include "grid16x16_test.h"

bool check_default_grid() {
  Grid16x16 grid;
  const bool is_pass = grid.countValues(ZERO) == 256;

  return is_pass;
}

bool check_example_from_assignment() {
  Grid16x16 grid;
  const auto bytes = {0xff, 0x11, 0x12};

  for (const auto byte : bytes) {
    const Point grid_point = Utils::byteToPoint(byte);
    grid.onSelect(grid_point);
  }

  const bool is_pass = grid.countValues(ZERO) == 200;

  std::cout << "Grid from assignment example: \n";
  grid.print();

  return is_pass;
}
