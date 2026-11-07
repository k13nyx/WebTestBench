# Test Result

## Functionality
- [X] FT-01: Create a rich-text note
  - Action: Click "New Note", enter a title and content with formatting (e.g., bold text), then save/create.
  - Expected: The note appears in the notes list with its title, content, and formatting preserved.
  - Note: The button is labeled "New"; creating immediately adds an "Untitled Note" that auto-saves. Bold formatting applied via the toolbar was preserved (rendered as `<strong>`).

- [X] FT-02: Edit an existing note
  - Action: Open an existing note, change its title and content, then save.
  - Expected: The changes are reflected when the note is reopened.

- [X] FT-03: Delete a note
  - Action: Select a note and click "Delete", then confirm.
  - Expected: The note is removed from the list and can no longer be opened.

- [X] FT-04: Create a folder
  - Action: Click "New Folder", enter a folder name, and confirm.
  - Expected: The folder appears in the folder list/sidebar.
  - Note: Triggered via the folder "+" button; an inline "Folder name..." field appears; Enter confirms. Created "QA Folder" (later renamed).

- [X] FT-05: Rename a folder
  - Action: Select a folder, choose "Rename", enter a new name, and confirm.
  - Expected: The folder shows the new name and its contained notes remain associated with it.

- [X] FT-06: Move a note to another folder
  - Action: Open a note, use "Move to folder" and select a different folder.
  - Expected: The note now appears under the target folder and no longer under the original.

- [X] FT-07: Add a tag to a note
  - Action: Open a note, enter a new tag in the tags field and add it.
  - Expected: The tag appears on the note and becomes available as a filter.
  - Note: New tags are created via the sidebar "Create New Tag" dialog (there is no inline tag-entry field directly on the note); once created, the tag is toggled onto the note via the note's "Tags" menu and becomes an available filter (sidebar count incremented). The end result matches the expected behavior.

- [X] FT-08: Remove a tag from a note
  - Action: Open a note and remove one of its existing tags.
  - Expected: The tag no longer appears on the note.

- [X] FT-09: Search notes by title and content
  - Action: Type a word present in a note's title or body into the search box.
  - Expected: Only notes containing that word in their title or content are listed.

- [X] FT-10: Search notes by tag
  - Action: Select or type a tag in search/filter.
  - Expected: Only notes that have that tag are listed.

- [X] FT-11: View notes filtered by folder and tag
  - Action: Select a folder, then apply a specific tag filter.
  - Expected: Only notes that are both in that folder and have that tag are shown.
  - Note: Verified with "Work" folder + "Idea" tag → only the single note that is both in Work AND has the Idea tag remained (the other Idea-tagged note, in a different folder, was correctly excluded), confirming the filters combine as an AND/intersection.

## Constraint
- [X] CS-01: Notes persist after page reload/revisit
  - Action: Create a note, then reload the page (or close and reopen the app).
  - Expected: The note is still present with its data intact.
  - Note: Verified after the IX-03 offline cycle — reloading the page retained the created note, the renamed folder ("QA Folder Renamed"), and the created tag ("QANewTag").

- [X] CS-02: Non-matching search yields a graceful empty state
  - Action: Search for a term that matches no note.
  - Expected: An empty-state message is shown; the app does not error or crash.

- [X] CS-03: A note cannot have duplicate tags
  - Action: Attempt to add a tag that the note already has.
  - Expected: The tag is not added a second time; the note shows it only once.
  - Note: At the note level, tags are a single toggle set (a tag shows a checkmark when applied; clicking it removes rather than duplicates), so duplicates are impossible. However, a related defect was found: the **"Create New Tag" dialog permits creating a tag whose name duplicates an existing tag** (e.g., a second tag named "Idea" was successfully created). This should be guarded to prevent duplicate tag names at the global level.

## Interaction
- [X] IX-01: Note edits are instant (auto-save)
  - Action: Type into a note's content field.
  - Expected: The content is saved/updated without requiring a manual save action.

- [ ] IX-02: Success feedback after creating/saving a note
  - Action: Create a new note.
  - Expected: A success indicator (toast or message) confirms the note was saved.
  - Bug Report:
    - Issue: Missing success feedback / No toast on save
    - Actual: After creating, editing, and deleting notes, no success toast or confirmation message appears in the notifications region. The only implicit feedback is the "Last edited …" timestamp and the note's appearance in the list. No explicit "Note saved" indicator is shown.

- [X] IX-03: Edits made offline are safe and retained
  - Action: Disconnect the internet, edit a note, then reload the page.
  - Expected: The offline edit is retained with no data loss.
  - Note: The offline edit was retained and present after restoring the connection and reloading (verified: "[OFFLINE-EDIT]" content persisted). One limitation observed: reloading/reopening the app while fully offline is not possible (the SPA fails to load its assets with `ERR_INTERNET_DISCONNECTED` because there is no service worker / offline app shell). Edits made in an already-open session are safe, but the app cannot be launched with no connectivity.

## Content
- [X] CT-01: Rich-text formatting renders correctly
  - Action: Create a note using bold, italic, and lists, then view it.
  - Expected: Formatting (bold, italics, lists) displays correctly in the note.
  - Note: Bold rendered as `<strong>`; the seed "Book Recommendations" note demonstrates headings (H1/H2), bold, and ordered/unordered lists rendering correctly in the editor.

- [X] CT-02: UI labels and icons match the note-management theme
  - Action: Inspect the main screen (folders, tags, search, notes areas).
  - Expected: All labels and icons (folder, tag, search, note) are relevant and clearly labeled.
  - Note: All elements are clearly themed — "Notes" title, "All Notes", "Folders" (with folder icons), "Tags" (with tag icons), "Search notes…" input with search icon, "New" button, per-note title/content/tag/timestamp, and a formatting toolbar (Bold, Italic, H1–H3, Bullet, Numbered, Quote). Minor dev-only console warnings (React DOM nesting, missing dialog `aria-description`) were observed but do not affect labeling clarity.
