package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main(){
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day4/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	lines := []string{}
	scanner := bufio.NewScanner(file)

	for scanner.Scan(){
		line := scanner.Text()
		lines = append(lines, line)
	}
	sum := 0; 
	for i := 0; i < len(lines); i++ {
		item := strings.Split(lines[i], ",")
		item1 := item[0]
		item2 := item[1] 
		first := strings.Split(item1, "-")
		second := strings.Split(item2, "-")
	
		range1Start, err := strconv.Atoi(first[0]);
		if err != nil {
			log.Fatal(err)
		}
		range1End, err := strconv.Atoi(first[1]);
		if err != nil {
			log.Fatal(err)
		}
		range2Start, err := strconv.Atoi(second[0]);
		if err != nil {
			log.Fatal(err)
		}
		range2End, err := strconv.Atoi(second[1]);
		if err != nil {
			log.Fatal(err)
		}
		
			// if ((range1Start >= range2Start && range1End <= range2End) || (range2Start >= range1Start && range1End >= range2End)){
			// 	sum +=1;
			// }
			if ((range1Start <= range2Start) && (range1End >= range2Start)) || ((range2Start <= range1Start) && (range2End >= range1Start)){
            sum += 1
			}
	}
	print((sum))
}