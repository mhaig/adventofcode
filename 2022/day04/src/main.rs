use std::io::{self, BufRead};

fn main() {
    let lines = io::stdin().lock().lines();

    let mut fully_contains: u32 = 0;
    let mut overlaps: u32 = 0;
    for line in lines {
        let l = line.unwrap();

        if !l.is_empty() {
            let l_parts: Vec<&str> = l.split(",").collect();
            let elf_1 = l_parts[0];
            let elf_2 = l_parts[1];
            let elf_1_start: u32 = elf_1.split("-").collect::<Vec<&str>>()[0].parse().unwrap();
            let elf_1_end: u32 = elf_1.split("-").collect::<Vec<&str>>()[1].parse().unwrap();
            let elf_2_start: u32 = elf_2.split("-").collect::<Vec<&str>>()[0].parse().unwrap();
            let elf_2_end: u32 = elf_2.split("-").collect::<Vec<&str>>()[1].parse().unwrap();

            if elf_1_start >= elf_2_start && elf_1_end <= elf_2_end {
                fully_contains += 1;
            } else if elf_2_start >= elf_1_start && elf_2_end <= elf_1_end {
                fully_contains += 1;
            }

            if elf_2_start <= elf_1_start && elf_1_start >= elf_2_start {
                if elf_1_start <= elf_2_end {
                    overlaps +=1;
                }
            } else if elf_1_start <= elf_2_start && elf_2_start >= elf_1_start {
                if elf_2_start <= elf_1_end {
                    overlaps += 1;
                }
            }
        }
    }

    println!("Fully contains: {fully_contains}");
    println!("Overlapping: {overlaps}");
}
