package main

import (
	"fmt"
	"bufio"
	// "sort"
	"log"
	"os"
	// "strconv"
)
type IntSlice []int
func main() {
	
	file, err := os.Open("/Users/johnwroge/advent_of_code/2023/Day1/day1.txt")
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
	for i := 0; i < len(lines); i++ {
		fmt.Println(lines[i])
		line := lines[i]
		for c in range()

	}
		
}