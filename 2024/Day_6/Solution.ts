import * as fs from 'fs';
import * as path from 'path';

interface Point {
    r: number;
    c: number;
}

interface State {
    r: number; 
    c: number;
    dir: string;
}


function createGrid(filename: string): string[][] {
    const content = fs.readFileSync(filename, 'utf8');
    return content.split('\n').map(row => row.split(''));
}

function findStart(grid: string[][]): Point {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === '^') return {r: i, c: j};
        }
    }
    return {r: 0, c: 0};
}

function partOne(grid: string[][]): number {
    const dyDx: Record<number, Point> = {
        0: {r: -1, c: 0},
        1: {r: 0, c: 1},
        2: {r: 1, c: 0},
        3: {r: 0, c: -1}
    };
    const directions = ['^', '>', 'v', '<'];
    let current = '^';
    const pos = findStart(grid);
    const visited = new Set<string>();
    
    while (true) {
        visited.add(`${pos.r},${pos.c}`);
        
        const idx = directions.indexOf(current);
        const delta = dyDx[idx];
        const newR = pos.r + delta.r;
        const newC = pos.c + delta.c;
        
        if (!inBounds(newR, newC, grid)) break;
        
        if (grid[newR][newC] !== '#') {
            pos.r = newR;
            pos.c = newC;
            continue;
        }
        
        current = directions[(idx + 1) % 4];
    }
    
    return visited.size;
}

function partTwo(grid: string[][]): number {
    const start = findStart(grid);
    let cycles = 0;
    
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === '.' && (i !== start.r || j !== start.c)) {
                const testGrid = copyGrid(grid);
                testGrid[i][j] = '#';
                if (simulate(testGrid, start)) cycles++;
            }
        }
    }
    return cycles;
}

function simulate(grid: string[][], start: Point): boolean {
    const dyDx: Record<number, Point> = {
        0: {r: -1, c: 0},
        1: {r: 0, c: 1}, 
        2: {r: 1, c: 0},
        3: {r: 0, c: -1}
    };
    const directions = ['^', '>', 'v', '<'];
    let current = '^';
    const pos = {...start};
    const visited = new Set<string>();
    
    while (true) {
        const state = `${pos.r},${pos.c},${current}`;
        if (visited.has(state)) return true;
        visited.add(state);
        
        const idx = directions.indexOf(current);
        const delta = dyDx[idx];
        const newR = pos.r + delta.r;
        const newC = pos.c + delta.c;
        
        if (!inBounds(newR, newC, grid)) return false;
        
        if (grid[newR][newC] !== '#') {
            pos.r = newR;
            pos.c = newC;
            continue;
        }
        
        current = directions[(idx + 1) % 4];
    }
}

function copyGrid(grid: string[][]): string[][] {
    return grid.map(row => [...row]);
}

function inBounds(r: number, c: number, grid: string[][]): boolean {
    return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
}

async function main() {
    const grid = await createGrid('2024/Day_6/data.txt');
    console.log('Part 1:', partOne(grid));
    console.log('Part 2:', partTwo(grid));
}

main();