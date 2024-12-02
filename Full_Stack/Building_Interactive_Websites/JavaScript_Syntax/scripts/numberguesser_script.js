let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget() {
    return Math.floor(Math.random() * 9);
}

function compareGuesses(userGuess, compGuess, secretTarget) {
    const userDiff = Math.abs(secretTarget - userGuess);
    const compDiff = Math.abs(secretTarget - compGuess);
    return userDiff <= compDiff ? true : false;
}

function updateScore(winner) {
    switch (winner) {
        case 'human':
            humanScore += 1;
        case 'computer':
            computerScore += 1;
    }
}

function advanceRound() {
    currentRoundNumber += 1;
}