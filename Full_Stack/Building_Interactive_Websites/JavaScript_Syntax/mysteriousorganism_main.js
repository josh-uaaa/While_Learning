// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)]
}

// Returns a random single strand of DNA containing 15 bases
const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
        newStrand.push(returnRandBase())
    }
    return newStrand
}

function pAequorFactory(num, arr) {
    return {
        _specimenNum: num,
        _dna: arr,
        get dna() { return this._dna; },
        get specimenNum() { return this._specimenNum; },
        mutate() {
            let randomIndex = Math.floor(Math.random() * 16);
            let newBase = returnRandBase();
            while (newBase === this._dna[randomIndex]) {
                newBase = returnRandBase();
            }
            this._dna = newBase;
            return this._dna;
        },
        compareDNA(obj) {
            let percentage = 0;
            for (let i = 0; i < this._dna.length; i++) {
                if (this._dna[i] === obj.dna[i]) {
                    percentage++;
                }
            }
            percentage = (percentage / this._dna.length) * 100;
            console.log(`Specimens have ${percentage}% DNA in common.`);
        },
        willLikelySurvive() {
            let percentage = 0;
            this._dna.forEach((b) => {
                if (b == 'C' || b == 'G') {
                    percentage++;
                }
            })
            percentage = (percentage / this._dna.length) * 100;
            return percentage >= 60;
        }
    };
}

let pAequorInstances = [];
while (pAequorInstances.length !== 30) {
    let newInstance = pAequorFactory(pAequorInstances.length + 1, mockUpStrand());
    if (newInstance.willLikelySurvive()) {
        pAequorInstances.push(newInstance);
    }
}
console.log('Finished creating 30 valid instances...');
pAequorInstances.forEach((obj) => {
    console.log(obj.dna);
})  