#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        l += 'X';
      }
      console.log(l);
    }
  }
}

module.exports = Rectangle;
