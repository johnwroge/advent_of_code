import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    static class FormatResult {
        List<Long> testValues;           // Changed from Integer to Long
        List<List<Long>> combine;        // Changed from Integer to Long
    
        FormatResult(List<Long> testValues, List<List<Long>> combine) {
            this.testValues = testValues;
            this.combine = combine;
        }
    }

    private static List<String> readFile(String filename) {
        try {
            Path path = Paths.get(System.getProperty("user.dir"),  "data.txt");
            return Files.readAllLines(path);
        } catch (IOException e) {
            throw new RuntimeException("Error reading file: " + e.getMessage());
        }
    }

    private static FormatResult format(List<String> lines) {
        List<Long> testValues = new ArrayList<>();    // Changed from Integer to Long
        List<List<Long>> combine = new ArrayList<>(); // Changed from Integer to Long
    
        for (String line : lines) {
            String[] parts = line.split(":");
            testValues.add(Long.parseLong(parts[0].trim())); // Changed parseInt to parseLong
            
            List<Long> nums = Arrays.stream(parts[1].trim().split("\\s+"))
                                   .map(Long::parseLong)      // Changed Integer to Long
                                   .collect(Collectors.toList());
            combine.add(nums);
        }
        return new FormatResult(testValues, combine);
    }

    private static List<List<String>> generateOperators(int ops, boolean part2) {
        List<String> items = new ArrayList<>(Arrays.asList("*", "+"));
        if (part2) {
            items.add("||");
        }

        List<List<String>> result = new ArrayList<>();
        generateCombinations(new ArrayList<>(), ops, items, result);
        return result;
    }

    private static void generateCombinations(List<String> current, int ops, 
                                          List<String> items, List<List<String>> result) {
        if (current.size() == ops) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (String item : items) {
            current.add(item);
            generateCombinations(current, ops, items, result);
            current.remove(current.size() - 1);
        }
    }

    public static long partOne(String file) {
        List<String> lines = readFile(file);
        FormatResult formatted = format(lines);
        long result = 0;
    
        for (int i = 0; i < formatted.testValues.size(); i++) {
            List<Long> nums = formatted.combine.get(i);        // Changed to Long
            long testV = formatted.testValues.get(i);         // Changed to long
            List<List<String>> ops = generateOperators(nums.size() - 1, false);
    
            for (List<String> combination : ops) {
                long curr = nums.get(0);
                int idx = 1;
                
                for (String op : combination) {
                    if (op.equals("+")) {
                        curr += nums.get(idx);
                    } else if (op.equals("*")) {
                        curr *= nums.get(idx);
                    }
                    idx++;
                }
                
                if (curr == testV) {
                    result += testV;
                    break;
                }
            }
        }
        return result;
    }
    
    public static long partTwo(String file) {
        List<String> lines = readFile(file);
        FormatResult formatted = format(lines);
        long result = 0;
    
        for (int i = 0; i < formatted.testValues.size(); i++) {
            List<Long> nums = formatted.combine.get(i);        // Changed to Long
            long testV = formatted.testValues.get(i);         // Changed to long
            List<List<String>> ops = generateOperators(nums.size() - 1, true);
    
            for (List<String> combination : ops) {
                long curr = nums.get(0);
                int idx = 1;
    
                for (String op : combination) {
                    if (op.equals("+")) {
                        curr += nums.get(idx);
                    } else if (op.equals("*")) {
                        curr *= nums.get(idx);
                    } else if (op.equals("||")) {
                        curr = Long.parseLong(curr + "" + nums.get(idx));
                    }
                    idx++;
                }
    
                if (curr == testV) {
                    result += testV;
                    break;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        // Time Part 1
        long startTime1 = System.nanoTime();
        long one = partOne("data.txt");
        long endTime1 = System.nanoTime();
        long duration1 = (endTime1 - startTime1) / 1_000_000;  // Convert to milliseconds
        
        // Time Part 2
        long startTime2 = System.nanoTime();
        long two = partTwo("data.txt");
        long endTime2 = System.nanoTime();
        long duration2 = (endTime2 - startTime2) / 1_000_000;  // Convert to milliseconds
        
        System.out.println("Part 1: " + one + " (Time: " + duration1 + "ms)");
        System.out.println("Part 2: " + two + " (Time: " + duration2 + "ms)");
        System.out.println("Total Time: " + (duration1 + duration2) + "ms");
    }
}