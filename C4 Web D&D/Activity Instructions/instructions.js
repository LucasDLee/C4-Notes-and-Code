//JS 1
console.log("apple");

console.log("someplace" + " " + "in" + " " + "richmond");

let num1 = 54;
let num2 = 34;

console.log(num1 + num2);

console.log(num1 % num2);

console.log(num1 / num2);

console.log(num1 * num2);

num1 = 34

console.log(num1 < num2);

// JS 2
let dice = -1;

if(dice % 2 == 0 && dice % 5 == 0) {
	console.log("You have rolled a mulitple of 10");
} else if(dice % 2 == 0) {
	console.log("This is an even number");
} else if(dice % 5 == 0) {
	console.log("You have rolled a multiple of 5");
} else {
	console.log("I cannot understand your dice roll");
}

let city = "";

switch(city) {
	case "Vancouver":
		console.log("Welcome to Vancouver")
		break;
	case "Ontario":
		console.log("You are in the capital of Canada");
		break;
	case "Toronto":
		console.log("Toronto is big");
		break;
	default:
		console.log("I don't recognize this city");
}

// JS 3
for(let i = 0; i < 10; i++) {
	console.log("Testing a for-loop");
}

let i = 0;
while(i < 10) {
	console.log(i);
	i++;
}

let j = 0;
do {
	console.log("This is sentence #" + j);
	j++;
} while(j < 10);

// JS Loops and Functions

function greeting(yourName) {
	for(let i = 0; i < 10; i++) {
		console.log("Hello, my name is " + yourName)
	}
}

function pythagorean(x, y, z) {
	return (x * x) + (y * y) == (z * z)
}

// Functions activity
function getName(name) {
	console.log("Hello, my name is " + name + "!")
}
getName("Lucas")
getName("Bob")

function checkIfNumber(num) {
	// return isNaN(num)
	if(isNaN(num)) {
		return true
	}
	return false
}

// Event listeners activity

// <h1 id="title">My Title</h1>
// <button onclick="findTitle()">Click me</button>

function findTitle() {
	let getTitle = document.getElementById("title")
	let yourTitle = prompt("What is your title?")
	getTitle.innerHTML = yourTitle
}