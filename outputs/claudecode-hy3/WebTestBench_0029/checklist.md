# Test Checklist

## Functionality
- [ ] FT-01: Add a book to the personal library
  - Action: Click "Add Book", fill Title, Author, Genre (required) and Notes (optional), click "Save".
  - Expected: The new book appears in the library (e.g., under the "To Read" list).

- [ ] FT-02: Edit an existing book's details
  - Action: Open a book, click "Edit", change Title/Author/Genre/Notes, click "Save".
  - Expected: The book's details update and persist in the library.

- [ ] FT-03: Track reading progress by percentage or page count
  - Action: Open a "Currently Reading" book, enter progress as percentage (e.g., 50%) or page count (e.g., 120/240), save.
  - Expected: Progress is displayed and reflects the entered value.

- [ ] FT-04: Set start and finish dates for a book
  - Action: Open a book, set "Start Date" and "Finish Date", save.
  - Expected: Both dates are recorded and shown on the book.

- [ ] FT-05: Move a book between lists
  - Action: Use the status control to move a book through "To Read" → "Currently Reading" → "Completed".
  - Expected: The book appears under each selected list accordingly.

- [ ] FT-06: Rate a completed book
  - Action: Open a "Completed" book, set a rating (e.g., 4 stars), save.
  - Expected: The rating is saved and shown on the book.

- [ ] FT-07: Write a review for a completed book
  - Action: Open a "Completed" book, enter review text, save.
  - Expected: The review is saved and associated with the book.

- [ ] FT-08: View completed books in reading history
  - Action: Open the "Reading History" section.
  - Expected: All "Completed" books with their ratings/reviews are listed.

- [ ] FT-09: Edit a rating/review from reading history
  - Action: In Reading History, select a book, edit its rating/review, save.
  - Expected: The updated rating/review persists in the history.

- [ ] FT-10: Delete a rating/review from reading history
  - Action: In Reading History, select a book, delete its rating/review.
  - Expected: The rating/review is removed; the book remains without it if applicable.

- [ ] FT-11: View book recommendations
  - Action: Open the "Recommendations" section.
  - Expected: Books are suggested based on most-read genres or highest-rated books.

- [ ] FT-12: Search books by keyword
  - Action: Type a title or author keyword in the search box, press Enter.
  - Expected: Only matching books are displayed.

- [ ] FT-13: Combine genre, status, and rating filters
  - Action: Apply Genre + Status + Rating filters simultaneously.
  - Expected: Only books matching all selected criteria are displayed.

## Constraint
- [ ] CS-01: Required fields enforced when adding a book
  - Action: Click "Add Book" and try to save with Title/Author/Genre empty.
  - Expected: Save is blocked with a validation message; Notes remain optional.

- [ ] CS-02: Rating/review only allowed for completed books
  - Action: Attempt to add a rating/review to a book not in "Completed" status.
  - Expected: The rating/review control is disabled or the action is rejected.

- [ ] CS-03: Finish date cannot precede start date
  - Action: Set a Finish Date earlier than the Start Date, save.
  - Expected: Save is blocked with a date-order validation message.

## Interaction
- [ ] IX-01: Success feedback on save actions
  - Action: Add/edit a book, or save progress, rating, or review.
  - Expected: A success confirmation (toast/message) appears.

- [ ] IX-02: Immediate status update when moving a book
  - Action: Move a book between lists via the status control.
  - Expected: The book immediately appears in the new list without a page reload.

## Content
- [ ] CT-01: Default library contains valid books
  - Action: Open the library page.
  - Expected: Pre-existing books display valid Title, Author, and Genre.

- [ ] CT-02: Recommendations are relevant library books
  - Action: Review the Recommendations list.
  - Expected: All suggestions are books from the user's library, aligned with most-read genres or high ratings.