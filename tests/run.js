import assert from 'node:assert/strict';
import { sum } from '../src/sum.js';

assert.equal(sum(1, 2), 3);
console.log('✓ sum works');