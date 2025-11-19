'use strict';

// When the form is submitted...
const mainForm = document.getElementById('mainForm');
const showsContainer = document.getElementById('showsContainer');
const apiShowsLink = 'https://api.tvmaze.com/';
let i = 1;
async function showRetAndPrint(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const code = document.getElementById('query').value;
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`${apiShowsLink}search/shows?q=${code}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        showsContainer.innerHTML = '';
        for (let x of jsonData) { //loop that creates articles for the shows
            console.log(x);    // log the result to the console
            const h2 = document.createElement('h2');
                h2.textContent = x.show.name;

            const a = document.createElement('a'); 
                a.textContent = x.show.url;
                a.target = '_blank';

            const br = document.createElement('br');

            const img = document.createElement('img');
            if (!x.show.image) {
                x.show.image = {medium: 'https://placecats.com/210/295'}
            }
                img.src = x.show.image?.medium;
            const sum = document.createElement('div');
                sum.innerText = x.show.summary;

            const article = document.createElement('article');
            article.classList.add('card', 'col-4', 'mx-auto', 'm-1')
            article.append(h2, a, br, img, sum);

            showsContainer.append(article);
            i++;
        }
    } catch (error) {
        console.log(error.message);
    }
}
mainForm.addEventListener('submit', showRetAndPrint);