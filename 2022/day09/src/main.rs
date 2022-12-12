use std::collections::HashMap;
use std::io::{self, BufRead};

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

fn print_grid(head: &Point, tail: &Point) {
    let mut grid: String = "".to_string();
    for i in (0..6).rev() {
        for j in 0..6 {
            if head.x == j && head.y == i {
                grid += "H";
            } else if tail.x == j && tail.y == i {
                grid += "T";
            } else {
                grid += ".";
            }
        }
        grid += "\n";
    }
    println!("{}", grid);
}

fn need_to_move_tail(head: Point, tail: Point) -> bool {
    let x = (head.x - tail.x).pow(2);
    let y = (head.y - tail.y).pow(2);

    if ((x + y) as f32).sqrt() >= 2.0 {
        return true;
    }

    false
}

fn move_one(direction: char, point: &mut Point) {
    match direction {
        'U' => {
            point.y += 1;
        }
        'D' => {
            point.y -= 1;
        }
        'L' => {
            point.x -= 1;
        }
        'R' => {
            point.x += 1;
        }
        _ => println!("Bad input!"),
    }
}

fn follow_one(head: Point, next: &mut Point) {
    if need_to_move_tail(head, *next) {
        let diff_x = head.x - next.x;
        let diff_y = head.y - next.y;

        println!("{} {}", (diff_x as f32 / 2.0), (diff_x as f32 / 2.0).ceil());
        println!("{} {}", (diff_y as f32 / 2.0), (diff_y as f32 / 2.0).ceil());

        next.x += match diff_x {
            diff_x if diff_x >= 0 => (diff_x as f32 / 2.0).ceil() as i32,
            diff_x if diff_x < 0 => (diff_x as f32 / 2.0).floor() as i32,
            _ => todo!(),
        };
        next.y += match diff_y {
            diff_y if diff_y >= 0 => (diff_y as f32 / 2.0).ceil() as i32,
            diff_y if diff_y < 0 => (diff_y as f32 / 2.0).floor() as i32,
            _ => todo!(),
        };
    }
}

fn main() {
    let lines = io::stdin().lock().lines();

    let mut visited: HashMap<Point, i32> = HashMap::new();
    let mut head: Point = Point { x: 0, y: 0 };
    let mut tail: Point = Point { x: 0, y: 0 };

    for l in lines {
        let line = l.unwrap();
        let parts: Vec<&str> = line.split(' ').collect();
        let direction: &str = parts[0];
        let steps: u32 = parts[1].parse::<u32>().unwrap();

        println!("Move {direction} {steps}");
        for _ in 0..steps {
            move_one(direction.chars().next().unwrap(), &mut head);
            println!("Head: {:?}", head);
            follow_one(head, &mut tail);
            println!("Tail: {:?}", tail);

            visited.insert(tail, 0);
            print_grid(&head, &tail);
            println!();
        }
    }
    println!("Head: {:?}", head);
    println!("Tail: {:?}", tail);

    println!("Part 1 Solution: {}", visited.len());
}
