# Test Checklist

## Functionality
- [ ] FT-01: Add a new book to the personal library with full details
  - Action: Click "Add Book", enter title, author, genre, and optional notes, then save
  - Expected: Book is saved and appears in the library with all entered details displayed
- [ ] FT-02: Track reading progress by percentage
  - Action: Open a book, set progress to a percentage value (e.g., 45%), and save
  - Expected: The book displays the entered progress percentage and reflects it in the library view
- [ ] FT-03: Track reading progress by page count
  - Action: Open a book, enter current page and total pages (e.g., 120/300), and save
  - Expected: Progress is stored and displayed as a page count
- [ ] FT-04: Record start and finish dates
  - Action: Set a "start date" on a book, then set a "finish date" on a completed book
  - Expected: Both dates are saved and displayed on the book's details
- [ ] FT-05: Move a book between "to read," "currently reading," and "completed" lists
  - Action: Change a book's status from "to read" to "currently reading," then to "completed"
  - Expected: The book appears in the selected list and is removed from the previous one
- [ ] FT-06: Rate a finished book
  - Action: Mark a book as "completed," then assign a rating (e.g., star rating)
  - Expected: The rating is saved and displayed for that book
- [ ] FT-07: Write a review for a finished book
  - Action: On a completed book, enter review text and save
  - Expected: The review is saved and visible on the book's details
- [ ] FT-08: Finished book appears in reading history
  - Action: Complete a book with a rating and review, then open "Reading History"
  - Expected: The completed book, its rating, and its review appear in the reading history
- [ ] FT-09: Edit or delete a rating/review from history
  - Action: In reading history, edit an existing rating/review and save; then delete another rating/review
  - Expected: Edited values update, and deleted values are removed from the history
- [ ] FT-10: Recommendations based on most-read genres or highly rated books
  - Action: Open the recommendations section after having completed/rated books
  - Expected: Suggested books are drawn from the library based on the user's most-read genres or highest-rated books
- [ ] FT-11: Search the collection
  - Action: Enter a keyword (e.g., a title or author) into the search field
  - Expected: Only matching books are shown
- [ ] FT-12: Filter by a single criterion and combine multiple filters
  - Action: Apply a genre filter, then combine it with status and rating filters
  - Expected: Results narrow to books matching all applied filters simultaneously

## Constraint
- [ ] CS-01: Required book fields are enforced
  - Action: Attempt to add a book leaving title, author, or genre empty
  - Expected: Save is blocked and a validation message indicates the missing required field(s)
- [ ] CS-02: Progress cannot exceed valid bounds
  - Action: Enter a percentage above 100% or a current page greater than the total page count
  - Expected: Invalid value is rejected with a message; progress is not saved beyond the maximum
- [ ] CS-03: Rating and review are restricted to completed books
  - Action: Attempt to rate or review a book in "to read" or "currently reading" status
  - Expected: Rating/review is unavailable or blocked until the book is marked "completed"
- [ ] CS-04: Finish date cannot precede start date
  - Action: Set a finish date earlier than the recorded start date
  - Expected: The conflicting date is rejected with a validation message
- [ ] CS-05: A book can only occupy one status at a time
  - Action: Move a book to a new status and inspect the "to read," "currently reading," and "completed" lists
  - Expected: The book appears in exactly one list with no duplicates across lists

## Interaction
- [ ] IX-01: Confirmation feedback on creating a book
  - Action: Add a new book successfully
  - Expected: A success message/toast confirms the book was added
- [ ] IX-02: Progress/status changes reflect immediately
  - Action: Update a book's progress or move it to another list
  - Expected: The library view updates instantly without a manual refresh

## Content
- [ ] CT-01: Recommendations are relevant to the library
  - Action: Inspect the recommendation results
  - Expected: Every recommended book exists in the user's library and matches the user's most-read genres or highly rated books