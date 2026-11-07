# Test Result

## Functionality

- [X] FT-01: Add a book to the personal library
  - Action: Click "Add Book", fill Title, Author, Genre (required) and Notes (optional), click "Save".
  - Expected: The new book appears in the library (e.g., under the "To Read" list).

- [ ] FT-02: Edit an existing book's details
  - Action: Open a book, click "Edit", change Title/Author/Genre/Notes, click "Save".
  - Expected: The book's details update and persist in the library.
  - Bug Report:
    - Issue: Edit operates on the wrong book (broken "Edit Details" menu action)
    - Actual: Opening *any* book's menu and clicking "Edit Details" always opens the **first book in the library** ("QA Test Book Edited"), not the book whose menu was opened. Verified twice: The Midnight Library → Edit Details opened QA Test Book; The Great Gatsby → Edit Details also opened QA Test Book. Editing therefore cannot target the selected (non-first) book.

- [ ] FT-03: Track reading progress by percentage or page count
  - Action: Open a "Currently Reading" book, enter progress as percentage or page count, save.
  - Expected: Progress is displayed and reflects the entered value.
  - Bug Report:
    - Issue: Progress entry unreachable due to broken Edit Details dialog + no percentage input
    - Actual: Progress is only editable inside the "Edit Book" dialog (Current Page / Total Pages), but that dialog always targets the first book (see FT-02), so a "Currently Reading" book cannot be updated. Also, there is no percentage input — only page counts (which are otherwise supported), so the "percentage" option is not implementable.

- [ ] FT-04: Set start and finish dates for a book
  - Action: Open a book, set "Start Date" and "Finish Date", save.
  - Expected: Both dates are recorded and shown on the book.
  - Bug Report:
    - Issue: No date input fields exist anywhere in the app
    - Actual: The "Edit Book" dialog and "Rate & Review" dialog contain only Title, Author, Genre, Status, Total Pages, Current Page, Cover URL, Notes (and Rating/Review). No "Start Date"/"Finish Date" inputs are present (confirmed via DOM scan: 0 date inputs). Dates shown on completed cards (e.g., "Started: 1/15/2024") are pre-seeded display-only data.

- [ ] FT-05: Move a book between lists
  - Action: Use the status control to move a book through "To Read" → "Currently Reading" → "Completed".
  - Expected: The book appears under each selected list accordingly.
  - Bug Report:
    - Issue: Status control (Edit Details) is broken; only To Read→Reading works
    - Actual: The card "Start Reading" button correctly moves a To Read book to Reading (verified: The Midnight Library moved immediately, counts updated 4→3 To Read / 2→3 Reading). However, moving a book to "Completed" requires the Status dropdown inside the broken "Edit Book" dialog, which always edits the first book — so a selected book cannot be set to Completed. The full To Read→Reading→Completed cycle cannot be completed for an arbitrary book.

- [X] FT-06: Rate a completed book
  - Action: Open a "Completed" book, set a rating (e.g., 4 stars), save.
  - Expected: The rating is saved and shown on the book.
  - (Opened The Great Gatsby's "Edit Review" — correctly targeted Gatsby — set 5 stars, saved; toast "Review Saved" appeared.)

- [X] FT-07: Write a review for a completed book
  - Action: Open a "Completed" book, enter review text, save.
  - Expected: The review is saved and associated with the book.
  - ("Review (optional)" text entered and saved successfully; toast "Your rating and review have been saved.")

- [X] FT-08: View completed books in reading history
  - Action: Open the "Reading History" section.
  - Expected: All "Completed" books with their ratings/reviews are listed.
  - (The "Completed" tab functions as the reading history and lists all completed books with their rating stars. Note: review text is stored/editable via "Edit Review" but is not displayed inline in the list.)

- [X] FT-09: Edit a rating/review from reading history
  - Action: In Reading History, select a book, edit its rating/review, save.
  - Expected: The updated rating/review persists in the history.
  - (The "Edit Review" dialog correctly targets the opened completed book and re-saving persists changes — verified on The Great Gatsby.)

- [ ] FT-10: Delete a rating/review from reading history
  - Action: In Reading History, select a book, delete its rating/review.
  - Expected: The rating/review is removed; the book remains without it if applicable.
  - Bug Report:
    - Issue: No control exists to delete/clear a rating or review
    - Actual: The "Rate & Review" dialog contains only "Save Review" and "Cancel". The per-book menu contains only "Edit Details", "Edit Review", and "Remove from Library" (which deletes the entire book, not just the rating/review). There is no way to remove a rating/review while keeping the book.

- [X] FT-11: View book recommendations
  - Action: Open the "Recommendations" section.
  - Expected: Books are suggested based on most-read genres or highest-rated books.
  - (The "Recommended for You" section is present on the main page and displays suggested books.)

- [X] FT-12: Search books by keyword
  - Action: Type a title or author keyword in the search box, press Enter.
  - Expected: Only matching books are displayed.
  - (Searching "Dune" + Enter filtered the library to only "Dune"; "Filters active" indicator appeared.)

- [X] FT-13: Combine genre, status, and rating filters
  - Action: Apply Genre + Status + Rating filters simultaneously.
  - Expected: Only books matching all selected criteria are displayed.
  - (Genre=Classic Fiction + Status=Completed + Rating=5 Stars narrowed to 2 books; changing to Status=To Read with the same Genre+Rating returned "No books found", confirming the three filters intersect correctly.)

## Constraint

- [X] CS-01: Required fields enforced when adding a book
  - Action: Click "Add Book" and try to save with Title/Author/Genre empty.
  - Expected: Save is blocked with a validation message; Notes remain optional.
  - (Saving with empty Title/Author kept the dialog open — Title and Author are `required`; Notes has no required attribute. Native validation blocks submission.)

- [X] CS-02: Rating/review only allowed for completed books
  - Action: Attempt to add a rating/review to a book not in "Completed" status.
  - Expected: The rating/review control is disabled or the action is rejected.
  - (The menu for To Read / Reading books shows only "Edit Details", "Start Reading"/"Mark …", and "Remove from Library" — there is no "Edit Review" option, so rating/review is restricted to Completed books.)

- [ ] CS-03: Finish date cannot precede start date
  - Action: Set a Finish Date earlier than the Start Date, save.
  - Expected: Save is blocked with a date-order validation message.
  - Bug Report:
    - Issue: No date fields exist, so the validation cannot exist
    - Actual: There are no Start/Finish Date inputs anywhere in the app (see FT-04), so date-order validation is not implemented.

## Interaction

- [X] IX-01: Success feedback on save actions
  - Action: Add/edit a book, or save progress, rating, or review.
  - Expected: A success confirmation (toast/message) appears.
  - (Toasts observed: "Book Added", "Book Updated", "Started Reading", "Review Saved".)

- [X] IX-02: Immediate status update when moving a book
  - Action: Move a book between lists via the status control.
  - Expected: The book immediately appears in the new list without a page reload.
  - (Clicking "Start Reading" on The Midnight Library moved it to Reading instantly — the card updated and tab counts changed with no navigation/reload.)

## Content

- [X] CT-01: Default library contains valid books
  - Action: Open the library page.
  - Expected: Pre-existing books display valid Title, Author, and Genre.
  - (The seeded library shows 10 books, each with valid Title, Author, and Genre; a test-added 11th book also displayed correctly.)

- [X] CT-02: Recommendations are relevant library books
  - Action: Review the Recommendations list.
  - Expected: All suggestions are books from the user's library, aligned with most-read genres or high ratings.
  - (All three suggestions — The Midnight Library, The Hobbit, The Name of the Wind — are books present in the user's library. Note: they are currently "To Read" (unrated) titles, so the "based on your reading history and favorite genres" alignment is weak, but they are valid in-library books.)
