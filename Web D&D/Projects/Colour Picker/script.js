let myColour = document.getElementById("chooseColour")
myColour.addEventListener("click", function() {
    let websiteBackground = document.querySelector("body")
    let getColour = document.getElementById("myColour")
    websiteBackground.style.backgroundColor = getColour.value
})