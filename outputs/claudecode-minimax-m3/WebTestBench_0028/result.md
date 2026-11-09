All checklist items have been executed. Here is the full result.

# Test Result

## Functionality

- [X] FT-01: User can create a new account
  - Action: Navigate to registration page, enter a valid email and password, click "Sign Up" / "Register"
  - Expected: Account is created and the user is logged in or redirected to the login page
- [X] FT-02: User can log in with valid credentials
  - Action: Enter the registered email and password on the login form, click "Log In"
  - Expected: User is authenticated and redirected to the vault dashboard
- [X] FT-03: User can log out
  - Action: While logged in, click the "Log Out" button
  - Expected: User session ends and the user is returned to the login page
- [X] FT-04: User can upload a document to the vault
  - Action: Click "Upload", select a file (e.g., PDF or image), confirm upload
  - Expected: The uploaded document appears in the vault's document list
- [X] FT-05: User can create a new folder
  - Action: Click "New Folder" / "Create Folder", enter a folder name, confirm
  - Expected: New folder appears in the folder list with the entered name
- [X] FT-06: User can organize documents into a folder
  - Action: Select an existing document, use "Move to" or drag it into an existing folder
  - Expected: Document is listed inside the selected folder and no longer appears in the root list
- [X] FT-07: User can add tags to documents (tagged collections)
  - Action: Select a document, click "Add Tag", enter a tag name, save
  - Expected: Tag is associated with the document and visible on its detail/list view
- [X] FT-08: User can rename a document
  - Action: Right-click a document (or click "Rename"), enter a new name, save
  - Expected: Document displays the new name throughout the vault list and search
- [X] FT-09: User can delete a document
  - Action: Select a document, click "Delete", confirm the deletion in the confirmation dialog
  - Expected: Document is removed from the vault and no longer appears in lists, folders, or search
- [X] FT-10: User can search documents by name
  - Action: Type a known full or partial document name into the search bar
  - Expected: Only documents whose names match the query are displayed in the results
- [X] FT-11: User can search documents by tag
  - Action: Type a known tag name (or select an existing tag) in the search/filter
  - Expected: Only documents associated with the matching tag are displayed in the results

## Constraint

- [X] CS-01: Login fails with invalid credentials
  - Action: Enter a registered email with an incorrect password, click "Log In"
  - Expected: Login is rejected and an error message such as "Invalid email or password" is shown
- [X] CS-02: Registration is blocked when required fields are missing
  - Action: Leave the email or password field empty on the registration form, click "Register"
  - Expected: Submission is prevented and a validation error is displayed for the empty field(s)
- [X] CS-03: Unauthenticated users cannot access vault content
  - Action: While logged out, attempt to navigate directly to a vault page (e.g., documents, folders, search)
  - Expected: Access is denied; user is redirected to the login page
- [X] CS-04: Users cannot view or manage another user's documents
  - Action: Log in as User B (after User A has uploaded documents), search for or attempt to open User A's documents
  - Expected: User B sees no documents belonging to User A and cannot open or modify them
- [ ] CS-05: Registration enforces password strength
  - Action: Attempt to register with a weak password (e.g., "123" or "password")
  - Expected: Registration is rejected with a message requiring a stronger password
  - Bug Report:
    - Issue: Insufficient password strength validation (weak password accepted)
    - Actual: With "123" registration was correctly blocked (native message: "Please lengthen this text to 8 characters or more (you are currently using 3 characters)"). However the checklist's other explicit example, "password" (8 chars), was **accepted**: the toast "Account created successfully" appeared, the account `weakpw.qa@test.com` was created and logged into the vault. The only rule is `minlength=8`; there is no complexity/strength check (no rejection of dictionary/weak passwords), and "Password must be at least 8 characters" is a static helper line, not an error message.

## Interaction

- [X] IX-01: Successful login provides positive feedback
  - Action: Submit valid login credentials
  - Expected: A success indicator (e.g., redirect to dashboard, welcome message, or toast) is shown
- [X] IX-02: Successful document upload shows confirmation
  - Action: Complete a document upload
  - Expected: A success message or confirmation (e.g., "Upload complete") appears, and the new document appears in the list
- [X] IX-03: Search results update dynamically as the user types
  - Action: Type different keywords/tags into the search bar
  - Expected: The result list updates to reflect the current query without requiring a manual refresh

## Content

- [X] CT-01: Uploaded document content is preserved intact
  - Action: Upload a file with known/unique content, then download or open it from the vault
  - Expected: The downloaded file matches the originally uploaded file in name, type, and content
- [X] CT-02: Document names and tags are displayed correctly
  - Action: View the document list after uploading, renaming, or tagging documents
  - Expected: Each document displays its correct name and any applied tag(s) without truncation or mismatch

---

### Evidence collected (key observations)

- **Auth flow:** "Account created successfully" → dashboard; "Welcome back!" → dashboard; "Invalid email or password" → stays on login; "Sign out" → login screen, `vault_session` removed from localStorage.
- **Upload/menu:** Document row menu exposes Download / Rename / Edit Tags / Move / Delete. Upload dialog shows "Drop files here or click to browse", preset tag chips (important, archive, pending, confidential) and "Add new tag…". After upload: "3 documents uploaded and encrypted", Documents (3) with correct names/sizes (52 B / 33 B / 30 B).
- **FT-06 proof:** After Move → "QA Reports": folder card reads "1 document", folder view (breadcrumb "Vault / QA Reports") lists `archive-notes.txt`, and root list dropped to "Documents (2)".
- **FT-08/FT-10 proof:** Renamed `qa-report.txt` → `renamed-vault-report.txt` (toast "Document renamed"); search "r"…"renamed" returned "Search Results (1) | renamed-vault-report.txt".
- **FT-11 proof:** Search "qa-tag" (a tag, not part of any filename) → "Search Results (1) | renamed-vault-report.txt"; search "important" → same; search "zzz-nomatch" → "No results found".
- **FT-09 proof:** Native confirm dialog `Delete "temp-delete-me.txt"? This cannot be undone.` → after accept, "Documents (1)" and search "temp" → "No results found".
- **CS-03 proof:** All vault content lives on the single route `/`; while logged out, `/` renders only the login form (no `<main>` vault), and paths such as `/vault`, `/documents`, `/search`, `/folders` render the "404 – Oops! Page not found" page.
- **CS-04 proof:** User B (`bob.qa@test.com`) sees only default folders Personal/Work, no "QA Reports"; searches for "renamed-vault-report", "qa-report", "qa-tag", "important", "archive-notes" all return "No results found"; each user gets a separate `vault_data_<uuid>` store key.
- **CT-01 proof:** Download produced `download="qa-report.txt"`, `data:text/plain;base64,U0VDVVJFVkFVTFQtUUEtTUFSS0VSLTQyCkxpbmUgdHdvIG9mIHRlc3QgZG9jdW1lbnQuCg==`, decoding exactly to `SECUREVAULT-QA-MARKER-42\nLine two of test document.\n` (52 bytes); the saved file on disk reads back byte-identical. Same for the renamed copy (`renamed-vault-report.txt`, 52 B, content intact).
- **CT-02 proof:** Doc headings show `scrollWidth == clientWidth` (no truncation), `title` attribute equals the displayed name, and tags render as separate chips `important`, `qa-tag`.

### Additional observation (not covered by any checklist item)

The app's UI states *"All files will be encrypted before storage"* and *"All data is encrypted and stored locally in your browser"*, but storage inspection shows `localStorage["vault_data_<uuid>"]` holds clear JSON metadata (`name`, `tags`) and the file body as a **plaintext base64 data URL** (`"content":"data:text/plain;base64,U0VDVVJFVkFVTFQtUUEtTUFSS0VSLTQy…"`), with only an `encryptedKey` field beside it; IndexedDB is empty. Document data at rest is therefore readable without the user's password — worth addressing given the stated "strongly encrypted" requirement, though no checklist item directly measures it.

### Artifacts left in the working directory

`.playwright-mcp/` now contains `doc-list.md`, `qa-report.txt`, `renamed-vault-report.txt` (downloads + a snapshot) from the run; the app is left logged in as `alice.qa@test.com`, and the accounts `bob.qa@test.com` and `weakpw.qa@test.com` remain in `vault_users` (the app exposes no account-deletion UI).