#!/usr/bin/node
// executes the a visbile function X times

exports.callMeMoby = function (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
};
