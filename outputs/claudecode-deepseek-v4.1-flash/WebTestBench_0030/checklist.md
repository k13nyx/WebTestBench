# Test Checklist

## Functionality
- [ ] FT-01: Create a new rich-text note
  - Action: Click "New Note", enter title "Shopping List", type content, apply bold to text.
  - Expected: Note is created in the notes list with title "Shopping List" and bold formatting preserved.
- [ ] FT-02: Edit an existing note
  - Action: Open a default note, change its content, apply an italic/list format.
  - Expected: Changes and formatting are reflected in the note body and saved.
- [ ] FT-03: Delete a note
  - Action: Select a note and click "Delete".
  - Expected: Note is removed from the list and no longer appears in search or folder views.
- [ ] FT-04: Create a folder
  - Action: Click "New Folder", enter name "Work".
  - Expected: "Work" folder appears in the folder list and is selectable.
- [ ] FT-05: Rename a folder
  - Action: Rename folder "Work" to "Projects".
  - Expected: Folder shows as "Projects" and notes inside remain associated with it.
- [ ] FT-06: Move a note between folders
  - Action: Move a note from "Projects" into another default folder.
  - Expected: Note disappears from the source folder and appears in the destination folder.
- [ ] FT-07: Add and remove a tag on a note
  - Action: Add tag "urgent" to a note, then remove it.
  - Expected: Tag "urgent" is added then removed; note's tag list reflects each change.
- [ ] FT-08: Search by title, content, tag, and folder
  - Action: Search a term matching a note title, one matching body content, one matching a tag, and one matching a folder name.
  - Expected: Each search returns the corresponding matching note(s).
- [ ] FT-09: Filtered view (folder + tag)
  - Action: Open a folder and apply a tag filter for a tag on some notes in that folder.
  - Expected: Only notes in that folder carrying that tag are shown.

## Constraint
- [ ] CS-01: Confirm before deleting a note
  - Action: Click "Delete" on a note.
  - Expected: A confirmation prompt appears; note is deleted only after confirming.
- [ ] CS-02: Prevent empty note title
  - Action: Attempt to save a new note with an empty title.
  - Expected: Save is blocked with a validation message requiring a title.
- [ ] CS-03: Prevent duplicate folder names
  - Action: Create a folder with a name identical to an existing folder.
  - Expected: Duplicate is rejected with an error message or disallowed.
- [ ] CS-04: Empty filter result handling
  - Action: Apply a folder + tag filter combination with no matching notes.
  - Expected: An explicit "no notes found" state is shown, not a broken or blank view.

## Interaction
- [ ] IX-01: Instant save feedback
  - Action: Edit a note and observe the save state.
  - Expected: A "Saved" indicator appears promptly without a manual save trigger.
- [ ] IX-02: Editing remains responsive while offline
  - Action: Disconnect the network, edit a note, and continue typing.
  - Expected: Editor stays responsive and accepts input without delay or errors.
- [ ] IX-03: Offline change survives reconnection
  - Action: While offline, edit a note, then reconnect.
  - Expected: Offline edits are retained and not lost or overwritten after reconnect.
- [ ] IX-04: Persistence across reload
  - Action: Create notes/folders/tags, then reload the browser page.
  - Expected: All notes, folders, and tags remain present after reload.

## Content
- [ ] CT-01: Rich-text formatting renders correctly
  - Action: Open a note containing bold, italic, and list formatting.
  - Expected: Formatting renders as intended (not raw markup characters).
- [ ] CT-02: Folder and tag labels display correctly
  - Action: View the folder sidebar and a note's tag list.
  - Expected: Folder and tag names display fully and accurately match what was entered.
- [ ] CT-03: Search results show relevant snippets
  - Action: Perform a content search that matches a note body.
  - Expected: Returned results show the matching note with identifiable title/label context.