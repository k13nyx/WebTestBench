# Test Result

## Functionality

- [X] FT-01: Add a new book to the library with full details
  - Action: Open the add-book form, enter title "Dune", author "Frank Herbert", genre "Sci-Fi", and an optional note, then submit.
  - Expected: "Dune" appears in the library with its author, genre, and note displayed.
  - Bug Report:
    - Issue: Saved note never rendered / form state leaks between modal openings
    - Actual: The book was added and its card showed title, author ("Frank Herbert") and genre ("Science Fiction"), and Total Books incremented. However, the note ("Reread for the sandworms") was never displayed anywhere in the page (verified via full-DOM text search; it is only visible when reopening the edit form). Additionally, the add/edit modal shares stale state between openings: after editing "1984", the Add Book modal opened pre-filled with "1984"/"George Orwell"/status "Currently Reading"/200-of-328 progress, and the newly added book silently inherited that stale status and progress.

- [X] FT-02: Track reading progress using page counts
  - Action: Open a book in "currently reading", set progress (e.g., 40% or pages 120/300), and save.
  - Expected: The book shows the updated progress value (40% or 120/300) on its card/detail view.
  - Note: Edit worked only after re-entering ALL fields, because the "Edit Details" modal opens completely blank (no prefill). After saving currentPage 200/328 for "1984", the card immediately showed "Progress 200 / 328 pages".

- [ ] FT-03: Set start and finish dates on a book
  - Action: Edit a book's dates, set a start date and a finish date, and save.
  - Expected: Both dates are displayed on the book and persist after reloading/returning to the page.
  - Bug Report:
    - Issue: Missing feature (date editing) + no data persistence
    - Actual: Neither the Add/Edit form nor any detail view exposes date inputs — the edit form only has Title, Author, Genre, Status, Total Pages, Current Page, Cover URL, Notes. Dates are only auto-set ("Started" on Start Reading, "Finished" on Mark as Completed) and are displayed on cards, but they cannot be edited as the checklist requires. Persistence also fails: after page reload the library reverted entirely to the 10 default books (1984 back to 150/328, The Hobbit back to "To Read", added books deleted).

- [X] FT-04: Move a book between status lists
  - Action: Use the status control (or drag) to move a book from "to read" to "currently reading", then to "completed".
  - Expected: The book appears under each respective list and no longer appears under the previous list.
  - Note: Done on "The Hobbit" via "Start Reading" (To Read → Reading) and kebab-menu "Mark as Completed" (Reading → Completed). Tab counts updated each time (To Read 2→1→0 for it, Reading +1, Completed 5→6).

- [ ] FT-05: Rate and review a finished book
  - Action: Open a book in "completed", select a rating (e.g., 4 stars) and enter review text, then save.
  - Expected: The rating and review text are shown on the book's entry.
  - Bug Report:
    - Issue: Review text never displayed
    - Actual: Rating selection and saving work — "The Great Gatsby" shows exactly 4 gold-filled stars after saving a 4-star rating. But the review text is never rendered anywhere (card, Completed tab, or page DOM — verified via full-document text and HTML search; even the app's default reviews are invisible). Only the rating is shown on the book's entry.

- [ ] FT-06: Completed books appear in reading history
  - Action: Complete a book, then open the reading history section.
  - Expected: The book appears in history with its title, finish date, rating, and review.
  - Bug Report:
    - Issue: Missing feature (no reading history section)
    - Actual: No reading history section exists anywhere in the UI (single page: stats, recommendations, filters, book tabs). There is no navigation link, and the URL /history returns a 404 page ("Oops! Page not found"). The closest substitute is the "Completed" tab, which shows title and finish date but no review text.

- [ ] FT-07: Edit an existing rating and review
  - Action: In reading history, open a rated book, change the rating to a different value and edit the review text, then save.
  - Expected: History and the book entry show the updated rating and review text.
  - Bug Report:
    - Issue: Review text not displayed / missing history section
    - Actual: Editing works at the data level — changing Gatsby from 4★ to 5★ and replacing the review text was saved (reopening "Edit Review" shows the new values, and the card now renders 5 gold stars). However, the updated review text is not displayed anywhere in the UI, and no reading history section exists to display it.

- [ ] FT-08: Delete a rating and review
  - Action: In reading history, delete the rating/review of a completed book and confirm.
  - Expected: The rating and review are removed for that book while the book itself remains in history/library.
  - Bug Report:
    - Issue: Missing feature (no delete control)
    - Actual: The completed-book menu offers only "Edit Details", "Edit Review", "Remove from Library"; the Rate & Review dialog offers only 5 stars, Cancel, Save Review, Close — no delete option. Clearing the review text and saving keeps the rating (Gatsby remained 5 gold stars), and clicking the active star does not toggle it off. A rating/review cannot be deleted once saved.

- [X] FT-09: Search books by text query
  - Action: Type a known book title or author name (from default data) into the search box.
  - Expected: Only matching books are listed; the match is visible in the results.
  - Note: "Harper Lee" → only "To Kill a Mockingbird"; "hobbit" → only "The Hobbit". Both author and title search work.

- [X] FT-10: Filter by genre
  - Action: Apply a genre filter using a genre that exists in the default library.
  - Expected: Only books of that genre are displayed.
  - Note: Genre = Dystopian → only "1984" listed.

- [X] FT-11: Combine multiple filters (genre + status + rating)
  - Action: Set genre, status, and minimum rating filters together so at least one default book matches all three.
  - Expected: Only the books satisfying all three conditions are displayed.
  - Note: Genre = Science Fiction + Status = Completed + Rating = "4+ Stars" → only "Project Hail Mary" (Sci-Fi, Completed, 4★) listed.

- [X] FT-12: Show recommendations based on reading data
  - Action: Open the recommendations section after having read/rated books of at least one genre.
  - Expected: Recommendations are shown that reference books/genres from the user's own library (e.g., based on most-read genre or highly rated books).
  - Note: After completing the Fantasy book "The Hobbit", "Recommended for You" showed "The Name of the Wind" (Fantasy) — a book/genre drawn from the user's own library and reading activity (earlier runs likewise recommended library titles like "Dune" and "The Hobbit" with matching genres).

## Constraint

- [X] CS-01: Cannot add a book without a title
  - Action: Submit the add-book form leaving the title empty (other fields filled).
  - Expected: Submission is blocked and a validation message is shown; no book is added.
  - Note: With an empty title, the title input is invalid and carries the native validation message "Please fill out this field."; the modal stays open and Total Books is unchanged (no book added).

- [X] CS-02: Progress value must stay within valid bounds
  - Action: Enter progress over the maximum (e.g., 150% or pages beyond total) and save.
  - Expected: The value is rejected/clamped with an error message, not saved as invalid.
  - Note: Setting Current Page 500 with Total Pages 328 is rejected — the field has max=328, reports "Value must be less than or equal to 328.", the modal stays open, and the card still shows 150/328. Saving a valid 200 afterwards succeeds.

- [X] CS-03: Rating is required bounded to the allowed scale
  - Action: Attempt to save a rating outside the allowed scale (e.g., 0 or 6 stars on a 1–5 scale).
  - Expected: The invalid rating is rejected with an error, and no invalid value is stored.
  - Note: The rating widget offers exactly 5 star buttons; no input path exists for 0 or 6 (clicking the already-active 5th star does not clear it to 0), so no out-of-scale value can be entered or stored. (Adjacent bug worth noting: the Rate & Review dialog leaks the previously opened book's rating/review — marking "The Hobbit" completed opened the dialog pre-filled with Gatsby's 5★ review.)

- [ ] CS-04: Finish date cannot precede start date
  - Action: Set a finish date earlier than the start date and save.
  - Expected: The change is blocked with a validation error; dates remain unchanged.
  - Bug Report:
    - Issue: Missing feature (date editing) — constraint unenforceable/untestable
    - Actual: No date fields exist anywhere in the UI, so a finish date earlier than a start date cannot even be attempted; there is no validation logic for date ordering. Dates are set automatically only via status changes (both were stamped 11/8/2026 for a same-day complete).

- [X] CS-05: A book exists in exactly one status list at a time
  - Action: Move a book from "to read" to "completed" and check all three lists.
  - Expected: The book appears only in "completed", not in "to read" or "currently reading".
  - Note: After completing "The Hobbit": tab counts read All (10) / Reading (3) / To Read (1) / Completed (6); The Hobbit appeared only in the Completed list (status badge "Completed", not present in Reading or To Read listings).

## Interaction

- [X] IX-01: Immediate list update when moving a book
  - Action: Change a book's status via the control/button.
  - Expected: The book disappears from its old list and appears in the new list immediately, without a page reload.
  - Note: Verified without reload (in-page JS marker survived both transitions): clicking "Start Reading" and "Mark as Completed" updated the card's status badge, the tab counts, and the stats bar immediately.

## Content

- [ ] CT-01: Library displays all required book details
  - Action: Inspect book entries in the library.
  - Expected: Each book shows title, author, genre, status, and progress; optional notes are shown when present.
  - Bug Report:
    - Issue: Missing details on book cards
    - Actual: Title, author, genre and status are shown on every card. Progress is only shown for "Currently Reading" books (e.g., "Progress 200 / 328 pages"); completed and to-read cards show no progress value at all. Notes are never rendered — a book added with the note "Le Guin classic, annotated copy." shows no note on its card, and the note text appears nowhere in the page DOM.

- [X] CT-02: Rating stars/indicators render correctly
  - Action: View a book with a saved rating (e.g., 4/5).
  - Expected: The rating is displayed visually (e.g., 4 of 5 stars) matching the stored value.
  - Note: "The Hobbit" (4/5) renders exactly 4 gold-filled stars + 1 empty; "Project Hail Mary" (4/5) the same; Gatsby (5/5) shows 5 filled stars — visual rendering matches stored values.
