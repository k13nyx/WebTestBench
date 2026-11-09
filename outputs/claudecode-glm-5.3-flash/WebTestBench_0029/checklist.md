# Test Checklist

## Functionality
- [ ] FT-01: Add a new book to the library with full details
  - Action: Open the add-book form, enter title "Dune", author "Frank Herbert", genre "Sci-Fi", and an optional note, then submit.
  - Expected: "Dune" appears in the library with its author, genre, and note displayed.
- [ ] FT-02: Track reading progress using percentage or page counts
  - Action: Open a book in "currently reading", set progress (e.g., 40% or pages 120/300), and save.
  - Expected: The book shows the updated progress value (40% or 120/300) on its card/detail view.
- [ ] FT-03: Set start and finish dates on a book
  - Action: Edit a book's dates, set a start date and a finish date, and save.
  - Expected: Both dates are displayed on the book and persist after reloading/returning to the page.
- [ ] FT-04: Move a book between status lists
  - Action: Use the status control (or drag) to move a book from "to read" to "currently reading", then to "completed".
  - Expected: The book appears under each respective list and no longer appears under the previous list.
- [ ] FT-05: Rate and review a finished book
  - Action: Open a book in "completed", select a rating (e.g., 4 stars) and enter review text, then save.
  - Expected: The rating and review text are shown on the book's entry.
- [ ] FT-06: Completed books appear in reading history
  - Action: Complete a book, then open the reading history section.
  - Expected: The book appears in history with its title, finish date, rating, and review.
- [ ] FT-07: Edit an existing rating and review
  - Action: In reading history, open a rated book, change the rating to a different value and edit the review text, then save.
  - Expected: History and the book entry show the updated rating and review text.
- [ ] FT-08: Delete a rating and review
  - Action: In reading history, delete the rating/review of a completed book and confirm.
  - Expected: The rating and review are removed for that book while the book itself remains in history/library.
- [ ] FT-09: Search books by text query
  - Action: Type a known book title or author name (from default data) into the search box.
  - Expected: Only matching books are listed; the match is visible in the results.
- [ ] FT-10: Filter by genre
  - Action: Apply a genre filter using a genre that exists in the default library.
  - Expected: Only books of that genre are displayed.
- [ ] FT-11: Combine multiple filters (genre + status + rating)
  - Action: Set genre, status, and minimum rating filters together so at least one default book matches all three.
  - Expected: Only the books satisfying all three conditions are displayed.
- [ ] FT-12: Show recommendations based on reading data
  - Action: Open the recommendations section after having read/rated books of at least one genre.
  - Expected: Recommendations are shown that reference books/genres from the user's own library (e.g., based on most-read genre or highly rated books).

## Constraint
- [ ] CS-01: Cannot add a book without a title
  - Action: Submit the add-book form leaving the title empty (other fields filled).
  - Expected: Submission is blocked and a validation message is shown; no book is added.
- [ ] CS-02: Progress value must stay within valid bounds
  - Action: Enter progress over the maximum (e.g., 150% or pages beyond total) and save.
  - Expected: The value is rejected/clamped with an error message, not saved as invalid.
- [ ] CS-03: Rating is required bounded to the allowed scale
  - Action: Attempt to save a rating outside the allowed scale (e.g., 0 or 6 stars on a 1–5 scale).
  - Expected: The invalid rating is rejected with an error, and no invalid value is stored.
- [ ] CS-04: Finish date cannot precede start date
  - Action: Set a finish date earlier than the start date and save.
  - Expected: The change is blocked with a validation error; dates remain unchanged.
- [ ] CS-05: A book exists in exactly one status list at a time
  - Action: Move a book from "to read" to "completed" and check all three lists.
  - Expected: The book appears only in "completed", not in "to read" or "currently reading".

## Interaction
- [ ] IX-01: Immediate list update when moving a book
  - Action: Change a book's status via the control/button.
  - Expected: The book disappears from its old list and appears in the new list immediately, without a page reload.

## Content
- [ ] CT-01: Library displays all required book details
  - Action: Inspect book entries in the library.
  - Expected: Each book shows title, author, genre, status, and progress; optional notes are shown when present.
- [ ] CT-02: Rating stars/indicators render correctly
  - Action: View a book with a saved rating (e.g., 4/5).
  - Expected: The rating is displayed visually (e.g., 4 of 5 stars) matching the stored value.