'use strict';

const printArea = document.getElementById("printArea");
const dice = parseInt(prompt("Number of dice: "));
const sum = parseInt(prompt("Value of sum: "));

if (sum >= dice) {
    let favorable = 0;
    for (let i = 0; i < 10000; i++) {
        if (Math.floor(Math.random() * (dice * 6)) === sum) {
            favorable++;
        }
    }
    printArea.innerHTML = `<p>The probability of ${sum} for ${dice} dice is ${favorable/100}%</p>`
}
else {
    printArea.innerHTML = `<p>${sum} is an invalid amount for ${dice} dice!!!</p>`
}
