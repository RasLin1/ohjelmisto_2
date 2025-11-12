'use strict';

const ol = document.getElementById("printList");
let allowNewNums = true;
let numbers = [];


while (allowNewNums) {
    let num = parseInt(prompt(`Please enter a new number`));
    if (num > 0) {
        numbers.push(num);
    }
    else {
        allowNewNums = false;
    }
    
}

numbers.sort();
numbers.reverse();

for (let i = 0; i < numbers.length; i++) {
    const li = document.createElement("li");
    li.innerText = numbers[i];
    ol.appendChild(li);
}