package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

func readFile(filename string) []string {
    content, err := os.ReadFile(filepath.Join("2024", "Day_7", filename))
    if err != nil {
        panic(err)
    }
    return strings.Split(string(content), "\n")
}

func format(lines []string) ([]int, [][]int) {
    testValues := make([]int, 0)
    combine := make([][]int, 0)
    
    for _, line := range lines {
        parts := strings.Split(line, ":")
        val, _ := strconv.Atoi(strings.TrimSpace(parts[0]))
        testValues = append(testValues, val)
        
        nums := make([]int, 0)
        for _, n := range strings.Fields(strings.TrimSpace(parts[1])) {
            num, _ := strconv.Atoi(n)
            nums = append(nums, num)
        }
        combine = append(combine, nums)
    }
    return testValues, combine
}

func generateOperators(ops int, part2 bool) [][]string {
    items := []string{"*", "+"}
    if part2 {
        items = append(items, "||")
    }
    
    result := make([][]string, 0)
    var generate func(curr []string)
    
    generate = func(curr []string) {
        if len(curr) == ops {
            temp := make([]string, len(curr))
            copy(temp, curr)
            result = append(result, temp)
            return
        }
        for _, item := range items {
            generate(append(curr, item))
        }
    }
    
    generate([]string{})
    return result
}

func PartOne(file string) int {
    lines := readFile(file)
    testVals, toCombine := format(lines)
    result := 0
    
    for i := 0; i < len(testVals); i++ {
        nums, testV := toCombine[i], testVals[i]
        ops := generateOperators(len(toCombine[i])-1, false)
        
        for _, combination := range ops {
            curr := nums[0]
            idx := 1
            for _, o := range combination {
                if o == "+" {
                    curr += nums[idx]
                } else if o == "*" {
                    curr *= nums[idx]
                }
                idx++
            }
            if curr == testV {
                result += testV
                break
            }
        }
    }
    return result
}

func PartTwo(file string) int {
    lines := readFile(file)
    testVals, toCombine := format(lines)
    result := 0
    
    for i := 0; i < len(testVals); i++ {
        nums, testV := toCombine[i], testVals[i]
        ops := generateOperators(len(toCombine[i])-1, true)
        
        for _, combination := range ops {
            curr := nums[0]
            idx := 1
            for _, o := range combination {
                if o == "+" {
                    curr += nums[idx]
                } else if o == "*" {
                    curr *= nums[idx]
                } else if o == "||" {
                    curr, _ = strconv.Atoi(fmt.Sprintf("%d%d", curr, nums[idx]))
                }
                idx++
            }
            if curr == testV {
                result += testV
                break
            }
        }
    }
    return result
}

func main() {
    one := PartOne("data.txt")
    fmt.Println("Part 1:", one)
    two := PartTwo("data.txt")
    fmt.Println("Part 2:", two)
}