#!/usr/bin/node
/*
 * gives the addition of two numbers
 * The first number and the second
 */
function add (a, b) {
  const c = a + b;
  console.log(c);
}
add(Number(process.argv[2]), Number(process.argv[3]));
