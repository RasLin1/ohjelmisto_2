const username = prompt('Please enter your username: ');

if (username !== null) {
    document.getElementById('print_area').innerHTML = 'Hello, ' + username + '!';
}