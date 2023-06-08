package main

import (
	"bufio"
	"log"
	"os"
	// "strconv"
	// "strings"
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

}