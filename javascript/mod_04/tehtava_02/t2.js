'use strict';

// When the form is submitted...
const airportForm = document.getElementById('mainForm')
airportForm.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const code = document.getElementById('query').value;
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        for (let shows of jsonData) {
            console.log(shows);    // log the result to the console
        }
    } catch (error) {
        console.log(error.message);
    }
});