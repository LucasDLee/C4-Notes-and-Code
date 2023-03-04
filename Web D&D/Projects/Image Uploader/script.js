let submit = document.getElementById("submitImg")
submit.addEventListener("click", function() { 
    const [file] = yourImage.files
    if (file) {
        websiteImage.src = URL.createObjectURL(file)
    }
})