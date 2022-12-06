// DAY06
use crate::common;
use std::collections::HashMap;

fn get_unique_substring_pos(stream: &str, n: usize) -> usize {
    let mut counts: HashMap<char, usize> = HashMap::new();
    let chars: Vec<char> = stream.chars().collect();
    for (i, c) in chars.iter().enumerate() {
        *counts.entry(*c).or_insert(0) += 1;
        if i >= n {
            let cprev = chars[i - n];
            let cnt = counts[&cprev] - 1;
            if cnt == 0 {
                counts.remove(&cprev);
            } else {
                counts.insert(cprev, cnt);
            }
        }
        if counts.len() == n {
            return i + 1;
        }
    }
    chars.len()
}

pub(crate) fn solution() {
    let stream = common::read_string(&common::data_file(6)).unwrap();
    let res1 = get_unique_substring_pos(&stream, 4);
    let res2 = get_unique_substring_pos(&stream, 14);
    println!("Answer 1: {}, Answer 2: {}", res1, res2);
}
