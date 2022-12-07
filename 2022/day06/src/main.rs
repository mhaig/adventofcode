use std::io::{self, BufRead};

fn get_next_index(slice: &[char]) -> i32 {
    for i in 0..slice.len() {
        for j in (i + 1)..slice.len() {
            if slice[i] == slice[j] {
                return (i + 1) as i32;
            }
        }
    }

    -1
}

fn main() {
    let lines = io::stdin().lock().lines();

    for l in lines {
        let line = l.unwrap();

        let mut i: usize = 0;
        while i < line.len() {
            let window: &[char] = &line.chars().collect::<Vec<char>>()[i..(i + 4)];

            let repeat: i32 = get_next_index(window);

            if repeat != -1 {
                i += repeat as usize;
            } else {
                println!("found start of code! {}", i + 4);

                // From here find a message
                let mut j: usize = i;
                while j < line.len() - 10 {
                    let message_window: &[char] = &line.chars().collect::<Vec<char>>()[j..(j + 14)];
                    let j_repeat: i32 = get_next_index(message_window);
                    if j_repeat != -1 {
                        j += j_repeat as usize;
                    } else {
                        println!("Found start of message! {}", j + 14);
                        break;
                    }
                }
                break;
            }
        }
    }
}
