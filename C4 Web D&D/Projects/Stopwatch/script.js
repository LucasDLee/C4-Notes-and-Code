// JavaScript code from: https://dev.to/gspteck/create-a-stopwatch-in-javascript-2mak

// Start with defining our variables
let seconds = 0
let minutes = 0
let hours = 0

let stopwatch = document.getElementById("time")
let buttonControls = document.querySelectorAll("button")

let stopTime = true // used for the startTimer(), timerCycle() stopTimer() functions

// Use a loop to connect to all of the buttons
buttonControls.forEach(function(individualButton) {
    let individualButtonId = individualButton.id

    // Use an event listener to respond to any button we click
    individualButton.addEventListener("click", function() {
        let buttonText = individualButton.innerHTML
        if(individualButtonId == "start") {
            startTimer()
        } else if(individualButtonId == "stop") {
            stopTimer()
        } else if(individualButtonId == "reset") {
            resetTimer()
        }    
    })
})

function startTimer() {
    if(stopTime == true) {
        stopTime = false
        timerCycle()
    }
}

function stopTimer() {
    if(stopTime == false) {
        stopTime = true
    }
}

function resetTimer() {
    seconds = 0
    minutes = 0
    hours = 0
    stopwatch.innerHTML = "00:00:00"
}

function timerCycle() {
    if(stopTime == false) {
        seconds = parseInt(seconds)
        minutes = parseInt(minutes)
        hours = parseInt(hours)
        //parseInt("3") changes a string/word to a number

        seconds = seconds + 1

        // Changes 60 seconds into 1 minute
        if(seconds == 60) {
            minutes = minutes + 1
            seconds = 0
        }
        
        // Changes 60 minutes into 1 hour
        if(minutes == 60) {
            hours = hours + 1
            minutes = 0
            seconds = 0
        }

        // The following 3 if-statements are used to change how our time is displayed
        if (seconds < 10 || seconds == 0) {
            seconds = '0' + seconds;
        }
        if (minutes < 10 || minutes == 0) {
            minutes = '0' + minutes;
        }
        if (hours < 10 || hours == 0) {
            hours = '0' + hours;
        }
    
        stopwatch.innerHTML = hours + ':' + minutes + ':' + seconds;
    
        setTimeout("timerCycle()", 1000)
        // setTimeout(function(), milliseconds) waits a certan amount of milliseconds
        // and then tells the function to run
        // 1 second = 1000 milliseconds
    }
}