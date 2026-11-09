# Test Result

## Functionality
- [X] FT-01: Create a new account
  - Action: Open the sign-up page, enter a valid email/username and password (e.g., `tester@example.com` / `Passw0rd!`), and submit.
  - Expected: Account is created successfully and the user is either logged in automatically or redirected to the login page with a success message.
- [X] FT-02: Log in with valid credentials
  - Action: Enter the credentials of an existing account on the login form and click the login button.
  - Expected: Login succeeds and the user is taken to the vault dashboard showing their documents/folders.
- [X] FT-03: Log out
  - Action: Click the logout control while logged in.
  - Expected: The user is logged out and returned to the login/landing page; vault content is no longer accessible.
- [X] FT-04: Upload a document
  - Action: While logged in, click the upload button and select a document file (e.g., `report.pdf`).
  - Expected: The file uploads successfully and appears in the document list with its filename.
- [X] FT-05: Create a folder
  - Action: Click the "Create Folder" (or equivalent) button and enter a folder name (e.g., `Taxes`).
  - Expected: The new folder `Taxes` appears in the vault navigation/folder list.
- [X] FT-06: Move a document into a folder
  - Action: Select an uploaded document and move it into a folder (e.g., drag it to or use "Move to" → `Taxes`).
  - Expected: The document is now listed inside the folder, and no longer in the previous location.
  - Note: Move worked via "Move" menu → "Move Document" dialog → destination `Taxes`. The doc disappeared from root and appeared inside `Personal > Taxes` (1 document). The dialog listed duplicate `Taxes` entries because of the CS-04 bug (duplicate folders exist).
- [X] FT-07: Add a tag to a document
  - Action: Select a document, use the tag control, and add a tag (e.g., `medical`).
  - Expected: The tag `medical` is displayed on the document and stored in its details.
  - Note: Tags `medical`/`confidential` were applied at upload and `pending` added via the document's "Edit Tags" dialog; all tags display on the card. Minor cosmetic issue: the upload dialog does not visibly render a chip when a custom tag is entered (the tag is still applied), and adding the same tag twice produced a duplicated chip (`medical` + `medicalmedical`) with no de-duplication.
- [X] FT-08: Rename a document
  - Action: Use the rename option on an existing document and change its name (e.g., `report.pdf` → `insurance-2026.pdf`).
  - Expected: The document list shows the new name immediately after confirming.
- [X] FT-09: Delete a document
  - Action: Select a document and choose the delete option; confirm if prompted.
  - Expected: The document is removed from the document list.
- [X] FT-10: Search documents by name
  - Action: Type a known document name (or a unique partial of it, e.g., `insurance`) into the search box and submit.
  - Expected: Only matching documents are returned, including the one named `insurance-2026.pdf`.
- [X] FT-11: Search documents by tag
  - Action: Type an existing tag (e.g., `medical`) into the search box.
  - Expected: All documents carrying that tag are returned; unrelated documents are not.
- [X] FT-12: Download/view a stored document
  - Action: Click a stored document to open/preview or download it.
  - Expected: The document's original readable content is retrieved successfully (not corrupted or unreadable).
  - Note: Download via "Download" menu item preserved the filename (`insurance-2026.pdf`) and the downloaded file's bytes exactly matched the uploaded content (37 B, verified on disk).

## Constraint
- [X] CS-01: Cannot create account with missing/invalid fields
  - Action: Submit the sign-up form with an empty field or an invalid email / too-short password (e.g., `123`).
  - Expected: Submission is rejected and a specific validation error is shown; no account is created.
  - Note: Rejected via native HTML validation — empty email → "Please fill out this field."; 3-char password → "Please lengthen this text to 8 characters or more…"; form never submits. Static hint "Password must be at least 8 characters" is also shown.
- [X] CS-02: Cannot log in with wrong password
  - Action: Enter a valid username with an incorrect password and submit.
  - Expected: Login fails with a generic error message (no confirmation that the username exists) and the user stays on the login page.
- [X] CS-03: Unauthenticated users cannot access the vault
  - Action: While logged out, navigate directly to the vault/documents URL.
  - Expected: Access is denied — the user is redirected to the login page and sees no documents.
  - Note: After sign-out, direct navigation to `/` shows only the auth screen (no vault data), and `/vault` returns a 404 page — no vault route or content is accessible unauthenticated.
- [ ] CS-04: Duplicate folder name is rejected
  - Action: Attempt to create a second folder with a name that already exists (e.g., `Taxes`).
  - Expected: The app prevents creation and shows an error like "Folder name already exists."
  - Bug Report:
    - Issue: Missing duplicate validation on folder creation
    - Actual: Creating a second folder named `Taxes` succeeded with the success toast `Folder "Taxes" created` — the vault now shows `Folders (4)` with two root folders both named `Taxes`, and the "Move Document" dialog consequently lists three ambiguous `Taxes` entries. No error message of any kind was shown.
- [X] CS-05: User data is isolated between accounts
  - Action: Log in with a different account and view the vault (or attempt to search for a document name created by the first account).
  - Expected: No documents, folders, or tags from the first account are visible or searchable.
  - Note: New account `other@example.com` sees only its own default `Personal`/`Work` folders with 0 documents; searching `insurance` and `medical` returns "No results found".

## Interaction
- [X] IX-01: Deletion requires confirmation
  - Action: Click delete on a document.
  - Expected: A confirmation prompt (e.g., "Are you sure you want to delete this document?") appears before deletion; canceling keeps the document.
  - Note: Native confirm dialog appears: `Delete "insurance-2026.pdf"? This cannot be undone.` — dismissing it left the document intact.
- [X] IX-02: Upload progress/error feedback
  - Action: Upload a document.
  - Expected: A visible progress indicator and/or success toast appears during/after upload, and the new document appears in the list without a page reload.
  - Note: Success toast `1 document uploaded and encrypted` appeared and the document appeared in the list immediately with no page reload.
- [X] IX-03: Search results update in response to the query
  - Action: Type a query into the search box.
  - Expected: The document list updates to reflect the query; a "no results" message appears when nothing matches.
  - Note: The list updated live on every keystroke; `zzznomatch` produced `No results found — No documents match "zzznomatch"…`.

## Content
- [X] CT-01: Document list shows meaningful details
  - Action: View the document list.
  - Expected: Each document shows its filename plus at least one useful detail (e.g., size, upload date, tags, or folder).
  - Note: Each card shows filename, file size (`37 B` / `62 B`), upload date (`Nov 8, 2026`), and tag chips.
- [X] CT-02: Encryption status is visible and truthful
  - Action: Inspect the vault UI for encryption indication (e.g., "Encrypted" badge, lock icon, security notice).
  - Expected: The UI clearly indicates that stored documents are encrypted, and it never displays any document's decrypted content in plain text in the list or search results.
  - Note: Each document card carries a lock icon overlay; upload dialog states "All files will be encrypted before storage"; toasts confirm "uploaded and encrypted"; footer reads "🔒 All data is encrypted and stored locally in your browser". Deliberate plaintext content ("SECRET CONTENT…") embedded in an uploaded file never appeared anywhere in the list or search results.
