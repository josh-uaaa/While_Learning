const gameToPlay = ['VALORANT', 'Call of Duty', 'CS2', 'Marvel Rivals', 'Fortnite', 'Apex Legends'];
const gameplayStatus = ['amazing', 'unbelievable', 'horrible', 'mentally-draining', 'pro-like'];
const mouseGrip = ['fingertip', 'relaxed-claw', 'aggressive-claw', 'palm'];

function messageFactory() {
    return {
        _game: gameToPlay[Math.floor(Math.random() * gameToPlay.length)],
        _gameplay: gameplayStatus[Math.floor(Math.random() * gameplayStatus.length)],
        _mousegrip: mouseGrip[Math.floor(Math.random() * mouseGrip.length)],
        displayMessage() {
            console.log(`You should play ${this._game} tonight.\nYou're going to have ${correctArticle(this._gameplay)} ${this._gameplay} game!\nTry using ${correctArticle(this._mousegrip)} ${this._mousegrip} grip when playing.`);
        }
    }
}

const correctArticle = (word) => {
    return ['a', 'e', 'i', 'o', 'u'].includes(word.charAt(0)) ? 'an' : 'a';
}

const ex1 = messageFactory();
ex1.displayMessage();