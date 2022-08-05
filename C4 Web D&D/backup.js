//DATA TYPES

//'let' is the keyword to make a variable
//'name' is the variable's name
//'Lucas' is my data type associated with my variable name
let name = "Lucas";
console.log(name);

//Strings (words)
//All strings have quotation marks
let bookTitle = "The Hobbit";
console.log(bookTitle);

//Numbers
let age = 20;
console.log(age);
let old = age + 10;
console.log(old);

//Booleans (true or false variables)
let isOpen = false;
console.log(isOpen);
isOpen = true;
console.log(isOpen);

//Connecting variables
console.log("Age: " + age);

console.log("Community " + "Centre");

console.log(age + age); //40

console.log("age + age"); //prints a word

//Using modulous (getting the remainder)
console.log(5 % 3);
console.log(5 / 3);

//Comparisons
console.log(6 > 1);
console.log(6 < 1);
console.log(5 >= 5);
console.log(5 <= 4);
console.log(3 == 3);

//Checking multiple conditions
//&&: both conditions must be true for the operation to work
//||: one of the conditions must be true for the operation to be true

//Booleans
console.log(true && false);
console.log(true && true);
console.log(true || false);

//Numbers
console.log(5 > 0 && 2 < 0);
console.log(5 > 0 || 2 < 0);

//If-statements
//3 parts of an if-statement:
//"if" keyword
//parameters found in ( )
//curly brackets where our code will be in { }
let number = -3;

if(number > 0) {
	console.log("This is a positive number");
	if(number % 2 == 0) {
		console.log("Even number");
	}
} else if(number < 0) {
	console.log("This is a negative number");
	if(number % 2 == -1) {
		console.log("Odd number");
	}
} else if(number == 0) {
    console.log("Zero");
} else {
    console.log("idk");
}

//Switch statements
let day = "Monday";

switch(day) {
	case "Monday":
		console.log("Today is M");
		break;
	default:
		console.log("Day is gone");
}

//Loops
//Definition: A loop is a coding mechanism in which you can repeat a task multiple times without having to rewrite it

//For-loop
//1. "for" keyword
//2. Starting condition (let i = 0)
//3. Ending condition (i < 10)
//4. Increment value/condition (i = i + 1)
//5. Curly brackets to hold our specific code ( { } )
for(let i = 0; i < 10; i = i + 1) {
	console.log("This is a for-loop");
}

function multiply(x, y) {
    return x * y
    // return says to set this function equal to whatever numbers we give it
}

let multipliedNumber = multiply(4, 5)
console.log(multipliedNumber)