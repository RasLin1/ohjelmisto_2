'use strict';

let ol = document.getElementById("printList");
const dogAmount = 6;
let dogs = [];

for (let i = 0; i < dogAmount; i++) {
    let dogName = prompt(`Please enter the name of dog nr.${i+1}`);
    dogs.push(dogName);
}

dogs.sort();
dogs.reverse();

for (let i = 0; i < dogAmount; i++) {
    const li = document.createElement("li");
    li.innerText = dogs[i];
    ol.appendChild(li);
}