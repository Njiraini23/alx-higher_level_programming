#!/usr/bin/node
/*
* prints a square whereby
* the size of the square is the argument
*/
const myArgs = process.argv.slice(2);
let myInt = '';
if (isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  for (let j = 0; j < parseInt(myArgs[0]); j++) {
    myInt += 'X';
  }
  for (let i = 0; i < parseInt(myArgs[0]); i++) {
    console.log(myInt);
  }
}
