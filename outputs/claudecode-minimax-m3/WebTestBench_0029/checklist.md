# Test Checklist

## Functionality
- [ ] FT-01: Add a new book to the personal library with title, author, genre, and optional notes
  - Action: Click "Add Book", fill in title "1984", author "George Orwell", genre "Dystopian", notes "Classic novel"
  - Expected: New book appears in the library list with all entered details

- [ ] FT-02: Move a book between "To Read", "Currently Reading", and "Completed" status lists
  - Action: On an existing book, change its status from "To Read" to "Currently Reading", then to "Completed"
  - Expected: Book appears in the selected status list at each step

- [ ] FT-03: Track reading progress using percentage or page count
  - Action: Open a "Currently Reading" book and update progress to 50% or equivalent pages
  - Expected: Progress value is saved and displayed on the book

- [ ] FT-04: Record start and finish dates for a book
  - Action: On a book, set start date "2024-01-01" and finish date "2024-01-15"
  - Expected: Both dates are saved and visible on the book

- [ ] FT-05: Add a star rating and written review to a completed book
  - Action: On a completed book, click "Rate & Review", select 5 stars, enter review text "Excellent read"
  - Expected: 5-star rating and review text are saved with the book

- [ ] FT-06: View reading history of completed books with their ratings and reviews
  - Action: Navigate to the "Reading History" section
  - Expected: All completed books are listed with their associated rating and review

- [ ] FT-07: Edit an existing rating and review
  - Action: Click "Edit" on a saved review, change rating to 4 stars and update review text
  - Expected: Rating and review text are updated and reflected in the book/history view

- [ ] FT-08: Delete an existing rating and review
  - Action: Click "Delete" on a saved review and confirm
  - Expected: Rating and review text are removed; book remains in the library

- [ ] FT-09: View book recommendations based on most-read genres or highly rated books
  - Action: Navigate to the "Recommendations" section
  - Expected: At least one recommendation matches a frequently-read genre or is similar to a highly rated book

- [ ] FT-10: Search the library by title or author
  - Action: Type "Orwell" in the search field using default library data
  - Expected: Only books whose title or author contains "Orwell" are displayed

- [ ] FT-11: Filter the library by combining genre, status, and rating
  - Action: Apply filter: genre = "Fiction", status = "Completed", rating = "5 stars"
  - Expected: Only books matching all three filter criteria are displayed

## Constraint
- [ ] CS-01: Cannot save a book without the required fields (title, author, genre)
  - Action: Click "Save Book" with title and author fields left empty
  - Expected: Save action is blocked and a validation message identifies the missing required fields

- [ ] CS-02: Cannot add a rating or review to a book that is not in "Completed" status
  - Action: Attempt to open "Rate & Review" on a book with status "Currently Reading" or "To Read"
  - Expected: The rating/review option is disabled or hidden; submission is blocked

- [ ] CS-03: Cannot set a finish date earlier than the start date
  - Action: On a book with start date "2024-01-15", set finish date "2024-01-01"
  - Expected: Save is blocked and an error indicates finish date must be on/after start date

## Interaction
- [ ] IX-01: Updating reading progress updates the book display immediately
  - Action: Change a book's progress value from 50% to 75% and observe the list/card view
  - Expected: Progress value updates on the book card without requiring a page refresh

- [ ] IX-02: Combining multiple filters updates the visible book list immediately
  - Action: Add a second filter (e.g., rating) on top of an existing genre filter
  - Expected: The book list re-renders to reflect both filters without a manual refresh

## Content
- [ ] CT-01: Each book card displays the core details relevant to a library entry
  - Action: View a book in the library list
  - Expected: Title, author, genre, current status, and progress are all visible on the card

- [ ] CT-02: Recommendations are relevant to the user's reading profile (genres read most or highly rated)
  - Action: Review the recommendations list with default library data present
  - Expected: Recommended books share a genre with a frequently-read book, or resemble a 5-star rated book