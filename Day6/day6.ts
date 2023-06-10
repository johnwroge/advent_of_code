import fs from 'fs';

const path = require('path');

const filePath = path.join(__dirname, 'data.txt');
const file = fs.readFileSync(filePath, 'utf-8');

function isDistinct(arr: string[]): boolean {
    const count: Record <string,number> = {};
    for (let i = 0; i < arr.length; i++){
        count[arr[i]] ? count[arr[i]] += 1 : count[arr[i]] = 1 
    }
   
    for (let value of Object.values(count)){
        if (value > 1) return false; 
    }
    return true; 
}

const window: string[] = [];
for (let i = 0; i < 14; i++){
    window.push(file[i])
}


for (let i = 4; i < file.length; i++){
    if (isDistinct(window)){
        console.log(i);
        break; 
    } 
    window.push(file[i]);
    window.shift();
}
