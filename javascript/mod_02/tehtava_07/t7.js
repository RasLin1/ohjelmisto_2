 'use strict';

const ul = document.getElementById('printList');
let allowNewNums = true;
const diceSides = parseInt(prompt('How many sides should the dice have?'))

function diceRoller () {
    const dice_value = Math.floor(Math.random() * diceSides) + 1;
    return dice_value;
}

while (allowNewNums) {
    let num = diceRoller();
    if (num == diceSides) {
        allowNewNums = false;
    }
    const li = document.createElement('li');
    li.innerText = num;
    ul.appendChild(li);
} 