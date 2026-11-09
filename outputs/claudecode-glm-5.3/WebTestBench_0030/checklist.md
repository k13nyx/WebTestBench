# Test Checklist

## Functionality

- [ ] FT-01: Create a new rich-text note
  - Action: Click the "New Note" button, enter a title (e.g., "Grocery List"), type body text, and save.
  - Expected: The new note appears in the notes list showing the entered title and content.

- [ ] FT-02: Apply rich-text formatting to note content
  - Action: Open a note in the editor, select a text passage, and apply Bold, Italic, and a bullet list via the toolbar.
  - Expected: The selected text is formatted (bold/italic/list) and the formatting is retained when the note is saved.

- [ ] FT-03: Edit an existing note
  - Action: Open an existing default note, change its title and body text, and save.
  - Expected: The list and editor show the updated title and content; no other notes are modified.

- [ ] FT-04: Delete a note
  - Action: Delete an existing note via its delete control.
  - Expected: The note is removed from the notes list; all remaining notes stay intact.

- [ ] FT-05: Create a folder and place a note in it
  - Action: Create a new folder (e.g., "Work") and move a note into it.
  - Expected: The folder appears in the folder list and the note is listed under it.

- [ ] FT-06: Rename a folder
  - Action: Rename the "Work" folder to "Projects".
  - Expected: The folder shows the new name "Projects"; its notes and their contents are unchanged.

- [ ] FT-07: Move a note between folders
  - Action: Move a note from folder "Projects" to another folder.
  - Expected: The note appears only in the destination folder and no longer in "Projects".

- [ ] FT-08: Add a tag to a note
  - Action: Add the tag "urgent" to an existing note.
  - Expected: The tag is displayed on the note and is available as a tag filter option.

- [ ] FT-09: Remove a tag from a note
  - Action: Remove the "urgent" tag from the tagged note.
  - Expected: The tag is no longer shown on the note; other notes' tags are unaffected.

- [ ] FT-10: Search notes by title
  - Action: Type a word that appears in an existing note's title into the search box.
  - Expected: Only notes whose titles contain the search word are listed.

- [ ] FT-11: Search notes by content
  - Action: Type a word that appears only inside an existing note's body text (not in any title).
  - Expected: Notes whose content contains the word are listed.

- [ ] FT-12: Search notes by tag
  - Action: Enter a tag name in the search box or select a tag filter (e.g., "urgent").
  - Expected: Only notes carrying that tag are listed.

- [ ] FT-13: Filter notes by folder
  - Action: Select a folder in the sidebar to view its notes.
  - Expected: Only notes belonging to that folder are listed.

- [ ] FT-14: Combined filter — folder plus tag
  - Action: Select a folder and then apply a specific tag filter within it.
  - Expected: Only notes that are both in that folder and carrying that tag are listed.

- [ ] FT-15: Notes persist in the browser across visits
  - Action: After creating/editing notes, close the tab, reopen the page, and reload.
  - Expected: All notes, folders, and tags are still present with the latest edits — no data loss.

- [ ] FT-16: Edit safely while connection is lost
  - Action: Set the browser to offline mode, then edit a note and save.
  - Expected: Editing and saving succeed with no error; the changes are still present after reload and when back online.

## Constraint

- [ ] CS-01: Cannot save a note without a title
  - Action: Attempt to create/save a note with an empty or whitespace-only title.
  - Expected: The save is blocked (disabled button or clear validation message) and no empty-titled note is added to the list.

- [ ] CS-02: Cannot create a folder with a duplicate name
  - Action: Attempt to create a new folder using the name of an existing folder.
  - Expected: The creation is rejected with a clear message; only one folder with that name exists.

## Interaction

- [ ] IX-01: Search results update instantly as you type
  - Action: Type a search query character by character into the search box.
  - Expected: The notes list updates after each keystroke without page reload or loading spinner.

## Content

- [ ] CT-01: Rich-text formatting displays correctly
  - Action: Open a note containing bold, italic, and bullet-list formatted text; check both the editor and the note list/preview.
  - Expected: Bold text renders bold, italic renders italic, and lists render as bullets — matching the formatting that was applied, with no stray markup symbols shown.