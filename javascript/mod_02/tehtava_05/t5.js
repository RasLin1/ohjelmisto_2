'use strict';

const ol = document.getElementById("printList");
let allowNewNums = true;
let numbers = [];

function numChecker(compNum) {
    for (let num of numbers) {
        if (num == compNum) {
            return true;
        }
    }
}

while (allowNewNums) {
    let num = parseInt(prompt(`Please enter a new number`));
    let numExists = numChecker(num);
    if (numExists) {
        console.log('Number exists in array');
        allowNewNums = false;
    }
    else {
        numbers.push(num);
    }
    
}

numbers.sort();

for (let i = 0; i < numbers.length; i++) {
    const li = document.createElement("li");
    li.innerText = numbers[i];
    ol.appendChild(li);
}