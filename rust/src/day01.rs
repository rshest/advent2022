extern crate kth;

use kth::SliceExtKth;

use crate::common;

pub(crate) fn solution() {
    let data = common::read_lines(&common::data_file(1)).unwrap();
    let cals: Vec<Vec<i64>> = data.into_iter().fold(Vec::new(), |mut res, x| {
        if x == "" || res.is_empty() {
            res.push(Vec::new());
        } else {
            res.last_mut().unwrap().push(x.parse().unwrap());
        }
        res
    });
    let mut sums: Vec<i64> = cals.iter().map(|x| x.iter().sum()).collect();
    let res1: i64 = *sums.iter().max().unwrap();
    let n = sums.len();
    sums.partition_by_kth(n - 3);
    let res2: i64 = sums.iter().rev().take(3).sum();
    println!("Answer 1: {}, Answer 2: {}", res1, res2);
}
