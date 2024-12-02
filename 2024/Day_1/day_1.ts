import * as fs from 'fs';
import * as path from 'path';

interface Counter {
    [key: number]: number;
}

function readData(): [number[], number[]] {
    const filePath = path.join(process.cwd(), '2024', 'Day_1', 'data.txt');
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const lines = fileContent.split('\n');

    const leftDistance: number[] = [];
    const rightDistance: number[] = [];

    lines.forEach(line => {
        if (line.trim()) {
            const [first, second] = line.split('   ').map(s => parseInt(s.trim()));
            if (!isNaN(first) && !isNaN(second)) {
                leftDistance.push(first);
                rightDistance.push(second);
            }
        }
    });

    return [
        leftDistance.sort((a, b) => a - b),
        rightDistance.sort((a, b) => a - b)
    ];
}

function partOne(leftDistance: number[], rightDistance: number[]): string {
    const total = leftDistance.reduce((sum, curr, i) => {
        return sum + Math.abs(curr - rightDistance[i]);
    }, 0);

    return `Total difference for Part 1 is ${total}`;
}

function partTwo(leftDistance: number[], rightDistance: number[]): string {
    let similarityScore = 0;
    const rightCount: Counter = rightDistance.reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1;
        return acc;
    }, {} as Counter);

    leftDistance.forEach(n => {
        if (rightCount[n]) {
            similarityScore += rightCount[n] * n;
        }
    });

    return `Similarity score for Part 2 is ${similarityScore}`;
}

try {
    const [leftDistance, rightDistance] = readData();
    console.log(partOne(leftDistance, rightDistance));
    console.log(partTwo(leftDistance, rightDistance));
} catch (error) {
    console.error('Error:', error);
}