#!/usr/bin/node
/*
 *  identify the second argest number in the list
 *  prints 0 if no argument is passed\
*/
const argv = process.argv;
const argc = process.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const myArray = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(myArray[1]);
}
