#!/bin/bash
# AI-assisted implementation based on the Lecture 4 activity description.
set -euo pipefail

cd "${REPORT_WORKSPACE:-/app}"
echo "Running task manager..."
python3 /app/.github/scripts/todo.py | tee task-output.txt

echo "Running unit tests..."
python3 /app/.github/scripts/todo-test.py | tee test-output.txt

bash /app/.github/scripts/update_index.sh task-output.txt test-output.txt
echo "Task manager, tests and HTML report completed."
