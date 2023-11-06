# Rust Examples

This file contains some examples of Rust code.

## Enum

- The following example defines an enum, and converts enum variants into str names and parses strings into enum variants
- To iterate over the variants of an enum, use [`strum` crate](https://docs.rs/strum_macros/0.25.2/strum_macros/derive.EnumIter.html)

```rs
use core::str::FromStr;

#[derive(Debug, PartialEq, Eq)]
enum Fruit {
    Apple = 0,
    Banana = 1,
    Cherry = 2,
    DragonFruit = 3,
}

impl Fruit {
    // String value of the enum field names
    pub fn as_str_name(&self) -> &'static str {
        match self {
            Self::Apple => "apple",
            Self::Banana => "banana",
            Self::Cherry => "cherry",
            Self::DragonFruit => "dragon fruit",
        }
    }
}

impl FromStr for Fruit {
    type Err = String;

    // Creates an enum from field names
    fn from_str(fruit: &str) -> Result<Self, Self::Err> {
        match fruit {
            "apple" => Ok(Self::Apple),
            "banana" => Ok(Self::Banana),
            "cherry" => Ok(Self::Cherry),
            "dragon fruit" => Ok(Self::DragonFruit),
            _ => Err(format!(
                "{fruit} is not in the list!"
            )
            .to_string()),
        }
    }
}

fn main() {
    assert_eq!(Fruit::Apple.as_str_name(), "apple");
    assert_eq!(Fruit::DragonFruit.as_str_name(), "dragon fruit");

    if let Ok(cherry) = "ChErrY".to_string().to_lowercase().parse::<Fruit>() {
        assert_eq!(cherry, Fruit::Cherry);
    }
    if let Err(error_msg) = "random fruit".to_string().to_lowercase().parse::<Fruit>() {
        assert_eq!(error_msg, format!("random fruit is not in the list!").to_string());
    }

    println!("Success!");
}
```

[Demo](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=ac45c4a807a0a9226a81be5c1c5a278c)

## Pattern Matching with `@`

```rs
struct SystemError {
   code: u8,
   msg: String,
}

struct Id(u8);

enum Error {
    System(SystemError),
    NotFound(Id),
}

fn process_error(e: Error) {
    match e {
        x @ Error::NotFound(_) => {
            // `x` is the outer error but only if the inner one is `NotFound`
            let _y: Error = x;
        }
        Error::System(x @ SystemError{code: 42, ..}) => {
            // `x` is system error but only for code 42
            let _y: SystemError = x;
        }
        Error::System(SystemError{code: 10, msg}) => {
            // extract message for system error w/ code 10
            let _y: String = msg;
        }
        Error::System(SystemError{code: 11, msg: x}) => {
            // similar to the one above but we rename `msg` to `x`
            let _y: String = x;
        }
        _ => {}
    }
}
```

[Demo](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=d4fb61e604aa5e4f6b153461a7d27c10)
