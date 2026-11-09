# Test Result

## Functionality
- [X] FT-01: User can create a rich-text note and it appears in the notes list
  - Action: Clicked "New" (no explicit "Save" button exists — app uses auto-save), typed title "QA Test Note" and body text.
  - Expected: A new note with that title is created and listed in the current folder's note list. → "QA Test Note" appeared at the top of the note list with its body preview; All Notes count incremented 5→6.

- [X] FT-02: Rich-text formatting (bold/italic) is applied and persists
  - Action: Selected words in the body, applied Bold ("zebraunique") and Italic ("keyword") via toolbar, switched to another note, reopened.
  - Expected: Formatting preserved → Editor showed `<strong>zebraunique</strong>` and `<em>keyword</em>` after reopen; formatting also survived page reload (verified in FT-12).

- [X] FT-03: User can edit an existing note
  - Action: Opened default note "Book Recommendations", changed title to "Book Lists EDITED" and appended body text, auto-saved.
  - Expected: List and view updated, no duplicate → Note list heading updated to "Book Lists EDITED", body marker "EDITED-BODY-MARKER" present in editor, total note count unchanged.

- [X] FT-04: User can delete a note
  - Action: Opened "QA Test Note" (folder Work, tag Important), clicked the note-options button → "Delete Note".
  - Expected: Note permanently removed from all views → Removed from All Notes (7→6), Work folder (3→2), Important tag (2→1), search, and localStorage. Note: deletion executed immediately with no confirmation dialog (deviation recorded under IX-02).

- [X] FT-05: Search returns notes matching title and body content
  - Action: Searched body-only word "zebraunique" and title-only word "Recommendations" in the All Notes view.
  - Expected: Matching notes listed, non-matching excluded → "zebraunique" returned only "QA Test Note"; "Recommendations" returned only "Book Recommendations". (Behavioral note: search is AND-combined with the active folder/tag filter, e.g. "Recommendations" returned nothing while #Important filter was active.)

- [X] FT-06: Notes can be found by tag
  - Action: Clicked sidebar tags "Reference", "To-Do", "Important".
  - Expected: Only notes carrying that tag shown → #Reference showed exactly "Book Recommendations" + "Welcome to Notes" (2); #To-Do showed exactly "Weekly Team Standup" + "Project Planning"; #Important showed the 2 Important-tagged notes.

- [X] FT-07: Notes can be found by folder
  - Action: Clicked "Personal" (later "Personal Renamed") folder in sidebar.
  - Expected: List shows only notes in that folder → View header changed to folder name and listed exactly its notes (Personal: QA Test Note + Book Recommendations = 2).

- [X] FT-08: User can rename a folder
  - Action: Opened folder options (⋯) → "Rename", typed "Personal Renamed", pressed Enter.
  - Expected: New name shown, notes still under it → Sidebar button, view header, and editor folder selector all showed "Personal Renamed" with its 2 notes intact.

- [X] FT-09: User can move a note between folders
  - Action: Selected "QA Test Note" in Personal Renamed, used editor folder dropdown ("Move to" equivalent) → chose "Work".
  - Expected: Removed from A, added to B → Personal Renamed count 2→1 (list showed only "Book Lists EDITED"); Work count 2→3 (list included "QA Test Note").

- [X] FT-10: User can add and remove tags on a note
  - Action: Via editor "Tags" menu added "Important" and "To-Do" to the note, then clicked the "x" on the "To-Do" chip.
  - Expected: Added tag shown & filterable; removed tag not shown/filterable → Chips rendered in editor; #Important view included the note; after removal the chip disappeared, To-Do count 3→2, and #To-Do view excluded the note.

- [X] FT-11: Combined filtered view (folder + specific tag) works
  - Action: Opened "Personal Renamed" folder, then clicked tag "Important".
  - Expected: Only notes in folder AND with tag → View showed exactly 1 note ("QA Test Note"); folder-only note ("Book Recommendations") and tag-only note ("Project Planning") were both hidden.

- [X] FT-12: Notes persist in the browser across reloads
  - Action: Created "Persistence Note" (title, body, bold word, folder "Ideas", tag "Reference"), reloaded the page (F5 equivalent).
  - Expected: Note still present with all attributes → After reload: title, body, `<strong>boldme</strong>`, Ideas folder count, and Reference tag chip all intact; data stored under localStorage key "notes-app-data".

- [X] FT-13: Editing is safe and instant when the connection is lost
  - Action: Set browser context to Offline (Playwright `context.setOffline(true)`), appended "OFFLINE-MARKER-42" to the note body, then restored the connection and reloaded.
  - Expected: No error blocks offline editing; edits kept locally and survive reconnection/reload → Typing was accepted instantly with no error toast; text was written to localStorage while offline; marker + bold formatting present after reconnect and reload.

## Constraint
- [ ] CS-01: An empty note cannot be created
  - Action: Clicked "New", left title and body empty (no Save button exists — the app persists immediately).
  - Expected: The note is not saved; no blank note added.
  - Bug Report:
    - Issue: Missing validation — empty note created instantly
    - Actual: Clicking "New" immediately created and saved an empty note: list showed "Untitled Note / Empty note", All Notes count incremented 6→7 (reconfirmed with a second probe: "IX-02 Probe / Empty note"). No validation message and no disabled Save; the blank note persists in the list and localStorage.

- [X] CS-02: A deleted note leaves no trace in any view
  - Action: Deleted "QA Test Note" (tagged "Important", in folder "Work"), then opened folder Work, tag #Important, and searched "zebraunique".
  - Expected: Deleted note absent from folder, tag, and search → Work folder dropped to 2 notes without it; Important tag count dropped 2→1; search for "zebraunique" showed "No notes found"; localStorage contained no "QA Test Note" or "zebraunique".

## Interaction
- [X] IX-01: Search results update live as the user types
  - Action: Typed into the search box without pressing Enter: "W" (all 6 notes matched — the letter occurs in every note's text), then extended to "We".
  - Expected: List filters progressively in real time → Without Enter, the list narrowed from 6 to exactly 2 ("Weekly Team Standup", "Welcome to Notes") as the query grew.

- [ ] IX-02: User gets feedback on create/save/delete
  - Action: Created a note, edited/saved notes (auto-save), deleted a note; sampled the "Notifications" toast region at 200 ms and 800 ms after a save.
  - Expected: Visible confirmation (toast or "Saved" indicator) after create/save, and a confirmation dialog before delete.
  - Bug Report:
    - Issue: No save/create feedback and no delete confirmation
    - Actual: Notifications region stayed empty after create and save; no "Saved" text anywhere in the DOM. Clicking "Delete Note" removed the note instantly — no confirmation dialog appeared (delete is irreversible with no undo prompt).

## Content
- [X] CT-01: Default seed data is present and relevant to a notes app
  - Action: Opened the app fresh.
  - Expected: At least one folder, one tag, one rich-text note with meaningful content, no broken placeholders → Seeded with 3 folders (Personal, Work, Ideas), 5 tags (Important, To-Do, Reference, Idea, Meeting), and 5 notes with meaningful titles and genuine rich text (e.g. "Book Recommendations" contains H1/H2 headings, a bolded book title, and bullet lists; "Welcome to Notes" intro note). No placeholder artifacts.

- [X] CT-02: Empty-state and no-results messages are shown
  - Action: Searched the non-matching string "qqqzzzxxx".
  - Expected: Clear "No results"/"No notes found" message → List area displayed "No notes found" (plus a "Create your first note" hint and `Search: "qqqzzzxxx"` context header); no blank screen or error.
