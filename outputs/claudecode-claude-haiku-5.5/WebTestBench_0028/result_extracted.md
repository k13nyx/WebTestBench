# Test Result

**Run note:** Executed against http://localhost:6028/ with Playwright. Creating a local PDF fixture was denied (Bash and Write both required approval and were refused), so no document could be uploaded. Every item that depends on an uploaded document is marked FAIL as not executed, and those reasons are concrete. Two of the failures are real UI deviations (CS-01, IX-03), and the Back-button result (CS-04) is also a deviation. The rest are blocked by the missing fixture, not by an app defect.

## Functionality

- [X] FT-01: User can create a new account
  - Action: On the sign-up page, enter a new unused email and a valid password, then click "Sign Up".
  - Expected: Account is created and the user reaches the vault (or a login prompt with a success message), with no error.
  - Note: The submit button is labeled "Create Vault", not "Sign Up". The outcome matched: "Account created successfully" toast and the vault opened.
- [X] FT-02: User can log in with an existing account
  - Action: Log in with the email and password from FT-01, then click "Log In".
  - Expected: Vault page opens and shows the logged-in user's email in the header.
  - Note: The submit button is labeled "Unlock Vault", not "Log In". The vault opened with "qa-tester-2026@example.com" in the header.
- [ ] FT-03: User can upload a document
  - Action: Click "Upload", choose a local document file (e.g., a PDF), and confirm.
  - Expected: The file appears in the document list under its original file name.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: The Upload dialog opened and its drop zone triggered the file chooser, but no local file could be supplied. Creating the fixture via Bash and Write was denied, and the Upload button stayed disabled. No file was uploaded.
- [ ] FT-04: User can create a folder and move a document into it
  - Action: Click "New Folder", enter "Taxes", click "Create". Then select the uploaded document and choose "Move to" > "Taxes".
  - Expected: Folder "Taxes" is listed, and the document appears inside it and no longer at the root level.
  - Bug Report:
    - Issue: Incomplete Execution (move step not executed)
    - Actual: Folder "Taxes" was created and listed ("Folders (3)", "Taxes — 0 documents"). The "Move to > Taxes" step could not run because no document exists (see FT-03).
- [ ] FT-05: User can add a tag to a document
  - Action: Select the document, click "Add Tag", type "2026", and press Enter.
  - Expected: A "2026" tag chip appears on the document.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No document exists to select, because the upload could not be performed (see FT-03). The Upload dialog does offer a tag input ("Add new tag..."), but the document-level "Add Tag" action could not be reached.
- [ ] FT-06: User can rename a document
  - Action: Select the document, click "Rename", change the name to "Renamed-Doc", and click "Save". Reload the page.
  - Expected: The list shows "Renamed-Doc" after reload, and the old name no longer appears.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No document exists to rename (see FT-03).
- [ ] FT-07: User can delete a document
  - Action: Select the document, click "Delete", then click the confirm "Delete" button.
  - Expected: The document is removed from the list and from its folder.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No document exists to delete (see FT-03).
- [ ] FT-08: User can search documents by name
  - Action: Type part of a stored document's name (e.g., "Renamed") into the search box.
  - Expected: Only documents whose names contain that text are listed.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No stored documents exist to search (see FT-03). Searching "Ren" hid the folders and showed "No results found", but that does not test document-name matching.
- [ ] FT-09: User can search documents by tag
  - Action: Type "2026" into the search box.
  - Expected: Only documents tagged "2026" are listed.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No tagged documents exist (see FT-03, FT-05).

## Constraint

- [ ] CS-01: Sign-up rejects an email that is already registered
  - Action: On the sign-up page, enter an email already used in FT-01 and click "Sign Up".
  - Expected: Error "Email already registered" appears, and no new account is created.
  - Bug Report:
    - Issue: Incorrect Error Message
    - Actual: The toast reads "An account with this email already exists", not "Email already registered". The sign-up was rejected and the page stayed on the sign-up form.
- [X] CS-02: Login rejects an incorrect password
  - Action: Enter the correct email with a wrong password and click "Log In".
  - Expected: Error "Invalid email or password" appears, and the vault does not open.
- [ ] CS-03: Sign-up enforces the password policy
  - Action: Enter the password "123" on the sign-up page and click "Sign Up".
  - Expected: Error lists the minimum password requirements, and the account is not created.
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: Submitting "123" (twice, with matching confirmation) produced no error notification or inline error. Only the static hint "Password must be at least 8 characters" was visible, and it was present before submission. The page stayed on the sign-up form and no vault opened.
- [ ] CS-04: Vault content is inaccessible after logout
  - Action: Click "Log Out", then press the browser Back button.
  - Expected: The login page is shown, and no document list or file names are visible.
  - Bug Report:
    - Issue: Unexpected Navigation Target
    - Actual: After clicking "Sign out", the vault closed correctly. Browser Back then landed on `about:blank` rather than the login page. No document or file names were visible. Caveat: the session history began with a direct navigation, so the Back target may lie outside the app.
- [ ] CS-05: Delete can be cancelled without removing the document
  - Action: Select a document, click "Delete", then click "Cancel" in the confirmation.
  - Expected: The document remains in the list with its name and tags unchanged.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No document exists to select (see FT-03).
- [ ] CS-06: A different user cannot see another user's documents
  - Action: Log out, log in with a different account, and view the document list. Search for "Renamed".
  - Expected: The first account's documents are not listed, and the search returns no results.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: The first account has no documents, so the isolation check cannot show anything. A second account was not created.

## Interaction

- [ ] IX-01: Each completed action shows a matching confirmation toast
  - Action: Upload a file, rename it, and delete it, observing the message after each action.
  - Expected: Toasts read "Document uploaded", "Document renamed", and "Document deleted" respectively, and each appears within 2 seconds.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No upload, rename, or delete could be performed (see FT-03). Toasts observed for other actions: "Account created successfully", "Welcome back!", "Folder "Taxes" created".
- [ ] IX-02: Search filters live and clearing restores the full list
  - Action: Type "Ren" into the search box without pressing Enter, then clear the box.
  - Expected: The list filters as text is typed, and clearing the box shows all documents again.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition for document filtering)
    - Actual: Folder filtering worked: typing "Ren" hid all folders and showed "No results found", and clearing the box restored "Folders (3)". Document filtering and document restoration could not be checked because no documents exist.
- [ ] IX-03: A no-match search shows an empty-state message
  - Action: Type "zzzz" into the search box.
  - Expected: The message "No documents found" is shown in place of the list.
  - Bug Report:
    - Issue: Incorrect Empty-State Message
    - Actual: The heading reads "No results found" with the body "No documents match "zzzz". Try a different search term or check your spelling." The expected text "No documents found" does not appear.

## Content

- [ ] CT-01: Document list shows accurate names, tags, and folder for each item
  - Action: Compare the list entries for the uploaded document against the local file name and the tags and folder assigned in FT-04 and FT-05.
  - Expected: Name, tag, and folder values match exactly, with no missing or swapped entries.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No document entry exists to compare (see FT-03).
- [ ] CT-02: Document metadata matches the actual file
  - Action: Compare the displayed size and upload date for the document with the local file's properties.
  - Expected: File size matches the local file (within display rounding), and the upload date is 2026-11-09.
  - Bug Report:
    - Issue: Test Not Executed (missing precondition)
    - Actual: No document exists to display metadata for (see FT-03). The system date reported is 2026-11-09, but this was not verified against the app.
