#!/bin/bash
# AI-assisted implementation based on the Lecture 4 activity description.
# Git commit and push will be handled by the workflow after successful checks.
set -euo pipefail

if [[ $# -lt 2 || $# -gt 3 ]]; then
  echo "Usage: bash update_index.sh TASK_OUTPUT TEST_OUTPUT [HTML_FILE]" >&2
  exit 1
fi

task_output="$1"
test_output="$2"
html_file="${3:-index.html}"

for input_file in "$task_output" "$test_output" "$html_file"; do
  if [[ ! -f "$input_file" ]]; then
    echo "File not found: $input_file" >&2
    exit 1
  fi
done

grep -Fxq 'ToDo Tasks:' "$task_output"
grep -Fxq 'Done Tasks:' "$task_output"
for section_id in todo-tasks done-tasks test-results; do
  grep -Fq "<pre id=\"$section_id\">" "$html_file"
done

todo_tasks=$(awk '/^ToDo Tasks:$/ {capture=1; next} /^Done Tasks:$/ {capture=0} capture {print}' "$task_output")
done_tasks=$(awk '/^Done Tasks:$/ {capture=1; next} capture {print}' "$task_output")
test_results=$(cat "$test_output")

update_pre() {
  SECTION_ID="$1" SECTION_TEXT="$2" perl -0777 -i -pe '
    BEGIN {
      $id = $ENV{"SECTION_ID"};
      $text = $ENV{"SECTION_TEXT"};
      $text =~ s/&/&amp;/g;
      $text =~ s/</&lt;/g;
      $text =~ s/>/&gt;/g;
    }
    $count = s{(<pre id="\Q$id\E">).*?(</pre>)}{$1 . $text . $2}gse;
    die "Expected one HTML section: $id\n" unless $count == 1;
  ' "$html_file"
}

update_pre todo-tasks "$todo_tasks"
update_pre done-tasks "$done_tasks"
update_pre test-results "$test_results"

echo "HTML report updated: $html_file"
