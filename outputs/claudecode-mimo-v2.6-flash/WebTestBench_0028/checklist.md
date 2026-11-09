# Test Checklist

## Functionality
- [ ] FT-01: User can create a new account
  - Action: Open the sign-up page, enter a unique username and password, and submit the form.
  - Expected: The account is created and the user is taken to the login page (or logged in directly) with no error shown.

- [ ] FT-02: User can log in with valid credentials
  - Action: On the login page, enter the registered username and correct password, then click "Log In".
  - Expected: The user is authenticated and the document vault dashboard is displayed.

- [ ] FT-03: User can upload a document
  - Action: While logged in, click the upload button, select a local file, and confirm the upload.
  - Expected: The file appears in the document list with its filename and is retrievable after a page refresh.

- [ ] FT-04: User can create a folder and organize a document into it
  - Action: Create a folder named "Taxes", then move or upload an existing document into that folder.
  - Expected: The folder "Taxes" exists and the document is listed inside it.

- [ ] FT-05: User can tag a document
  - Action: Open a document's options and add the tag "important" to it.
  - Expected: The tag "important" is attached to the document and visible on its entry.

- [ ] FT-06: User can rename a document
  - Action: Select a stored document, choose rename, enter "Insurance Policy 2026", and save.
  - Expected: The document is now displayed as "Insurance Policy 2026" in the list.

- [ ] FT-07: User can delete a document
  - Action: Select a stored document and use the delete action, confirming when prompted.
  - Expected: The document no longer appears in the list or in any folder/tag view.

- [ ] FT-08: User can search documents by name
  - Action: Type a known document's name (or a distinct part of it) into the search field.
  - Expected: Only documents whose filenames match the query are shown in the results.

- [ ] FT-09: User can search documents by tag
  - Action: Search using the tag "important" that was applied to a document.
  - Expected: The tagged document appears in the search results.

## Constraint
- [ ] CS-01: Account creation is blocked when required fields are empty
  - Action: Submit the sign-up form with an empty username or empty password.
  - Expected: No account is created and an inline error indicates the required field is missing.

- [ ] CS-02: Registration is blocked for an already-used username
  - Action: Attempt to sign up with a username that already exists.
  - Expected: The submission is rejected with a message stating the username is taken.

- [ ] CS-03: Login is rejected with a wrong password
  - Action: Enter a valid username with an incorrect password and click "Log In".
  - Expected: The user is not authenticated; an error message is shown and the vault remains inaccessible.

- [ ] CS-04: Document deletion requires confirmation
  - Action: Click the delete action on a document but cancel at the confirmation prompt.
  - Expected: The document remains in the vault unchanged.

- [ ] CS-05: Vault content is inaccessible without an authenticated session
  - Action: Log out (or open the vault URL in a fresh browser session with no login).
  - Expected: The user is redirected to the login page and no document names, tags, or file content are visible.

- [ ] CS-06: Folder creation is blocked with an empty name
  - Action: Attempt to create a folder while the folder name field is empty.
  - Expected: No folder is created and an error asks for a folder name.

## Interaction
- [ ] IX-01: A success confirmation appears after uploading a document
  - Action: Complete a valid file upload and observe the interface.
  - Expected: A success message (toast/notice) such as "Upload complete" is displayed and the list refreshes to include the new file.

- [ ] IX-02: Search results respond live to the query
  - Action: Type into the search field, then clear the query completely.
  - Expected: Results filter as the query changes, and clearing it restores the full document list.

## Content
- [ ] CT-01: Document entries display correct metadata
  - Action: After uploading a file, inspect its entry in the list.
  - Expected: The entry shows the exact original filename and a file-type indicator matching the uploaded file.

- [ ] CT-02: Applied tags and folder names are shown accurately on documents
  - Action: Review a document that has tag "important" inside folder "Taxes".
  - Expected: The document entry displays the tag "important" and indicates it belongs to folder "Taxes" with no typos or missing labels.