const dice_amount = parseInt(prompt('How many dice do you want to roll'));
let dice_values = 0;

for (let i = 0; i < dice_amount; i++) {
    const temp_dice_value = Math.floor(Math.random() * 7) + 1;
    dice_values = dice_values + temp_dice_value
    console.log(i)
}

document.getElementById('print_area').innerHTML = 'Total value is' + dice_values