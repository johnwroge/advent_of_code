import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {
    private static final String FILE_PATH = "data.txt";
    public static void main(String[] args) {
        Solution solution = new Solution();
        String content = solution.readFileContent();
        
        if (content != null) {
            long partOneSum = solution.calculatePartOne(content);
            long partTwoSum = solution.calculatePartTwo(content);
            
            System.out.printf("Total sum for part 1: %d%n", partOneSum);
            System.out.printf("Total sum for part 2: %d%n", partTwoSum);
        }
    }

    private String readFileContent() {
        try {
            Path filePath = Paths.get(System.getProperty("user.dir"), FILE_PATH);
            return Files.readString(filePath);
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            return null;
        }
    }

    private long calculatePartOne(String content) {
        Pattern pattern = Pattern.compile("mul\\((\\d+),(\\d+)\\)");
        Matcher matcher = pattern.matcher(content);
        long total = 0;

        while (matcher.find()) {
            int num1 = Integer.parseInt(matcher.group(1));
            int num2 = Integer.parseInt(matcher.group(2));
            total += (long) num1 * num2;
        }

        return total;
    }

    private long calculatePartTwo(String content) {
        Pattern pattern = Pattern.compile("(?:mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\))");
        Matcher matcher = pattern.matcher(content);
        boolean enabled = true;
        long total = 0;

        while (matcher.find()) {
            String operation = matcher.group(0);
            
            if ("do()".equals(operation)) {
                enabled = true;
            } else if ("don't()".equals(operation)) {
                enabled = false;
            } else if (enabled && operation.startsWith("mul")) {
                int num1 = Integer.parseInt(matcher.group(1));
                int num2 = Integer.parseInt(matcher.group(2));
                total += (long) num1 * num2;
            }
        }

        return total;
    }
}