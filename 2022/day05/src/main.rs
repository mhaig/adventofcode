use std::io::{self, BufRead};

enum Reading {
    Stacks,
    Moves,
}

fn get_stacks(mut crates: Vec<String>) -> Vec<Vec<char>> {
    let mut stack_index: Vec<usize> = Vec::new();
    let mut stacks: Vec<Vec<char>> = Vec::new();

    let last_line = crates.pop().unwrap();
    for (i, c) in last_line.chars().enumerate() {
        if c.is_numeric() {
            stack_index.push(i);
            stacks.push(Vec::new());
        }
    }

    for c in crates.iter().rev() {
        for (s, i) in stack_index.iter().enumerate() {
            let string_vec: Vec<char> = c.chars().collect();
            if string_vec[*i].is_alphabetic() {
                stacks[s].push(string_vec[*i]);
            }
        }
    }

    stacks
}

fn part_1_move(stacks: &mut [Vec<char>], count: i32, from: usize, to: usize) {
    for _ in 0..count {
        let temp: char = stacks[from].pop().unwrap();
        stacks[to].push(temp);
    }
}

fn part_2_move(stacks: &mut [Vec<char>], count: i32, from: usize, to: usize) {
    let mut temp: Vec<char> = Vec::new();
    for _ in 0..count {
        temp.push(stacks[from].pop().unwrap());
    }
    for c in temp.iter().rev() {
        stacks[to].push(*c);
    }
}

fn main() {
    let lines = io::stdin().lock().lines();

    // Build the stacks of crates.
    let mut crates: Vec<String> = Vec::new();
    let mut moves: Vec<String> = Vec::new();
    let mut read: Reading = Reading::Stacks;
    for l in lines {
        let line = l.unwrap();

        if line.is_empty() {
            read = Reading::Moves;
            continue;
        }

        match read {
            Reading::Stacks => crates.push(line),
            Reading::Moves => moves.push(line),
        }
    }
    let stacks: Vec<Vec<char>> = get_stacks(crates);

    let mut part_1_stacks = stacks.clone();
    let mut part_2_stacks = stacks;

    // Process the moves.
    for m in moves {
        let parts: Vec<&str> = m.split(' ').collect();
        let count: i32 = parts[1].parse().unwrap();
        let from: usize = parts[3].parse::<usize>().unwrap() - 1;
        let to: usize = parts[5].parse::<usize>().unwrap() - 1;

        part_1_move(&mut part_1_stacks, count, from, to);
        part_2_move(&mut part_2_stacks, count, from, to);
    }

    let mut part_1_solution: Vec<char> = Vec::new();
    for s in part_1_stacks {
        part_1_solution.push(*s.last().unwrap());
    }

    let mut part_2_solution: Vec<char> = Vec::new();
    for s in part_2_stacks {
        part_2_solution.push(*s.last().unwrap());
    }

    println!(
        "Part 1 Solution: {}",
        part_1_solution.iter().collect::<String>()
    );
    println!(
        "Part 2 Solution: {}",
        part_2_solution.iter().collect::<String>()
    );
}
