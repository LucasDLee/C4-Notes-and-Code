document.getElementById("chooseColour").addEventListener("click", function() {
    let websiteBackground = document.querySelector("html")
    let getColour = document.getElementById("getColour")
    websiteBackground.style.backgroundColor = getColour.value
})