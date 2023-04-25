#!/usr/bin/node
/*
 *A class square that defines square and inherits
 *from square of 5-square.js
 */
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
