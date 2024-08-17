// const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split(" ").map(Number);

//1. 입력값이 하나일 경우(문자)
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

/*
# BOJ 1000 A + B
"use strict";
let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0])
let b = parseInt(input[1])
console.log(a+b)

*/