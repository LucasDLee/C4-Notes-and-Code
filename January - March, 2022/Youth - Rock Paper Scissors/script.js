let rock = document.getElementById("rock");
let paper = document.getElementById("paper");
let scissors = document.getElementById("scissors");
//Make a variable that connects the "reset" button from our HTML file into our JavaScript file
let resetButton = document.getElementById("reset");

let playerScore = 0;
let computerScore = 0;
let buttons = document.querySelectorAll("button");

let winAmount = 3;

buttons.forEach(function(item) {
	item.addEventListener("click", function() {
		
		if(item.id == resetButton.id) {
			resetGame();
			return;
		}
		
		if(item.id == rock.id) {
			playerSymbol = 0;
			playerMove = "Your move was rock!";
		} else if(item.id == paper.id) {
			playerSymbol = 1;
			playerMove = "Your move was paper!";
		} else if(item.id == scissors.id) {
			playerSymbol = 2;
			playerMove = "Your move was scissors!";
		}

		document.getElementById("playerMove").innerHTML = playerMove;

		let generateComputerSymbol = Math.floor(Math.random() * 3);
		if(generateComputerSymbol == 0) {
			//change the variable of "computerMove" to "The computer's move was rock!"
			computerMove = "The computer's move was rock!";
		} else if(generateComputerSymbol == 1) {
			//change the variable of "computerMove" to "The computer's move was paper!"
			computerMove = "The computer's move was paper!";
		} else if(generateComputerSymbol == 2) {
			//change the variable of "computerMove" to "The computer's move was scissors!"
			computerMove = "The computer's move was scissors!";
		}
		
		computerSymbol = generateComputerSymbol;
		document.getElementById("computerMove").innerHTML = computerMove;

		if(playerSymbol < computerSymbol) { //the computer is winning
			if(playerSymbol == 0 && computerSymbol == 2) {
				playerScore = playerScore + 1;
			} else {
				computerScore = computerScore + 1;
			}
		} else if(computerSymbol < playerSymbol) { //the player is winning
			if(playerSymbol == 2 && computerSymbol == 0) {
				computerScore = computerScore + 1;
			} else {
				playerScore = playerScore + 1;
			}
		} else {
			//it was a tie
			console.log("It was a tie!");
			alert("It was a tie!");
		}
		document.getElementById("playerScore").innerHTML = playerScore;
		document.getElementById("computerScore").innerHTML = computerScore;

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
	//Make sure that the score's and the player and computer's move are all reset
	playerScore = 0;
	computerScore = 0;
	document.getElementById("playerScore").innerHTML = playerScore;
	document.getElementById("computerScore").innerHTML = computerScore;
	document.getElementById("playerMove").innerHTML = "Your move was ???";
	document.getElementById("computerMove").innerHTML = "The computer's move was ???";
}