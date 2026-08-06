#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstArg = parseInt(process.argv[2], 10);
const secondArg = parseInt(process.argv[3], 10);

console.log(add(firstArg, secondArg));
