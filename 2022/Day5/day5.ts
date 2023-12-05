import fs from 'fs';

const path = require('path');

const filePath = path.join(__dirname, 'moves.txt');
const file = fs.readFileSync(filePath, 'utf-8');

const filePath2 = path.join(__dirname, 'stacks.txt');
let file2 = fs.readFileSync(filePath2, 'utf-8');

let stacks = file2.split('\n');
let moves = file.split("\n");
const order: any = {
    "1":[],
    "2":[],
    "3":[],
    "4":[],
    "5":[],
    "6":[],
    "7":[],
    "8":[],
    "9":[]
}
const map:any = {"1": "1" , "5": "2", "9": "3", "13": "4", "17": "5", "21": "6", "25": "7", "29":"8", "33": "9"}
for (let line of stacks){
    let pos:any = 0;
    for (let char of line){
        if (map[pos] && char !== " "){
            order[map[pos]].unshift(char)
        }
        pos++
    }
}

for (let struct of moves){
    let order1 = struct.split(" ")
    let num = Number(order1[1])
    let src = order1[3]
    let dest = order1[5]
    remove(num, src, dest)
}


// function remove (len: number, src: string, dest: string){
//     for (let i = 0; i < len; i++){
//         let val = order[src].pop()
//         order[dest].push(val)
//     }
// }

function remove (len: number, src: string, dest: string){
    let ordering = []
    for (let i = 0; i < len; i++){
        let val = order[src].pop()
        ordering.push(val)
    }
    ordering.reverse()
    order[dest].push(...ordering)
}

console.log(order)