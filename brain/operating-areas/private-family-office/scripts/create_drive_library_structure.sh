#!/usr/bin/env bash
set -euo pipefail

PARENT_ID="1Y_2O_dCXKZcQfZo3fyWaI6nklpzaBcHp"

books=(
  "Household Finance"
  "Risk & Protection"
  "Home Operations"
  "Children & Dependents"
  "Health & Environment"
  "Travel & Mobility"
  "Time & Calendar"
  "Giving & Community"
)

sections=(
  "Field Guide"
  "Checklist"
  "Product Recommendations"
  "Digital Products"
  "People Recommendations"
)

find_child_folder_id() {
  local parent_id="$1"
  local folder_name="$2"

  gog drive ls --parent "$parent_id" --max 100 --json \
    | jq -r --arg name "$folder_name" '.files[]? | select(.name == $name and .mimeType == "application/vnd.google-apps.folder") | .id' \
    | head -n 1
}

ensure_child_folder() {
  local parent_id="$1"
  local folder_name="$2"
  local folder_id
  local folder_json

  folder_id="$(find_child_folder_id "$parent_id" "$folder_name")"
  if [[ -n "$folder_id" ]]; then
    printf '%s\n' "$folder_id"
    return
  fi

  folder_json="$(gog drive mkdir "$folder_name" --parent "$parent_id" --json)"
  printf '%s\n' "$folder_json" | jq -r '.file.id // .folder.id // .id'
}

for book in "${books[@]}"; do
  book_id="$(ensure_child_folder "$PARENT_ID" "$book")"
  printf 'Book folder ready: %s (%s)\n' "$book" "$book_id"

  for section in "${sections[@]}"; do
    section_id="$(ensure_child_folder "$book_id" "$section")"
    printf '  Section folder ready: %s (%s)\n' "$section" "$section_id"
  done
done
