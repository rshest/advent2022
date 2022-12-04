use crate::common;
use regex::Regex;

fn parse(s: &str) -> Vec<i64> {
    lazy_static! {
        static ref REGEX: Regex = Regex::new(r"-|,").unwrap();
    }
    REGEX
        .split(s)
        .map(|val| val.parse::<i64>().unwrap())
        .collect()
}

fn contains(x: i64, y: i64, a: i64, b: i64) -> bool {
    x >= a && y <= b
}

fn overlaps(x: i64, y: i64, a: i64, b: i64) -> bool {
    (x <= b && y >= a) || (a <= y && b >= x)
}

pub(crate) fn solution() {
    let data: Vec<Vec<i64>> = common::read_lines(&common::data_file(4))
        .unwrap()
        .iter()
        .map(|s| parse(s))
        .collect();

    let res1: i64 = data
        .iter()
        .map(|s| (contains(s[0], s[1], s[2], s[3]) || contains(s[2], s[3], s[0], s[1])) as i64)
        .sum();
    let res2: i64 = data
        .iter()
        .map(|s| overlaps(s[0], s[1], s[2], s[3]) as i64)
        .sum();
    println!("Answer 1: {}, Answer 2: {}", res1, res2);
}
