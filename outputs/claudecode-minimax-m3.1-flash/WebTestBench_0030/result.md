All 20 checklist items have been executed and verified. Here is the complete report.

# Test Result

## Functionality

- [X] FT-01: User can create a new note with a title and body
  - Action: Click the "New Note" control, type a title and body text, save/submit the note.
  - Expected: The note is created, appears in the notes list with its title, and opens in the editor with the entered content.
  - Verified: "QA Test Note Alpha" was created via the **New** button; title typed into the "Note title..." input and body into the TipTap editor. List item rendered as `QA Test Note Alpha / Zebra body content for alpha note.` and the editor reopened with both values.

- [X] FT-02: Notes support rich-text formatting
  - Action: In the note editor, apply bold, italic, and a list format to portions of the note body and save.
  - Expected: The formatted content is preserved and rendered with the applied styling (bold text bold, list displayed as a list) when the note is reopened.
  - Verified: After switching notes and re-opening, the editor DOM contained `<ul><li><p><strong><em>…</em></strong></p><li>…</ul>` — bold, italic and bullet-list markup all persisted through save/reload.

- [X] FT-03: User can edit an existing note
  - Action: Open an existing note, change its title and body text, and save.
  - Expected: The updated title and body are shown in the notes list and editor; the previous content is fully replaced.
  - Verified: "Draft Entry / Original body alpha" became "Edited Entry Title / Final rewritten content beta"; the old title and body were gone from both list and editor.

- [X] FT-04: User can delete a note
  - Action: Select an existing note and invoke the delete action, confirming the deletion.
  - Expected: The note is removed from the notes list and from any folder/tag-filtered view it appeared in.
  - Verified: "Delete Target" was removed via the editor's ⋮ menu → **Delete Note**; it disappeared from the list and from `localStorage` (`notes-app-data`), and the All Notes count dropped 10 → 9.

- [X] FT-05: User can create a folder
  - Action: Use the folder/new-folder control in the sidebar to create a folder with a name.
  - Expected: The folder appears in the sidebar folder list and can be selected to filter notes.
  - Verified: "Zeta Folder" and "Omega Folder" were created with the sidebar `+` control, appeared in the Folders list with counts, and selecting them filtered the notes list correctly.

- [X] FT-06: User can move a note between folders
  - Action: Open a note that belongs to Folder A, change its folder to Folder B using the note's folder control, and save.
  - Expected: The note is listed under Folder B and no longer under Folder A.
  - Verified: "Edited Entry Title" was moved from *Zeta Folder Renamed* to *Omega Folder*; folder counts went Zeta 3→2 / Omega 1→2, the Zeta-filtered view no longer listed it and the Omega-filtered view did.

- [X] FT-07: User can rename a folder
  - Action: Invoke rename on an existing folder, enter a new name, and confirm.
  - Expected: The sidebar shows the new folder name, and all notes previously in that folder remain in it under the new name.
  - Verified: "Zeta Folder" → "Zeta Folder Renamed" via the folder row menu → **Rename**. Sidebar label updated immediately, count stayed 3, and all three notes remained under the renamed folder.

- [X] FT-08: User can add a tag to a note
  - Action: Open a note and add a tag (via the tag control or by typing a new tag name).
  - Expected: The tag is displayed on the note and is listed among the application's tags.
  - Verified: "Kappa Tag" and "Sigma Tag" were created via the sidebar `+` tag control and applied to "QA Test Note Alpha" through the editor's **Tags** control; both chips rendered on the note card and in the editor, and the sidebar TAGS list showed `Kappa Tag 1 / Sigma Tag 1`.

- [X] FT-09: User can remove a tag from a note
  - Action: Open a tagged note and remove one of its tags using the tag control.
  - Expected: The tag no longer appears on the note, and the note no longer appears in that tag's filtered view.
  - Verified: The `×` control on the "Kappa Tag" chip in the editor removed the tag; the chip vanished, the sidebar count dropped 3→2, and in the `#Kappa Tag` filtered view "Edited Entry Title" was excluded while still present under All Notes.

- [X] FT-10: User can search notes by title
  - Action: Type a word that appears in an existing note's title (and not in any body) into the search field.
  - Expected: Only the note with that title is returned in the results list.
  - Verified: Searching `Edited` returned exactly `["Edited Entry Title"]`.

- [X] FT-11: User can search notes by body content
  - Action: Type a word that appears only in an existing note's body text into the search field.
  - Expected: The note containing that text in its body is returned in the results list.
  - Verified: Searching `theta` (present only in "Plain Folder Note" body) returned exactly `["Plain Folder Note"]`.

- [X] FT-12: User can search notes by tag
  - Action: Type an existing tag name into the search field.
  - Expected: All notes carrying that tag are returned, and notes without the tag are excluded.
  - Verified: Searching `Kappa Tag` returned `["Tagged Elsewhere", "QA Test Note Alpha"]` — exactly the two notes carrying that tag.

- [X] FT-13: User can search notes by folder
  - Action: Type an existing folder name into the search field.
  - Expected: All notes assigned to that folder are returned, and notes in other folders are excluded.
  - Verified: Searching `Omega Folder` returned `["Tagged Elsewhere", "Edited Entry Title"]` — both and only the notes in that folder.

- [X] FT-14: User can view notes filtered by folder combined with a specific tag
  - Action: Select a folder and additionally apply a specific tag filter within it.
  - Expected: The list shows only notes that are both in the selected folder and carry the selected tag; notes in the folder without the tag and notes with the tag in other folders are not shown.
  - Verified: With *Zeta Folder* selected and then the *Kappa Tag* chip applied, the list was `["Edited Entry Title", "QA Test Note Alpha"]` — "Plain Folder Note" (in folder, no tag) and "Tagged Elsewhere" (tag, other folder) were both excluded.

## Constraint

- [X] CS-01: Notes persist in the browser after leaving and revisiting the page
  - Action: Create/edit a note, then reload the page or close and reopen the browser at the same URL.
  - Expected: All notes, their body text, folder assignments, and tags are still present and unchanged.
  - Verified: After a full page reload, all 10 notes were listed, the Folders list still showed `Personal 1 / Work 2 / Ideas 1 / Zeta Folder Renamed 2 / Omega Folder 2 / Crème Brûlée (Café)! 1`, the TAGS list still showed all seven tags with correct counts, and the re-opened note retained its title, body, rich-text HTML (`<strong><em>` inside `<ul><li>`), folder (`Crème Brûlée (Café)!`) and tag chip.

- [X] CS-02: Edits made while the internet connection is unavailable are not lost
  - Action: Disconnect the network (disable the network adapter / set the browser offline), edit a note's title and body, save, then restore the connection and reload the page.
  - Expected: The edit is applied and saved without an error blocking the save, no user input is discarded, and the edited content is intact after reload; no data-loss or unsaved-changes warning is shown.
  - Verified: With the browser context set offline (`navigator.onLine === false`), the title and body edits were applied and the list updated immediately; the notification region stayed completely empty (no toast, error banner, or "unsaved changes" warning) and no save-related console errors appeared (only a pre-existing React `validateDOMNesting` warning). After restoring the connection and reloading, both the title edit and the body edit were intact.

- [X] CS-03: A note's tag/folder filters never produce an inconsistent result set
  - Action: Apply a folder filter and a tag filter together, then remove the tag from one of the listed notes and rename the folder.
  - Expected: The list updates immediately to reflect the change (the untagged note is dropped from the filtered list), and the remaining notes stay under the renamed folder without duplication or disappearance.
  - Verified: In the combined *Zeta Folder + Kappa Tag* view (showing "Edited Entry Title" and "QA Test Note Alpha"), removing "Kappa Tag" from "Edited Entry Title" instantly dropped it from the list (`["QA Test Note Alpha"]`) and the tag count went 3→2. Renaming the folder to "Zeta Folder Renamed" kept the remaining note listed under the new label with its count preserved (3) and no duplicated or vanished entries.

## Interaction

- [X] IX-01: Search results update as the user types and can be cleared
  - Action: Type progressively into the search field, observe the results list, then clear the field.
  - Expected: The result list re-renders on each keystroke to match the current query, and clearing the search restores the unfiltered list of all notes.
  - Verified: Keystroke-by-keystroke the list re-rendered live — `Q` → 5 notes, `Qu` → 3 notes, `Qua` → 1 note ("Project Planning"). Clearing the field restored the full unfiltered list of all 11 notes.

- [X] IX-02: The interface gives immediate feedback for save, delete, rename, and tag changes
  - Action: Perform a note save, note delete, folder rename, and tag addition in turn, observing the interface after each.
  - Expected: Each action produces immediate visible feedback (e.g., updated list item, removed item, renamed folder label, updated tag label, and/or a status/toast message) with no manual refresh needed.
  - Verified: Save → the notes-list card updated to the new title immediately; Delete → the card vanished from the list immediately; Rename → the sidebar folder label changed to "Temp Folder Renamed" immediately; Tag addition → the "Sigma Tag" chip appeared on the note immediately. No refresh was needed for any of the four.

## Content

- [X] CT-01: Displayed note and organization content matches exactly what the user entered
  - Action: Create notes, folders, and tags with distinctive names (including mixed case, punctuation, and a non-ASCII character), then review the sidebar, tags list, notes list, and note editor.
  - Expected: Every title, body text, folder name, and tag name is displayed exactly as entered — same characters, case, punctuation, and no truncation, placeholder, or garbled characters.
  - Verified: Folder `Crème Brûlée (Café)!` and tag `Ünïcode-Tag_Ünï` were rendered byte-identically in the Folders and TAGS sidebar lists; note title `Rapport «Final» Ünïcödé 50% (v2)` and body `Élève a réussi 50% (v2) & Cie — résumé ✓` were rendered identically in the notes list card, in the title input value, and in the editor body (`innerText`). Accents, guillemets, em dash, ampersand, parentheses, `!`, `_` and the check mark all rendered correctly; the placeholder "Start writing..." did not appear, no `…`/ellipsis truncation was present, and the values survived a reload unchanged.

---

**Minor observations (not checklist failures):**
- Deleting a note (FT-04) happens immediately with no confirmation dialog — the "Delete Note" menu item removes the note at once. The expected outcome (removal from list and storage) was met.
- The app surfaces no toast/status messages (the Sonner notification region remained empty throughout), so all IX-02 feedback came from in-place UI updates (list item, folder label, tag chip) rather than status messages.
- Clicking an already-active folder or tag in the sidebar does not toggle that filter off (it stays active); the filter is cleared via the "All Notes" entry. This did not affect any checklist item, since no item requires toggling a filter off.