// JavaScript code from: https://dev.to/gspteck/create-a-stopwatch-in-javascript-2mak

// Start with defining our variables
let centiseconds = 0
let seconds = 0
let minutes = 0

let stopwatch = document.getElementById("time")
let buttonControls = document.querySelectorAll(".controls button")

let stopTime = true // used for the startTimer(), timerCycle() stopTimer() functions

// Use a loop to connect to all of the buttons
buttonControls.forEach(function(individualButton) {
    let individualButtonId = individualButton.id

    // Adding an event listener connects to each individual button
    individualButton.addEventListener("click", function() {
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
    // Mini-activity: Stop the timer by changing stopTime to false if it is currently true
    // Do not add the timerCycle() function
    if(stopTime == false) {
        stopTime = true
    }
}

function resetTimer() {
    stopTime = true
    centiseconds = 0
    seconds = 0
    minutes = 0
    stopwatch.innerHTML = "00:00:00"
}

function timerCycle() {
    if(stopTime == false) {
        centiseconds = parseInt(centiseconds)
        seconds = parseInt(seconds)
        minutes = parseInt(minutes)
        //parseInt("3") changes a string/word to a number
        //parseInt("45") => 45

        centiseconds = centiseconds + 1

        // Changes 100 centiseconds to 1 second
        if(centiseconds == 100) {
            seconds = seconds + 1
            centiseconds = 0
        }
        
        // Mini-activity: If we have 60 seconds, increase the minutes by 1 and reset seconds and centiseconds to 0
        // Changes 60 seconds into 1 minute
        if(seconds == 60) {
            minutes = minutes + 1
            seconds = 0
            centiseconds = 0
        }

        // The following 3 if-statements are used to change how our time is displayed
        if (centiseconds < 10 || centiseconds == 0) {
            centiseconds = '0' + centiseconds;
        }
        if (seconds < 10 || seconds == 0) {
            seconds = '0' + seconds;
        }
        // Mini-activity: If our minutes is 0 or less than 10, display a 0 in front of our current minutes
        if (minutes < 10 || minutes == 0) {
            minutes = '0' + minutes;
        }
    
        // Display the new time
        stopwatch.innerHTML = minutes + ':' + seconds + ':' + centiseconds;
    
        setTimeout("timerCycle()", 10)
        // setTimeout("function()", milliseconds) waits a certan amount of milliseconds
        // and then tells the function to run
        // 1 second = 1000 milliseconds
        // 1 centisecond = 10 milliseconds
    }
}