package main

import (
	"bufio"
	"log"
	"os"
	"fmt"
	"strings"
)
// qnjjqgjqgglqqwrrvvcww
func main(){
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day6/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	lines := []string{}

	//var line string; 
	scanner := bufio.NewScanner(file)
	for scanner.Scan(){
		line := scanner.Text()
		item := strings.Split(line, "")
		lines = append(lines, item...)
	}

	var runes[]rune
	for i := 0; i < 14; i++ {
		str := lines[i]
		runeSlice := []rune(str)
		runes = append(runes,runeSlice[0])
	} 
	for i := 14; i < len(lines); i++ {
		// fmt.Print(runes, "\n")
		if isDistinct(runes) {
			fmt.Print(i)
			break; 
		}
		str := lines[i]
		runeSlice := []rune(str)
		runes = runes[1:]
		runes = append(runes, runeSlice...)
		//fmt.Print(runes)
	}

}
//part 1: 1625


func isDistinct(slice []rune) bool{
	count := make(map[rune]int)
	for i := 0; i < len(slice); i++ {
		val,isPresent := count[slice[i]]
		if isPresent{
			count[slice[i]] = val + 1
		} else {
			count[slice[i]] = 1
		}
	}
	for _,value := range(count){
		if value > 1 {
			 return false
		}
	}
return true; 
}


