# Test Checklist

## Functionality
- [ ] FT-01: User can create a new account
  - Action: On the sign-up page, enter a new unused email and a valid password, then click "Sign Up".
  - Expected: Account is created and the user reaches the vault (or a login prompt with a success message), with no error.
- [ ] FT-02: User can log in with an existing account
  - Action: Log in with the email and password from FT-01, then click "Log In".
  - Expected: Vault page opens and shows the logged-in user's email in the header.
- [ ] FT-03: User can upload a document
  - Action: Click "Upload", choose a local document file (e.g., a PDF), and confirm.
  - Expected: The file appears in the document list under its original file name.
- [ ] FT-04: User can create a folder and move a document into it
  - Action: Click "New Folder", enter "Taxes", click "Create". Then select the uploaded document and choose "Move to" > "Taxes".
  - Expected: Folder "Taxes" is listed, and the document appears inside it and no longer at the root level.
- [ ] FT-05: User can add a tag to a document
  - Action: Select the document, click "Add Tag", type "2026", and press Enter.
  - Expected: A "2026" tag chip appears on the document.
- [ ] FT-06: User can rename a document
  - Action: Select the document, click "Rename", change the name to "Renamed-Doc", and click "Save". Reload the page.
  - Expected: The list shows "Renamed-Doc" after reload, and the old name no longer appears.
- [ ] FT-07: User can delete a document
  - Action: Select the document, click "Delete", then click the confirm "Delete" button.
  - Expected: The document is removed from the list and from its folder.
- [ ] FT-08: User can search documents by name
  - Action: Type part of a stored document's name (e.g., "Renamed") into the search box.
  - Expected: Only documents whose names contain that text are listed.
- [ ] FT-09: User can search documents by tag
  - Action: Type "2026" into the search box.
  - Expected: Only documents tagged "2026" are listed.

## Constraint
- [ ] CS-01: Sign-up rejects an email that is already registered
  - Action: On the sign-up page, enter an email already used in FT-01 and click "Sign Up".
  - Expected: Error "Email already registered" appears, and no new account is created.
- [ ] CS-02: Login rejects an incorrect password
  - Action: Enter the correct email with a wrong password and click "Log In".
  - Expected: Error "Invalid email or password" appears, and the vault does not open.
- [ ] CS-03: Sign-up enforces the password policy
  - Action: Enter the password "123" on the sign-up page and click "Sign Up".
  - Expected: Error lists the minimum password requirements, and the account is not created.
- [ ] CS-04: Vault content is inaccessible after logout
  - Action: Click "Log Out", then press the browser Back button.
  - Expected: The login page is shown, and no document list or file names are visible.
- [ ] CS-05: Delete can be cancelled without removing the document
  - Action: Select a document, click "Delete", then click "Cancel" in the confirmation.
  - Expected: The document remains in the list with its name and tags unchanged.
- [ ] CS-06: A different user cannot see another user's documents
  - Action: Log out, log in with a different account, and view the document list. Search for "Renamed".
  - Expected: The first account's documents are not listed, and the search returns no results.

## Interaction
- [ ] IX-01: Each completed action shows a matching confirmation toast
  - Action: Upload a file, rename it, and delete it, observing the message after each action.
  - Expected: Toasts read "Document uploaded", "Document renamed", and "Document deleted" respectively, and each appears within 2 seconds.
- [ ] IX-02: Search filters live and clearing restores the full list
  - Action: Type "Ren" into the search box without pressing Enter, then clear the box.
  - Expected: The list filters as text is typed, and clearing the box shows all documents again.
- [ ] IX-03: A no-match search shows an empty-state message
  - Action: Type "zzzz" into the search box.
  - Expected: The message "No documents found" is shown in place of the list.

## Content
- [ ] CT-01: Document list shows accurate names, tags, and folder for each item
  - Action: Compare the list entries for the uploaded document against the local file name and the tags and folder assigned in FT-04 and FT-05.
  - Expected: Name, tag, and folder values match exactly, with no missing or swapped entries.
- [ ] CT-02: Document metadata matches the actual file
  - Action: Compare the displayed size and upload date for the document with the local file's properties.
  - Expected: File size matches the local file (within display rounding), and the upload date is 2026-11-09.