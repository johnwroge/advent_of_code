package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

type Solution struct {
    reports [][]int
}

func NewSolution() *Solution {
    cwd, _ := os.Getwd()
    file, _ := os.Open(filepath.Join(cwd, "2024", "Day_2", "data.txt"))
    defer file.Close()

    var reports [][]int
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        var numbers []int
        for _, num := range strings.Fields(scanner.Text()) {
            n, _ := strconv.Atoi(num)
            numbers = append(numbers, n)
        }
        reports = append(reports, numbers)
    }
    return &Solution{reports: reports}
}

func (s *Solution) isValidSequence(report []int, isIncreasing bool) bool {
    if len(report) < 2 {
        return true
    }

    for i := 1; i < len(report); i++ {
        prev := i - 1
        diff := 0
        if isIncreasing {
            diff = report[i] - report[prev]
        } else {
            diff = report[prev] - report[i]
        }
        if diff > 3 || diff < 1 {
            return false
        }
    }
    return true
}

func (s *Solution) isIncreasing(report []int) bool {
    for i := 1; i < len(report); i++ {
        if report[i] <= report[i-1] {
            return false
        }
    }
    return true
}

func (s *Solution) isDecreasing(report []int) bool {
    for i := 1; i < len(report); i++ {
        if report[i] >= report[i-1] {
            return false
        }
    }
    return true
}

func (s *Solution) solve(part2 bool) int {
    safeReports := 0
    for _, report := range s.reports {
        if (s.isIncreasing(report) && s.isValidSequence(report, true)) ||
           (s.isDecreasing(report) && s.isValidSequence(report, false)) {
            safeReports++
            continue
        }

        if part2 {
            foundValid := false
            for i := range report {
                testReport := make([]int, 0, len(report)-1)
                testReport = append(testReport, report[:i]...)
                testReport = append(testReport, report[i+1:]...)
                
                if (s.isIncreasing(testReport) && s.isValidSequence(testReport, true)) ||
                   (s.isDecreasing(testReport) && s.isValidSequence(testReport, false)) {
                    foundValid = true
                    break
                }
            }
            if foundValid {
                safeReports++
            }
        }
    }
    return safeReports
}

func main() {
    solution := NewSolution()
    fmt.Println(solution.solve(false))
    fmt.Println(solution.solve(true))
}