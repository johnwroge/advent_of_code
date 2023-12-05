/*
first column is what opponent is going to play 
A Rock B Paper C Scissors
second column is what you play
X Rock Y Paper Z Scissors

0 lost (wrong answer)
3 draw (same answer)
6 won (right answer)

and
1 rock
2 paper
3 scissors

*/

//read from the file
import fs from 'fs';
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');
const file = fs.readFileSync(filePath, 'utf-8');
const inputArray = file.split('\n')
//iterate over rounds
let yourPlay;
let theirPlay;
let yourScore = 0;
let theirScore = 0; 
// for (let i = 0; i < inputArray.length; i++){
//     yourPlay = inputArray[i][2];
//     theirPlay = inputArray[i][0];
    // A Rock B Paper C Scissors
    // second column is what you play
    // X Rock Y Paper Z Scissors
//     if (yourPlay === "X" && theirPlay === "A"){
//         yourScore += 4;
//         theirScore += 4; 
//     }
//     else if (yourPlay === "X" && theirPlay === "B"){
//         yourScore += 1;
//         theirScore += 8; 
//     }
//     else if (yourPlay === "X" && theirPlay === "C"){
//         yourScore += 7;
//         theirScore += 3; 
//     }
//     else if (yourPlay === "Y" && theirPlay === "A"){
//         yourScore += 8;
//         theirScore += 1; 
//     }
//     else if (yourPlay === "Y" && theirPlay === "B"){
//         yourScore += 5;
//         theirScore += 5; 
//     }
//     else if (yourPlay === "Y" && theirPlay === "C"){
//         yourScore += 2;
//         theirScore += 9; 
//     }
//     else if (yourPlay === "Z" && theirPlay === "A"){
//         yourScore += 3;
//         theirScore += 7; 
//     }
//     else if (yourPlay === "Z" && theirPlay === "B"){
//         yourScore += 9;
//         theirScore += 2; 
//     }
//     else if (yourPlay === "Z" && theirPlay === "C"){
//         yourScore += 6;
//         theirScore += 6; 
//     }
// }
console.log(yourScore)

for (let i = 0; i < inputArray.length; i++){
    yourPlay = inputArray[i][2];
    theirPlay = inputArray[i][0];
  
    if (yourPlay === "X" && theirPlay === "A"){
        yourScore += 3;
        theirScore += 7; 
    }
    //lose rock 1
    else if (yourPlay === "X" && theirPlay === "B"){
        yourScore += 1;
        theirScore += 8; 
    }
    //lose paper 2
    else if (yourPlay === "X" && theirPlay === "C"){
        yourScore += 2;
        theirScore += 9; 
    }
    //draw rock 1
    else if (yourPlay === "Y" && theirPlay === "A"){
        yourScore += 4;
        theirScore += 4; 
    }
    //draw paper 2
    else if (yourPlay === "Y" && theirPlay === "B"){
        yourScore += 5;
        theirScore += 5; 
    }
    //draw scissors 3
    else if (yourPlay === "Y" && theirPlay === "C"){
        yourScore += 6;
        theirScore += 6; 
    }
    //win paper 2
    else if (yourPlay === "Z" && theirPlay === "A"){
        yourScore += 8;
        theirScore += 1; 
    }
    //win scissor 3
    else if (yourPlay === "Z" && theirPlay === "B"){
        yourScore += 9;
        theirScore += 2; 
    }
    //win rock 1
    else if (yourPlay === "Z" && theirPlay === "C"){
        yourScore += 7;
        theirScore += 3;
    }
}
console.log(yourScore)
