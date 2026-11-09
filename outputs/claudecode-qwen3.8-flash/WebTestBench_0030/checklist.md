# Test Checklist

## Functionality
- [ ] FT-01: User can create a rich-text note and it appears in the notes list
  - Action: Click the "New Note" / "Add Note" button, type a title, type body text, click "Save".
  - Expected: A new note with that title is created and listed in the current folder's note list.
- [ ] FT-02: Rich-text formatting (bold/italic) is applied and persists
  - Action: In the editor, select a word, apply **Bold** and *Italic* via the toolbar, save, reopen the note.
  - Expected: The formatting is preserved in the editor and the note view (not stripped to plain text).
- [ ] FT-03: User can edit an existing note
  - Action: Open a default note, change its title and body text, click "Save".
  - Expected: The note list and note view show the updated title and text; no duplicate note is created.
- [ ] FT-04: User can delete a note
  - Action: Select a note, click "Delete", confirm the dialog.
  - Expected: The note is permanently removed and no longer appears in any folder, tag, or search view.
- [ ] FT-05: Search returns notes matching title and body content
  - Action: Type a known word that appears only in a note's body, and separately a word appearing only in a title, into the search box.
  - Expected: The matching notes are listed for each query; non-matching notes are excluded.
- [ ] FT-06: Notes can be found by tag
  - Action: Click a tag (e.g. a tag shown on a default note) or enter the tag name in search.
  - Expected: Only notes carrying that tag are shown.
- [ ] FT-07: Notes can be found by folder
  - Action: Click a folder in the folder sidebar.
  - Expected: The note list shows only notes inside that folder.
- [ ] FT-08: User can rename a folder
  - Action: Open the folder options menu, choose "Rename", change the folder name, save.
  - Expected: The folder shows the new name in the sidebar, and its notes still appear under it.
- [ ] FT-09: User can move a note between folders
  - Action: Select a note in Folder A, choose "Move to" and pick Folder B.
  - Expected: The note is removed from Folder A's list and now appears in Folder B's list.
- [ ] FT-10: User can add and remove tags on a note
  - Action: On a note, add a new tag via the tag input; then click the "x" on an existing tag to remove it.
  - Expected: The added tag is shown on the note and found via tag filter; the removed tag no longer appears or filters.
- [ ] FT-11: Combined filtered view (folder + specific tag) works
  - Action: Open a folder, then apply a tag filter while in that folder.
  - Expected: Only notes that are BOTH in that folder AND carry that tag are shown; folder-only or tag-only notes are hidden.
- [ ] FT-12: Notes persist in the browser across reloads
  - Action: Create a note, then reload the page (F5) in the same browser.
  - Expected: The created note (title, body, formatting, folder, tags) is still present after reload.
- [ ] FT-13: Editing is safe and instant when the connection is lost
  - Action: Open DevTools → set network to "Offline", edit a note and type/save, then restore the connection and reload.
  - Expected: No error blocks editing while offline, edits are kept locally, and the changes survive reconnection/reload (no lost data).

## Constraint
- [ ] CS-01: An empty note cannot be created
  - Action: Click "New Note", leave title and body empty, click "Save".
  - Expected: The note is not saved (validation message or disabled Save); no blank note is added to the list.
- [ ] CS-02: A deleted note leaves no trace in any view
  - Action: Delete a note that has a tag and lives in a folder, then open that folder, that tag filter, and search its title.
  - Expected: The deleted note does not appear in the folder, tag, or search results.

## Interaction
- [ ] IX-01: Search results update live as the user types
  - Action: In the search box, type a query one character at a time without pressing Enter.
  - Expected: The note list filters down progressively in real time as the query grows.
- [ ] IX-02: User gets feedback on create/save/delete
  - Action: Create a note, edit/save a note, and delete a note.
  - Expected: A visible confirmation (toast or "Saved" indicator) appears after create/save, and a confirmation dialog appears before delete.

## Content
- [ ] CT-01: Default seed data is present and relevant to a notes app
  - Action: Open the app fresh.
  - Expected: At least one folder, one tag, and one rich-text note with meaningful title/body are pre-loaded (no broken placeholders).
- [ ] CT-02: Empty-state and no-results messages are shown
  - Action: Search for a string that matches nothing.
  - Expected: A clear "No results" / "No notes found" message is displayed instead of a blank screen or an error.