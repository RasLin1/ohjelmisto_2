 'use strict';

const ul = document.getElementById('printList');
let allowNewNums = true;
let numberArray = [1, 2, 3, 4, 5, 6];

function evenNumSeparator(numbers) {
    let evenNumbers = [];
    for (let x of numbers) {
        if (x % 2 == 0) {
            evenNumbers.push(x)
        }
    }
    return evenNumbers
}

const evenNumbers = evenNumSeparator(numberArray);
for (let i = 0; i < evenNumbers.length; i++) {
    const li = document.createElement("li");
    li.innerText = evenNumbers[i];
    ul.appendChild(li);
}