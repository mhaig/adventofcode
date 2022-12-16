extern crate pathfinding;

use pathfinding::prelude::bfs;
use std::collections::HashMap;
use std::hash::Hash;
use std::io::{self, BufRead};

#[derive(Clone, Copy, Debug, Default, Eq, Hash, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}
impl Point {
    fn neighbors(&self) -> Vec<Point> {
        let mut ret: Vec<Point> = Vec::new();
        for i in [-1, 1] {
            ret.push(Point {
                x: self.x + i,
                y: self.y,
            });
            ret.push(Point {
                x: self.x,
                y: self.y + i,
            });
        }
        ret
    }
}

fn get_successors(heightmap: &HashMap<Point, char>, position: &Point) -> Vec<Point> {
    let mut successors: Vec<Point> = Vec::new();
    let current_height: i32 = heightmap[position] as i32;

    for p in position.neighbors() {
        if heightmap.contains_key(&p) {
            let neighbor_height = heightmap[&p] as i32;

            if neighbor_height <= current_height || neighbor_height - current_height == 1 {
                successors.push(p);
            }
        }
    }

    successors
}

fn main() {
    let mut heightmap: HashMap<Point, char> = HashMap::new();
    let mut start: Point = Default::default();
    let mut starts: Vec<Point> = Vec::new();
    let mut goal: Point = Default::default();

    let lines = io::stdin().lock().lines();
    for (y, l) in lines.enumerate() {
        let line: Vec<char> = l.unwrap().chars().collect();
        for (x, c) in line.iter().enumerate() {
            heightmap.insert(
                Point {
                    x: x as i32,
                    y: y as i32,
                },
                *c,
            );
            if *c == 'S' {
                start.x = x as i32;
                start.y = y as i32;
                heightmap.insert(start, 'a');
                println!("Found start (S) at {:?}", start);
            }
            if *c == 'a' {
                starts.push(Point {
                    x: x as i32,
                    y: y as i32,
                });
            }
            if *c == 'E' {
                goal.x = x as i32;
                goal.y = y as i32;
                heightmap.insert(goal, 'z');
                println!("Found end (E) at {:?}", goal);
            }
        }
    }

    let mut results: Vec<usize> = Vec::new();
    let result = bfs(&start, |p| get_successors(&heightmap, p), |p| *p == goal);
    let result = result.expect("No path found!");
    results.push(result.len() - 1);
    for s in starts {
        let result = bfs(&s, |p| get_successors(&heightmap, p), |p| *p == goal);
        match result {
            None => (),
            Some(result) => results.push(result.len() - 1),
        }
    }
    println!("Part 1 Solution {}", results[0]);
    results.sort();
    println!("Part 2 Solution {:?}", results[0]);
}
