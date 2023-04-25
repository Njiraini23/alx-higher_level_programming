#!/usr/bin/node
// prints the  number of arguments already printed and the new arguments values
let narg = 0;
exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
