#!/usr/bin/node
/*
 * class square that creates a square and inherits from a rectangle
 * in the 4-rectangle
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
