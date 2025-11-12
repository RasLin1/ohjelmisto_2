'use strict';

let ol = document.getElementById("printList");
const partAmount = parseInt(prompt("Please enter the amount of participants: "));
let participants = [];

for (let i = 0; i < partAmount; i++) {
    let partName = prompt(`Enter the name of participant nr.${i+1}`);
    participants.push(partName);
}

participants.sort();

for (let i = 0; i < partAmount; i++) {
    const li = document.createElement("li");
    li.innerText = participants[i];
    ol.appendChild(li);
}