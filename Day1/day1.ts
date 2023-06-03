import fs from 'fs';
const path = require('path');

const filePath = path.join(__dirname, 'data.txt');
const file = fs.readFileSync(filePath, 'utf-8');

const inputArray = file.split('\n')

let current: number = 0; 
let max: number = -Infinity; 
let results: Array<number> = [];

inputArray.forEach(line => {

    if(line === ''){
        max = Math.max(max, current)
        results.push(current)
        current = 0; 

    } else {
        current += Number(line); 
    }
return max; 
})
results.sort((a,b) => b - a);

console.log(results[0] + results[1] + results[2])