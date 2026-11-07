# Test Checklist

## Functionality
- [ ] FT-01: Add a book with title, author, and genre
  - Action: Click "Add Book", enter a title, an author, and a genre, submit the form.
  - Expected: The form closes/saves, and the new book appears in the "To Read" list showing its title, author, and genre.
- [ ] FT-02: Notes field is optional on add
  - Action: Add a book leaving the "Notes" field empty; then add another book with notes text.
  - Expected: Both books are saved successfully; the first shows no notes without an error, the second shows its notes text.
- [ ] FT-03: Update reading progress using percentage or page count
  - Action: Open a book in "Currently Reading", enter a progress value (percentage) and separately a page count, and save.
  - Expected: The book card/detail shows the saved progress (percentage and/or pages) and the updated value is reflected in the library view.
- [ ] FT-04: Set start date and finish date
  - Action: Open a book, set a "Start Date" and a "Finish Date", and save.
  - Expected: Both dates are displayed on the book's card/detail after saving and after reloading the page.
- [ ] FT-05: Move a book to "Currently Reading"
  - Action: Change the status of a book in "To Read" to "Currently Reading".
  - Expected: The book appears in the "Currently Reading" list and no longer appears in "To Read".
- [ ] FT-06: Move a book to "Completed"
  - Action: Change the status of a book in "Currently Reading" to "Completed".
  - Expected: The book appears in the "Completed" list and no longer appears in "Currently Reading".
- [ ] FT-07: Give a rating and write a review for a completed book
  - Action: Open a book with status "Completed", select a star rating, type review text in the review field, and save.
  - Expected: The selected rating and the review text are displayed for that book and are retrievable when reopening it.
- [ ] FT-08: Completed books appear in reading history
  - Action: Complete a book with a rating and review, then open the "Reading History" section.
  - Expected: A history entry exists for that book showing its title, author, rating, review text, and completion/finish date.
- [ ] FT-09: Edit an existing rating and review in reading history
  - Action: In "Reading History", open the Edit control on a rated/reviewed book, change the rating and the review text, and save.
  - Expected: The history entry shows the new rating and new review text; the old values are not displayed.
- [ ] FT-10: Delete a rating/review from reading history
  - Action: In "Reading History", click Delete on a book that has a rating and review, and confirm.
  - Expected: The rating and review are removed from that history entry and the entry no longer displays them.
- [ ] FT-11: Recommendations based on most-read genre and highly rated books
  - Action: Have several books in the library, with multiple books in one genre and other books rated 4–5 stars, then open the "Recommendations" section.
  - Expected: Recommended titles are drawn only from the user's own library and reflect the top genre and/or the highly rated books.
- [ ] FT-12: Search the library by title or author
  - Action: Type a word appearing in a book title in the search field, then a word appearing in an author name.
  - Expected: Only matching books are shown for each query, and clearing the search restores the full library.
- [ ] FT-13: Combine genre, status, and rating filters
  - Action: Select a genre, a status, and a minimum rating in the filter controls together.
  - Expected: Only books matching all three conditions are listed, and changing or clearing any filter updates the result list accordingly.

## Constraint
- [ ] CS-01: Required fields are enforced when adding a book
  - Action: Attempt to submit the Add Book form with title, author, and genre each omitted one at a time.
  - Expected: Each attempt shows a validation error on the missing field and no book is created.
- [ ] CS-02: Progress percentage is bounded to 0–100
  - Action: Enter a progress percentage of 0, 100, and an out-of-range value such as 150, then save.
  - Expected: 0 and 100 are accepted, the out-of-range value is rejected with an error (or clamped to a valid value) and never saved as 150.
- [ ] CS-03: Rating is limited to completed books and a valid star range
  - Action: Open a book whose status is "To Read" or "Currently Reading" and attempt to submit a rating; then on a completed book attempt to select a rating outside the 1–5 star range.
  - Expected: Rating cannot be submitted for a book that is not completed, and only a valid 1–5 star rating is accepted.

## Interaction
- [ ] IX-01: Status lists and counts update immediately on a status change
  - Action: Move a book between "To Read", "Currently Reading", and "Completed" and watch the lists and their item counts.
  - Expected: The book appears in the destination list, disappears from the origin list, and the displayed counts update without a page reload.
- [ ] IX-02: Search/filter results update live and show an empty state when nothing matches
  - Action: Type a nonsense string in the search field, then apply filters for a genre/status/rating combination that matches no book.
  - Expected: The result list updates as the input changes and a clear "no books match" message is shown instead of an empty or broken area.

## Content
- [ ] CT-01: Book details display the correct saved data
  - Action: Open a book in the library and compare the displayed title, author, genre, status, progress, notes, start date, and finish date against the values entered.
  - Expected: Every displayed field matches the saved values exactly, with no blank or placeholder text where data exists.
- [ ] CT-02: History and recommendation entries show relevant, meaningful content
  - Action: Review the "Reading History" and "Recommendations" sections.
  - Expected: History entries show the exact review text and star rating entered, and each recommendation displays book details (title, author, genre) plus an indication of why it was recommended; no lorem ipsum or unrelated filler text appears.