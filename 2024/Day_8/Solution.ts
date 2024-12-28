import * as fs from 'fs';
import * as path from 'path';


type Position = [number, number];
type Grid = string[][];
type Positions = { [key: string]: Position[] };


function readFile(filename: string) {
  const filePath = path.join('2024', 'Day_8', filename);
  return fs.readFileSync(filePath, 'utf-8').split('\n');
}

function create_grid(lines: string[]): Grid{
  const grid: string[][] = [];
  for (let line of lines) {
    grid.push(line.split(''));
  }
  return grid;
}

function print_grid(grid:  string[][]): void {
  for (let line of grid) {
    console.log(line.join(''));
  }
}

function get_distance(a: number[], b: number[]): Position{
    return [b[0] - a[0], b[1] - a[1]];
}


function Part_One() {
  let content: string[] = readFile('data.txt');
  let grid: Grid = create_grid(content);
  let positions: Positions = {};
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] != '.') {
        if (!positions.hasOwnProperty(grid[i][j])){
            positions[grid[i][j]] = []
        }
        positions[grid[i][j]].push([i, j])
      }
    }
  }
  const antiNodes = new Set<string>();
  for (const char of Object.keys(positions)) {
      const possibleNodes = positions[char];
      for (let i = 0; i < possibleNodes.length; i++) {
          const curr = possibleNodes[i];
          for (let j = i + 1; j < possibleNodes.length; j++) {
              const toCheck = possibleNodes[j];
              const [dy1, dx1] = get_distance(curr, toCheck);
              const [dy2, dx2] = get_distance(toCheck, curr);
              antiNodes.add(`${toCheck[0] + dy1},${toCheck[1] + dx1}`);
              antiNodes.add(`${curr[0] + dy2},${curr[1] + dx2}`);
          }
      }
  }
  let result = 0;
    for (const node of antiNodes) {
        const [x, y] = node.split(',').map(Number);
        if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
            result++;
        }
    }
    return result;
}


function Part_Two() {
let content: string[] = readFile('data.txt');
  let grid: Grid = create_grid(content);
    const positions: Positions = {};

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] !== '.') {
                if (!positions.hasOwnProperty(grid[i][j])) {
                    positions[grid[i][j]] = [];
                }
                positions[grid[i][j]].push([i, j]);
            }
        }
    }

    const antiNodes = new Set<string>();
    
    for (const char of Object.keys(positions)) {
        const possibleNodes = positions[char];
        for (let i = 0; i < possibleNodes.length; i++) {
            const curr = possibleNodes[i];
            for (let j = i + 1; j < possibleNodes.length; j++) {
                const toCheck = possibleNodes[j];
                const [dy1, dx1] = get_distance(curr, toCheck);
                const [dy2, dx2] = get_distance(toCheck, curr);
                
                let p1 = toCheck[0] + dy1;
                let p2 = toCheck[1] + dx1;
                while (p1 >= 0 && p1 < grid.length && p2 >= 0 && p2 <= grid[0].length) {
                    antiNodes.add(`${p1},${p2}`);
                    p1 += dy1;
                    p2 += dx1;
                }
                
                let p3 = curr[0] + dy2;
                let p4 = curr[1] + dx2;
                while (p3 >= 0 && p3 < grid.length && p4 >= 0 && p4 <= grid[0].length) {
                    antiNodes.add(`${p3},${p4}`);
                    p3 += dy2;
                    p4 += dx2;
                }
            }
        }
    }

    for (const node of antiNodes) {
        const [x, y] = node.split(',').map(Number);
        if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
            grid[x][y] = '#';
        }
    }

    let result = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid.length; j++) {
            if (grid[i][j] !== '.') {
                result++;
            }
        }
    }
    
    return result;
}


console.log('Part 1:', Part_One())
console.log('Part 2:', Part_Two())