#!/usr/bin/node
// imports an array and computes a new array
const list = require('./-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
