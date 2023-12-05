import fs from 'fs';

const path = require('path');

const filePath = path.join(__dirname, 'data.txt');
const file = fs.readFileSync(filePath, 'utf-8');

const lines = file.split("\n")

let index: number = 0; 
let files: any = [];
let directory: any = [];

while (index < lines.length){
    //case 1, changing directories
    if (lines[index][1] === "cd"){
        //if changing to home directory, create an empty file
        if (lines[index][2] === "/"){
            var direct:any = [];
            //otherwise if changing into outer directory, remove the last file from the file system
        } else if (lines[index][2] === ".."){
            direct.pop()
            //otherwise, push the current file into the created file
        } else {
            direct.push(lines[index][2])
        }
        //at the end of the loop increment the index
        index += 1
        //check if the command is to list
    } else if (lines[index][1] === "ls"){
        //iterate index(go to next element)
        index += 1
        //loop while the current line is not a command
        while (lines[index][0] != "$"){
            //check if the current element is not 'dir'
            if (lines[index][0] != "dir"){
                //invoke helper function
                Add([lines[index][0], lines[index][1]], direct, lines)
            }
            index += 1; 
        }
    }
}



function Add (file: any[], direct: string[], filesystem: string[]){
    if (direct === []){
        if (filesystem)
    }
}   

function Sum (){

}