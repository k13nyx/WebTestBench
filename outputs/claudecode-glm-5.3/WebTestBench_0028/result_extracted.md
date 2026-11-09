# Test Result

**Test environment note:** The app seeds each new account with default folders (Personal, Work, Taxes) but no default documents, so test documents were uploaded first and used as the vault's existing documents for all subsequent checklist items. All interaction was performed via DOM/a11y-tree automation only.

## Functionality
- [X] FT-01: User can create a new account
  - Action: On the sign-up page, fill in a valid email and password, then click the "Sign Up" (or equivalent) button.
  - Expected: Account is created and the user is logged in and taken to the vault/dashboard, or shown a success message.
  - Verified: Filled `userA@example.com` / password on the "Sign Up" tab → clicked "Create Vault" → toast "Account created successfully" appeared, user was logged in (email shown in header) and taken to the vault with default folders.

- [X] FT-02: User can log in with valid credentials
  - Action: On the login page, enter the registered email and password, then click "Log In".
  - Expected: User is authenticated and redirected to their document vault.
  - Verified: Entered `userA@example.com` / correct password → clicked "Unlock Vault" → toast "Welcome back!", user authenticated and vault displayed with all previously created folders/documents intact.

- [X] FT-03: User can log out
  - Action: While logged in, click the "Log Out" button.
  - Expected: User session ends and user is returned to the login page.
  - Verified: Clicked "Sign out" in the header → session ended, app returned to the login page (Sign In / Sign Up tabs, "Unlock Vault" button).

- [X] FT-04: User can upload a document
  - Action: Click the "Upload" button, select a file (e.g., a PDF), and confirm the upload.
  - Expected: The uploaded document appears in the vault's document list with its original file name.
  - Verified: Opened Upload dialog → selected 4 files → clicked "Upload (4)" → all 4 files (`qa-report.txt`, `tour-room2.md`, `snap.md`, `snap1.md`) appear in the vault's "Documents" list with their original file names, sizes and upload dates.

- [X] FT-05: User can create a folder and move a document into it
  - Action: Create a new folder (e.g., "Finance"), then move a default document into it using the move option.
  - Expected: The document is listed inside the "Finance" folder and no longer appears at the vault root.
  - Verified: Created folder "Finance" (toast: `Folder "Finance" created`) → opened `tour-room2.md` options → "Move" → selected "Finance" → "Move Here". Opening Finance shows `tour-room2.md` ("Documents (1)"); the vault root document count dropped from 4 to 3 and `tour-room2.md` no longer appears there.

- [X] FT-06: User can add a tag to a document
  - Action: Open a default document's options and add a tag (e.g., "insurance"), then save.
  - Expected: The tag is displayed on the document and the document is findable under that tag.
  - Verified: Opened `qa-report.txt` options → "Edit Tags" → typed "insurance" + Enter → "Save Tags" → the "insurance" tag is displayed on the `qa-report.txt` card, and searching "insurance" (FT-10) returns exactly that document.

- [X] FT-07: User can rename a document
  - Action: Select a default document, choose "Rename", enter a new name, and confirm.
  - Expected: The document list shows the new name; the old name no longer appears.
  - Verified: Opened `snap.md` options → "Rename" → entered `team-notes-2026.md` → clicked "Rename" → toast "Document renamed"; the list shows `team-notes-2026.md` and the old name `snap.md` no longer appears anywhere.

- [X] FT-08: User can delete a document
  - Action: Select a default document, choose "Delete", then confirm.
  - Expected: The document is removed from the vault and no longer appears in any folder, tag list, or search result.
  - Verified: Opened `snap1.md` options → "Delete" → confirmed the dialog → document removed from the root list (Documents went 3 → 2); searching "snap1" returns "No results found / No documents match 'snap1'".

- [X] FT-09: User can search documents by name
  - Action: Type the (partial) name of a default document into the search bar.
  - Expected: Search results show only documents whose names match the query.
  - Verified: Typed partial name "qa-re" into the search bar → results list shows only `qa-report.txt`; typed "team" → shows only `team-notes-2026.md`. Non-matching documents are excluded.

- [X] FT-10: User can search documents by tag
  - Action: Type an existing tag name (e.g., "insurance") into the search bar, or click the tag.
  - Expected: Search results show only documents carrying that tag.
  - Verified: Typed "insurance" into the search bar → results show only `qa-report.txt`, the sole document carrying the "insurance" tag; all untagged documents are excluded.

## Constraint
- [X] CS-01: Registration rejects an already-registered email
  - Action: Attempt to sign up using an email that already has an account.
  - Expected: Registration is blocked with an error message (e.g., "Email already in use"); no duplicate account is created.
  - Verified: Signed up again with `userA@example.com` → error toast "An account with this email already exists"; stayed on the sign-up form, no account created and no login occurred.

- [X] CS-02: Login fails with wrong credentials
  - Action: Attempt to log in with a valid email but an incorrect password.
  - Expected: Login is rejected with an error message (e.g., "Invalid email or password") and the vault is not accessible.
  - Verified: Logged in with `userA@example.com` + wrong password → error toast "Invalid email or password"; remained on the login page with no vault access.

- [X] CS-03: Vault is inaccessible without authentication
  - Action: While logged out, open the vault/documents URL directly in the browser.
  - Expected: User is not shown any documents and is redirected to the login page.
  - Verified: After sign out, opened `http://localhost:6028/` (the vault URL) directly → the login page is displayed; no folders, documents, or user data are rendered. (`/vault` is a 404 route; the vault lives at `/` behind authentication.)

- [X] CS-04: User cannot see another user's documents
  - Action: Log in as user A and note the visible documents; log out, create/log in as user B, and check the vault.
  - Expected: User B sees only their own (default) documents — none of user A's documents, folders, or tags are visible.
  - Verified: User A had folders Personal/Work/Taxes/Finance and documents `qa-report.txt` [insurance], `team-notes-2026.md`, `Finance/tour-room2.md`. After creating and logging in as User B, B's vault shows only the default folders Personal and Work (0 documents) — no Finance folder, none of A's documents, and no "insurance" tag. Searches for "qa-report", "team-notes", and "insurance" as User B all return "No results found".

- [X] CS-05: Upload cannot be completed without selecting a file
  - Action: Open the upload dialog and click "Upload"/"Confirm" without choosing any file.
  - Expected: Upload is blocked (button disabled or validation error shown); no empty document entry is created.
  - Verified: Opened the Upload dialog without a file → the "Upload" confirm button is rendered `[disabled]` and cannot be clicked; after canceling, the document list is unchanged (no empty document entry created).

## Interaction
- [X] IX-01: Success feedback after document upload
  - Action: Upload a valid document.
  - Expected: A success toast/notification (e.g., "Document uploaded") appears and the new document shows in the list without a full page reload error.
  - Verified: After confirming the upload, a toast notification "4 documents uploaded and encrypted" appeared; all new documents immediately appeared in the "Documents" list with no page reload or errors (SPA URL unchanged).

- [X] IX-02: Confirmation dialog before deleting a document
  - Action: Click "Delete" on a default document.
  - Expected: A confirmation dialog appears (e.g., "Are you sure you want to delete this document?"); the document is only deleted after confirming, and remains if canceled.
  - Verified: Clicking "Delete" on `snap1.md` raises a confirmation dialog: `Delete "snap1.md"? This cannot be undone.` Choosing Cancel leaves the document in the list (verified present, "Documents (3)"); choosing Delete (confirm) removes it.

- [X] IX-03: Search results update dynamically
  - Action: Type characters into the search bar and observe the results list.
  - Expected: The results list updates to reflect the current query without requiring a page reload.
  - Verified: Typed queries character-by-character ("qa-re" → "team") — the results list re-rendered after each keystroke sequence (first `qa-report.txt` only, then `team-notes-2026.md` only) with no page reload (URL remained `http://localhost:6028/`, no navigation events).

## Content
- [X] CT-01: Document list displays accurate metadata
  - Action: Browse the vault and open a default document's details.
  - Expected: Each document shows a correct name, its assigned tags, and its folder location; no placeholder or broken entries are displayed.
  - Verified: Each document card displays correct name, size, and date (`qa-report.txt` — "52 B • Nov 8, 2026" — with its "insurance" tag; `team-notes-2026.md` — "4.6 KB • Nov 8, 2026"; `tour-room2.md` — "6.2 KB" — inside the Finance folder, matching where it was moved). Folder location is reflected by folder navigation (Finance shows "Documents (1)"). No placeholder or broken entries observed anywhere. (Note: the app has no separate detail view — clicking a card does not open one; the card list is the metadata display, and it is accurate.)

- [X] CT-02: Document content is only viewable through the authenticated app
  - Action: While logged in, open a default document and verify its content displays correctly; then log out and attempt to reopen the same document's URL/content.
  - Expected: Content renders fully when authenticated in the app, and cannot be viewed or downloaded after logout (indicating protected/encrypted access).
  - Verified: While logged in as User A, used Download on `qa-report.txt` — the app decrypted and served the file, whose content is intact readable plaintext (`SECUREVAULT-QA-MARKER-42` / "Line two of test document.", exactly 52 B matching the listed size), confirming the encryption round-trip works. After logging out, reopening the vault/document URL shows only the login page — the document cannot be viewed or downloaded, and all stored data remains behind authentication/encryption.
