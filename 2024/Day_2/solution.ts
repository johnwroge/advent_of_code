import * as fs from 'fs';
import * as path from 'path';

function readReports(): number[][] {
    const filePath = path.join(process.cwd(), '2024/Day_2/data.txt');
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    return fileContent.split('\n')
        .map(line => line.trim())
        .filter(line => line.length > 0)
        .map(line => line.split(/\s+/).map(Number));
}

function isValidSequence(report: number[], isIncreasing: boolean): boolean {
    for (let i = 1; i < report.length; i++) {
        const diff = isIncreasing ? 
            report[i] - report[i - 1] : 
            report[i - 1] - report[i];
        if (diff > 3 || diff < 1) return false;
    }
    return true;
}

function isIncreasing(report: number[]): boolean {
    for (let i = 1; i < report.length; i++) {
        if (report[i] <= report[i - 1]) return false;
    }
    return true;
}

function isDecreasing(report: number[]): boolean {
    for (let i = 1; i < report.length; i++) {
        if (report[i] >= report[i - 1]) return false;
    }
    return true;
}

function solve(part2: boolean): number {
    const reports = readReports();
    let safeReports = 0;

    for (const report of reports) {
        if ((isIncreasing(report) && isValidSequence(report, true)) || 
            (isDecreasing(report) && isValidSequence(report, false))) {
            safeReports++;
            continue;
        }

        if (part2) {
            let foundValid = false;
            for (let i = 0; i < report.length; i++) {
                const testReport = [...report.slice(0, i), ...report.slice(i + 1)];
                if ((isIncreasing(testReport) && isValidSequence(testReport, true)) ||
                    (isDecreasing(testReport) && isValidSequence(testReport, false))) {
                    foundValid = true;
                    break;
                }
            }
            if (foundValid) {
                safeReports++;
            }
        }
    }
    return safeReports;
}

console.log(solve(false));
console.log(solve(true));