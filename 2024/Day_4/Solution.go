package main

import (
	"fmt"
	"os"
	"strings"
	"path/filepath"
)

type Position struct {
	row, col int
}

type Match struct {
	direction string
	pos       Position
}

func readGrid(filename string) ([][]string, error) {
    cwd, err := os.Getwd()
    if err != nil {
        return nil, fmt.Errorf("error getting current directory: %v", err)
    }

    content, err := os.ReadFile(filepath.Join(cwd, "2024", "Day_4", "data.txt"))
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

func PartOne(grid [][]string) int {
	rows := len(grid)
	cols := len(grid[0])
	var matches []Match
	target := "XMAS"

	for row := 0; row < rows; row++ {
		for col := 0; col < cols-3; col++ {
			sequence := ""
			for i := 0; i < 4; i++ {
				sequence += grid[row][col+i]
			}
			if sequence == target {
				matches = append(matches, Match{"horizontal-right", Position{row, col}})
			}
		}
	}

	for row := 0; row < rows; row++ {
		for col := 3; col < cols; col++ {
			sequence := ""
			for i := 0; i < 4; i++ {
				sequence += grid[row][col-i]
			}
			if sequence == target {
				matches = append(matches, Match{"horizontal-left", Position{row, col}})
			}
		}
	}

	for row := 0; row < rows-3; row++ {
		for col := 0; col < cols; col++ {
			sequence := ""
			for i := 0; i < 4; i++ {
				sequence += grid[row+i][col]
			}
			if sequence == target {
				matches = append(matches, Match{"vertical-down", Position{row, col}})
			}
		}
	}

	for row := 3; row < rows; row++ {
		for col := 0; col < cols; col++ {
			sequence := ""
			for i := 0; i < 4; i++ {
				sequence += grid[row-i][col]
			}
			if sequence == target {
				matches = append(matches, Match{"vertical-up", Position{row, col}})
			}
		}
	}

	directions := [][2]int{
		{1, 1},   
		{1, -1},
		{-1, 1},  
		{-1, -1}, 
	}
	directionNames := []string{"down-right", "down-left", "up-right", "up-left"}

	for dirIdx, dir := range directions {
		startRow := 0
		endRow := rows
		startCol := 0
		endCol := cols

		if dir[0] < 0 {
			startRow = 3
		} else {
			endRow = rows - 3
		}

		if dir[1] < 0 {
			startCol = 3
		} else {
			endCol = cols - 3
		}

		for row := startRow; row < endRow; row++ {
			for col := startCol; col < endCol; col++ {
				sequence := ""
				for i := 0; i < 4; i++ {
					sequence += grid[row+i*dir[0]][col+i*dir[1]]
				}
				if sequence == target {
					matches = append(matches, Match{directionNames[dirIdx], Position{row, col}})
				}
			}
		}
	}

	return len(matches)
}

func PartTwo(grid [][]string) int {
	rows := len(grid)
	cols := len(grid[0])
	var allMas []Match

	checkDiagonalMas := func(row, col int) []Match {
		var found []Match

		if row < rows-2 && col < cols-2 {
			if grid[row][col] == "M" &&
				grid[row+1][col+1] == "A" &&
				grid[row+2][col+2] == "S" {
				found = append(found, Match{"down-right", Position{row, col}})
			}
		}

		if row < rows-2 && col >= 2 {
			if grid[row][col] == "M" &&
				grid[row+1][col-1] == "A" &&
				grid[row+2][col-2] == "S" {
				found = append(found, Match{"down-left", Position{row, col}})
			}
		}

		if row >= 2 && col < cols-2 {
			if grid[row][col] == "M" &&
				grid[row-1][col+1] == "A" &&
				grid[row-2][col+2] == "S" {
				found = append(found, Match{"up-right", Position{row, col}})
			}
		}

		if row >= 2 && col >= 2 {
			if grid[row][col] == "M" &&
				grid[row-1][col-1] == "A" &&
				grid[row-2][col-2] == "S" {
				found = append(found, Match{"up-left", Position{row, col}})
			}
		}

		return found
	}

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			diagonals := checkDiagonalMas(row, col)
			allMas = append(allMas, diagonals...)
		}
	}

	type Intersection struct {
		dir1, dir2 string
		pos1, pos2 Position
	}

	var intersections []Intersection

	for i := 0; i < len(allMas); i++ {
		for j := i + 1; j < len(allMas); j++ {
			m1 := allMas[i]
			m2 := allMas[j]

			var a1Row, a1Col, a2Row, a2Col int

			switch m1.direction {
			case "down-right":
				a1Row, a1Col = m1.pos.row+1, m1.pos.col+1
			case "down-left":
				a1Row, a1Col = m1.pos.row+1, m1.pos.col-1
			case "up-right":
				a1Row, a1Col = m1.pos.row-1, m1.pos.col+1
			default: // up-left
				a1Row, a1Col = m1.pos.row-1, m1.pos.col-1
			}

			switch m2.direction {
			case "down-right":
				a2Row, a2Col = m2.pos.row+1, m2.pos.col+1
			case "down-left":
				a2Row, a2Col = m2.pos.row+1, m2.pos.col-1
			case "up-right":
				a2Row, a2Col = m2.pos.row-1, m2.pos.col+1
			default: 
				a2Row, a2Col = m2.pos.row-1, m2.pos.col-1
			}

			if a1Row == a2Row && a1Col == a2Col {
				intersections = append(intersections, Intersection{
					m1.direction, m2.direction, m1.pos, m2.pos,
				})
			}
		}
	}

	return len(intersections)
}

func main() {
	grid, _ := readGrid("data.txt")
	fmt.Println(PartOne(grid))
	fmt.Println(PartTwo(grid))
}