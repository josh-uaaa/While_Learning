// To run this test, type 'npm test' in the terminal in the correct subdirectory.

var assert = require("assert");
var Calculate = require('../factorial_main.js')

describe('Calculate', () => {
    describe('.factorial', () => {
        it('returns 120 for 5 factorial', () => {
            const expected = 120;
            const input = 5;
            const result = Calculate.factorial(input);
            assert.equal(result, expected);
        });

        it('returns 6 for 3 factorial', () => {
            const expected = 6;
            const input = 3;
            const result = Calculate.factorial(input);
            assert.equal(result, expected);
        });

        it('returns 0 for 0 factorial', () => {
            const expected = 0;
            const input = 0;
            const result = Calculate.factorial(input);
            assert.equal(result, expected);
        });
    });
});