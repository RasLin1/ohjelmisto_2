const printArea = document.getElementById("printArea")
const name = prompt('Please enter your name: ')
const house_number = Math.floor(Math.random() * 4) + 1;
const houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

printArea.innerHTML = `${name} you are a ${houses[house_number - 1]}`

