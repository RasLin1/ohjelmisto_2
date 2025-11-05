'use strict';

const start_year = parseInt(prompt("Enter start year: "));
const end_year = parseInt(prompt("Enter end year: "));
const printArea = document.getElementById("printArea");
let ul = document.createElement("ul");
let years = [];
let actual_year = 0;

if (start_year < end_year && start_year >= 0) {
    for (let i = start_year; i <= end_year; i++) {
        if (i % 4 === 0){
            if (i % 100 === 0 && i % 400 !== 0) {
            }
            else {
                years.push(i);
            }
        }
    }
    for (let i = 0; i < years.length; i++) {
        let li = document.createElement("li");
        li.textContent = years[i];
        ul.appendChild(li);
    }
}
else {
    printArea.innerHTML += '<p>Invalid years</p>'
}

printArea.appendChild(ul);
