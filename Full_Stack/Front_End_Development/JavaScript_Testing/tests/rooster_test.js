// To run this test, type 'npm test' in the terminal in the correct subdirectory.

const assert = require('assert');
const Rooster = require('../rooster_main.js');

describe('Rooster', () => {
    describe('.announceDawn', () => {
        it('returns a rooster call', () => {
            const expected = 'cock-a-doodle-doo!';
            const result = Rooster.announceDawn();
            assert.equal(result, expected);
        });
    });

    describe('.timeAtDawn', () => {
        it('returns its arguments as a string', () => {
            const input = 4;
            const result = Rooster.timeAtDawn(input);
            assert.strictEqual(result, input);
        });

        it('throws an error if passed a number less than 0', () => {
            const input = -1;
            assert.throws(() => {
                Rooster.timeAtDawn(input);
            },
                RangeError
            );
        });

        it('throws an error if passed a number greater than 23', () => {
            const input = 25;
            assert.throws(() => {
                Rooster.timeAtDawn(input);
            },
                RangeError
            );
        });
    });
});