package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

type Row struct {
	Column1 string
	Column2 string
}

func main() {
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day2/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	rows := []Row{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		columns := strings.Split(line, " ")
		if len(columns) == 2 {
			row := Row{
				Column1: columns[0],
				Column2: columns[1],
			}
			rows = append(rows, row)
		}
	}
	yourScore := 0;
	theirScore := 0; 

	for i := 0; i < len(rows); i++ {
		row := rows[i]
		// Access the columns of each row
		theirPlay := row.Column1
		yourPlay := row.Column2

		// if yourPlay == "X" && theirPlay == "A"{
		// 	yourScore += 4;
		// 	theirScore += 4; 
		// } else if yourPlay == "X" && theirPlay == "B"{
		// 	yourScore += 1;
		// 	theirScore += 8; 
		// } else if yourPlay == "X" && theirPlay == "C"{
		// 	yourScore += 7;
		// 	theirScore += 3; 
		// } else if yourPlay == "Y" && theirPlay == "A"{
		// 	yourScore += 8;
		// 	theirScore += 1; 
		// } else if yourPlay == "Y" && theirPlay == "B"{
		// 	yourScore += 5;
		// 	theirScore += 5; 
		// } else if yourPlay == "Y" && theirPlay == "C"{
		// 	yourScore += 2;
		// 	theirScore += 9; 
		// } else if yourPlay == "Z" && theirPlay == "A"{
		// 	yourScore += 3;
		// 	theirScore += 7; 
		// } else if yourPlay == "Z" && theirPlay == "B"{
		// 	yourScore += 9;
		// 	theirScore += 2; 
		// } else if yourPlay == "Z" && theirPlay == "C"{
		// 	yourScore += 6;
		// 	theirScore += 6; 
		// }
		
  
    if (yourPlay == "X" && theirPlay == "A"){
        yourScore += 3;
        theirScore += 7; 
    } else if (yourPlay == "X" && theirPlay == "B"){
        yourScore += 1;
        theirScore += 8; 
    } else if (yourPlay == "X" && theirPlay == "C"){
        yourScore += 2;
        theirScore += 9; 
    } else if (yourPlay == "Y" && theirPlay == "A"){
        yourScore += 4;
        theirScore += 4; 
    } else if (yourPlay == "Y" && theirPlay == "B"){
        yourScore += 5;
        theirScore += 5; 
    } else if (yourPlay == "Y" && theirPlay == "C"){
        yourScore += 6;
        theirScore += 6; 
    } else if (yourPlay == "Z" && theirPlay == "A"){
        yourScore += 8;
        theirScore += 1; 
    }  else if (yourPlay == "Z" && theirPlay == "B"){
        yourScore += 9;
        theirScore += 2; 
    } else if (yourPlay == "Z" && theirPlay == "C"){
        yourScore += 7;
        theirScore += 3;
    }
}
print(yourScore)
		
	}
	
