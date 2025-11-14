'use strict';

let ul = document.getElementById("printList");
let nums = [];

function arrayReverser (array) {
    let tempArray = []
    for (let i = array.length - 1; i >= 0; i--) {
    tempArray.push(array[i]);
    }
    return tempArray
}

for (let i = 0; i < 5; i++) {
    nums.push(prompt("Please enter a number: "));
}

nums = arrayReverser(nums);

for (let i = 0; i < nums.length; i++) {
    const li = document.createElement("li");
    li.innerText = nums[i];
    ul.insertAdjacentElement('beforeend', li);
    console.log(nums[i]);
}
