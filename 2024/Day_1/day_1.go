package main 

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
)

func readData() ([]int, []int, error) {
	cwd, err := os.Getwd()
	if err != nil {
		return nil, nil, err
	}

	file, err := os.Open(filepath.Join(cwd, "2024", "Day_1", "data.txt"))
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	var leftDistance, rightDistance []int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), "   ")
		if len(parts) != 2 {
			continue
		}

		left, err := strconv.Atoi(strings.TrimSpace(parts[0]))
		if err != nil {
			continue
		}

		right, err := strconv.Atoi(strings.TrimSpace(parts[1]))
		if err != nil {
			continue
		}

		leftDistance = append(leftDistance, left)
		rightDistance = append(rightDistance, right)
	}

	sort.Ints(leftDistance)
	sort.Ints(rightDistance)

	return leftDistance, rightDistance, nil
}

func partOne(leftDistance, rightDistance []int) string {
	total := 0
	for i := range leftDistance {
		diff := leftDistance[i] - rightDistance[i]
		if diff < 0 {
			diff = -diff
		}
		total += diff
	}
	return fmt.Sprintf("Total difference for Part 1 is %d", total)
}

func partTwo(leftDistance, rightDistance []int) string {
	similarityScore := 0
	rightCount := make(map[int]int)

	for _, n := range rightDistance {
		rightCount[n]++
	}

	for _, n := range leftDistance {
		if count, exists := rightCount[n]; exists {
			similarityScore += count * n
		}
	}

	return fmt.Sprintf("Similarity score for Part 2 is %d", similarityScore)
}

func main() {
	leftDistance, rightDistance, err := readData()
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	fmt.Println(partOne(leftDistance, rightDistance))
	fmt.Println(partTwo(leftDistance, rightDistance))
}