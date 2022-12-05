use std::collections::HashMap;
use std::io::{self, BufRead};

// them:
//   A -> Rock
//   B -> Paper
//   C -> Scissors
// us:
//   X -> Rock
//   Y -> Paper
//   Z -> Scissors
fn resolve_and_score(them: char, expect: char) -> u32 {
    let win = HashMap::from([('A', 'Y'), ('B', 'Z'), ('C', 'X')]);

    let draw = HashMap::from([('A', 'X'), ('B', 'Y'), ('C', 'Z')]);

    let lose = HashMap::from([('A', 'Z'), ('B', 'X'), ('C', 'Y')]);

    let r = match expect {
        'X' => lose,
        'Y' => draw,
        'Z' => win,
        _ => HashMap::new(),
    };

    score_round(them, r[&them])
}

// them:
//   A -> Rock
//   B -> Paper
//   C -> Scissors
// us:
//   X -> Rock
//   Y -> Paper
//   Z -> Scissors
fn us_win(them: char, us: char) -> bool {
    match them {
        'A' if us == 'Y' => true,
        'B' if us == 'Z' => true,
        'C' if us == 'X' => true,
        _ => false,
    }
}

fn score_round(them: char, us: char) -> u32 {
    let them_scores = HashMap::from([('A', 1), ('B', 2), ('C', 3)]);

    let us_scores = HashMap::from([('X', 1), ('Y', 2), ('Z', 3)]);

    if us_scores[&us] == them_scores[&them] {
        us_scores[&us] + 3
    } else if us_win(them, us) {
        us_scores[&us] + 6
    } else {
        us_scores[&us]
    }
}

fn main() {
    let lines = io::stdin().lock().lines();

    let mut part_1_score: u32 = 0;
    let mut part_2_score: u32 = 0;

    for line in lines {
        let last_input = line.unwrap();

        if !last_input.is_empty() {
            let them: char = last_input.chars().next().unwrap();
            let us: char = last_input.chars().nth_back(0).unwrap();
            part_1_score += score_round(them, us);
            part_2_score += resolve_and_score(them, us);
        }
    }

    println!("Part 1 score: {part_1_score}");
    println!("Part 2 score: {part_2_score}")
}
