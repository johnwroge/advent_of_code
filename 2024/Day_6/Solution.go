
package main

import (
    // "bufio"
    "fmt"
    "os"
    "strings"
	"path/filepath"
)

type Point struct {
    r, c int
}

type State struct {
    r, c int
    dir  string 
}

func createGrid(filename string) ([][]string, error) {
    cwd, err := os.Getwd()
    if err != nil {
        return nil, fmt.Errorf("error getting current directory: %v", err)
    }

    content, err := os.ReadFile(filepath.Join(cwd, "2024", "Day_6", "data.txt"))
    if err != nil {
        return nil, fmt.Errorf("error reading file: %v", err)
    }

    lines := strings.Split(string(content), "\n")
    grid := make([][]string, 0, len(lines))
    
    for _, line := range lines {
        if len(line) > 0 { 
            row := strings.Split(line, "")
            grid = append(grid, row)
        }
    }

    return grid, err
}

// func createGrid(lines []string) [][]string {
//     grid := make([][]string, len(lines))
//     for i, line := range lines {
//         grid[i] = strings.Split(line, "")
//     }
//     return grid
// }

func findStart(grid [][]string) Point {
    for i, row := range grid {
        for j, cell := range row {
            if cell == "^" {
                return Point{i, j}
            }
        }
    }
    return Point{0, 0}
}

func partOne(grid [][]string) int {
    dyDx := map[int]Point{
        0: {-1, 0},
        1: {0, 1},
        2: {1, 0},
        3: {0, -1},
    }
    directions := []string{"^", ">", "v", "<"}
    current := "^"
    pos := findStart(grid)
    visited := make(map[Point]bool)
    
    for {
        visited[pos] = true
        
        idx := indexOf(directions, current)
        delta := dyDx[idx]
        newR, newC := pos.r + delta.r, pos.c + delta.c
        
        if !inBounds(newR, newC, grid) {
            break
        }
        
        if grid[newR][newC] != "#" {
            pos.r, pos.c = newR, newC
            continue
        }
        
        current = directions[(idx + 1) % 4]
    }
    
    return len(visited)
}

func partTwo(grid [][]string) int {
    start := findStart(grid)
    cycles := 0
    
    for i := range grid {
        for j := range grid[0] {
            if grid[i][j] == "." && (i != start.r || j != start.c) {
                testGrid := copyGrid(grid)
                testGrid[i][j] = "#"
                if simulate(testGrid, start) {
                    cycles++
                }
            }
        }
    }
    return cycles
}

func simulate(grid [][]string, start Point) bool {
    dyDx := map[int]Point{
        0: {-1, 0},
        1: {0, 1},
        2: {1, 0},
        3: {0, -1},
    }
    directions := []string{"^", ">", "v", "<"}
    current := "^"
    pos := start
    visited := make(map[State]bool)
    
    for {
        state := State{pos.r, pos.c, current}
        if visited[state] {
            return true
        }
        visited[state] = true
        
        idx := indexOf(directions, current)
        delta := dyDx[idx]
        newR, newC := pos.r + delta.r, pos.c + delta.c
        
        if !inBounds(newR, newC, grid) {
            return false
        }
        
        if grid[newR][newC] != "#" {
            pos.r, pos.c = newR, newC
            continue
        }
        
        current = directions[(idx + 1) % 4]
    }
}

func copyGrid(grid [][]string) [][]string {
    newGrid := make([][]string, len(grid))
    for i := range grid {
        newGrid[i] = make([]string, len(grid[i]))
        copy(newGrid[i], grid[i])
    }
    return newGrid
}

func indexOf(slice []string, val string) int {
    for i, item := range slice {
        if item == val {
            return i
        }
    }
    return -1
}

func inBounds(r, c int, grid [][]string) bool {
    return r >= 0 && r < len(grid) && c >= 0 && c < len(grid[0])
}

func main() {
  
    grid, _ := createGrid("data.txt")
    fmt.Println("Part 1:", partOne(grid))
    fmt.Println("Part 2:", partTwo(grid))
}
