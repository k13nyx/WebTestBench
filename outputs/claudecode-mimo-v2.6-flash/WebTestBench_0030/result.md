# Test Result

## Functionality
- [X] FT-01: Create a new note with a title and rich-text body
  - Action: Create a new note, enter title "Meeting Notes" and a short formatted body, save it.
  - Expected: The note appears in the note list titled "Meeting Notes" and is selectable.

- [X] FT-02: Edit an existing note
  - Action: Open a default note, change its title to "Updated Title" and modify its body text, then reopen it.
  - Expected: The note shows "Updated Title" and the modified body text.

- [X] FT-03: Delete a note
  - Action: Delete one of the default notes from its list/folder view.
  - Expected: The note disappears from the note list and no longer opens.

- [X] FT-04: Create a new folder
  - Action: Create a folder named "Recipes".
  - Expected: "Recipes" appears in the folder list and can be selected.

- [X] FT-05: Rename a folder
  - Action: Rename an existing folder to "Work Archive".
  - Expected: Folder list shows "Work Archive", and the notes previously in it are still listed under it.

- [X] FT-06: Move a note between folders
  - Action: Move a note from its current folder to another folder.
  - Expected: The note is listed under the destination folder.

- [X] FT-07: Add and then remove a tag on a note
  - Action: Add tag "urgent" to a note, then remove the same tag.
  - Expected: "urgent" is visible on the note after adding and gone after removal.

- [X] FT-08: Search by title
  - Action: Type an exact word from a default note's title (e.g., part of "Meeting Notes") into search.
  - Expected: That note appears in the search results.

- [X] FT-09: Search by content
  - Action: Type a distinctive word that appears only inside a note's body into search.
  - Expected: The note containing that word appears in the search results.

- [X] FT-10: Search by tag
  - Action: Search using the name of an existing tag (e.g., "urgent").
  - Expected: All notes carrying that tag appear in the results.

- [X] FT-11: Search by folder
  - Action: Search using an existing folder name (e.g., "Recipes").
  - Expected: Notes belonging to that folder appear in the results.

- [X] FT-12: Filtered view combining folder and tag
  - Action: Select folder "Work" and apply tag filter "urgent".
  - Expected: The view lists only notes that are in folder "Work" AND carry tag "urgent".

- [X] FT-13: Notes persist across browser revisit
  - Action: Create a note, edit another note, and delete a third; then reload the page (or close and reopen the browser).
  - Expected: The new note, the edits, and the deletion are all still reflected after reload.

## Constraint
- [X] CS-01: A note belongs to exactly one folder at a time
  - Action: After moving a note to a new folder, inspect both the old and new folder listings.
  - Expected: The note appears only in the new folder, never in both.

- [X] CS-02: Edits survive a lost/stable-less internet connection
  - Action: While editing a note, disconnect the internet; keep typing, then reload the page after reconnecting.
  - Expected: No error blocks typing, and all text entered while offline is still present after reload.

## Interaction
- [X] IX-01: Instant navigation feedback
  - Action: Click a folder in the sidebar, then click a different tag filter.
  - Expected: The note list updates immediately to the selected folder/tag without requiring a manual refresh.

- [X] IX-02: Editing feels instant (no explicit save step)
  - Action: Type a change into an open note, navigate to another note, then return to the edited note.
  - Expected: The latest typed content is shown without needing to press a "Save" button first.

- [X] IX-03: Search results update live
  - Action: Type a query into the search box and continue typing to refine it.
  - Expected: Results update as the query changes, with no page reload and no submit button required.

## Content
- [X] CT-01: Rich-text formatting is preserved and rendered
  - Action: Apply bold, italic, a heading, and a bulleted list in a note, save, and reopen it.
  - Expected: Bold, italic, heading style, and bullets all render correctly in the note view.

- [X] CT-02: Displayed labels match user-entered names exactly
  - Action: Compare the folder names, tag labels, and note titles shown in the UI against the names entered.
  - Expected: Every displayed folder, tag, and title matches the entered text exactly (no truncation, renaming, or duplication).