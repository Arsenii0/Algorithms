#include "grid16x16.h"

Grid16x16::Grid16x16() { memset(_grid, ZERO, GRID_SIZE); }

void Grid16x16::onSelect(const Point &point) {
  if (!isWithinGridBounds(point)) {
    std::cerr << "Requested point is out of grid range: " << point.x << " "
              << point.y;
    return;
  }

  const unsigned char selected_value = getValue(point).value();
  if (selected_value == ZERO) {
    fillRow(point.x, ONE);
    fillCol(point.y, ONE);
  } else {
    fillAssociatedDiagonals(point, ZERO);
  }
}

size_t Grid16x16::countValues(unsigned char value) const {
  const auto result = std::count_if(
      std::begin(_grid), std::end(_grid),
      [this, value](unsigned char grid_value) { return grid_value == value; });

  return result;
}

void Grid16x16::print() const {
  for (int x = 0; x < GRID_WIDTH; ++x) {
    for (int y = 0; y < GRID_WIDTH; ++y) {
      std::cout << getValue({x, y}).value() << " ";
    }

    std::cout << "\n";
  }
}

const unsigned char *const Grid16x16::raw_data() const { return _grid; }

bool Grid16x16::setValue(const Point &point, unsigned char value) {
  const int index = get1DCoordinate(point);
  if (index >= GRID_SIZE)
    return false;

  _grid[index] = value;

  return true;
}

int Grid16x16::get1DCoordinate(const Point &point) const {
  return point.x + GRID_WIDTH * point.y;
}

bool Grid16x16::isWithinGridBounds(const Point &point) const {
  const int index = get1DCoordinate(point);
  return index < GRID_SIZE;
}

std::optional<unsigned char> Grid16x16::getValue(const Point &point) const {
  const int index = get1DCoordinate(point);
  if (index < GRID_SIZE) {
    return _grid[index];
  }

  return {};
}

void Grid16x16::fillRow(int row, unsigned char value) {
  if (row >= GRID_WIDTH) {
    std::cerr << "Row " << row << " is out of Grid range\n";
    return;
  }

  for (int col = 0; col < GRID_WIDTH; ++col) {
    setValue({row, col}, value);
  }
}

void Grid16x16::fillCol(int col, unsigned char value) {
  if (col >= GRID_WIDTH) {
    std::cerr << "Column " << col << " is out of Grid range\n";
    return;
  }

  for (int row = 0; row < GRID_WIDTH; ++row) {
    setValue({row, col}, value);
  }
}

void Grid16x16::fillAssociatedDiagonals(const Point &point,
                                        unsigned char value) {

  if (!isWithinGridBounds(point)) {
    std::cerr << "Requested point is out of grid range: " << point.x << " "
              << point.y;
    return;
  }

  for (int row = 0; row < GRID_WIDTH; ++row) {

    const int principal_diagonal_y = row - point.x + point.y;
    if (principal_diagonal_y >= 0 && principal_diagonal_y < GRID_WIDTH) {
      setValue({row, principal_diagonal_y}, value);
    }

    const int secondary_diagonal_y = point.x + point.y - row;
    if (secondary_diagonal_y >= 0 && secondary_diagonal_y < GRID_WIDTH) {
      setValue({row, secondary_diagonal_y}, value);
    }
  }
}
