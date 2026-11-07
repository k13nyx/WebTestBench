# Test Checklist

## Functionality

- [ ] FT-01: Create a new rich-text note with formatted content
  - Action: Click "New Note" (or equivalent), type a title, type body text, apply Bold to one word and a bulleted list to one line.
  - Expected: Note is created and appears in the note list; its body renders the word in bold and the line as a bulleted list.

- [ ] FT-02: Edit an existing note's title and body
  - Action: Select an existing default note, change its title to "Edited Test Note", and add a new line of text to its body.
  - Expected: The note list shows the new title and the editor displays the added line; the change is still present after navigating to another note and back.

- [ ] FT-03: Delete an existing note
  - Action: Select an existing default note, click Delete (or the delete/trash icon), and confirm if prompted.
  - Expected: The note is removed from the note list and no longer appears anywhere in the app.

- [ ] FT-04: Create a new folder
  - Action: Click "New Folder" (or equivalent) in the folder area, enter "Test Folder", and confirm.
  - Expected: "Test Folder" appears in the folder list and is selectable with an empty note list.

- [ ] FT-05: Rename an existing folder
  - Action: Select an existing default folder, trigger rename (context menu or rename control), change its name to "Renamed Folder", and confirm.
  - Expected: The folder list shows "Renamed Folder" in place of the old name, and the notes inside it are unchanged and still listed when that folder is selected.

- [ ] FT-06: Move a note between folders
  - Action: Select an existing default note, use the move/change-folder control to move it to a different existing folder, then select that target folder.
  - Expected: The note is listed inside the target folder and is no longer listed under its previous folder.

- [ ] FT-07: Add a tag to a note
  - Action: Select an existing default note, use the tag control to add the tag "testtag" (create it if the control allows new tags), and save/apply.
  - Expected: "testtag" is displayed on the note (in the editor and/or note list entry) and the note becomes findable under that tag.

- [ ] FT-08: Remove a tag from a note
  - Action: On the note tagged in FT-07, click the remove control (x) on the "testtag" chip.
  - Expected: The "testtag" chip disappears from the note and the note no longer appears when filtering by "testtag".

- [ ] FT-09: Search matches note titles and note content
  - Action: Type a word that exists only in an existing note's title into the search field, note the results, then clear it and type a word that exists only inside another note's body.
  - Expected: The first query returns the title-matching note; the second query returns the body-matching note; results list only matching notes.

- [ ] FT-10: Filter notes by folder
  - Action: Click an existing folder that contains at least one default note.
  - Expected: Only the notes belonging to that folder are listed, and the view is labeled with the folder name.

- [ ] FT-11: Filter notes by tag
  - Action: Click an existing tag that is assigned to at least one default note.
  - Expected: Only the notes carrying that tag are listed, and the view is labeled with the tag name.

- [ ] FT-12: Combined filtered view: all notes in a folder that also have a specific tag
  - Action: Select a folder containing several notes, then within that view select a tag that is on only some of those notes.
  - Expected: The list shows exactly the notes that are both in that folder and carry that tag; notes in the folder without the tag and notes with the tag outside the folder are excluded.

- [ ] FT-13: Notes persist in the browser across a page reload
  - Action: Create a note titled "Persistence Check", then reload the page (F5) in the same browser.
  - Expected: "Persistence Check" is still present in the note list after reload, along with any folders, tags, and edits made during this session.

## Constraint

- [ ] CS-01: Editing remains safe and is not lost when the internet connection is unavailable
  - Action: Switch the browser to offline mode, edit an existing note's body, create a new note, wait a few seconds, then reload the page while still offline.
  - Expected: No data-loss error or "failed to save" blocking message appears; both the edit and the new note are still present after the offline reload, and remain present after going back online.

- [ ] CS-02: A deleted note is removed from every view
  - Action: Delete a note that belongs to a folder and carries a tag, then check All Notes, its folder view, its tag filter, and a search for its title.
  - Expected: The note appears in none of those views.

- [ ] CS-03: A search with no matches shows an empty state, and clearing the query restores the list
  - Action: Type "zzzzzznomatch" into the search field, observe the result area, then clear the search field.
  - Expected: A "no notes found" style message (not a blank/broken area or error) is shown, and clearing the query restores the full default note list.

## Interaction

- [ ] IX-01: Editing feels instant and confirms a saved state without a manual save step
  - Action: Click into a note's body and type a sentence continuously, watching for any save button press, spinner, or lag between keystroke and on-screen character.
  - Expected: Characters appear immediately with no perceptible delay or blocking spinner, and a save status indicator (e.g., "Saved" / "All changes saved") appears within a few seconds without the tester clicking Save.

- [ ] IX-02: Selecting a note highlights it and loads its content
  - Action: Click a second note in the note list, then click back to the first note.
  - Expected: The clicked note is visually highlighted/active in the list each time, and the editor and title area update to that note's content.

## Content

- [ ] CT-01: The rich-text editor provides relevant, labeled formatting controls
  - Action: Inspect the editor toolbar and hover/click each control (e.g., Bold, Italic, list).
  - Expected: Controls are labeled or show tooltips matching their function, each applies the corresponding formatting, and no placeholder, "lorem ipsum", or unrelated/off-topic text appears in the UI.

- [ ] CT-02: Default notes, folders, and tags display real, consistent content
  - Action: Browse the default note list, folder list, and tag list; open at least two default notes.
  - Expected: Every entry shows a real title and content (no empty/placeholder rows, no broken image or missing icons), and the note count shown next to each folder/tag matches the number of notes actually listed when it is selected.