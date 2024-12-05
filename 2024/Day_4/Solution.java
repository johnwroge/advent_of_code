import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    private static class Position {
        int row, col;

        Position(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    private static class Match {
        String direction;
        Position pos;

        Match(String direction, Position pos) {
            this.direction = direction;
            this.pos = pos;
        }
    }

    private static class Intersection {
        String dir1, dir2;
        Position pos1, pos2;

        Intersection(String dir1, String dir2, Position pos1, Position pos2) {
            this.dir1 = dir1;
            this.dir2 = dir2;
            this.pos1 = pos1;
            this.pos2 = pos2;
        }
    }

    private static String[][] readGrid(String filename) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filename));
        String[][] grid = new String[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            grid[i] = lines.get(i).split("");
        }
        return grid;
    }

    public static int partOne(String[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        List<Match> matches = new ArrayList<>();
        String target = "XMAS";

        // Horizontal right
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols - 3; col++) {
                StringBuilder sequence = new StringBuilder();
                for (int i = 0; i < 4; i++) {
                    sequence.append(grid[row][col + i]);
                }
                if (sequence.toString().equals(target)) {
                    matches.add(new Match("horizontal-right", new Position(row, col)));
                }
            }
        }

        // Horizontal left
        for (int row = 0; row < rows; row++) {
            for (int col = 3; col < cols; col++) {
                StringBuilder sequence = new StringBuilder();
                for (int i = 0; i < 4; i++) {
                    sequence.append(grid[row][col - i]);
                }
                if (sequence.toString().equals(target)) {
                    matches.add(new Match("horizontal-left", new Position(row, col)));
                }
            }
        }

        // Vertical down
        for (int row = 0; row < rows - 3; row++) {
            for (int col = 0; col < cols; col++) {
                StringBuilder sequence = new StringBuilder();
                for (int i = 0; i < 4; i++) {
                    sequence.append(grid[row + i][col]);
                }
                if (sequence.toString().equals(target)) {
                    matches.add(new Match("vertical-down", new Position(row, col)));
                }
            }
        }

        // Vertical up
        for (int row = 3; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                StringBuilder sequence = new StringBuilder();
                for (int i = 0; i < 4; i++) {
                    sequence.append(grid[row - i][col]);
                }
                if (sequence.toString().equals(target)) {
                    matches.add(new Match("vertical-up", new Position(row, col)));
                }
            }
        }

        // Diagonal directions
        int[][] directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        String[] directionNames = {"down-right", "down-left", "up-right", "up-left"};

        for (int dirIdx = 0; dirIdx < directions.length; dirIdx++) {
            int[] dir = directions[dirIdx];
            int startRow = dir[0] < 0 ? 3 : 0;
            int endRow = dir[0] < 0 ? rows : rows - 3;
            int startCol = dir[1] < 0 ? 3 : 0;
            int endCol = dir[1] < 0 ? cols : cols - 3;

            for (int row = startRow; row < endRow; row++) {
                for (int col = startCol; col < endCol; col++) {
                    StringBuilder sequence = new StringBuilder();
                    for (int i = 0; i < 4; i++) {
                        sequence.append(grid[row + i * dir[0]][col + i * dir[1]]);
                    }
                    if (sequence.toString().equals(target)) {
                        matches.add(new Match(directionNames[dirIdx], new Position(row, col)));
                    }
                }
            }
        }

        return matches.size();
    }

    public static int partTwo(String[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        List<Match> allMas = new ArrayList<>();

        // Check for diagonal MAS patterns
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                // down-right
                if (row < rows - 2 && col < cols - 2) {
                    if (grid[row][col].equals("M") &&
                        grid[row + 1][col + 1].equals("A") &&
                        grid[row + 2][col + 2].equals("S")) {
                        allMas.add(new Match("down-right", new Position(row, col)));
                    }
                }

                // down-left
                if (row < rows - 2 && col >= 2) {
                    if (grid[row][col].equals("M") &&
                        grid[row + 1][col - 1].equals("A") &&
                        grid[row + 2][col - 2].equals("S")) {
                        allMas.add(new Match("down-left", new Position(row, col)));
                    }
                }

                // up-right
                if (row >= 2 && col < cols - 2) {
                    if (grid[row][col].equals("M") &&
                        grid[row - 1][col + 1].equals("A") &&
                        grid[row - 2][col + 2].equals("S")) {
                        allMas.add(new Match("up-right", new Position(row, col)));
                    }
                }

                // up-left
                if (row >= 2 && col >= 2) {
                    if (grid[row][col].equals("M") &&
                        grid[row - 1][col - 1].equals("A") &&
                        grid[row - 2][col - 2].equals("S")) {
                        allMas.add(new Match("up-left", new Position(row, col)));
                    }
                }
            }
        }

        List<Intersection> intersections = new ArrayList<>();

        // Find intersections
        for (int i = 0; i < allMas.size(); i++) {
            for (int j = i + 1; j < allMas.size(); j++) {
                Match m1 = allMas.get(i);
                Match m2 = allMas.get(j);

                int a1Row, a1Col, a2Row, a2Col;

                switch (m1.direction) {
                    case "down-right":
                        a1Row = m1.pos.row + 1;
                        a1Col = m1.pos.col + 1;
                        break;
                    case "down-left":
                        a1Row = m1.pos.row + 1;
                        a1Col = m1.pos.col - 1;
                        break;
                    case "up-right":
                        a1Row = m1.pos.row - 1;
                        a1Col = m1.pos.col + 1;
                        break;
                    default: // up-left
                        a1Row = m1.pos.row - 1;
                        a1Col = m1.pos.col - 1;
                        break;
                }

                switch (m2.direction) {
                    case "down-right":
                        a2Row = m2.pos.row + 1;
                        a2Col = m2.pos.col + 1;
                        break;
                    case "down-left":
                        a2Row = m2.pos.row + 1;
                        a2Col = m2.pos.col - 1;
                        break;
                    case "up-right":
                        a2Row = m2.pos.row - 1;
                        a2Col = m2.pos.col + 1;
                        break;
                    default: // up-left
                        a2Row = m2.pos.row - 1;
                        a2Col = m2.pos.col - 1;
                        break;
                }

                if (a1Row == a2Row && a1Col == a2Col) {
                    intersections.add(new Intersection(
                        m1.direction, m2.direction, m1.pos, m2.pos));
                }
            }
        }

        return intersections.size();
    }

    public static void main(String[] args) {
        try {
            String[][] grid = readGrid("data.txt");
            System.out.println(partOne(grid));
            System.out.println(partTwo(grid));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}