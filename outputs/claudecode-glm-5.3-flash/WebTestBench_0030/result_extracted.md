# Test Result

## Functionality
- [X] FT-01: Create a new rich-text note
  - Action: Click the "New Note" (or equivalent) button, type a title and body text, apply bold/italic formatting via the editor toolbar.
  - Expected: A new note is created with the entered title and rich-text formatting (bold/italic) preserved in the saved content.
- [X] FT-02: Edit an existing note
  - Action: Open a previously saved note, modify its body text, and click away or close it.
  - Expected: The note shows the updated text immediately in the editor and the change persists in the note list.
- [X] FT-03: Delete a note
  - Action: Select a note and click its "Delete" control (confirm if a dialog appears).
  - Expected: The note disappears from the note list and from any folder/tag view it previously appeared in.
- [X] FT-04: Create a folder
  - Action: Click the "New Folder" control in the sidebar and enter a folder name (e.g., "Work").
  - Expected: The new folder appears in the sidebar and can be selected as a view.
- [X] FT-05: Rename a folder
  - Action: Use the folder's rename option (e.g., context menu or edit icon) and change "Work" to "Projects".
  - Expected: The sidebar shows the new name, and notes inside remain in the renamed folder.
- [X] FT-06: Move a note between folders
  - Action: Open a note (or use its list item menu) and change its folder from "Projects" to another folder, or drag it onto the target folder.
  - Expected: The note is removed from the old folder view and appears under the new folder; its folder label updates.
- [X] FT-07: Add and remove tags on a note
  - Action: Open a note's tag control, add a tag (e.g., "urgent"), then remove another existing tag.
  - Expected: The note's visible tag list shows "urgent" and no longer shows the removed tag.
- [X] FT-08: Search by title
  - Action: Type an exact word from a known note's title into the search box.
  - Expected: The matching note appears in the results list; unrelated notes are excluded.
- [X] FT-09: Search by note content and tag
  - Action: Search for a word that exists only in a note's body content, then search for an existing tag name (e.g., "urgent").
  - Expected: The note containing that body word is returned, and all notes carrying the tag are returned.
- [X] FT-10: Filtered view — all notes in a folder with a specific tag
  - Action: Select folder "Projects", then apply/enable tag filter "urgent" while inside that folder view.
  - Expected: Only notes that are both in "Projects" and tagged "urgent" are listed.
- [X] FT-11: Notes persist after browser revisit
  - Action: Create a note, folder, and tag assignment, then fully reload the page (or close and reopen the browser tab to the same URL).
  - Expected: All notes, folders, tags, and assignments are still present with the same content.

## Constraint
- [X] CS-01: Cannot create a note without required title
  - Action: Attempt to create/save a note with an empty title.
  - Expected: Creation is blocked or the title is auto-filled with a placeholder (e.g., "Untitled"); no blank/broken note entry appears in the list.
- [ ] CS-02: Duplicate folder names are rejected
  - Action: Try to create a folder with the same name as an existing folder, and try renaming a folder to an existing folder's name.
  - Expected: The action is rejected with a clear error (e.g., "A folder with this name already exists"); no duplicate folder is created.
  - Bug Report:
    - Issue: Missing validation — duplicate folder creation accepted silently
    - Actual: Creating a second folder named "Work" (an existing folder) succeeded with no error message; the sidebar then listed two "Work" folders simultaneously ("Work 2" and "Work 0"). No "already exists" feedback of any kind was shown.
- [ ] CS-03: Deleting a folder handles contained notes safely
  - Action: Delete a folder that currently contains notes.
  - Expected: A confirmation is shown; after deletion the notes are either deleted with it or moved to a default/unfiled location — no notes disappear silently into an unreachable state, and the folder is removed from the sidebar.
  - Bug Report:
    - Issue: Destructive action without confirmation
    - Actual: Deleting the "Ideas" folder (containing 1 note) executed immediately upon clicking the Delete menu item — no confirmation dialog appeared (0 dialogs detected). The contained note was preserved (it remained visible in All Notes), and the folder was removed from the sidebar, but the required confirmation step is absent, making accidental folder deletion possible with a single click.
- [X] CS-04: Search with no matches shows an empty state, not errors
  - Action: Type a gibberish query (e.g., "zzzqqqxxx") into the search box.
  - Expected: A "No notes found" (or equivalent) empty-state message is displayed; no crashing, blank screen, or stale results from a previous query.

## Interaction
- [X] IX-01: Editor responds instantly to typing and formatting
  - Action: Type continuously in the note editor and toggle bold/italic/heading while typing.
  - Expected: Each keystroke and formatting change appears in the editor with no perceptible lag or page reload.
- [X] IX-02: Offline/unstable connection does not lose edits
  - Action: While editing a note, disconnect the network (e.g., DevTools "Offline" mode), make further edits, wait a few seconds, then restore the connection.
  - Expected: An offline indicator may appear, no error dialog blocks editing, and all edits made offline are retained after reconnecting and after a page reload.
- [X] IX-03: Selecting a folder, tag, or search result updates the view immediately
  - Action: Click a folder in the sidebar, then a tag filter, then a note in the results.
  - Expected: The note list and the opened note update instantly on each click without a full page reload.

## Content
- [X] CT-01: Notes list shows meaningful metadata
  - Action: View the notes list/sidebar with several saved notes.
  - Expected: Each note entry displays its title, its assigned folder and/or tags, and content is displayed with formatting intact when opened (no raw HTML/markdown code shown to the user).
- [X] CT-02: UI labels and iconography match a notes app
  - Action: Inspect buttons, icons, and headers across the app (sidebar, editor, search bar).
  - Expected: All labels/icons are relevant to note-taking (e.g., folder, tag, search, trash icons); no placeholder text like "Lorem ipsum", broken images, or off-topic content.
