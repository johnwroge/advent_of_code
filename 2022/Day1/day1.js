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
let current = 0;
let max = -Infinity;
let results = [];
inputArray.forEach(line => {
    if (line === '') {
        max = Math.max(max, current);
        results.push(current);
        current = 0;
    }
    else {
        current += Number(line);
    }
    return max;
});
results.sort((a, b) => b - a);
console.log(results[0] + results[1] + results[2]);
