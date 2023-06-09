package main

import (
	// "bufio"
	"log"
	"os"
	// "fmt"
)
// qnjjqgjqgglqqwrrvvcww
func main(){
	file, err := os.Open("/Users/johnwroge/advent_of_code/Day6/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	// lines := []string{}
	// scanner := bufio.NewScanner(file)
	// var line string
	// for scanner.Scan(){
	// 	line = scanner.Text()
	// }

	//fmt.Println(line)
	// for i := 0; i < len(line); i++ {

	// }

	print(isDistinct([]rune{'a','b','c','c'}))
}


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

