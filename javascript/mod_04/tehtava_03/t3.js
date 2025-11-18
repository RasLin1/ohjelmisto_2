'use strict';

// When the form is submitted...
const mainForm = document.getElementById('mainForm');
const showsContainer = document.getElementById('showsContainer');
let i = 1;
async function showRetAndPrint(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const code = document.getElementById('query').value;
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        for (let x of jsonData) {
            console.log(x);    // log the result to the console
            const div = document.createElement("div");
                div.id = `tDiv${i}`;
                div.classList.add('card', 'col-4');
            showsContainer.insertAdjacentElement('beforeend', div);
            const divTarget = document.getElementById(`tDiv${i}`);
            const h2 = document.createElement("h2");
                h2.textContent = x.show.name;
            const a = document.createElement("a");
                a.textContent = x.show.url;
                a.target = "_blank";
            const img = document.createElement("img");
                img.src = x.show.image.medium;
            divTarget.insertAdjacentElement('beforeend', h2);
            divTarget.insertAdjacentElement('beforeend', a);
            divTarget.insertAdjacentElement('beforeend', img);
            i++;
        }
    } catch (error) {
        console.log(error.message);
    }
}
mainForm.addEventListener('submit', showRetAndPrint);