import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.Collectors;

public class solution {
    private List<List<Integer>> reports;

    public solution() throws IOException {
        Path path = Paths.get(System.getProperty("user.dir"), "data.txt");
        reports = Files.lines(path)
            .map(line -> Arrays.stream(line.trim().split("\\s+"))
                .map(Integer::parseInt)
                .collect(Collectors.toList()))
            .collect(Collectors.toList());
    }

    private boolean isValidSequence(List<Integer> report, boolean isIncreasing) {
        for (int i = 1; i < report.size(); i++) {
            int diff = isIncreasing ? 
                      report.get(i) - report.get(i - 1) :
                      report.get(i - 1) - report.get(i);
            if (diff > 3 || diff < 1) return false;
        }
        return true;
    }

    private boolean isIncreasing(List<Integer> report) {
        for (int i = 1; i < report.size(); i++) {
            if (report.get(i) <= report.get(i - 1)) return false;
        }
        return true;
    }

    private boolean isDecreasing(List<Integer> report) {
        for (int i = 1; i < report.size(); i++) {
            if (report.get(i) >= report.get(i - 1)) return false;
        }
        return true;
    }

    public int solve(boolean part2) {
        int safeReports = 0;
        for (List<Integer> report : reports) {
            if ((isIncreasing(report) && isValidSequence(report, true)) || 
                (isDecreasing(report) && isValidSequence(report, false))) {
                safeReports++;
                continue;
            }

            if (part2) {
                boolean foundValid = false;
                for (int i = 0; i < report.size(); i++) {
                    List<Integer> testReport = new ArrayList<>(report);
                    testReport.remove(i);
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

    public static void main(String[] args) {
        try {
            solution sol = new solution();
            System.out.println(sol.solve(false));
            System.out.println(sol.solve(true));
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }
}