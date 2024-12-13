package me.voidxwalker.autoreset;

import java.io.*;
import java.nio.file.Files;
import java.util.*;

public class Main {
    public static Board board;
    public static Map<Character, List<Point>> antennas = new HashMap<>();

    public static void main(String... args) throws IOException {
        List<String> lines = Files.readAllLines(new File("input").toPath());
        board = new Board( lines.get(0).trim().length(), lines.size());
        for (int y = 0; y < lines.size(); y++) {
            String line = lines.get(y).trim();
            for (int x = 0; x < line.length(); x++) {
                char antenna = line.charAt(x);
                board.putAt(x, y, antenna);
                if (antenna == '.') {
                    continue;
                }
                List<Point> locations = antennas.get(antenna);
                if (locations == null) {
                    locations = new ArrayList<>();
                    antennas.put(antenna, locations);
                }
                locations.add(new Point(x, y));
            }
        }

        List<Point> antinodes = new ArrayList<>();
        for (List<Point> locations : antennas.values()) {
            for (Point first : locations) {
                for (Point second : locations) {
                    if (first.equals(second)) {
                        continue;
                    }
                    Point antinode = first.getAntinode(second);
                    if (!board.inBounds(antinode)) {
                        continue;
                    }
                    if (antinodes.contains(antinode)) {
                        continue;
                    }
                    antinodes.add(antinode);
                }
            }
        }

        System.out.println(antinodes.size());
    }

    public static class Board {
        public int sizeX;
        public int sizeY;
        public char[][] board;

        public Board(int sizeX, int sizeY) {
            this.sizeX = sizeX;
            this.sizeY = sizeY;
            board = new char[sizeY][sizeX];
        }

        public int getSizeX() {
            return sizeX;
        }

        public int getSizeY() {
            return sizeY;
        }

        public char getAt(int x, int y) {
            return board[y][x];
        }

        public void putAt(int x, int y, char antenna) {
            board[y][x] = antenna;
        }

        public boolean inBounds(Point point) {
            return point.getX() >= 0 && point.getY() >= 0 && point.getX() < this.getSizeX() && point.getY() < this.getSizeY();
        }
    }

    public static class Point {
        private final int x;
        private final int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public Point getAntinode(Point other) {
            int diffX = this.getX() - other.getX();
            int diffY = this.getY() - other.getY();
            return new Point(this.getX() + diffX, this.getY() + diffY);
        }

        @Override
        public boolean equals(Object other) {
            Point point = (Point) other;
            return x == point.x && y == point.y;
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }
}
