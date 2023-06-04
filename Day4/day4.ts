import fs from 'fs';
const path = require('path');

const filePath = path.join(__dirname, 'data.txt');
const file = fs.readFileSync(filePath, 'utf-8');

const inputArray = file.split('\n')

//iterate over inputArray
let item: Array<string>
let first: any;
let second: any; 
let range1Start: any;
let range1End: any;
let range2Start: any;
let range2End: any;
let sum: number = 0; 
for(let i = 0; i < inputArray.length; i++){
   item = inputArray[i].split(',');
   const [one, two] = item;
   first = one.split('-');
   second = two.split('-');
   range1Start = Number(first[0]);
   range1End = Number(first[1]);
   range2Start = Number(second[0]);
   range2End = Number(second[1]);
    if ((range1Start >= range2Start && range1End <= range2End) || (range2Start >= range1Start && range1End >= range2End)){
        sum +=1;
    }
}
console.log(sum)