'use strict';
const target = document.getElementById('weatherTarget');

mainForm.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    try {                                               // error handling: try/catch/finally
        const query = document.getElementById('query').value;
        const weatherResponse = await fetch(`${apiLink}/weather?q=${query}&appid=${key}&units=metric`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await weatherResponse.json();          // retrieving the data retrieved from the response object using the json() function
        const iconeResponse = await fetch(`${apiIcons}/${jsonData['weather']['0']['icon']}@2x.png`);
        console.log(iconeResponse)
        console.log(jsonData);
        const place = document.createElement('h2');
            place.textContent = jsonData['name'];
        const temp = document.createElement('p');
            temp.textContent = `Current temperature: ${jsonData['main']['temp']}`;
        const feelsLike = document.createElement('p');
            feelsLike.textContent = `Feels like: ${jsonData['main']['feels_like']}`;
        const weatherIcon = document.createElement('img');
            weatherIcon.src = iconeResponse['url'];
        const weatherDescription = document.createElement('p');
            weatherDescription.textContent = jsonData['weather']['0']['description'];
        const article = document.createElement('article');
            article.classList.add('card', 'col-2', 'mx-auto', 'm-1')
            article.append(place, temp, feelsLike, weatherIcon, weatherDescription);
            target.append(article);
    } catch (error) {
        console.log(error.message);
    }
});