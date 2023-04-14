#!/usr/bin/node
/* prints C is fun X times
 * X is the number of arguments in the script
*/
if (process.argv[2]) {
  for (let j = 0; j < process.argv[2]; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
