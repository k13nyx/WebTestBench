All tests executed. Here is the complete checklist with updated statuses.

# Test Result

## Functionality
- [X] FT-01: Create a new rich-text note
  - Action: Click "New Note", enter title "Shopping List", type content, apply bold to text.
  - Expected: Note is created in the notes list with title "Shopping List" and bold formatting preserved.
- [X] FT-02: Edit an existing note
  - Action: Open a default note, change its content, apply an italic/list format.
  - Expected: Changes and formatting are reflected in the note body and saved.
- [X] FT-03: Delete a note
  - Action: Select a note and click "Delete".
  - Expected: Note is removed from the list and no longer appears in search or folder views.
- [X] FT-04: Create a folder
  - Action: Click "New Folder", enter name "Work".
  - Expected: "Work" folder appears in the folder list and is selectable.
- [X] FT-05: Rename a folder
  - Action: Rename folder "Work" to "Projects".
  - Expected: Folder shows as "Projects" and notes inside remain associated with it.
- [X] FT-06: Move a note between folders
  - Action: Move a note from "Projects" into another default folder.
  - Expected: Note disappears from the source folder and appears in the destination folder.
- [X] FT-07: Add and remove a tag on a note
  - Action: Add tag "urgent" to a note, then remove it.
  - Expected: Tag "urgent" is added then removed; note's tag list reflects each change.
- [X] FT-08: Search by title, content, tag, and folder
  - Action: Search a term matching a note title, one matching body content, one matching a tag, and one matching a folder name.
  - Expected: Each search returns the corresponding matching note(s).
- [X] FT-09: Filtered view (folder + tag)
  - Action: Open a folder and apply a tag filter for a tag on some notes in that folder.
  - Expected: Only notes in that folder carrying that tag are shown.

## Constraint
- [ ] CS-01: Confirm before deleting a note
  - Action: Click "Delete" on a note.
  - Expected: A confirmation prompt appears; note is deleted only after confirming.
  - Bug Report:
    - Issue: Unresponsive Confirmation / Missing Destructive-Action Guard
    - Actual: Selecting "Delete Note" from the note's ellipsis menu deletes the note immediately. No native confirm dialog, no `role="dialog"`/`role="alertdialog"` modal, and no undo toast was detected; the note was already gone from the list right after the click.
- [ ] CS-02: Prevent empty note title
  - Action: Attempt to save a new note with an empty title.
  - Expected: Save is blocked with a validation message requiring a title.
  - Bug Report:
    - Issue: Missing Input Validation
    - Actual: A new note was created and its title cleared to empty; on typing content the note was saved with a blank title (an empty-titled `<h3>` card appeared in "All Notes"). No validation message or error styling was rendered anywhere.
- [ ] CS-03: Prevent duplicate folder names
  - Action: Create a folder with a name identical to an existing folder.
  - Expected: Duplicate is rejected with an error message or disallowed.
  - Bug Report:
    - Issue: Duplicate-Name Not Rejected
    - Actual: Entering "Work" while a "Work" folder already existed created a second "Work" folder (folder list became Personal 1, Work 2, Ideas 1, Work 0). No error message was shown and the duplicate was accepted.
- [X] CS-04: Empty filter result handling
  - Action: Apply a folder + tag filter combination with no matching notes.
  - Expected: An explicit "no notes found" state is shown, not a broken or blank view.

## Interaction
- [ ] IX-01: Instant save feedback
  - Action: Edit a note and observe the save state.
  - Expected: A "Saved" indicator appears promptly without a manual save trigger.
  - Bug Report:
    - Issue: Missing Save-Status Indicator
    - Actual: While typing into a note, no "Saved"/"Saving" text or toast appeared in ~20 rapid polls (120 ms intervals). The only status shown is the static "Last edited less than a minute ago" which did not change on edit.
- [X] IX-02: Editing remains responsive while offline
  - Action: Disconnect the network, edit a note, and continue typing.
  - Expected: Editor stays responsive and accepts input without delay or errors.
- [X] IX-03: Offline change survives reconnection
  - Action: While offline, edit a note, then reconnect.
  - Expected: Offline edits are retained and not lost or overwritten after reconnect.
- [X] IX-04: Persistence across reload
  - Action: Create notes/folders/tags, then reload the browser page.
  - Expected: All notes, folders, and tags remain present after reload.

## Content
- [X] CT-01: Rich-text formatting renders correctly
  - Action: Open a note containing bold, italic, and list formatting.
  - Expected: Formatting renders as intended (not raw markup characters).
- [X] CT-02: Folder and tag labels display correctly
  - Action: View the folder sidebar and a note's tag list.
  - Expected: Folder and tag names display fully and accurately match what was entered.
- [X] CT-03: Search results show relevant snippets
  - Action: Perform a content search that matches a note body.
  - Expected: Returned results show the matching note with identifiable title/label context.

---

### Summary
- **Passed:** 15 / 20
- **Failed:** 5 — `CS-01` (no delete confirmation), `CS-02` (empty title allowed), `CS-03` (duplicate folder names allowed), `IX-01` (no save indicator)

Note: `FT-04` was confirmed by creating a folder named "Work"; because a "Work" folder already existed by default, the app created a duplicate rather than rejecting it — this is reported as the `CS-03` failure. Search was found to be scoped to the active folder view when a folder is selected (global in "All Notes"); results were correct in both contexts, so no item was failed on that basis.