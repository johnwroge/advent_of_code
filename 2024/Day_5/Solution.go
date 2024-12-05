package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strings"
    "strconv"
)

type Rule struct {
    before, after int
}

func contains(slice []int, val int) bool {
    for _, item := range slice {
        if item == val {
            return true
        }
    }
    return false
}

func indexOf(slice []int, val int) int {
    for i, item := range slice {
        if item == val {
            return i
        }
    }
    return -1
}

func findSumOfMedians(group [][]int) int {
    sum := 0
    for _, update := range group {
        index := len(update) / 2
        sum += update[index]
    }
    return sum
}

func copySlice(slice []int) []int {
    copy := make([]int, len(slice))
    for i, v := range slice {
        copy[i] = v
    }
    return copy
}

func partOne(updates [][]int, rules []Rule) (int, [][]int) {
    toInclude := [][]int{}
    broken := [][]int{}

    for _, update := range updates {
        count := len(rules)
        isBroken := false

        for _, rule := range rules {
            if contains(update, rule.before) && contains(update, rule.after) {
                firstIndex := indexOf(update, rule.before)
                secondIndex := indexOf(update, rule.after)
                
                if firstIndex < secondIndex {
                    count--
                } else {
                    broken = append(broken, update)
                    isBroken = true
                    break
                }
            } else {
                count--
            }
        }

        if count == 0 && !isBroken {
            toInclude = append(toInclude, update)
        }
    }

    answer := findSumOfMedians(toInclude)
    return answer, broken
}

func partTwo(unsorted [][]int, rules []Rule) int {
    fixed := [][]int{}

    for _, update := range unsorted {
        copy := copySlice(update)
        changesMade := true

        for changesMade {
            changesMade = false
            for _, rule := range rules {
                if contains(copy, rule.before) && contains(copy, rule.after) {
                    firstIndex := indexOf(copy, rule.before)
                    secondIndex := indexOf(copy, rule.after)
                    if firstIndex > secondIndex {
                        copy[firstIndex], copy[secondIndex] = copy[secondIndex], copy[firstIndex]
                        changesMade = true
                    }
                }
            }
        }
        fixed = append(fixed, copy)
    }

    return findSumOfMedians(fixed)
}

func main() {
    cwd, err := os.Getwd()
    if err != nil {
        fmt.Printf("Error getting current directory: %v\n", err)
        return
    }

    content, err := os.ReadFile(filepath.Join(cwd, "2024", "Day_5", "data.txt"))
    if err != nil {
        fmt.Printf("Error reading file: %v\n", err)
        return
    }

    lines := strings.Split(string(content), "\n")
    
    var rules []Rule
    var updates [][]int

    for _, line := range lines {
        if strings.Contains(line, "|") {
            parts := strings.Split(line, "|")
            if len(parts) == 2 {
                before, err1 := strconv.Atoi(strings.TrimSpace(parts[0]))
                after, err2 := strconv.Atoi(strings.TrimSpace(parts[1]))
                if err1 == nil && err2 == nil {
                    rules = append(rules, Rule{before, after})
                }
            }
        } else if strings.Contains(line, ",") {
            parts := strings.Split(line, ",")
            var nums []int
            valid := true
            for _, part := range parts {
                num, err := strconv.Atoi(strings.TrimSpace(part))
                if err != nil {
                    valid = false
                    break
                }
                nums = append(nums, num)
            }
            if valid && len(nums) > 0 {
                updates = append(updates, nums)
            }
        }
    }

    part1, unsorted := partOne(updates, rules)
    fmt.Println("Part 1:", part1)
    
    part2 := partTwo(unsorted, rules)
    fmt.Println("Part 2:", part2)
}