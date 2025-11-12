 'use strict';

const ul = document.getElementById("printList");
let allowNewNums = true;

function diceRoller () {
    const dice_value = Math.floor(Math.random() * 6) + 1;
    return dice_value;
}

while (allowNewNums) {
    let num = diceRoller();
    if (num == 6) {
        console.log('Number exists in array');
        allowNewNums = false;
    }
    const li = document.createElement("li");
    li.innerText = num;
    ul.appendChild(li);
} 