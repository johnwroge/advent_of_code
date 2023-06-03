package main

import (
	"fmt"
	"bufio"
	"sort"
	"log"
	"os"
	"strconv"
)
type IntSlice []int
func main() {
	
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day1/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	lines := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	current := 0; 
	max := 0; 
	maxSlice := make([]int,0)
for i := 0; i < len(lines); i++ {
	if lines[i] == "" {
		max = findMax(current, max)
		maxSlice = append(maxSlice, current)
		current = 0; 
	} else {
		num, err := strconv.Atoi(lines[i])
    	if err != nil {
        fmt.Println("Failed to convert string to integer:", err)
        return
    	}
		current += num
	}
}
sort.Slice(maxSlice, func(i, j int) bool {
    return maxSlice[i] > maxSlice[j]
})
print(maxSlice[0] + maxSlice[1] + maxSlice[2])

}


func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}