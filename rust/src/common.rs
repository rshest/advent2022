use std::fs;
use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind};

pub fn read_string(path: &str) -> Result<String, Error> {
    let data = fs::read_to_string(path)?;
    Ok(data)
}

pub fn read_lines(path: &str) -> Result<Vec<String>, Error> {
    let file = File::open(path)?;
    BufReader::new(file).lines().collect()
}

#[allow(dead_code)]
pub fn read_integers(path: &str) -> Result<Vec<i64>, Error> {
    let mut v = Vec::new();
    for line in read_lines(path)? {
        let n = line
            .trim()
            .parse()
            .map_err(|e| Error::new(ErrorKind::InvalidData, e))?;
        v.push(n);
    }
    Ok(v)
}

const DATA_ROOT: &str = "../data/";

pub fn data_file(problem_id: u32) -> String {
    format!("{}/{:02}.txt", DATA_ROOT, problem_id)
}

#[allow(dead_code)]
pub fn test_file(problem_id: u32, test_id: u32) -> String {
    format!("{}/{:02}t{}.txt", DATA_ROOT, problem_id, test_id)
}
