 'use strict';

const div = document.getElementById('mainContainer');
let allowNewNums = true;
const personArray =  ['Petrus', 'Matteus', 'Bartolomaios', 'Simon'];

function concat(array) {
    let nameString = '';
    for (let x of array) {
        nameString += x;
    }
    return nameString
}



const concatArray =  concat(personArray);


const span = document.createElement('span');
span.innerText = concatArray;
div.appendChild(span);