import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

class Rule {
    int before;
    int after;

    Rule(int before, int after) {
        this.before = before;
        this.after = after;
    }
}

public class Solution {
    private List<Rule> rules;
    private List<List<Integer>> updates;

    public Solution() {
        rules = new ArrayList<>();
        updates = new ArrayList<>();
    }

    private void readFile() throws IOException {
        Path currentPath = Paths.get(System.getProperty("user.dir"),  "data.txt");
        List<String> lines = Files.readAllLines(currentPath);

        for (String line : lines) {
            if (line.contains("|")) {
                String[] parts = line.split("\\|");
                int before = Integer.parseInt(parts[0].trim());
                int after = Integer.parseInt(parts[1].trim());
                rules.add(new Rule(before, after));
            } else if (line.contains(",")) {
                List<Integer> numbers = Arrays.stream(line.split(","))
                    .map(String::trim)
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
                updates.add(numbers);
            }
        }
    }

    private int findSumOfMedians(List<List<Integer>> group) {
        int sum = 0;
        for (List<Integer> update : group) {
            int index = update.size() / 2;
            sum += update.get(index);
        }
        return sum;
    }

    public Result partOne() {
        List<List<Integer>> toInclude = new ArrayList<>();
        List<List<Integer>> broken = new ArrayList<>();

        for (List<Integer> update : updates) {
            int count = rules.size();
            boolean isBroken = false;

            for (Rule rule : rules) {
                if (update.contains(rule.before) && update.contains(rule.after)) {
                    int firstIndex = update.indexOf(rule.before);
                    int secondIndex = update.indexOf(rule.after);

                    if (firstIndex < secondIndex) {
                        count--;
                    } else {
                        broken.add(new ArrayList<>(update));
                        isBroken = true;
                        break;
                    }
                } else {
                    count--;
                }
            }

            if (count == 0 && !isBroken) {
                toInclude.add(new ArrayList<>(update));
            }
        }

        int answer = findSumOfMedians(toInclude);
        return new Result(answer, broken);
    }

    public int partTwo(List<List<Integer>> unsorted) {
        List<List<Integer>> fixed = new ArrayList<>();

        for (List<Integer> update : unsorted) {
            List<Integer> copy = new ArrayList<>(update);
            boolean changesMade = true;

            while (changesMade) {
                changesMade = false;
                for (Rule rule : rules) {
                    if (copy.contains(rule.before) && copy.contains(rule.after)) {
                        int firstIndex = copy.indexOf(rule.before);
                        int secondIndex = copy.indexOf(rule.after);
                        if (firstIndex > secondIndex) {
                            Collections.swap(copy, firstIndex, secondIndex);
                            changesMade = true;
                        }
                    }
                }
            }
            fixed.add(copy);
        }

        return findSumOfMedians(fixed);
    }

    private static class Result {
        int answer;
        List<List<Integer>> broken;

        Result(int answer, List<List<Integer>> broken) {
            this.answer = answer;
            this.broken = broken;
        }
    }

    public static void main(String[] args) {
        try {
            Solution solution = new Solution();
            solution.readFile();

            Result result = solution.partOne();
            System.out.println("Part 1: " + result.answer);

            int part2Answer = solution.partTwo(result.broken);
            System.out.println("Part 2: " + part2Answer);

        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}