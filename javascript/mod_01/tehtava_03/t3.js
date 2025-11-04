const num1 = parseInt(prompt('Please enter an integer: '));
const num2 = parseInt(prompt('Please enter an integer: '));
const num3 = parseInt(prompt('Please enter an integer: '));

sum = num1 + num2 + num3;
prod = num1 * num2 * num3;
avr = (num1 + num2 + num3)/3;

document.getElementById('sum').innerHTML = 'Sum of the numbers is ' + sum;
document.getElementById('prod').innerHTML = 'Product of the numbers is ' + prod;
document.getElementById('avr').innerHTML = 'Avarage of the numbers is ' + avr;
