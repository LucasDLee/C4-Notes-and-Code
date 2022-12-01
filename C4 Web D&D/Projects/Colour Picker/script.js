let myColour = document.getElementById("chooseColour")
myColour.addEventListener("click", function() {
    let websiteBackground = document.querySelector("html")
    let getColour = document.getElementById("getColour")
    websiteBackground.style.backgroundColor = getColour.value
})