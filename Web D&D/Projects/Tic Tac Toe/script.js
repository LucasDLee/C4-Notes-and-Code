const boardButtons = document.querySelectorAll(".board button") //get all buttons on the board

//declare players
const p1 = 'X';
const p2 ='O';
let currentTurn = p1; //initialize the game to start with player 1

boardButtons.forEach(function(b) {
    b.addEventListener("click", () => {
        b.innerHTML = currentTurn 
        b.disabled = true //needed to prevent the board from changing back
        alternateTurns()
        checkWinner()
    })
});

function alternateTurns() {
    if(currentTurn == p1) {
        currentTurn = p2
    } else if(currentTurn == p2) {
        currentTurn = p1
    } else {
        currentTurn = '' //set the currentTurn to nothing
    }
}

function checkWinner() {
    for(let i = 0; i < 3; i++) { //check all vertical combinations
        if(boardButtons[i].innerHTML == boardButtons[i+3].innerHTML && boardButtons[i+3].innerHTML == boardButtons[i+6].innerHTML && boardButtons[i].innerHTML != "") {
            displayWinner(boardButtons[i].innerHTML)
        }
    }

    for(let i = 0; i < boardButtons.length; i += 3) { //check all horizontal combinations
        if(boardButtons[i].innerHTML == boardButtons[i+1].innerHTML && boardButtons[i+1].innerHTML == boardButtons[i+2].innerHTML && boardButtons[i].innerHTML != "") {
            displayWinner(boardButtons[i].innerHTML)
        }
    }

    if(boardButtons[0].innerHTML == boardButtons[4].innerHTML && boardButtons[4].innerHTML == boardButtons[8].innerHTML && boardButtons[4].innerHTML != "") {
        displayWinner(boardButtons[4].innerHTML)
    }

    if(boardButtons[2].innerHTML == boardButtons[4].innerHTML && boardButtons[4].innerHTML == boardButtons[6].innerHTML && boardButtons[4].innerHTML != "") {
        displayWinner(boardButtons[4].innerHTML)
    }

    isFull = true
    
    for(let i = 0; i < boardButtons.length; i++) { //check if the board is full
        if(boardButtons[i].innerHTML == "") {
            isFull = false
            break
        }
    }

    if(isFull) { //if isFull is true
        displayWinner("")
    }
}

function displayWinner(player) {
    if(player == p1) {
        alert("Player 1 has won!")
    } else if(player == p2) {
        alert("Player 2 has won!")
    } else {
        alert("It was a tie!")
    }
    disableBoard()
}

function disableBoard() {
    boardButtons.forEach(function(b) {
        b.disabled = true
    })
}

function reset() {
    boardButtons.forEach(function(b) {
        b.innerHTML = ""
        b.disabled = false
    })
    currentTurn = p1
}
