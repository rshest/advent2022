// DAY05
use crate::common;
use std::str::FromStr;

#[derive(Debug, PartialEq, Copy, Clone)]
struct CratesMove {
    src: usize,
    dst: usize,
    num: usize,
}

impl FromStr for CratesMove {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let parts: Vec<&str> = s.split(" ").collect();
        Ok(CratesMove {
            src: parts[3].parse()?,
            dst: parts[5].parse()?,
            num: parts[1].parse()?,
        })
    }
}

#[derive(Debug, PartialEq, Clone)]
struct CratesField {
    crates: Vec<Vec<char>>,
    tops: Vec<usize>,
}

impl CratesField {
    fn apply_move(&mut self, mv: &CratesMove, reverse: bool) {
        let src = mv.src - 1;
        let dst = mv.dst - 1;
        let w = self.crates[0].len();
        let ts = self.tops[src];
        let td = self.tops[dst];
        for i in 0..mv.num {
            let ps = ts - i - 1;
            let pd = if reverse { td + i } else { td + mv.num - i - 1 };
            while self.crates.len() <= pd {
                self.crates.push(vec![' '; w]);
            }
            self.crates[pd][dst] = self.crates[ps][src];
            self.crates[ps][src] = ' ';
        }
        self.tops[src] -= mv.num;
        self.tops[dst] += mv.num;
    }

    fn get_top(self) -> String {
        self.tops
            .iter()
            .enumerate()
            .map(|(i, t)| self.crates[t - 1][i])
            .collect()
    }
}

fn parse_crates(lines: &Vec<&str>) -> CratesField {
    let h = lines.len() - 1;
    let w = (lines[0].len() + 1) / 4;
    let mut crates = vec![vec![' '; w]; h];
    let mut tops = vec![0; w];
    for j in 0..h {
        let line: Vec<_> = lines[j].chars().collect();
        for i in 0..w {
            let c = line[1 + i * 4];
            crates[j][i] = c;
            if c == ' ' {
                tops[i] += 1;
            }
        }
    }
    crates.reverse();
    for i in 0..w {
        tops[i] = h - tops[i];
    }
    CratesField {
        crates: crates,
        tops: tops,
    }
}
pub(crate) fn solution() {
    let data = common::read_string(&common::data_file(5)).unwrap();
    let parts: Vec<Vec<&str>> = data
        .split("\n\n")
        .map(|s| s.split("\n").collect())
        .collect();
    let moves: Vec<CratesMove> = parts[1].iter().map(|s| s.parse().unwrap()).collect();

    let mut field1 = parse_crates(&parts[0]);
    let mut field2 = field1.clone();

    for mv in &moves {
        field1.apply_move(mv, true);
    }
    let res1 = &field1.get_top();

    for mv in &moves {
        field2.apply_move(mv, false);
    }
    let res2 = &field2.get_top();
    println!("Answer 1: {}, Answer 2: {}", res1, res2);
}
