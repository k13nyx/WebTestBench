# Test Result

## Functionality

- [X] FT-01: Create a rich-text note
  - Action: Select **“New Note”**, enter a title and body text, and apply available rich-text formatting such as bold, italic, a heading, and a bulleted list.
  - Expected: The note is created, appears in the notes list, and displays the entered title and formatted content.

- [X] FT-02: Edit an existing note
  - Action: Open an existing note, change its title and body content, then leave and reopen the note.
  - Expected: The updated title and content are displayed exactly as entered.

- [X] FT-03: Delete a note
  - Action: Open an existing note, select **“Delete”**, and confirm the deletion if prompted.
  - Expected: The note is removed from the notes list and cannot be found through search or folder views.

- [X] FT-04: Create and rename a folder
  - Action: Create a folder using **“New Folder”**, then use **“Rename”** to change its name.
  - Expected: The folder appears with the new name, and its notes remain associated with it.

- [X] FT-05: Move a note between folders
  - Action: Move an existing note from one folder to another using the note’s folder control or **“Move to Folder”** action.
  - Expected: The note appears in the destination folder and no longer appears in the previous folder.

- [X] FT-06: Add and remove tags
  - Action: Add a tag to an existing note, verify it is displayed, then remove the same tag.
  - Expected: The tag appears on the note after adding and is absent from the note after removal.

- [X] FT-07: Search by note title
  - Action: Enter a unique word from an existing note’s title in the **“Search”** field.
  - Expected: The matching note is displayed in the results.

- [X] FT-08: Search by note content
  - Action: Enter a unique word or phrase that appears only in an existing note’s body content in the **“Search”** field.
  - Expected: The note containing that content is displayed in the results.

- [X] FT-09: Search by tag and folder
  - Action: Search for a tag name and a folder name used by existing notes.
  - Expected: Notes associated with the matching tag or folder are returned, and unrelated notes are excluded.

- [X] FT-10: Filter notes by folder and tag together
  - Action: Select a folder filter and a tag filter that are both used by at least one note.
  - Expected: Only notes belonging to the selected folder and carrying the selected tag are displayed.

- [X] FT-11: Preserve notes after revisiting the page
  - Action: Create or edit a note, close or reload the webpage, and return to the notes page.
  - Expected: The note, its rich-text content, folder, and tags are still present.

- [ ] FT-12: Edit and save while offline
  - Action: Open an existing note, temporarily disable the browser’s internet connection, edit the title and content, then reload or revisit the page while still offline.
  - Expected: The edit is immediately visible and remains available after the reload or revisit.
  - Bug Report:
    - Issue: Offline page reload fails
    - Actual: While offline, reloading the notes page failed with `ERR_INTERNET_DISCONNECTED`. The edit was retained after restoring the connection and revisiting, but the page could not be reloaded or revisited successfully while still offline.

## Constraint

- [ ] CS-01: Prevent accidental note deletion
  - Action: Select **“Delete”** for an existing note and dismiss or cancel the confirmation prompt.
  - Expected: The note remains available with its original content, folder, and tags.
  - Bug Report:
    - Issue: Missing deletion confirmation
    - Actual: Selecting “Delete Note” removed the note immediately without presenting a confirmation prompt, so the deletion could not be dismissed or canceled.

- [X] CS-02: Keep combined filters consistent
  - Action: Apply a folder filter and tag filter, then inspect every displayed note.
  - Expected: Every displayed note belongs to the selected folder and has the selected tag; no note missing either condition is shown.

- [X] CS-03: Keep folder and tag assignments after editing
  - Action: Edit the content of a note that has a folder and tags, save or leave the note, and reopen it.
  - Expected: The note’s folder and tags are unchanged unless explicitly modified.

## Interaction

- [X] IX-01: Reflect edits immediately
  - Action: Type changes into a note title or body without navigating away.
  - Expected: The edited text appears immediately in the editor and the note’s visible preview or list entry updates without requiring a page refresh.

- [ ] IX-02: Show safe save state during editing
  - Action: Edit a note and observe the interface before and after the change is stored.
  - Expected: The interface provides a clear saved, saving, or offline-pending indication, and does not indicate that changes were saved when they were not.
  - Bug Report:
    - Issue: Missing save-state indication
    - Actual: No visible “saved,” “saving,” “offline,” or “pending” status was present before or after editing.

- [X] IX-03: Retain local edits through connection loss
  - Action: Begin editing a note, interrupt the internet connection during the edit, continue typing, and restore the connection.
  - Expected: No entered text disappears, and the completed local edit remains available after the connection is restored.

- [X] IX-04: Update views after note organization changes
  - Action: Add or remove a tag, rename a folder, or move a note while a list or filter view is open.
  - Expected: The visible note list, folder name, tag display, and active filter results update to reflect the change without showing stale assignments.

## Content

- [X] CT-01: Preserve rich-text content and formatting
  - Action: Create or edit a note using supported headings, bold or italic text, lists, and multiple paragraphs, then reopen it.
  - Expected: All entered text, paragraph structure, and applied formatting remain intact and readable.

- [X] CT-02: Display accurate search and organization information
  - Action: Inspect note cards, folder views, tag displays, and search results for existing notes.
  - Expected: Each note shows its correct title, relevant content preview, folder, and tags, and search results identify only notes that actually match the query.
