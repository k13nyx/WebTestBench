# Test Checklist

## Functionality
- [ ] FT-01: Create a new note.
  - Action: Click the "New Note" button, enter title "QA Test Note", and type "Hello world" in the body.
  - Expected: The note appears in the note list with title "QA Test Note" and opens in the editor showing "Hello world".
- [ ] FT-02: Edit the title and body of an existing note.
  - Action: Open a default note, change its title to "Edited Title", and append "edit check" to the body.
  - Expected: The list and editor both show "Edited Title" and the appended text.
- [ ] FT-03: Rich-text formatting is applied and kept.
  - Action: Select a word in the body, click Bold, Italic, and Bulleted List, then open another note and return.
  - Expected: The word is bold and italic, and the list formatting is still present.
- [ ] FT-04: Delete a note.
  - Action: Select the note "QA Test Note" and click the "Delete" button.
  - Expected: The note disappears from the list and is no longer accessible.
- [ ] FT-05: Rename a folder.
  - Action: Right-click an existing folder, choose "Rename", enter "Renamed Folder", and confirm.
  - Expected: The sidebar and the folder label on its notes show "Renamed Folder".
- [ ] FT-06: Move a note to another folder.
  - Action: Open a note's folder menu and select a different folder.
  - Expected: The note appears under the new folder and no longer appears under the original folder.
- [ ] FT-07: Add a tag to a note.
  - Action: In the note's tag field, type "urgent" and press Enter.
  - Expected: A tag chip labeled "urgent" appears on the note and in the note list.
- [ ] FT-08: Remove a tag from a note.
  - Action: Click the × on the "urgent" tag chip of the note.
  - Expected: The chip is removed from that note and the tag is still on other notes that have it.
- [ ] FT-09: Search by title.
  - Action: Type a distinctive part of a default note's title in the search box.
  - Expected: Only notes whose titles contain that text are listed.
- [ ] FT-10: Search by content.
  - Action: Type a distinctive phrase from a default note's body (not its title) in the search box.
  - Expected: That note is listed in the results.
- [ ] FT-11: Search by tag and by folder name.
  - Action: Type an existing tag name, then an existing folder name, in the search box.
  - Expected: Each search lists only the notes carrying that tag or located in that folder.
- [ ] FT-12: Filtered view of a folder with a specific tag.
  - Action: Select an existing folder in the sidebar, then select one of its tags in the tag filter.
  - Expected: Only notes that are in that folder and have that tag are shown.
- [ ] FT-13: Notes persist after reloading the page.
  - Action: Edit a note's title, add a tag, then reload the browser page.
  - Expected: After reload, the title and tag are still present.
- [ ] FT-14: Edits made while offline sync when the connection returns.
  - Action: Disconnect the network, edit a note body with "offline text", then reconnect.
  - Expected: The edit is retained in the editor with no loss, and the save status changes to "Saved" after reconnecting.

## Constraint
- [ ] CS-01: Folder rename rejects empty or duplicate names.
  - Action: Rename a folder to an empty string, then to the name of another existing folder.
  - Expected: Each attempt is blocked with an error message (e.g., "Folder name required" / "Folder already exists") and the original name is kept.
- [ ] CS-02: A note cannot have the same tag twice.
  - Action: On a note that already has "urgent", type "urgent" in the tag field and press Enter.
  - Expected: No duplicate "urgent" chip is added.
- [ ] CS-03: Edits made while offline survive a reload that happens while still offline.
  - Action: Disconnect the network, type "survive test" in a note, then reload the page without reconnecting.
  - Expected: After reload, the "survive test" text is still in the note.

## Interaction
- [ ] IX-01: The save status indicator reflects save state, including offline state.
  - Action: Type in a note, watch the status indicator, then disconnect the network and type again.
  - Expected: While typing online it shows "Saving..." then "Saved"; while offline it shows "Saved locally – offline" (or equivalent) instead of "Saved".

## Content
- [ ] CT-01: Note list metadata matches the note's stored data.
  - Action: Compare each note's row in the list (title, folder name, tags, last-modified date) with the same note opened in the editor.
  - Expected: Title, folder, tags, and date shown in the list match the editor exactly for every note.
- [ ] CT-02: Rich-text content displays without raw markup.
  - Action: Format a note's text as bold and as a list, then reopen the note.
  - Expected: The text shows formatted, with no visible HTML or markup characters (e.g., "<b>", "**") in the editor or list preview.