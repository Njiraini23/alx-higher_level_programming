#!/usr/bin/node
/* prints a factorial whereby first argument is
*the integer used to compute the factorial
*/
function factorial (n) {
  if (n === 0) {
    return (1);
  } else {
    return (factorial(n - 1) * n);
  }
}
const n = process.argv[2];
if (n) {
  const result = factorial(n);
  console.log(result);
} else {
  console.log(1);
}
