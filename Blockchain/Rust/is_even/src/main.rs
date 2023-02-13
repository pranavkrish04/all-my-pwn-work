fn main(){
    println!("{}", is_even(2));
    //array
    let arr = [0,1,2,3,4,5,6]; // length is known
    //slice
    let slice = &arr[1..3]; // length is not know at compile time/
    //string
    let str: &str = "Hello world";
    let string: String = String::from("Hello world");
    // for loop
    for i in 1..10{
        println!("{}", i);
    }
    //making a struct
    let birdie = Bird{name: string, attack: 5};
    birdie.print_name();
}

//define a struct
struct Bird{
    name: String,
    attack: u8
}

//implement methods for the struct
impl Bird{
    fn print_name(&self){
        println!("{}", self.name);
    }
}

//function
pub fn is_even(num: u8) -> bool{
    let digit: u8 = num%2;
    digit == 0
}

/*
functions and variables:
- by default functions are private.
- by default all the variables are immutable and cant be changed.
*/
