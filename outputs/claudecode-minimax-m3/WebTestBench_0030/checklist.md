# Test Checklist

## Functionality
- [ ] FT-01: Create a new rich-text note from default data
  - Action: Click the "New Note" / "Create Note" button, enter a title and body text, then save.
  - Expected: The new note appears in the notes list with the entered title, and opens in the editor.

- [ ] FT-02: Edit an existing note and save changes
  - Action: Open an existing note, modify its title or body content, then save.
  - Expected: The note's updated content is visible after saving and on re-opening the note.

- [ ] FT-03: Delete an existing note
  - Action: Select an existing note and click the "Delete" option.
  - Expected: The note is removed from the notes list and no longer accessible.

- [ ] FT-04: Create a new folder
  - Action: Click the "New Folder" / "Create Folder" button and enter a folder name.
  - Expected: The new folder appears in the folders sidebar/list and can be selected.

- [ ] FT-05: Rename an existing folder
  - Action: Right-click or open options on an existing folder and select "Rename", then enter a new name.
  - Expected: The folder's new name is displayed in the sidebar; notes inside remain intact.

- [ ] FT-06: Move a note from one folder to another
  - Action: Drag-and-drop or use the "Move to" option on an existing note to select a different folder.
  - Expected: The note now appears in the destination folder and not in the original folder.

- [ ] FT-07: Add a tag to an existing note
  - Action: Open an existing note and add a new tag (e.g., "work") via the tag input.
  - Expected: The tag is saved on the note and visible in the note's tag list.

- [ ] FT-08: Remove a tag from an existing note
  - Action: Open a note that has at least one tag and click the remove (×) icon on that tag.
  - Expected: The tag is removed from the note and no longer appears in the note's tag list.

- [ ] FT-09: Search notes by title
  - Action: Type a unique word from an existing note's title into the search box.
  - Expected: Only notes whose title contains the search term are shown in the results.

- [ ] FT-10: Search notes by body content
  - Action: Type a unique word that exists only in an existing note's body content into the search box.
  - Expected: The matching note appears in the search results.

- [ ] FT-11: Search notes by tag
  - Action: Type or click an existing tag in the search/filter area.
  - Expected: Only notes carrying that tag are shown in the results.

- [ ] FT-12: Search/filter notes by folder
  - Action: Select a folder from the folders panel.
  - Expected: Only notes that belong to the selected folder are displayed.

- [ ] FT-13: Filter notes by folder + specific tag combination
  - Action: Select a folder, then apply a tag filter that does not exist in every note of that folder.
  - Expected: Only notes within the selected folder that also carry the selected tag are shown.

- [ ] FT-14: Notes persist after page reload
  - Action: Create a new note (or edit an existing one), then fully reload the browser page.
  - Expected: The note (with all edits, folder placement, and tags) is still present after reload.

## Constraint
- [ ] CS-01: Confirmation required before deleting a note
  - Action: Click "Delete" on an existing note.
  - Expected: A confirmation dialog appears; the note is only deleted after the user confirms.

- [ ] CS-02: Folder creation requires a non-empty name
  - Action: Click "New Folder" and attempt to save with an empty (or whitespace-only) name.
  - Expected: The folder is not created and an inline validation message is shown.

- [ ] CS-03: Note edits succeed while offline
  - Action: Disable the network connection (e.g., via DevTools "Offline"), then create or edit a note and save.
  - Expected: The note is saved successfully and remains visible after going back online and reloading.

## Interaction
- [ ] IX-01: Editing a note autosaves / shows save indicator
  - Action: Type changes into an open note and pause typing for a few seconds without manually clicking save.
  - Expected: A "Saved" status, autosave indicator, or equivalent appears, and reloading shows the typed content.

- [ ] IX-02: Filtered view updates immediately when folder/tag selection changes
  - Action: With the notes list visible, change the selected folder, then change the active tag filter.
  - Expected: The notes list updates without requiring a manual refresh, matching the new criteria each time.

## Content
- [ ] CT-01: Rich-text formatting renders correctly after save and reload
  - Action: Create a note applying at least two rich-text formats (e.g., bold and a bullet list), save it, then reload the page and reopen the note.
  - Expected: The formatted text is displayed with the applied styling preserved (bold appears bold, list appears as a list).