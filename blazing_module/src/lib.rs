#[no_mangle]
pub extern "C" fn add(left: usize, right: usize) -> usize {
    left + right
}

#[no_mangle]
pub extern "C" fn hello(){
    println!("Hello PyCon Portugal 2023!!!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        hello();
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}

