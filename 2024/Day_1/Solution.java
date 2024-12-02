import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private List<Integer> leftDistance = new ArrayList<>();
    private List<Integer> rightDistance = new ArrayList<>();

    public Solution() {
        readData();
    }

    private void readData() {
        try {
            Path path = Paths.get(System.getProperty("user.dir"), "data.txt");
            List<String> lines = Files.readAllLines(path);

            for (String line : lines) {
                String[] parts = line.split("   ");
                if (parts.length == 2) {
                    leftDistance.add(Integer.parseInt(parts[0].trim()));
                    rightDistance.add(Integer.parseInt(parts[1].trim()));
                }
            }

            Collections.sort(leftDistance);
            Collections.sort(rightDistance);

        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }

    public String partOne() {
        int total = 0;
        for (int i = 0; i < leftDistance.size(); i++) {
            total += Math.abs(leftDistance.get(i) - rightDistance.get(i));
        }
        return String.format("Total difference for Part 1 is %d", total);
    }

    public String partTwo() {
        int similarityScore = 0;
        Map<Integer, Integer> rightCount = new HashMap<>();

        // Count occurrences in rightDistance
        for (int n : rightDistance) {
            rightCount.put(n, rightCount.getOrDefault(n, 0) + 1);
        }

        for (int n : leftDistance) {
            if (rightCount.containsKey(n)) {
                similarityScore += rightCount.get(n) * n;
            }
        }

        return String.format("Similarity score for Part 2 is %d", similarityScore);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.partOne());
        System.out.println(solution.partTwo());
    }
}