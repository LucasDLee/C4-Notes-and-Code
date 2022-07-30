console.log("bruh");

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

//While loop
let j = 0;
while(j < 10) {
	console.log("This is loop number " + j);
	j++;
}

//do-while loop
let m = 0;
do {
	console.log(m)
	m += 1;
} while(m < 5)

//Functions
//A function is a piece of our code we can reuse that'll do a certain thing such as using loops or printing our name to the console

//3 things in a function:
//"function" keyword
//function name: always comes after the "function" keyword
//parameters: variables that we need to make our function work
function add(x, y) {
	console.log(x + y)
}

//Calling our function
add(8, 6)
add(30, 1)

function printLocation() {
	console.log("City Centre Community Centre")
}
printLocation()

function multiply(x, y) {
	return x * y
	//return: instead of printing a value to the console, we can give out a new value by returning something
}

let multipliedNumber = multiply(4, 5)
console.log(multipliedNumber)
multipliedNumber = 3

//Arrays
let cars = ['BMW', 'Toyota', 'Volvo']
console.log(cars[0])
cars[0] = 'Ferrari';
console.log(cars[0])

//Printing all the items in my array
for(let i = 0; i < cars.length; i++) {
	console.log(cars[i])
}

//Math
console.log(Math.PI)
console.log(Math.round(0.5))
console.log(Math.ceil(0.1)) //always rounds up when using Math.ceil
console.log(Math.floor(1.9)) //always rounds DOWN when using Math.floor
console.log(Math.pow(2, 8)) //first parameter: number we're multiplying
//second parameter: our power number
console.log(Math.sqrt(9))
console.log(Math.random()) //0 <= Math.random() < 1

//Document Object Model
//A way to connect our HTML file (website) to our JavaScript
function callDemoFunction() {
	let getDemoId = document.getElementById("demo")
	getDemoId.innerHTML = "We are using the Document Object Model to change this text with JavaScript!"
}

//Event listeners
//Part of the DOM, they wait for a certain action on our website and react accordingly
let testAlert = document.getElementById("event")
console.log(testAlert.innerHTML)
testAlert.addEventListener("click", function() {
	alert("You used an event listener to call a pop up!")
})

function divide() {
	//Prompt: looks like an alert but the user can input something inside the prompt's text box
	let x = prompt("What is your numerator?")
	let y = prompt("What is your denominator?")
	let result = x / y
	let divideParagraphText = document.getElementById("divide")
	divideParagraphText.innerHTML = "You have divided " + x + " and " + y + " to get " + result
}