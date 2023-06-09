package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
	"fmt"
)

func main(){
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day5/moves.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()


	file2, err := os.Open("/Users/johnwroge/advent_of_code/Day5/stacks.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file2.Close()

	//the instructions
	lines := []string{}
	scanner := bufio.NewScanner(file)

	for scanner.Scan(){
		line := scanner.Text()
		lines = append(lines, line)
	}
	// the stacks
	lines2 := []string{}
	scanner2 := bufio.NewScanner(file2)
	
	for scanner2.Scan(){
		line := scanner2.Text()
		lines2 = append(lines2, line)
	}
	// fmt.Println(lines2)

	stack := make(map[int][]string)
	stack[1] = []string{}
	stack[2] = []string{}
	stack[3] = []string{}
	stack[4] = []string{}
	stack[5] = []string{}
	stack[6] = []string{}
	stack[7] = []string{}
	stack[8] = []string{}
	stack[9] = []string{}

	keys := make(map[int]int)
	keys[1] = 1;
	keys[5] = 2;
	keys[9] = 3;
	keys[13] = 4;
	keys[17] = 5;
	keys[21] = 6;
	keys[25] = 7;
	keys[29] = 8;
	keys[33] = 9;

/*
	// iterating over stacks
	*/
	
	for i := 0; i < len(lines2); i++ {
		index := 0
		for _, char := range lines2[i] {
			str := string(char)
			if str != " " {
				val := keys[index]
				stack[val] = append(stack[val], "")
				copy(stack[val][1:],stack[val])
				stack[val][0] = str
			}
			index += 1
		}
	}
	helper := func(amt string, src string, dest string) {
		length,_ := strconv.Atoi(amt)
		index,_ := strconv.Atoi(src)
		desInd,_ := strconv.Atoi(dest)
		tempSlice := []string{}
		for i := 0; i < length; i++ {
			removedElement := stack[index][len(stack[index]) - 1]
			stack[index] = stack[index][:len(stack[index]) - 1]
			// fmt.Print(removedElement, "\n", stack[index])
			// stack[desInd] = append(stack[desInd], removedElement)
			tempSlice = append(tempSlice, removedElement)
		}
		length2 := len(tempSlice)
		left := 0
		right := length2 - 1
		
		for left < right {
			tempSlice[left], tempSlice[right] = tempSlice[right], tempSlice[left]
			left++
			right--
}

		stack[desInd] = append(stack[desInd], tempSlice...)
	}

	
	
	//iterating over instructions
	for i := 0; i < len(lines); i++ {
		line := strings.Split(lines[i], " ")
		amt := line[1]
		src := line[3]
		dest := line[5]
		// fmt.Println(amt, src, dest)
		helper(amt, src, dest)
	}
	fmt.Print(stack)

}