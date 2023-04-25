#!/usr/bin/node
// Returns the number of the occurence in a list:
exports.nbOccurences = function (list, searchEelement) {
  let occurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchEelement) {
      occurences++;
    }
  }
  return occurences;
};
