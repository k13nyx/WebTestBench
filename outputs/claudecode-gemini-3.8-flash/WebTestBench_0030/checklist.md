# Test Checklist

## Functionality
- [ ] FT-01: Create a new rich-text note
  - Action: Click the "+ New Note" button, enter a title, type formatted text (bold and headings) in the editor, and click "Save".
  - Expected: The note is created and appears in the notes list with its title and rich-text formatting preserved.
- [ ] FT-02: Edit existing rich-text note content
  - Action: Select an existing note, apply italic styling and a bulleted list to the body text, and update the title.
  - Expected: The note updates immediately with new formatting reflected in both the editor and preview.
- [ ] FT-03: Delete an existing note
  - Action: Select an existing note, click the "Delete Note" button, and confirm the prompt.
  - Expected: The note is removed from the notes list and editor, and is no longer accessible.
- [ ] FT-04: Rename an existing folder
  - Action: Click the "Rename" option on an existing folder in the sidebar, enter a new folder name, and confirm.
  - Expected: The folder name updates in the sidebar and reflects across all notes assigned to it.
- [ ] FT-05: Move a note between folders
  - Action: Open an existing note, select a different folder from the folder dropdown menu, and confirm.
  - Expected: The note is relocated to the target folder and no longer appears under the original folder.
- [ ] FT-06: Add a tag to a note
  - Action: Select an existing note, enter a tag name into the "Add Tag" input field, and press Enter.
  - Expected: The tag pill appears attached to the note and displays in the note metadata.
- [ ] FT-07: Remove a tag from a note
  - Action: Click the "x" remove icon on an existing tag attached to a note.
  - Expected: The tag pill is removed from the note and disappears from its metadata.
- [ ] FT-08: Search notes across title, content, tags, and folder
  - Action: Enter a search query in the search bar that matches keywords from a note's title, body, tag, or folder name.
  - Expected: The notes list filters in real time to show only notes containing matching text.
- [ ] FT-09: Filter notes by combined folder and tag
  - Action: Select a specific folder from the sidebar navigation and click an active tag filter chip.
  - Expected: The list displays only notes that simultaneously belong to the selected folder and contain the selected tag.
- [ ] FT-10: Persist notes across browser reload
  - Action: Make edits to an existing note, refresh the browser window, and inspect the note.
  - Expected: All recent note edits, folder structures, and tags remain intact exactly as left before reload.
- [ ] FT-11: Offline note editing and preservation
  - Action: Disconnect internet connectivity (offline mode), edit note content in the editor, and navigate between notes.
  - Expected: Edits are applied and saved locally without errors, data loss, or blocking interruptions.

## Constraint
- [ ] CS-01: Prevent empty or duplicate folder names
  - Action: Attempt to rename a folder to an empty string or to a name identical to an existing folder.
  - Expected: The system rejects the submission, retains the original name, and shows an inline error message.
- [ ] CS-02: Prevent accidental note deletion via cancellation
  - Action: Click the "Delete Note" button on an active note and click "Cancel" in the confirmation dialog.
  - Expected: The dialog closes, and the note remains intact in the notes list and editor.
- [ ] CS-03: Empty state when search or filter yields no results
  - Action: Enter a random non-matching string into the search input.
  - Expected: The notes list displays a clear "No notes found" empty state message instead of broken UI elements.

## Interaction
- [ ] IX-01: Visual auto-save feedback
  - Action: Type changes into the active note editor.
  - Expected: A save status indicator dynamically changes from "Saving..." to "Saved" upon keystroke completion.
- [ ] IX-02: Offline status indicator
  - Action: Disconnect the browser's internet connection.
  - Expected: An "Offline Mode" status banner or badge appears in the header without disrupting current editing.
- [ ] IX-03: Active note list item highlighting
  - Action: Click on a note card in the notes list.
  - Expected: The selected note card visually changes to an active/highlighted background state distinguishing it from unselected notes.

## Content
- [ ] CT-01: Rich-text toolbar control visibility and tooltips
  - Action: Inspect the rich-text formatting toolbar in the note editor.
  - Expected: Standard editing controls (Bold, Italic, Headings, Bullet List, Numbered List) display with correct icons and hover tooltips.
- [ ] CT-02: Note card metadata display
  - Action: Inspect any note card listed in the notes list panel.
  - Expected: The card clearly displays the note title, text snippet preview, assigned folder name, tag pills, and last modified timestamp.