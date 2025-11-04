const year = prompt('Please enter a year number: ')

if ((year % 4) === 0){
    if ((year % 100) === 0 && (year % 400) !== 0) {
        document.getElementById('print_area').innerHTML = 'The year of ' + year + ' is not a leap year'
    }
    else {
        document.getElementById('print_area').innerHTML = 'The year of ' + year + ' is a leap year'
    }
}
else {
    document.getElementById('print_area').innerHTML = 'The year of ' + year + ' is not a leap year'
}