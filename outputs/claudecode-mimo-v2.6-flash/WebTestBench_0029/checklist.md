# Test Checklist

## Functionality
- [ ] FT-01: Add a new book with title, author, genre, and optional notes
  - Action: Use the add-book form to enter a title, author, genre, and notes, then save.
  - Expected: The book is saved and appears in the library with all entered details displayed.
- [ ] FT-02: Add a new book without notes (notes are optional)
  - Action: Add a book filling only title, author, and genre, leaving notes empty.
  - Expected: The book is saved successfully and appears in the library.
- [ ] FT-03: Track reading progress by percentage
  - Action: On a book, enter a progress value (e.g., 40%) and save.
  - Expected: The book displays the updated progress percentage.
- [ ] FT-04: Track reading progress by page count
  - Action: On a book, enter a current page number and save.
  - Expected: The book displays the updated page-based progress.
- [ ] FT-05: Record a start date for a book
  - Action: Set a start date on a book and save.
  - Expected: The start date is stored and shown on the book.
- [ ] FT-06: Record a finish date for a book
  - Action: Set a finish date on a book and save.
  - Expected: The finish date is stored and shown on the book.
- [ ] FT-07: Move a book to the "To Read" list
  - Action: Change a book's status to "To Read."
  - Expected: The book appears under the "To Read" list and no longer under its previous list.
- [ ] FT-08: Move a book to the "Currently Reading" list
  - Action: Change a book's status to "Currently Reading."
  - Expected: The book appears under the "Currently Reading" list and no longer under its previous list.
- [ ] FT-09: Move a book to the "Completed" list
  - Action: Change a book's status to "Completed."
  - Expected: The book appears under the "Completed" list and no longer under its previous list.
- [ ] FT-10: Rate and review a finished book, and it appears in reading history
  - Action: On a completed book, select a star rating, write a review, and submit.
  - Expected: The rating and review are saved, and the book appears in the reading history showing both.
- [ ] FT-11: Edit an existing rating and review from reading history
  - Action: In the reading history, edit a book's rating and review text, then save.
  - Expected: The updated rating and review replace the previous values.
- [ ] FT-12: Delete a rating and review from reading history
  - Action: In the reading history, delete a book's rating/review.
  - Expected: The rating and review are removed from the entry.
- [ ] FT-13: View personalized book recommendations
  - Action: Open the recommendations area of the library.
  - Expected: Recommendations are shown based on the most-read genres and/or highest-rated books in the library.
- [ ] FT-14: Search the library by text
  - Action: Type a known book title (or author name) into the search box.
  - Expected: Only matching books are listed; clearing the search restores the full list.
- [ ] FT-15: Combine multiple filters (genre + status + rating)
  - Action: Apply a genre filter, a status filter, and a rating filter simultaneously.
  - Expected: Only books matching all three criteria are displayed.

## Constraint
- [ ] CS-01: Cannot add a book with a missing title, author, or genre
  - Action: Attempt to save a new book with the title, author, or genre field left empty.
  - Expected: The save is blocked and an error message identifies the required field(s); no book is added.
- [ ] CS-02: Progress values must be within valid bounds
  - Action: Attempt to save a percentage outside 0–100 or a page number outside the book's page range (or negative).
  - Expected: The save is rejected with a clear validation message; stored progress remains unchanged.
- [ ] CS-03: Finish date cannot be earlier than start date
  - Action: Set a finish date earlier than the existing start date and save.
  - Expected: The save is rejected with a validation message; the dates remain unchanged.
- [ ] CS-04: Rating/review is only available for completed books
  - Action: On a "To Read" or "Currently Reading" book, look for the rating/review controls.
  - Expected: Rating/review cannot be submitted for a non-completed book (controls absent or submission blocked with a message).

## Interaction
- [ ] IX-01: Saving a book provides immediate visible feedback
  - Action: Save a new book (or update a book's details).
  - Expected: A success confirmation (e.g., toast/message) appears, and the UI updates to show the change without a manual refresh.
- [ ] IX-02: Status change immediately updates list placement with feedback
  - Action: Move a book between status lists and observe the interface.
  - Expected: The book instantly appears in the target list, disappears from the source list, and a confirmation message is shown.

## Content
- [ ] CT-01: Book details display the exact data entered
  - Action: Open a book whose title, author, genre, notes, dates, and progress you know.
  - Expected: Every displayed value matches what was entered, with no missing or garbled fields.
- [ ] CT-02: Recommendations are relevant to the user's reading data
  - Action: Inspect the recommended books against your most-read genres and highest-rated books.
  - Expected: Every recommendation belongs to a genre you read frequently or is otherwise justified by your ratings; no unrelated books appear.