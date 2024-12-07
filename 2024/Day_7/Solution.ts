import * as fs from 'fs';
import * as path from 'path';

interface FormatResult {
    testValues: number[];
    combine: number[][];
}

function readFile(filename: string): string[] {
    const filePath = path.join('2024', 'Day_7', filename);
    return fs.readFileSync(filePath, 'utf-8').split('\n');
}

function format(lines: string[]): FormatResult {
    const testValues: number[] = [];
    const combine: number[][] = [];

    for (const line of lines) {
        const [val, row] = line.split(':');
        testValues.push(parseInt(val.trim()));
        combine.push(row.trim().split(/\s+/).map(n => parseInt(n)));
    }
    return { testValues, combine };
}

function generateOperators(ops: number, part2: boolean): string[][] {
    const items: string[] = ['*', '+'];
    if (part2) {
        items.push('||');
    }

    const result: string[][] = [];
    
    function generateCombinations(current: string[]) {
        if (current.length === ops) {
            result.push([...current]);
            return;
        }
        for (const item of items) {
            generateCombinations([...current, item]);
        }
    }

    generateCombinations([]);
    return result;
}

function partOne(file: string): number {
    const lines = readFile(file);
    const { testValues, combine } = format(lines);
    let result = 0;

    for (let i = 0; i < testValues.length; i++) {
        const nums = combine[i];
        const testV = testValues[i];
        const ops = generateOperators(nums.length - 1, false);

        for (const combination of ops) {
            let curr = nums[0];
            let idx = 1;

            for (const op of combination) {
                if (op === '+') {
                    curr += nums[idx];
                } else if (op === '*') {
                    curr *= nums[idx];
                }
                idx++;
            }

            if (curr === testV) {
                result += testV;
                break;
            }
        }
    }
    return result;
}

function partTwo(file: string): number {
    const lines = readFile(file);
    const { testValues, combine } = format(lines);
    let result = 0;

    for (let i = 0; i < testValues.length; i++) {
        const nums = combine[i];
        const testV = testValues[i];
        const ops = generateOperators(nums.length - 1, true);

        for (const combination of ops) {
            let curr = nums[0];
            let idx = 1;

            for (const op of combination) {
                if (op === '+') {
                    curr += nums[idx];
                } else if (op === '*') {
                    curr *= nums[idx];
                } else if (op === '||') {
                    curr = parseInt(`${curr}${nums[idx]}`);
                }
                idx++;
            }

            if (curr === testV) {
                result += testV;
                break;
            }
        }
    }
    return result;
}

function main() {
    const one = partOne('data.txt');
    console.log('Part 1:', one);
    const two = partTwo('data.txt');
    console.log('Part 2:', two);
}

main();