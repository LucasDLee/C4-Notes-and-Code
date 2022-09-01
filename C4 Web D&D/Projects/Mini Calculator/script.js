let mathButtons = document.querySelectorAll("#math button")

// Use a loop to connect to each button
mathButtons.forEach(function(b) {

    // Adding an event listener connects to each individual button
    b.addEventListener("click", function() {
        if(b.id == "add") {
            addNumbers()
        } else if(b.id == "subtract") {
            subtractNumbers()
        } else if(b.id == "multiply") {
            multiplyNumbers()
        } else if(b.id == "divide") {
            divideNumbers()
        }
    })
})

function addNumbers() {
    let num1 = prompt("What is your first number?")
    let num2 = prompt("What is your second number")
    let answer = parseInt(num1) + parseInt(num2) 
    //parseInt(number) changes our words into numbers

    showAnswer(num1, num2, answer, "&plus;")
}

function subtractNumbers() {
    let num1 = prompt("What is your first number?")
    let num2 = prompt("What is your second number")
    let answer = num1 - num2

    showAnswer(num1, num2, answer, "&minus;")
}

function multiplyNumbers() {
    let num1 = prompt("What is your first number?")
    let num2 = prompt("What is your second number")
    let answer = num1 * num2

    showAnswer(num1, num2, answer, "&times;")
}

function divideNumbers() {
    let num1 = prompt("What is your first number?")
    let num2 = prompt("What is your second number")
    let answer = num1 / num2

    showAnswer(num1, num2, answer, "&divide;")
}

function showAnswer(num1, num2, answer, symbol) {
    document.getElementById("num1").innerHTML = num1
    document.getElementById("num2").innerHTML = num2
    document.getElementById("operator").innerHTML = symbol
    document.getElementById("result").innerHTML = answer
}