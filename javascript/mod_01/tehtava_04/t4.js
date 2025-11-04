const name = prompt('Please enter your name: ')
const house_number = Math.floor(Math.random() * 5) + 1;

if (house_number === 1) {
    document.getElementById('print_area').innerHTML = name + ' you are a Gryffindor'
}
else if (house_number === 2) {
    document.getElementById('print_area').innerHTML = name + 'you are a Slytherin'
}
else if (house_number === 3) {
    document.getElementById('print_area').innerHTML = name + 'you are a Hufflepuff'
}
else if (house_number === 4) {
    document.getElementById('print_area').innerHTML = name + 'you are a Ravenclaw'
}

