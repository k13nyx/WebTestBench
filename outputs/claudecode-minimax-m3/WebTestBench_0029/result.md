Filters cleared. I now have enough information to produce the final Test Result markdown document.

# Test Result

## Functionality

- [X] **FT-01 Add a new book with valid title, author, genre and notes**
  - Book "Brave New World" by Aldous Huxley (Dystopian, notes: "Test book") was successfully added; "Book Added" notification appeared; total book count incremented from 10 to 11.

- [ ] **FT-02 Update reading status (To Read → Reading → Completed)**
  - Status transition menu options appear, but transitioning to Completed triggers a duplicate, stale "Rate & Review" dialog (review text from a previously opened book is shown instead of fresh empty fields).
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open any Reading-status book menu → Mark as Completed. 2) Cancel/dismiss the "Rate & Review" prompt. 3) Open a different Completed book's menu → Edit Review. 4) Observe review textarea.
    - **Expected**: Edit Review dialog for the second book shows that book's own existing review.
    - **Actual**: Dialog shows the stale review text "A powerful exploration of racial injustice..." from a previously opened book.
    - **Impact**: Users edit or overwrite the wrong book's review, silently corrupting data.

- [ ] **FT-03 Edit progress (percentage / current page) for a Reading-status book**
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open the menu (⋮) of any Reading-status book. 2) Click "Edit Details". 3) Observe the Edit Book dialog.
    - **Expected**: Dialog opens with the book's existing title, author, genre, status, notes, current page, and total pages pre-filled.
    - **Actual**: All fields render empty (`<input>` values are `""`); the status defaults to "To Read" and genre defaults to "Classic Fiction". The book being edited is not recognized.
    - **Impact**: Users cannot edit progress, total pages, notes, or status for any existing book. Editing is effectively broken.

- [ ] **FT-04 Record start and finish dates manually**
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open Edit Book dialog (via "Edit Details") for any book.
    - **Expected**: Manual date inputs (e.g., `<input type="date">`) for "Started" and "Finished".
    - **Actual**: No date input fields exist in the Add/Edit Book dialog. Dates are auto-generated on status change and cannot be customized.
    - **Impact**: Users cannot back-date a book, fix an incorrect auto-date, or set a planned finish date.

- [X] **FT-05 Rate a completed book and write a review**
  - Rate & Review dialog on a Completed book accepts 5-star rating and free-text review; the new rating/review displays on the book card (e.g., "Project Hail Mary" 5★ "Amazing scientific mystery...").

- [ ] **FT-06 View reading history (books read over time)**
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open the application. 2) Look for a "Reading History", "History", "Timeline", or similar view.
    - **Expected**: A distinct view showing reading activity over time (chronologically, monthly, etc.).
    - **Actual**: No such section exists. The page only exposes "All", "To Read", "Reading", "Completed" tabs of the current library.
    - **Impact**: Users cannot review their past reading activity or trends.

- [X] **FT-07 Edit an existing rating/review**
  - "Edit Review" menu option on a Completed book opens a dialog pre-loaded with the existing review text and current rating (verified on To Kill a Mockingbird — text "A powerful exploration..." pre-filled).

- [ ] **FT-08 Delete a rating/review**
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open the menu (⋮) of a Completed book that has a rating/review. 2) Look for a "Delete Review" or "Remove Rating" action.
    - **Expected**: An option to clear the rating and review while keeping the book in the library.
    - **Actual**: No delete/clear option exists; only "Edit Review" is available. Users must overwrite with new content — they cannot return a book to "unrated".
    - **Impact**: Users cannot undo a review or remove an accidental rating.

- [X] **FT-09 See recommendations based on frequently-read genres / highly-rated books**
  - "Recommended for You" section displays 3 suggestions (The Midnight Library, The Hobbit, The Name of the Wind).

- [X] **FT-10 Search books by title or author**
  - Typing "hob" into the search bar filters the list to "The Hobbit" only; clearing the search restores the full list.

- [X] **FT-11 Combine Genre + Status + Rating filters**
  - Applying Genre="Classic Fiction" + Status="Completed" + Rating="5 Stars" filters the list down to the matching subset; all three filter chips become active simultaneously; results narrow on each click without a manual refresh.

## Constraint

- [X] **CS-01 Title and Author are required when adding a book**
  - With title and author blank, the Add Book dialog's "Add Book" submit button is disabled. HTML5 `required` attributes are also present (`<input required>`).

- [X] **CS-02 Rating and review can only be added/edited for Completed books**
  - "Edit Review" only appears in the menu of Completed books. Reading-status books (Dune) and To-Read books (The Midnight Library) show no such option — instead "Mark as Completed" / "Start Reading".

- [ ] **CS-03 Finish date must be on or after the start date**
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open Edit Book dialog. 2) Look for start-date and finish-date inputs. 3) Attempt to enter a finish date earlier than the start date.
    - **Expected**: Validation prevents or warns about a finish date earlier than the start date.
    - **Actual**: No date inputs exist in the Add/Edit Book dialog (same root cause as FT-04). The constraint cannot be satisfied because the inputs are missing.
    - **Impact**: This constraint is impossible to honor for the user.

## Interaction

- [ ] **IX-01 Editing reading progress updates the list view immediately without a separate save action**
  - **Bug Report**:
    - **Steps to reproduce**: 1) Open the menu of a Reading-status book. 2) Click "Edit Details". 3) Change the current page value. 4) Click "Save Changes". 5) Observe the card.
    - **Expected**: The progress bar and "X / Y pages" text on the card update immediately after saving, without requiring a page reload.
    - **Actual**: The Edit Details dialog opens with empty fields (FT-03), so the user cannot reliably change progress from the existing value. Any value entered is effectively a replacement of the entire book record rather than an in-place progress edit; without a working edit flow, the immediate-update behavior cannot be exercised.
    - **Impact**: Progress edits either fail silently or require destructive re-entry of all fields, discouraging use.

- [X] **IX-02 Filter combination updates the list view immediately, no separate "Apply" needed**
  - Each filter dropdown change re-renders the list immediately; no "Apply" button is present or required.

## Content

- [X] **CT-01 Each book card displays core details (title, author, genre, status)**
  - Every card shows title (heading), author (paragraph), status badge, and genre badge. Reading cards additionally show "X / Y pages" + a progress bar; Completed cards additionally show started/finished dates and rating stars.

- [X] **CT-02 Recommended books share a genre with a frequently-read book, or resemble a 5-star rated book**
  - Recommendations include 2 Fantasy titles (The Hobbit, The Name of the Wind); Fantasy is a frequently-read genre in this library, satisfying the relevance criterion.