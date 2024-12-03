import * as fs from 'fs';
import * as path from 'path';

function readFileContent(filePath: string): string {
    try {
        return fs.readFileSync(path.join(process.cwd(), filePath), 'utf-8');
    } catch (error) {
        console.error('Error reading file:', error);
        return '';
    }
}

function calculatePartOne(content: string): number {
    const pattern = /mul\((\d+),(\d+)\)/g;
    let total = 0;
    let match: RegExpExecArray | null;
    
    while ((match = pattern.exec(content)) !== null) {
        const num1 = parseInt(match[1]);
        const num2 = parseInt(match[2]);
        total += num1 * num2;
    }
    
    return total;
}

function calculatePartTwo(content: string): number {
    const pattern = /(?:mul\((\d+),(\d+)\)|do\(\)|don't\(\))/g;
    let enabled = true;
    let total = 0;
    let match: RegExpExecArray | null;
    
    while ((match = pattern.exec(content)) !== null) {
        const operation = match[0];
        
        if (operation === "do()") {
            enabled = true;
        } else if (operation === "don't()") {
            enabled = false;
        } else if (enabled && operation.startsWith("mul")) {
            const num1 = parseInt(match[1]);
            const num2 = parseInt(match[2]);
            total += num1 * num2;
        }
    }
    
    return total;
}

function main(): void {
    const filePath = '2024/Day_3/data.txt';
    const content = readFileContent(filePath);
    
    if (content) {
        const partOneSum = calculatePartOne(content);
        const partTwoSum = calculatePartTwo(content);
        
        console.log(`Total sum for part 1: ${partOneSum}`);
        console.log(`Total sum for part 2: ${partTwoSum}`);
    }
}

main();