use std::io::{self, BufRead};

#[derive(Debug)]
struct Elf {
    id: u32,
    calories: i32,
}

fn main() -> io::Result<()> {
    let lines = io::stdin().lock().lines();

    let mut elfs: Vec<Elf> = Vec::new();

    let mut id: u32 = 1;
    let mut current_id: u32 = u32::MAX;
    for line in lines {
        let last_input = line.unwrap();

        if id != current_id {
            elfs.push(Elf { id, calories: 0 });
            current_id = id;
        }

        if !last_input.is_empty() {
            let cals: i32 = last_input.parse().unwrap();

            if let Some(e) = elfs.last_mut() {
                e.calories += cals;
            }
        } else {
            id += 1;
        }
    }

    // Sort the elves by calories.
    elfs.sort_unstable_by(|a, b| b.calories.cmp(&a.calories));

    if let Some(elf) = elfs.first() {
        let max_calories = elf.calories;
        let id = elf.id;
        println!("Elf carrying the most calories: {id}, {max_calories} cals");
    } else {
        println!("Program didn't work!");
    }

    let mut top_three_cals = 0;
    for e in &elfs[0..3] {
        top_three_cals += e.calories;
    }
    println!("Top three elfs are carying {top_three_cals} cals");

    Ok(())
}
