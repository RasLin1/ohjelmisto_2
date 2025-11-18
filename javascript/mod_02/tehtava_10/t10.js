 'use strict';

const ul = document.getElementById('printList');
let candidates = [];
const candAmount = parseInt(prompt('Please enter the  number of candidates'));

for (let i = 0; i < candAmount; i++) {
    let candName = prompt(`Please enter the name of candidate nr.${i + 1} `);
    let tempCand = {'name': candName, 'votes': 0};
    candidates.push(tempCand);
}


const voterAmount = parseInt(prompt("Please enter the number of voters"));

for (let i = 0; i < voterAmount; i++) {
    let voteTarget = prompt('Enter the name of your preferd candidate');
    let candFound = false;
    for (let c of candidates) {
        if (c['name'] == voteTarget) {
            c['votes'] += 1;
            candFound =  true;
        }
    }
    if (voteTarget == ""){
        console.log('An empty vote');
    }
    else if (candFound == false){
        console.log('Invalid voter input!');
    }
}

candidates.sort((a, b) => {
   console.log(a, b);
   return b - a;
});

for (let c of candidates) {
    const li = document.createElement("li");
    li.innerText = `Candidate name: ${c['name']} | Vote amount: ${c['votes']}`;
    ul.appendChild(li);
}