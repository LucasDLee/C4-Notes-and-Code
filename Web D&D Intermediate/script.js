// Adding Facts!!! //
let getFactButton = document.getElementById('add-fact')
getFactButton.addEventListener('click', function() {
  let listOfFacts = document.getElementById('facts')

  let newFact = prompt('Enter a new fact:')

  let createListItem = document.createElement('li')
  createListItem.textContent = newFact

  listOfFacts.appendChild(createListItem)
})

// Change Image //

// Set up variables
let currentIndex = 0
let images = ["images/fish.jpg", "images/popper-and-pop.jpg", "images/snow.jpg"]

// Function to change the image
function changeImage(direction) {
  if (direction === 'next') {
    currentIndex = (currentIndex + 1) % images.length
  } else if (direction === 'prev') {
    currentIndex = (currentIndex - 1 + images.length) % images.length
  }

  let picture = document.getElementById('picture')
  picture.src = images[currentIndex]
}

// Event listeners for left and right arrows
document.getElementById('left').addEventListener('click', function() {
  changeImage('prev')
})

document.getElementById('right').addEventListener('click', function() {
  changeImage('next')
})