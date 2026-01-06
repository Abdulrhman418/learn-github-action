#!/bin/bash


OUTPUT=$(node src/app.js)

EXPECTED="Hello, Abdulrahman!"


if [ "$OUTPUT" == "$EXPECTED" ]; then
    echo "✅ Test Passed!"
else
    echo "❌ Test Failed!"
    echo "Expected: $EXPECTED"
    echo "Got: $OUTPUT"
fi
