package main

import (
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "strconv"
)

func main() {
    // Read the file content
    cwd, err := os.Getwd()
    if err != nil {
        fmt.Printf("Error getting current directory: %v\n", err)
        return
    }

    content, err := os.ReadFile(filepath.Join(cwd, "2024", "Day_3", "data.txt"))
    if err != nil {
        fmt.Printf("Error reading file: %v\n", err)
        return
    }

    PartOne(string(content))
    PartTwo(string(content))
}

func PartOne(content string) {
    pattern := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
    matches := pattern.FindAllStringSubmatch(content, -1)
    
    total := 0
    for _, match := range matches {
        num1, _ := strconv.Atoi(match[1])
        num2, _ := strconv.Atoi(match[2])
        product := num1 * num2
        total += product
    }
    
    fmt.Printf("Total sum for part 1: %d\n", total)
}

func PartTwo(content string) {
    pattern := regexp.MustCompile(`(?:mul\((\d+),(\d+)\)|do\(\)|don't\(\))`)
    matches := pattern.FindAllStringSubmatch(content, -1)
    
    enabled := true
    total := 0
    
    for _, match := range matches {
        operation := match[0]
        
        switch {
        case operation == "do()":
            enabled = true
        case operation == "don't()":
            enabled = false
        case enabled && len(match[1]) > 0: // If it's a multiplication and enabled
            num1, _ := strconv.Atoi(match[1])
            num2, _ := strconv.Atoi(match[2])
            product := num1 * num2
            total += product
        }
    }
    
    fmt.Printf("Total sum for part 2: %d\n", total)
}