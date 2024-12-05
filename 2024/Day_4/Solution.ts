import * as fs from 'fs';

interface Position {
    row: number;
    col: number;
}

interface Match {
    direction: string;
    pos: Position;
}

interface Intersection {
    dir1: string;
    dir2: string;
    pos1: Position;
    pos2: Position;
}

function readGrid(filename: string): string[][] {
    const content = fs.readFileSync(filename, 'utf8');
    return content.split('\n').map(row => row.split(''));
}

function partOne(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    const matches: Match[] = [];
    const target = "XMAS";

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols - 3; col++) {
            const sequence = Array.from({ length: 4 }, (_, i) => grid[row][col + i]).join('');
            if (sequence === target) {
                matches.push({ direction: "horizontal-right", pos: { row, col } });
            }
        }
    }

    for (let row = 0; row < rows; row++) {
        for (let col = 3; col < cols; col++) {
            const sequence = Array.from({ length: 4 }, (_, i) => grid[row][col - i]).join('');
            if (sequence === target) {
                matches.push({ direction: "horizontal-left", pos: { row, col } });
            }
        }
    }

    // Vertical down
    for (let row = 0; row < rows - 3; row++) {
        for (let col = 0; col < cols; col++) {
            const sequence = Array.from({ length: 4 }, (_, i) => grid[row + i][col]).join('');
            if (sequence === target) {
                matches.push({ direction: "vertical-down", pos: { row, col } });
            }
        }
    }

    for (let row = 3; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const sequence = Array.from({ length: 4 }, (_, i) => grid[row - i][col]).join('');
            if (sequence === target) {
                matches.push({ direction: "vertical-up", pos: { row, col } });
            }
        }
    }

    const directions: [number, number][] = [[1, 1], [1, -1], [-1, 1], [-1, -1]];
    const directionNames = ["down-right", "down-left", "up-right", "up-left"];

    directions.forEach((dir, dirIdx) => {
        const startRow = dir[0] < 0 ? 3 : 0;
        const endRow = dir[0] < 0 ? rows : rows - 3;
        const startCol = dir[1] < 0 ? 3 : 0;
        const endCol = dir[1] < 0 ? cols : cols - 3;

        for (let row = startRow; row < endRow; row++) {
            for (let col = startCol; col < endCol; col++) {
                const sequence = Array.from(
                    { length: 4 }, 
                    (_, i) => grid[row + i * dir[0]][col + i * dir[1]]
                ).join('');
                if (sequence === target) {
                    matches.push({ direction: directionNames[dirIdx], pos: { row, col } });
                }
            }
        }
    });

    return matches.length;
}

function partTwo(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    const allMas: Match[] = [];

    const checkDiagonalMas = (row: number, col: number): Match[] => {
        const found: Match[] = [];

        if (row < rows - 2 && col < cols - 2) {
            if (grid[row][col] === 'M' &&
                grid[row + 1][col + 1] === 'A' &&
                grid[row + 2][col + 2] === 'S') {
                found.push({ direction: "down-right", pos: { row, col } });
            }
        }

        if (row < rows - 2 && col >= 2) {
            if (grid[row][col] === 'M' &&
                grid[row + 1][col - 1] === 'A' &&
                grid[row + 2][col - 2] === 'S') {
                found.push({ direction: "down-left", pos: { row, col } });
            }
        }

        if (row >= 2 && col < cols - 2) {
            if (grid[row][col] === 'M' &&
                grid[row - 1][col + 1] === 'A' &&
                grid[row - 2][col + 2] === 'S') {
                found.push({ direction: "up-right", pos: { row, col } });
            }
        }

        if (row >= 2 && col >= 2) {
            if (grid[row][col] === 'M' &&
                grid[row - 1][col - 1] === 'A' &&
                grid[row - 2][col - 2] === 'S') {
                found.push({ direction: "up-left", pos: { row, col } });
            }
        }

        return found;
    };

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            allMas.push(...checkDiagonalMas(row, col));
        }
    }

    const intersections: Intersection[] = [];

    for (let i = 0; i < allMas.length; i++) {
        for (let j = i + 1; j < allMas.length; j++) {
            const m1 = allMas[i];
            const m2 = allMas[j];

            let a1Row: number, a1Col: number, a2Row: number, a2Col: number;

            switch (m1.direction) {
                case "down-right":
                    a1Row = m1.pos.row + 1;
                    a1Col = m1.pos.col + 1;
                    break;
                case "down-left":
                    a1Row = m1.pos.row + 1;
                    a1Col = m1.pos.col - 1;
                    break;
                case "up-right":
                    a1Row = m1.pos.row - 1;
                    a1Col = m1.pos.col + 1;
                    break;
                default: // up-left
                    a1Row = m1.pos.row - 1;
                    a1Col = m1.pos.col - 1;
                    break;
            }

            switch (m2.direction) {
                case "down-right":
                    a2Row = m2.pos.row + 1;
                    a2Col = m2.pos.col + 1;
                    break;
                case "down-left":
                    a2Row = m2.pos.row + 1;
                    a2Col = m2.pos.col - 1;
                    break;
                case "up-right":
                    a2Row = m2.pos.row - 1;
                    a2Col = m2.pos.col + 1;
                    break;
                default: 
                    a2Row = m2.pos.row - 1;
                    a2Col = m2.pos.col - 1;
                    break;
            }

            if (a1Row === a2Row && a1Col === a2Col) {
                intersections.push({
                    dir1: m1.direction,
                    dir2: m2.direction,
                    pos1: m1.pos,
                    pos2: m2.pos
                });
            }
        }
    }

    return intersections.length;
}

const grid = readGrid('2024/Day_4/data.txt');
console.log(partOne(grid));
console.log(partTwo(grid));