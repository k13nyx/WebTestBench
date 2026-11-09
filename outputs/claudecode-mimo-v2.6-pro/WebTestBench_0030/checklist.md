# Test Checklist

## Functionality
- [ ] FT-01: User can create a new note with rich-text content.
  - Action: Click the "New Note" button, type a title "Meeting notes", and type body text applying bold and bullet-list formatting via the toolbar.
  - Expected: A new note appears in the note list titled "Meeting notes"; opening it shows the body text with bold text and a bullet list rendered as rich text.

- [ ] FT-02: User can edit an existing note and changes are applied.
  - Action: Open an existing note from the list, change its title to "Updated title" and append body text "new line of text".
  - Expected: The note list shows the title "Updated title" and reopening the note shows the appended text.

- [ ] FT-03: User can delete a note.
  - Action: Select an existing note and click the "Delete" control for that note, confirming if prompted.
  - Expected: The note is removed from the note list and no longer appears in any view or search result.

- [ ] FT-04: User can create a folder and it appears in the folder list.
  - Action: Click "New Folder" (or equivalent), enter the name "Projects", and confirm.
  - Expected: A folder named "Projects" appears in the folder/sidebar list.

- [ ] FT-05: User can rename a folder.
  - Action: Select the folder "Projects", choose "Rename", enter "Work", and confirm.
  - Expected: The folder list now shows "Work" and no longer shows "Projects"; notes inside keep the same folder membership.

- [ ] FT-06: User can move a note between folders.
  - Action: Open a note in folder "Work" and use "Move to folder" to move it to a different existing folder.
  - Expected: The note disappears from "Work" and appears in the target folder; its title and content are unchanged.

- [ ] FT-07: User can add and remove tags on a note.
  - Action: Open a note, add tag "urgent" via the tag input, then remove tag "urgent" from the same note.
  - Expected: After adding, tag "urgent" is shown on the note and is available as a tag filter; after removing, the tag no longer appears on the note or in its tag list.

- [ ] FT-08: Search finds notes by title.
  - Action: Enter a word that exists in an existing note's title into the search box.
  - Expected: The matching note is listed in search results; notes without that word in the title are not listed.

- [ ] FT-09: Search finds notes by content.
  - Action: Enter a word that exists only in an existing note's body text into the search box.
  - Expected: The matching note is listed in search results.

- [ ] FT-10: Search finds notes by tag and by folder.
  - Action: Enter the name of an existing tag into search, then enter the name of an existing folder into search.
  - Expected: Tag search lists all notes carrying that tag; folder search lists all notes in that folder.

- [ ] FT-11: Filtered view shows all notes in a folder with a specific tag.
  - Action: Select folder "Work" and then filter by an existing tag applied to some but not all notes in "Work".
  - Expected: Only notes that are both in "Work" and carry that tag are shown; notes in "Work" without the tag are excluded.

- [ ] FT-12: Notes persist in the browser after revisiting.
  - Action: Create or edit a note, close the browser tab, reopen the application in a new tab.
  - Expected: All previously created/edited notes, folders, tags, and their assignments are present and unchanged.

- [ ] FT-13: Edits are saved without an internet connection and survive reconnection/reload.
  - Action: Disable the network, edit an existing note's content, re-enable the network (or reload the page).
  - Expected: The edit is accepted while offline, and after reconnection/reload the edited content is still present.

## Constraint
- [ ] CS-01: Cannot save a note with an empty title.
  - Action: Create a new note, leave the title empty, enter body text, and attempt to save/close.
  - Expected: The note is not saved with an empty title; a validation message appears or the save is blocked until a title is entered.

- [ ] CS-02: Cannot create a duplicate tag name on a note.
  - Action: On a note that already has tag "urgent", attempt to add tag "urgent" again.
  - Expected: The duplicate tag is not added; only one "urgent" tag appears on the note.

- [ ] CS-03: Deleting a folder does not leave orphaned notes unreachable.
  - Action: Delete folder "Work" that contains existing notes, confirming if prompted.
  - Expected: Either deletion is blocked while the folder contains notes, or the contained notes are moved to a visible default location (e.g., "All Notes"/"Unfileded") and remain accessible.

- [ ] CS-04: Search with a query matching nothing shows an empty result state, not an error.
  - Action: Enter a random string such as "zzzqqqxyz" into the search box.
  - Expected: An explicit empty/no-results state is shown; no error message or broken UI appears.

## Interaction
- [ ] IX-01: Editing a note updates the note list/state immediately (instant feedback).
  - Action: Type into an existing note's body and observe the UI while typing, without clicking a save button.
  - Expected: Edits are reflected/saved automatically within a second with no manual save step required, and no "unsaved changes" blocker appears.

- [ ] IX-02: Deleting a note provides confirmation or undo feedback.
  - Action: Delete a note and observe the interface immediately after.
  - Expected: A confirmation prompt is shown before deletion, or a success/undo message (e.g., toast with "Undo") appears after deletion.

- [ ] IX-03: Selecting a folder or tag filter visibly updates the note list and active filter state.
  - Action: Click folder "Work", then click an existing tag filter.
  - Expected: The note list refreshes to the filtered set, and the active folder/tag is visually indicated as selected.

## Content
- [ ] CT-01: Rich-text formatting entered in the editor is preserved and displayed as formatted content when the note is reopened.
  - Action: Create a note with a heading, bold text, an italic phrase, and a bullet list; save, navigate away, and reopen the note.
  - Expected: The reopened note displays the heading, bold, italic, and bullet list exactly as entered (no raw markup such as `**` or HTML tags shown as text).

- [ ] CT-02: Note titles, folder names, and tag names are displayed accurately wherever they appear.
  - Action: Compare a note's title, its folder name, and its tag names in the note list, editor header, sidebar, and search results.
  - Expected: All displayed names match exactly what was entered, with no truncation hiding the distinguishing text or altered characters.