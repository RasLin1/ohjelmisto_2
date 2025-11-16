'use strict';

const items = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < items.length; i++) {
    if (i == 1) {
        const li = document.createElement("li");
        li.innerText = items[i];
        li.classList.add('my-item');
        document.getElementById('target').appendChild(li);
    }
    else {
        const li = document.createElement("li");
        li.innerText = items[i];
        document.getElementById('target').appendChild(li);
    }
    
}