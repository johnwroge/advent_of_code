/*
Determine total size of each directory
find directories with size of at most 100,000

cd
ls - gives us files and sizes
dir

split each line into parts

if first element is cd, and second is not / we changed 
directory and second element is not .. we need a separate sum

if first element is cd and second is .., then we need to change to 
outer directory

if first element is ls, then the values that 

*/

package main

import (
	"bufio"
	"log"
	"os"
	"strings"
	"fmt"
)

func main() {

	file, err := os.Open("/Users/johnwroge/advent_of_code/Day7/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	lines := [][]string{}
	scanner := bufio.NewScanner(file)

	//iterate while there is text
	for scanner.Scan(){
		//retrieve the current line of text
		line := scanner.Text()
		//split the line of text by spaces into a slice 
		item := strings.Split(line, " ")
		//append slice to 2d slice 
		lines = append(lines, item)
	}

 

}

// func Add(directories []string){
// 	vals := []
// }

func Sum(){
}
