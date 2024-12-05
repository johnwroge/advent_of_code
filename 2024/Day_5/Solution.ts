import * as fs from 'fs';
import * as path from 'path';

interface Rule {
    before: number;
    after: number;
}

function readFile(): { rules: Rule[], updates: number[][] } {
    const content = fs.readFileSync(path.join(process.cwd(), '2024', 'Day_5', 'data.txt'), 'utf8');
    const lines = content.split('\n');
    
    const rules: Rule[] = [];
    const updates: number[][] = [];

    for (const line of lines) {
        if (line.includes('|')) {
            const [before, after] = line.split('|').map(n => parseInt(n.trim()));
            if (!isNaN(before) && !isNaN(after)) {
                rules.push({ before, after });
            }
        } else if (line.includes(',')) {
            const nums = line.split(',').map(n => parseInt(n.trim()));
            if (nums.every(n => !isNaN(n))) {
                updates.push(nums);
            }
        }
    }

    return { rules, updates };
}

function findSumOfMedians(group: number[][]): number {
    return group.reduce((sum, update) => {
        const index = Math.floor(update.length / 2);
        return sum + update[index];
    }, 0);
}

function partOne(updates: number[][], rules: Rule[]): [number, number[][]] {
    const toInclude: number[][] = [];
    const broken: number[][] = [];

    for (const update of updates) {
        let count = rules.length;
        let isBroken = false;

        for (const rule of rules) {
            if (update.includes(rule.before) && update.includes(rule.after)) {
                const firstIndex = update.indexOf(rule.before);
                const secondIndex = update.indexOf(rule.after);

                if (firstIndex < secondIndex) {
                    count--;
                } else {
                    broken.push(update);
                    isBroken = true;
                    break;
                }
            } else {
                count--;
            }
        }

        if (count === 0 && !isBroken) {
            toInclude.push(update);
        }
    }

    const answer = findSumOfMedians(toInclude);
    return [answer, broken];
}

function partTwo(unsorted: number[][], rules: Rule[]): number {
    const fixed: number[][] = [];

    for (const update of unsorted) {
        const copy = [...update];
        let changesMade = true;

        while (changesMade) {
            changesMade = false;
            for (const rule of rules) {
                if (copy.includes(rule.before) && copy.includes(rule.after)) {
                    const firstIndex = copy.indexOf(rule.before);
                    const secondIndex = copy.indexOf(rule.after);
                    if (firstIndex > secondIndex) {
                        [copy[firstIndex], copy[secondIndex]] = [copy[secondIndex], copy[firstIndex]];
                        changesMade = true;
                    }
                }
            }
        }
        fixed.push(copy);
    }

    return findSumOfMedians(fixed);
}

function main() {
    try {
        const { rules, updates } = readFile();
        
        const [part1Answer, unsorted] = partOne(updates, rules);
        console.log('Part 1:', part1Answer);
        
        const part2Answer = partTwo(unsorted, rules);
        console.log('Part 2:', part2Answer);
    } catch (error) {
        console.error('Error:', error instanceof Error ? error.message : error);
    }
}

main();