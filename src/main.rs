use std::fs;

fn main() {
    let file_path = "slides.md";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file. Are you in the right directory?");

    get_presenter_notes
}

fn get_presenter_notes () -> Vec<str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains("<!--") {
            results.push(line);
        }
    }

    results
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn inline_presenter_note() {
        let contents = "\
foo bar
bar foo
<!--Read this!-->
bla blue";

        assert_eq!(vec!["Read this!"], get_presenter_notes());
    }
}