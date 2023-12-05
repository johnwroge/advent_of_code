"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
const path = require('path');
const filePath = path.join(__dirname, 'moves.txt');
const file = fs_1.default.readFileSync(filePath, 'utf-8');
const filePath2 = path.join(__dirname, 'stacks.txt');
let file2 = fs_1.default.readFileSync(filePath2, 'utf-8');
let stacks = file2.split('\n');
let moves = file.split("\n");
console.log(stacks);
const order = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": []
};
const map = { "1": "1", "5": "2", "9": "3", "13": "4", "17": "5", "21": "6", "25": "7", "29": "8", "33": "9" };
for (let line of stacks) {
    let pos = 0;
    for (let char of line) {
        if (map[pos] && char) {
            order[map[pos]].push(char);
        }
    }
}
// function remove (len: number, src: number, dest: number){
//     for (let i = 0; i < len; i++){
//         let val = stacks[src].pop()
//         stacks[dest].push(val)
//     }
// }
