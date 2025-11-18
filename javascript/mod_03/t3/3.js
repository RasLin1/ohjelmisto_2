'use strict';
const names = ['John', 'Paul', 'Jones'];
const ul = document.getElementById('target');

for (let i = 0; i < names.length; i++) {
    const li = document.createElement("li");
    li.innerText = names[i];
    ul.insertAdjacentElement('beforeend', li);
}
