let rock = document.getElementById("rock");
let paper = document.getElementById("paper");
let scissors = document.getElementById("scissors");
let reset = document.getElementById("reset");

let playerScore = 0;
let computerScore = 0;
let playerMove = "";
let playerSymbol = -1;
let computerMove = "";
let computerSymbol = -1;

let winAmount = 3;

//querySelectorAll() looks for all HTML elements associated with the inputted element in the website
//querySelector() looks for the first HTMl element inputted into its brackets
let buttons = document.querySelectorAll("button");
buttons.forEach(function(item) {
	item.addEventListener("click", function() {
		
		if(item.id == reset.id) {
			resetGame();
			return;
		}
		
		//console.log(item.id);
		if(item.id == rock.id) {
			// console.log("Your move was rock");
			playerSymbol = 0;
			playerMove = "Your move was rock!";
		} else if(item.id == paper.id) {
			// console.log("Your move was paper");
			playerSymbol = 1;
			playerMove = "Your move was paper!";
		} else if(item.id == scissors.id) {
			// console.log("Your move was scissors");
			playerSymbol = 2;
			playerMove = "Your move was scissors!";
		}

		document.getElementById("playerMove").innerHTML = playerMove;

		computerSymbol = Math.floor(Math.random() * 3);

		if(computerSymbol == 0) {
			computerMove = "The computer's move was rock!";
		} else if(computerSymbol == 1) {
			computerMove = "The computer's move was paper!";
		} else if(computerSymbol == 2) {
			computerMove = "The computer's move was scissors!";
		}

		document.getElementById("computerMove").innerHTML = computerMove;

		if(playerSymbol < computerSymbol) {
			if(playerSymbol == 0 && computerSymbol == 2) {
				playerScore += 1;
			} else {
				computerScore += 1;
			}
		} else if(computerSymbol < playerSymbol) {
			if(playerSymbol == 2 && computerSymbol == 0) {
				computerScore += 1;
			} else {
				playerScore += 1;
			}
		} else {
			//it was a tie
			// console.log("tie");
			alert("It was a tie!");
		}
		
		document.getElementById("computerScore").innerHTML = computerScore;
		document.getElementById("playerScore").innerHTML = playerScore;

		if(playerScore == winAmount) {
			alert("The player has won!");
			resetGame();
		} else if(computerScore == winAmount) {
			alert("The computer has won!");
			resetGame();
		}
	});
});

function resetGame() {
	playerScore = 0;
	computerScore = 0;
	document.getElementById("playerMove").innerHTML = "Your move was ???";
	document.getElementById("computerMove").innerHTML = "The computer's move was ???";
	document.getElementById("computerScore").innerHTML = computerScore;
	document.getElementById("playerScore").innerHTML = playerScore;
}