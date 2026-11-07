# Test Result

**Application:** http://localhost:6028/ — SecureVault (client‑side SPA, Vite + React, all data in `localStorage`)
**Test accounts:** `qa.newuser@example.com` / `SuperSecret123!` (Account A), `qa.second@example.com` / `SecondUser456!` (Account B)

## Functionality

- [X] FT-01: Visitor can create an account with a new email and password
  - Action: On the sign-up page, enter a valid unique email and password (e.g. `qa.newuser@example.com`), then submit the registration form.
  - Expected: Account is created, the user is authenticated, and the vault (dashboard/document list) is displayed.

- [X] FT-02: Registered user can log in with valid credentials
  - Action: Log out, then enter the registered email and the correct password on the login form and submit.
  - Expected: Login succeeds and the user lands in the vault with their documents visible.

- [X] FT-03: Default documents are listed in the vault after login
  - Action: Log in with an account that has pre-existing documents and observe the document list.
  - Expected: All pre-existing documents are listed with their names, and no document from another account appears.
  - Note: the root list shows unfiled documents only (by design — filed docs leave the root list, see FT-06); the pre-existing document `Lease Agreement.pdf` was listed by its exact name in its folder view (“Taxes 2024 → Documents (1) → Lease Agreement.pdf”), and no Account‑B artifact ever appeared.

- [X] FT-04: User can upload a document to the vault
  - Action: Click the upload control, choose a file from the local filesystem, confirm the upload, and wait for completion.
  - Expected: The document appears in the document list with its original filename and is stored in the current location.

- [X] FT-05: User can create a folder
  - Action: Click the "New Folder" / create-folder control, enter a folder name, and confirm.
  - Expected: The new folder appears in the folder list or sidebar with the given name.

- [X] FT-06: User can organize a document into a folder
  - Action: Open the organize/move options for an existing document, select an existing folder, and save.
  - Expected: The document is listed under the selected folder and is no longer shown in the unfiled/root list.

- [X] FT-07: User can tag a document with one or more tags
  - Action: Open the tag control for an existing document, add a tag name, and confirm.
  - Expected: The document displays the new tag and the tag appears in the tag/collection list.

- [X] FT-08: User can rename a document
  - Action: Open the rename option for an existing document, enter a new name, and confirm.
  - Expected: The document displays the new name everywhere it appears (list, folder view, search results), and the old name is no longer shown.

- [X] FT-09: User can delete a document
  - Action: Open the delete option for an existing document and confirm the deletion.
  - Expected: The document is removed from the document list, from its folder, and from search results for that document.

## Constraint

- [X] CS-01: Registration rejects an email that is already registered
  - Action: Attempt to create an account using an email that already exists in the application.
  - Expected: Registration is blocked with a visible duplicate/already-registered error, and no second account is created.

- [X] CS-02: Login rejects invalid credentials and invalidates the session
  - Action: Enter a valid registered email with an incorrect password and submit; then try to access the vault URL directly.
  - Expected: A visible invalid-credentials error is shown, no vault content is revealed, and direct access is redirected to the login page.

- [X] CS-03: Vault is not accessible while logged out
  - Action: Log out, then attempt to open the vault, document, and folder pages/URLs directly in the browser.
  - Expected: All requests to view documents, folders, or search results are blocked and the user is redirected to the login page.
  - Note: after sign-out, `http://localhost:6028/` renders the Sign In / Sign Up screen with no vault content; the app defines only the routes `/` and `*` (source: `/src/App.tsx`), so direct requests to `/vault`, `/documents/<id>`, `/folders/<id>` resolve to the generic “404 – Oops! Page not found” page and leak nothing.

- [X] CS-04: One user's documents are never visible to another user
  - Action: Log in as a second account and browse all folders, tags, and search results.
  - Expected: No documents, folders, or tags belonging to the first account are listed or openable.

- [ ] CS-05: Stored document content is not readable as plaintext outside the app
  - Action: Inspect the stored/uploaded file data and the network traffic for a document's contents.
  - Expected: The document bytes are encrypted (no readable filename or file body appears in storage or in network responses), and content is only recoverable after the owner's authenticated decryption.
  - Bug Report:
    - Issue: Content stored unencrypted (base64 only) — "encryption" is cosmetic
    - Actual: The persisted vault record is plain JSON in `localStorage["vault_data_<userId>"]`, e.g. `"content":"data:text/plain;base64,UEFZUk9MTC1QTEFJTlRFWFQtTUFSS0VSLTQ0MjEgc2FsYXJ5IGRldGFpbHM="` — this base64 decodes verbatim to the uploaded plaintext `PAYROLL-PLAINTEXT-MARKER-4421 salary details`. The filename (`"name":"Compensation Statement 2024.txt"`) and tag list are also stored in cleartext in the same record. Source confirms the body is persisted via `reader.readAsDataURL(file)` with no `crypto.subtle` usage; the `encryptedKey` field (`"d5b2ec01…"`) is a random value that is never used to encrypt or decrypt anything. The UI still claims “All files will be encrypted before storage” / “All data is encrypted and stored locally in your browser”, which is false. (No network exposure was observed — the app makes zero API requests — but storage is plaintext.)

- [ ] CS-06: Rename and delete cannot target a non-existent document
  - Action: Invoke the rename and delete operations for a document identifier that does not exist (e.g. after the document was already deleted).
  - Expected: The operation fails safely with a clear error, and no unrelated document is renamed or deleted.
  - Bug Report:
    - Issue: Missing existence validation — operation on a non-existent id succeeds silently and re-creates the record
    - Actual: With the document's entry removed from the persisted store while it was still displayed, opening **Rename** → “Ghost Rename.txt” reported success (`Document renamed` toast) and **re-inserted** the removed record into storage (`{"id":"76e97d14-…","name":"Ghost Rename.txt", …}`) instead of failing with a clear error. **Delete** on the same stale id completed with no error message at all. Source confirms the root cause: `renameDocument = (id, newName) => setDocuments(prev => prev.map(d => d.id === id ? {...d, name: newName} : d))` and `deleteDocument = (id) => setDocuments(prev => prev.filter(d => d.id !== id))` — neither checks that the id exists, and the whole in-memory array is persisted back afterwards. (No unrelated document was renamed or deleted in these runs.)

## Interaction

- [X] IX-01: Successful upload gives immediate visual confirmation
  - Action: Complete an upload and observe the screen immediately afterward.
  - Expected: A success toast/notification appears and the new document is shown in the list without a manual page reload.

- [X] IX-02: Failed login gives immediate visual feedback
  - Action: Submit the login form with a wrong password.
  - Expected: An inline error message appears on the form, the invalid credentials are not accepted, and no vault content is shown.

- [X] IX-03: Delete asks for confirmation and cancels cleanly
  - Action: Click delete on an existing document, then cancel the confirmation; then repeat and confirm.
  - Expected: Cancelling leaves the document intact and listed; confirming removes it from the list.

- [X] IX-04: Search results update as the query is typed
  - Action: Type a partial document name and a tag name into the search field.
  - Expected: The result list narrows to matching documents as typing proceeds, and matches are shown for both name and tag queries.

## Content

- [X] CT-01: Interface labels match the vault feature set
  - Action: Inspect the visible labels and headings across the sign-up, login, vault, folder, and search views.
  - Expected: Labels are accurate and relevant to a personal document vault (e.g. "Upload", "New Folder", "Tags", "Search", "Rename", "Delete") with no placeholder or lorem-ipsum text and no unrelated feature wording.

- [X] CT-02: Document names and tags are displayed accurately
  - Action: Open the document list, a folder view, and the tag list, and compare each displayed name/tag with the original filename and tag applied.
  - Expected: Filenames and tag labels are shown exactly as stored, with no truncation that changes the visible name, no garbled characters, and no tags attached to the wrong document.

---

### Summary
18 of 20 checks passed. The two failures are both in the encryption/safety guarantees:
- **CS-05 (critical):** file bodies and filenames are stored as unencrypted base64 in `localStorage`; the `encryptedKey` field is decorative and no real cryptography is performed, despite the UI promising encryption.
- **CS-06:** `renameDocument`/`deleteDocument` are blind array operations with no existence check — a stale/non-existent id yields no error and rename resurrects the deleted record.