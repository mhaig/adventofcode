use std::{io::{self, BufRead}, collections::HashMap};

fn score(a: char) -> u32 {
    match a {
        'A'..='Z' => a as u32 - 'A' as u32 + 27,
        'a'..='z' => a as u32 - 'a' as u32 + 1,
        _ => 0,
    }
}

fn main() {
    let mut lines = io::stdin().lock().lines();

    let mut priority: u32 = 0;
    let mut badge: u32 = 0;
    let mut group_count: u32 = 0;
    let mut badge_map: HashMap<char, i32> = HashMap::new();
    while let Some(line) = lines.next() {
        let last_input = line.unwrap();

        if last_input.len() > 0 {
            let compartment_1 = &last_input[0..last_input.len()/2];
            let compartment_2 = &last_input[last_input.len()/2..];

            let mut compartment_1_items: HashMap<char, i32> = HashMap::new();
            for c in compartment_1.chars() {
                compartment_1_items.insert(c, 0);
            }

            let mut compartment_2_items: HashMap<char, i32> = HashMap::new();
            let mut scored: bool = false;
            for c in compartment_2.chars() {
                if compartment_1_items.contains_key(&c) && !scored {
                    priority += score(c);
                    scored = true;
                }

                compartment_2_items.insert(c, 0);
            }

            if badge_map.len() == 0 {
                badge_map.extend(compartment_1_items);
                badge_map.extend(compartment_2_items);
            }
            else {
                for (k, _) in compartment_1_items.iter() {
                    badge_map.entry(*k).and_modify(|f| { *f += 1 });
                }
                for (k, _) in compartment_2_items.iter() {
                    badge_map.entry(*k).and_modify(|f| { *f += 1 });
                }
            }

            if group_count == 2 {
                // Find the badge.
                for (k, v) in badge_map.iter() {
                    if *v == 2 {
                        badge += score(*k);
                    }
                }
                group_count = 0;
                badge_map = HashMap::new();
            }
            else {
                group_count += 1;
            }
        }
    }

    println!("Sum of repeat item priorities: {priority}");
    println!("Sum of badge item priorities: {badge}");
}
