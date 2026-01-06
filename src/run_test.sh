#!/bin/bash

# تشغيل app.js وتخزين الناتج
OUTPUT=$(node src/app.js)

# القيمة المتوقعة
EXPECTED="Hello, Abdulrahman!"

# اختبار الناتج
if [ "$OUTPUT" = "$EXPECTED" ]; then
    echo "✅ Test Passed!"
else
    echo "❌ Test Failed!"
    echo "Expected: $EXPECTED"
    echo "Got: $OUTPUT"
    exit 1  # يرجع خطأ لكي يفشل GitHub Action في حالة الفشل
fi
