"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');
const file = fs_1.default.readFileSync(filePath, 'utf-8');
const inputArray = file.split('\n');
let sum = 0;
let results = [];
let prior;
let length;
let first;
let second;
let second2;
let val;
let index;
let temp;
// inputArray.forEach(line => {
//     length = Math.floor(line.length/2);
//     first = line.slice(0,length).split('');
//     second = line.slice(length).split('');
//     second2 = line.slice(length);
//     for (let char of first){
//         index = second.indexOf(char);
//         temp = char.charCodeAt(0);
//         if (index !== -1){
//             if (temp >= 97){
//                 prior = temp - 96;
//                 sum += prior;
//                 break;
//             } else {
//                 prior = temp - 38;
//                 sum += prior; 
//                 break;
//             }        
//         }
//     }
// })
const result = [];
for (let i = 0; i < inputArray.length; i += 3) {
    const row = [];
    for (let j = 0; j < 3; j++) {
        row.push(inputArray[i + j]);
    }
    result.push(row);
}
const chars = [];
for (let i = 0; i < result.length; i++) {
    const [first, second, third] = result[i];
    first.split('');
    second.split('');
    third.split('');
    for (let char of first) {
        if (second.indexOf(char) !== -1) {
            if (third.indexOf(char) !== -1) {
                chars.push(char);
                break;
            }
        }
    }
}
function calculate(char) {
    let temp = char.charCodeAt(0);
    sum = 0;
    if (temp >= 97) {
        prior = temp - 96;
        sum += prior;
    }
    else {
        prior = temp - 38;
        sum += prior;
    }
    return sum;
}
let total = 0;
for (let i = 0; i < chars.length; i++) {
    total += calculate(chars[i]);
}
console.log(total);
