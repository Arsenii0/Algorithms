#pragma once

#include <algorithm>
#include <cstring>
#include <iostream>
#include <optional>

struct Point {
  int x{-1};
  int y{-1};
};

static constexpr unsigned char ZERO{'0'};
static constexpr unsigned char ONE{'1'};

class Grid16x16 {

public:
  Grid16x16();

  void onSelect(const Point &point);

  size_t countValues(unsigned char value) const;
  void print() const;

  const unsigned char *const raw_data() const;

private: // methods
  int get1DCoordinate(const Point &point) const;
  bool isWithinGridBounds(const Point &point) const;
  std::optional<unsigned char> getValue(const Point &point) const;

  bool setValue(const Point &point, unsigned char value);
  void fillRow(int row, unsigned char value);
  void fillCol(int col, unsigned char value);
  void fillAssociatedDiagonals(const Point &point, unsigned char value);

private: // members
  static constexpr int GRID_WIDTH{16};
  static constexpr int GRID_SIZE{GRID_WIDTH * GRID_WIDTH};

  unsigned char _grid[GRID_SIZE];
};
