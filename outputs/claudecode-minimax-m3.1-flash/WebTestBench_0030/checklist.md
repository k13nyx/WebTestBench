# Test Checklist

## Functionality
- [ ] FT-01: User can create a new note with a title and body
  - Action: Click the "New Note" control, type a title and body text, save/submit the note.
  - Expected: The note is created, appears in the notes list with its title, and opens in the editor with the entered content.

- [ ] FT-02: Notes support rich-text formatting
  - Action: In the note editor, apply bold, italic, and a list format to portions of the note body and save.
  - Expected: The formatted content is preserved and rendered with the applied styling (bold text bold, list displayed as a list) when the note is reopened.

- [ ] FT-03: User can edit an existing note
  - Action: Open an existing note, change its title and body text, and save.
  - Expected: The updated title and body are shown in the notes list and editor; the previous content is fully replaced.

- [ ] FT-04: User can delete a note
  - Action: Select an existing note and invoke the delete action, confirming the deletion.
  - Expected: The note is removed from the notes list and from any folder/tag-filtered view it appeared in.

- [ ] FT-05: User can create a folder
  - Action: Use the folder/new-folder control in the sidebar to create a folder with a name.
  - Expected: The folder appears in the sidebar folder list and can be selected to filter notes.

- [ ] FT-06: User can move a note between folders
  - Action: Open a note that belongs to Folder A, change its folder to Folder B using the note's folder control, and save.
  - Expected: The note is listed under Folder B and no longer under Folder A.

- [ ] FT-07: User can rename a folder
  - Action: Invoke rename on an existing folder, enter a new name, and confirm.
  - Expected: The sidebar shows the new folder name, and all notes previously in that folder remain in it under the new name.

- [ ] FT-08: User can add a tag to a note
  - Action: Open a note and add a tag (via the tag control or by typing a new tag name).
  - Expected: The tag is displayed on the note and is listed among the application's tags.

- [ ] FT-09: User can remove a tag from a note
  - Action: Open a tagged note and remove one of its tags using the tag control.
  - Expected: The tag no longer appears on the note, and the note no longer appears in that tag's filtered view.

- [ ] FT-10: User can search notes by title
  - Action: Type a word that appears in an existing note's title (and not in any body) into the search field.
  - Expected: Only the note with that title is returned in the results list.

- [ ] FT-11: User can search notes by body content
  - Action: Type a word that appears only in an existing note's body text into the search field.
  - Expected: The note containing that text in its body is returned in the results list.

- [ ] FT-12: User can search notes by tag
  - Action: Type an existing tag name into the search field.
  - Expected: All notes carrying that tag are returned, and notes without the tag are excluded.

- [ ] FT-13: User can search notes by folder
  - Action: Type an existing folder name into the search field.
  - Expected: All notes assigned to that folder are returned, and notes in other folders are excluded.

- [ ] FT-14: User can view notes filtered by folder combined with a specific tag
  - Action: Select a folder and additionally apply a specific tag filter within it.
  - Expected: The list shows only notes that are both in the selected folder and carry the selected tag; notes in the folder without the tag and notes with the tag in other folders are not shown.

## Constraint
- [ ] CS-01: Notes persist in the browser after leaving and revisiting the page
  - Action: Create/edit a note, then reload the page or close and reopen the browser at the same URL.
  - Expected: All notes, their body text, folder assignments, and tags are still present and unchanged.

- [ ] CS-02: Edits made while the internet connection is unavailable are not lost
  - Action: Disconnect the network (disable the network adapter / set the browser offline), edit a note's title and body, save, then restore the connection and reload the page.
  - Expected: The edit is applied and saved without an error blocking the save, no user input is discarded, and the edited content is intact after reload; no data-loss or unsaved-changes warning is shown.

- [ ] CS-03: A note's tag/folder filters never produce an inconsistent result set
  - Action: Apply a folder filter and a tag filter together, then remove the tag from one of the listed notes and rename the folder.
  - Expected: The list updates immediately to reflect the change (the untagged note is dropped from the filtered list), and the remaining notes stay under the renamed folder without duplication or disappearance.

## Interaction
- [ ] IX-01: Search results update as the user types and can be cleared
  - Action: Type progressively into the search field, observe the results list, then clear the field.
  - Expected: The result list re-renders on each keystroke to match the current query, and clearing the search restores the unfiltered list of all notes.

- [ ] IX-02: The interface gives immediate feedback for save, delete, rename, and tag changes
  - Action: Perform a note save, note delete, folder rename, and tag addition in turn, observing the interface after each.
  - Expected: Each action produces immediate visible feedback (e.g., updated list item, removed item, renamed folder label, updated tag label, and/or a status/toast message) with no manual refresh needed.

## Content
- [ ] CT-01: Displayed note and organization content matches exactly what the user entered
  - Action: Create notes, folders, and tags with distinctive names (including mixed case, punctuation, and a non-ASCII character), then review the sidebar, tags list, notes list, and note editor.
  - Expected: Every title, body text, folder name, and tag name is displayed exactly as entered — same characters, case, punctuation, and no truncation, placeholder, or garbled characters.