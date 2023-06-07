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
//iterate over inputArray
let item;
let first;
let second;
let range1Start;
let range1End;
let range2Start;
let range2End;
let sum = 0;
for (let i = 0; i < inputArray.length; i++) {
    item = inputArray[i].split(',');
    const [one, two] = item;
    first = one.split('-');
    second = two.split('-');
    range1Start = Number(first[0]);
    range1End = Number(first[1]);
    range2Start = Number(second[0]);
    range2End = Number(second[1]);
    // if ((range1Start >= range2Start && range1End <= range2End) || (range2Start >= range1Start && range1End >= range2End)){
    //     sum +=1;
    // }
    if ((range1Start <= range2Start && range1End >= range2Start) || (range2Start <= range1Start) && (range2End >= range1Start)) {
        sum += 1;
    }
}
console.log(sum);
