#!/usr/bin/node
// Increases the function calls
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
