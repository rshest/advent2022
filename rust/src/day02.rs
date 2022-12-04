use crate::common;
use std::str::FromStr;

#[derive(Debug, PartialEq, Copy, Clone)]
enum Move {
    Rock,
    Paper,
    Scissors,
}

#[derive(Debug, PartialEq, Copy, Clone)]
enum MoveOutcome {
    Win,
    Draw,
    Loss,
}

impl FromStr for Move {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "A" | "X" => Ok(Move::Rock),
            "B" | "Y" => Ok(Move::Paper),
            "C" | "Z" => Ok(Move::Scissors),
            _ => Err(()),
        }
    }
}

impl FromStr for MoveOutcome {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" => Ok(MoveOutcome::Loss),
            "Y" => Ok(MoveOutcome::Draw),
            "Z" => Ok(MoveOutcome::Win),
            _ => Err(()),
        }
    }
}

impl Move {
    fn score(&self) -> i64 {
        match self {
            Self::Rock => 1,
            Self::Paper => 2,
            Self::Scissors => 3,
        }
    }
}

impl MoveOutcome {
    fn score(&self) -> i64 {
        match self {
            Self::Win => 6,
            Self::Draw => 3,
            Self::Loss => 0,
        }
    }
}

fn beats(m1: &Move, m2: &Move) -> bool {
    match (m1, m2) {
        (Move::Rock, Move::Scissors)
        | (Move::Paper, Move::Rock)
        | (Move::Scissors, Move::Paper) => true,
        _ => false,
    }
}

fn get_outcome(m1: &Move, m2: &Move) -> MoveOutcome {
    if m1 == m2 {
        return MoveOutcome::Draw;
    } else if beats(m1, m2) {
        return MoveOutcome::Win;
    } else {
        return MoveOutcome::Loss;
    }
}

fn get_move_for_outcome(m: &Move, outcome: &MoveOutcome) -> Move {
    match outcome {
        MoveOutcome::Draw => *m,
        MoveOutcome::Win => match m {
            Move::Rock => Move::Paper,
            Move::Paper => Move::Scissors,
            Move::Scissors => Move::Rock,
        },
        MoveOutcome::Loss => match m {
            Move::Rock => Move::Scissors,
            Move::Paper => Move::Rock,
            Move::Scissors => Move::Paper,
        },
    }
}

pub(crate) fn solution() {
    let data = common::read_lines(&common::data_file(2)).unwrap();
    let moves: Vec<Vec<&str>> = data.iter().map(|line| line.split(" ").collect()).collect();

    let moves1: Vec<(Move, Move)> = moves
        .iter()
        .map(|s| (s[0].parse().unwrap(), s[1].parse().unwrap()))
        .collect();
    let moves2: Vec<(Move, MoveOutcome)> = moves
        .iter()
        .map(|s| (s[0].parse().unwrap(), s[1].parse().unwrap()))
        .collect();

    let res1: i64 = moves1
        .iter()
        .map(|(m1, m2)| m2.score() + get_outcome(m2, m1).score())
        .sum();

    let res2: i64 = moves2
        .iter()
        .map(|(m, r)| r.score() + get_move_for_outcome(m, r).score())
        .sum();

    println!("Answer 1: {}, Answer 2: {:?}", res1, res2);
}
