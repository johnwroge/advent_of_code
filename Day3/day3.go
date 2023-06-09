package main

import (
	"bufio"
	"log"
	"os"
	"strings"
	"fmt"
)

func main() {
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day3/data.txt")
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
	
	var word string; 
	sum := 0; 
	// part 1

	// for i := 0; i < len(lines); i++ {
	// 	word = lines[i]
	// 	length := len(word)/2; 
	// 	first := word[0:length]
	// 	second := word[length:]
	// 	for _, char := range first {
	// 		if strings.ContainsRune(second, char){
	// 			charCode := int(char)
	// 			if charCode >= 97 {
	// 				sum += charCode - 96
	// 				break;
	// 			} else {
	// 				sum += charCode - 38
	// 				break
	// 			}
	// 		}
	// 	}
	// }

	//part 2
	
	var word2 string; 
	var word3 string; 
	fmt.Println(lines)
	for i := 0; i < len(lines); i+=3 {
		word = lines[i]
		word2 = lines[i + 1]
		word3 = lines[i + 2]
		for _, char := range word {
			if strings.ContainsRune(word2, char){
				if strings.ContainsRune(word3, char){
				charCode := int(char)
				if charCode >= 97 {
					sum += charCode - 96
					break;
				} else {
					sum += charCode - 38
					break
					}
				}
			}
		}
	}
print(sum)
}

		
