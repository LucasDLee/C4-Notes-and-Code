let submit = document.getElementById("submitColour")
submit.addEventListener("click", function() {
    let websiteBackground = document.querySelector("body")
    let getColour = document.getElementById("chooseColour")
    websiteBackground.style.backgroundColor = getColour.value
})