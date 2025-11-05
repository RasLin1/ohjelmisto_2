'use strict';

const printArea = document.getElementById("printArea");
const num = parseInt(prompt("Enter a number to check if it is prime: "));

for (let i = 2; i < num - 1; i++) {
    if (num % i === 0) {
        printArea.innerHTML = `<p>${num} is not a prime number</p>`
        break
    }
    else{
        printArea.innerHTML = `<p>${num} is a prime number</p>`
    }
}