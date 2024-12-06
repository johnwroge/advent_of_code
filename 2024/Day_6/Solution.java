import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

class Point {
    int r, c;
    
    Point(int r, int c) {
        this.r = r;
        this.c = c;
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return r == point.r && c == point.c;
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(r, c);
    }
}

class State {
    int r, c;
    String dir;
    
    State(int r, int c, String dir) {
        this.r = r;
        this.c = c;
        this.dir = dir;
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        State state = (State) o;
        return r == state.r && c == state.c && dir.equals(state.dir);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(r, c, dir);
    }
}

public class Solution {
    private static String[][] createGrid(String filename) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filename));
        String[][] grid = new String[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            grid[i] = lines.get(i).split("");
        }
        return grid;
    }
    private static Point findStart(String[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j].equals("^")) return new Point(i, j);
            }
        }
        return new Point(0, 0);
    }
    
    
    public static int partOne(String[][] grid) {
        Map<Integer, Point> dyDx = new HashMap<>();
        dyDx.put(0, new Point(-1, 0));
        dyDx.put(1, new Point(0, 1));
        dyDx.put(2, new Point(1, 0));
        dyDx.put(3, new Point(0, -1));
        
        List<String> directions = Arrays.asList("^", ">", "v", "<");
        String current = "^";
        Point pos = findStart(grid);
        int r = pos.r, c = pos.c;
        Set<String> visited = new HashSet<>();
        
        while (true) {
            visited.add(r + "," + c);
            
            int idx = directions.indexOf(current);
            Point delta = dyDx.get(idx);
            int newR = r + delta.r;
            int newC = c + delta.c;
            
            if (!inBounds(newR, newC, grid)) break;
            
            if (!grid[newR][newC].equals("#")) {
                r = newR;
                c = newC;
                continue;
            }
            
            current = directions.get((idx + 1) % 4);
        }
        
        return visited.size();
    }
    
    public static int partTwo(String[][] grid) {
        Point start = findStart(grid);
        int cycles = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j].equals(".") && (i != start.r || j != start.c)) {
                    String[][] testGrid = copyGrid(grid);
                    testGrid[i][j] = "#";
                    if (simulate(testGrid, start)) cycles++;
                }
            }
        }
        return cycles;
    }
    
    private static boolean simulate(String[][] grid, Point start) {
        Map<Integer, Point> dyDx = new HashMap<>();
        dyDx.put(0, new Point(-1, 0));
        dyDx.put(1, new Point(0, 1));
        dyDx.put(2, new Point(1, 0));
        dyDx.put(3, new Point(0, -1));
        
        List<String> directions = Arrays.asList("^", ">", "v", "<");
        String current = "^";
        int r = start.r, c = start.c;
        Set<String> visited = new HashSet<>();
        
        while (true) {
            String state = r + "," + c + "," + current;
            if (visited.contains(state)) return true;
            visited.add(state);
            
            int idx = directions.indexOf(current);
            Point delta = dyDx.get(idx);
            int newR = r + delta.r;
            int newC = c + delta.c;
            
            if (!inBounds(newR, newC, grid)) return false;
            
            if (!grid[newR][newC].equals("#")) {
                r = newR;
                c = newC;
                continue;
            }
            
            current = directions.get((idx + 1) % 4);
        }
    }
    
    private static String[][] copyGrid(String[][] grid) {
        String[][] copy = new String[grid.length][];
        for (int i = 0; i < grid.length; i++) {
            copy[i] = grid[i].clone();
        }
        return copy;
    }
    
    private static boolean inBounds(int r, int c, String[][] grid) {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
    }
    
    public static void main(String[] args) throws IOException {
        String[][] grid = createGrid("data.txt");
        System.out.println("Part 1: " + partOne(grid));
        System.out.println("Part 2: " + partTwo(grid));
    }
}