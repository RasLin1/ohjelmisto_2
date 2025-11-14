'use strict';

// When the form is submitted...
const mainForm = document.getElementById('mainForm');
const showsContainer = document.getElementById('showsContainer');
mainForm.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const code = document.getElementById('query').value;
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        for (let x of jsonData) {
            console.log(x);    // log the result to the console
            const li = document.createElement("li");
            li.innerText = nums[i];
            showsContainer.insertAdjacentElement('beforeend', `<h2>${x.show.name}</h2>`);
        }
    } catch (error) {
        console.log(error.message);
    }
});