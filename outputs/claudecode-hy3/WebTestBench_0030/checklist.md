# Test Checklist

## Functionality
- [ ] FT-01: Create a rich-text note
  - Action: Click "New Note", enter a title and content with formatting (e.g., bold text), then save/create.
  - Expected: The note appears in the notes list with its title, content, and formatting preserved.

- [ ] FT-02: Edit an existing note
  - Action: Open an existing note, change its title and content, then save.
  - Expected: The changes are reflected when the note is reopened.

- [ ] FT-03: Delete a note
  - Action: Select a note and click "Delete", then confirm.
  - Expected: The note is removed from the list and can no longer be opened.

- [ ] FT-04: Create a folder
  - Action: Click "New Folder", enter a folder name, and confirm.
  - Expected: The folder appears in the folder list/sidebar.

- [ ] FT-05: Rename a folder
  - Action: Select a folder, choose "Rename", enter a new name, and confirm.
  - Expected: The folder shows the new name and its contained notes remain associated with it.

- [ ] FT-06: Move a note to another folder
  - Action: Open a note, use "Move to folder" and select a different folder.
  - Expected: The note now appears under the target folder and no longer under the original.

- [ ] FT-07: Add a tag to a note
  - Action: Open a note, enter a new tag in the tags field and add it.
  - Expected: The tag appears on the note and becomes available as a filter.

- [ ] FT-08: Remove a tag from a note
  - Action: Open a note and remove one of its existing tags.
  - Expected: The tag no longer appears on the note.

- [ ] FT-09: Search notes by title and content
  - Action: Type a word present in a note's title or body into the search box.
  - Expected: Only notes containing that word in their title or content are listed.

- [ ] FT-10: Search notes by tag
  - Action: Select or type a tag in search/filter.
  - Expected: Only notes that have that tag are listed.

- [ ] FT-11: View notes filtered by folder and tag
  - Action: Select a folder, then apply a specific tag filter.
  - Expected: Only notes that are both in that folder and have that tag are shown.

## Constraint
- [ ] CS-01: Notes persist after page reload/revisit
  - Action: Create a note, then reload the page (or close and reopen the app).
  - Expected: The note is still present with its data intact.

- [ ] CS-02: Non-matching search yields a graceful empty state
  - Action: Search for a term that matches no note.
  - Expected: An empty-state message is shown; the app does not error or crash.

- [ ] CS-03: A note cannot have duplicate tags
  - Action: Attempt to add a tag that the note already has.
  - Expected: The tag is not added a second time; the note shows it only once.

## Interaction
- [ ] IX-01: Note edits are instant (auto-save)
  - Action: Type into a note's content field.
  - Expected: The content is saved/updated without requiring a manual save action.

- [ ] IX-02: Success feedback after creating/saving a note
  - Action: Create a new note.
  - Expected: A success indicator (toast or message) confirms the note was saved.

- [ ] IX-03: Edits made offline are safe and retained
  - Action: Disconnect the internet, edit a note, then reload the page.
  - Expected: The offline edit is retained with no data loss.

## Content
- [ ] CT-01: Rich-text formatting renders correctly
  - Action: Create a note using bold, italic, and lists, then view it.
  - Expected: Formatting (bold, italics, lists) displays correctly in the note.

- [ ] CT-02: UI labels and icons match the note-management theme
  - Action: Inspect the main screen (folders, tags, search, notes areas).
  - Expected: All labels and icons (folder, tag, search, note) are relevant and clearly labeled.