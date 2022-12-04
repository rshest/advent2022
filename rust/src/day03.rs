use crate::common;
use std::collections::HashSet;

fn halve(s: &str) -> (&str, &str) {
    let n = s.len() / 2;
    (&s[..n], &s[n..])
}

fn get_priority(c: char) -> i64 {
    let n = c as i64;
    if n >= 'a' as i64 && n <= 'z' as i64 {
        n - ('a' as i64) + 1
    } else if n >= 'A' as i64 && n <= 'Z' as i64 {
        n - ('A' as i64) + 27
    } else {
        0
    }
}

fn get_matching(a: &str, b: &str) -> String {
    let ach: HashSet<char> = a.chars().collect();
    let bch: HashSet<char> = b.chars().collect();
    ach.intersection(&bch).collect()
}

fn get_matching3(a: &str, b: &str, c: &str) -> String {
    get_matching(a, &get_matching(b, c))
}

pub(crate) fn solution() {
    let data = common::read_lines(&common::data_file(3)).unwrap();
    let halves: Vec<(&str, &str)> = data.iter().map(|s| halve(s)).collect();
    let res1: i64 = halves
        .iter()
        .map(|(a, b)| {
            get_matching(a, b)
                .chars()
                .map(|c| get_priority(c))
                .sum::<i64>()
        })
        .sum();
    let res2: i64 = data
        .chunks(3)
        .map(|s| {
            get_matching3(&s[0], &s[1], &s[2])
                .chars()
                .map(|c| get_priority(c))
                .sum::<i64>()
        })
        .sum();
    println!("Answer 1: {:?}, Answer 2: {:?}", res1, res2);
}
