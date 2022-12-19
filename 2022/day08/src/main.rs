use std::{
    collections::HashMap,
    io::{self, BufRead},
};

#[derive(Clone, Copy, Debug, Default, Eq, Hash, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

fn is_first_same_height(a: &u8, height: u8, first_match: &mut bool) -> bool {
    if *first_match {
        return false;
    }
    if *a >= height {
        *first_match = true;
    }
    true
}

fn main() {
    let mut tree_map: HashMap<Point, u8> = HashMap::new();
    let mut max_x: i32 = 0;
    let mut max_y: i32 = 0;

    let lines = io::stdin().lock().lines();
    for (y, l) in lines.enumerate() {
        let line: Vec<char> = l.unwrap().chars().collect();
        max_x = line.len() as i32;
        for (x, c) in line.iter().enumerate() {
            tree_map.insert(
                Point {
                    x: x as i32,
                    y: y as i32,
                },
                c.to_digit(10).unwrap() as u8,
            );
        }
        max_y = (y as i32) + 1;
    }

    let mut visible: i32 = 0;
    // Count the sides first.
    visible += max_x * 2;
    visible += (max_y - 2) * 2;

    // Iterate through the interior to see if tree is visible.
    for x in 1..(max_x - 1) {
        for y in 1..(max_y - 1) {
            // From this point, check the row to see if visible.
            let height = tree_map[&Point { x, y }];
            let mut left = (0..x)
                .map(|r| Point { x: r, y })
                .filter(|p| tree_map[p] >= height);
            let mut right = ((x + 1)..max_x)
                .map(|r| Point { x: r, y })
                .filter(|p| tree_map[p] >= height);

            let mut up = (0..y)
                .map(|c| Point { x, y: c })
                .filter(|p| tree_map[p] >= height);
            let mut down = ((y + 1)..max_y)
                .map(|c| Point { x, y: c })
                .filter(|p| tree_map[p] >= height);

            if left.next().is_none()
                || right.next().is_none()
                || up.next().is_none()
                || down.next().is_none()
            {
                visible += 1;
            }
        }
    }

    println!("Part 1 Solution: {visible}");

    let mut max_score = 0;
    // Iterate through the interior to see if tree is visible.
    for x in 1..(max_x - 1) {
        for y in 1..(max_y - 1) {
            // From this point, check the row to see if visible.
            let height = tree_map[&Point { x, y }];
            let mut first_match: bool = false;

            let left: Vec<u8> = (0..x)
                .rev()
                .map(|r| tree_map[&Point { x: r, y }])
                .filter(|h| is_first_same_height(h, height, &mut first_match))
                .collect();
            first_match = false;
            let right: Vec<u8> = ((x + 1)..max_x)
                .map(|r| tree_map[&Point { x: r, y }])
                .filter(|h| is_first_same_height(h, height, &mut first_match))
                .collect();

            first_match = false;
            let up: Vec<u8> = (0..y)
                .rev()
                .map(|c| tree_map[&Point { x, y: c }])
                .filter(|h| is_first_same_height(h, height, &mut first_match))
                .collect();
            first_match = false;
            let down: Vec<u8> = ((y + 1)..max_y)
                .map(|c| tree_map[&Point { x, y: c }])
                .filter(|h| is_first_same_height(h, height, &mut first_match))
                .collect();

            let score = left.len() * right.len() * up.len() * down.len();
            if score > max_score {
                max_score = score;
            }
        }
    }

    println!("Part 2 Solution: {max_score}");
}
