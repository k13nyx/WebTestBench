# Test Checklist

## Functionality
- [ ] FT-01: User can edit a default book's title, author, genre, and notes.
  - Action: Open a book's details, change Notes to "Test note", click Save.
  - Expected: The new Notes text appears in the book details and the library list after reload.
- [ ] FT-02: User can update reading progress by page count or percentage.
  - Action: Open a "Currently Reading" book, enter page 150 of 300 (or 50%), click Save.
  - Expected: Progress shows 150/300 pages and 50%.
- [ ] FT-03: User can set a start date on a book.
  - Action: Open a "Currently Reading" book, set Start Date to a valid past date, click Save.
  - Expected: The Start Date field shows the chosen date after reload.
- [ ] FT-04: User can move a book from "To Read" to "Currently Reading."
  - Action: Open a "To Read" book and click "Start Reading" (or the status control, selecting "Currently Reading").
  - Expected: The book leaves the "To Read" list and appears in "Currently Reading" with that status label.
- [ ] FT-05: User can finish a book, rate it, review it, and see it in Reading History.
  - Action: On a "Currently Reading" book, click "Mark as Finished," set Finish Date, select 4 stars, enter review "Good read," and submit.
  - Expected: The book appears in "Completed," and Reading History shows the entry with 4 stars, the review text, and the finish date.
- [ ] FT-06: User can edit a rating and review from Reading History.
  - Action: In Reading History, click Edit on a completed entry, change the rating to 5 and the review to "Updated review," then Save.
  - Expected: The history entry shows 5 stars and "Updated review."
- [ ] FT-07: User can delete a rating and review from Reading History.
  - Action: In Reading History, click Delete on a rated entry and confirm.
  - Expected: The rating and review are removed from the entry, and the book remains in "Completed."
- [ ] FT-08: Search returns only books whose title or author matches the query.
  - Action: Type a partial author name from the default library into the search box.
  - Expected: Only books by matching authors are listed; all others are hidden.
- [ ] FT-09: Combined filters return only books matching all selected criteria.
  - Action: Set Genre to a default genre, Status to "Completed," and Minimum Rating to 4 stars.
  - Expected: Only books that meet all three conditions are listed; clearing filters restores the full list.
- [ ] FT-10: A Recommendations section lists books from the user's library.
  - Action: Open the "Recommendations" section on the library page.
  - Expected: At least one default library book is listed under "Recommended for You," each with a visible reason label.

## Constraint
- [ ] CS-01: Current page cannot exceed the book's total pages.
  - Action: On a 300-page book, enter 999 as the current page and click Save.
  - Expected: Save is blocked with the error "Current page cannot exceed total pages," and the old value remains.
- [ ] CS-02: Finish date cannot be earlier than start date.
  - Action: Set Start Date to 2026-05-01 and Finish Date to 2026-04-01, then click Save.
  - Expected: Save is blocked with a date-order error, and neither date changes.
- [ ] CS-03: Rating accepts only whole values from 1 to 5.
  - Action: In the rating field of a finished book, enter 6, then 0.
  - Expected: Both values are rejected with a range error, and the rating is not saved.
- [ ] CS-04: Title and Author are required; Genre and Notes are optional.
  - Action: Clear the Title field and click Save. Then clear Notes only and click Save.
  - Expected: Saving with an empty Title is blocked with an error. Saving with empty Notes succeeds.
- [ ] CS-05: A book appears in exactly one status list at a time.
  - Action: Move a "Currently Reading" book to "Completed," then check "To Read" and "Currently Reading."
  - Expected: The book appears only in "Completed" and in no other status list.
- [ ] CS-06: Rating and review fields are unavailable for books not yet completed.
  - Action: Open a "To Read" book and look for rating and review fields.
  - Expected: Rating and review fields are absent or disabled.

## Interaction
- [ ] IX-01: Deleting a rating or review requires confirmation.
  - Action: In Reading History, click Delete on a rated entry, then click Cancel in the dialog.
  - Expected: A dialog reading "Delete this rating and review?" appears; after Cancel, the dialog closes and the rating and review remain.
- [ ] IX-02: Changing any filter updates the results immediately.
  - Action: Select a genre in the Genre filter without clicking any other button.
  - Expected: The book list updates to match the filter without a page reload or a separate Apply step.
- [ ] IX-03: A "no results" message appears when no books match.
  - Action: Type a search term that matches no books, such as "zzzz," and press Enter.
  - Expected: The message "No books match your search and filters" appears, and the book list is empty.

## Content
- [ ] CT-01: Recommended books are relevant to the user's most-read genres or highly rated books.
  - Action: Open Recommendations and read the reason label on each recommended book.
  - Expected: Each reason names a genre that appears among the user's completed books, or a book the user rated 4 stars or higher.
- [ ] CT-02: Reading History lists only books with "Completed" status.
  - Action: Open Reading History and compare each entry against the "Completed" list.
  - Expected: Every entry in Reading History is a completed book, and no "To Read" or "Currently Reading" books appear.