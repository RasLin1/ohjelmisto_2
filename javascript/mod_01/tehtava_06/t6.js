const confimation = confirm('Should I calculate the square root?')

if (confimation === true) {
    const num = parseInt(prompt('Please enter a number: '))
    if (num < 0) {
        document.getElementById('print_area').innerHTML = 'You cant enter a negative number'
    }
    else {
        const sqrt = Math.sqrt(num)
        document.getElementById('print_area').innerHTML = 'The square root of ' + num + ' is ' + sqrt
    }
}
else {
    document.getElementById('print_area').innerHTML = 'Alright ;('
}