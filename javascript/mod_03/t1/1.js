'use strict';

const items = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < items.length; i++) {
    document.getElementById('target').innerHTML += `<li class="my-list">${items[i]}</li>`;
}