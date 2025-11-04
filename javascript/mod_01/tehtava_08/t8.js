'use strict';

const start_year = parseInt(prompt("Enter start year: "))
const end_year = parseInt(prompt("Enter end year: "))

if (start_year < end_year && start_year >= 0) {
    for (let year = start_year; year < end_year; year++) {
        if ((year % 4) === 0 && (year % 100) !== 0 && (year % 400) === 0){
                document.getElementById('print_list').innerHTML += `<li>${year}</li>`
                document.getElementById('print_list').innerHTML += `<li>${year}</li>`
        }
    }
}
else {
    document.getElementById("print_area").innerHTML += '<p>Invalid years</p>'
}
