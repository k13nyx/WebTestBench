# Test Checklist

## Functionality
- [ ] FT-01: Open a tour from the catalog
  - Action: On the catalog page, click the card of any tour.
  - Expected: The tour detail page opens and shows the tour title, description, and a "Start Tour" button.
- [ ] FT-02: Move between rooms or areas
  - Action: Start a tour, click "Next" once, then click "Previous".
  - Expected: The view changes to the next room and the room name indicator updates. "Previous" returns to the first room.
- [ ] FT-03: Open an exhibit's overview
  - Action: In any room, click an exhibit hotspot.
  - Expected: An exhibit panel opens with the exhibit name, an "Overview" tab selected, and overview text with an image.
- [ ] FT-04: Open deeper dive and related items
  - Action: In the open exhibit panel, click the "Deeper Dive" tab, then the "Related Items" tab.
  - Expected: "Deeper Dive" shows more detailed text than the overview. "Related Items" lists at least one linked exhibit, and clicking it opens that exhibit's panel.
- [ ] FT-05: Complete a quiz and see a score
  - Action: Open a quiz in a tour, select one answer per question, and click "Submit" on each question until the quiz ends.
  - Expected: The quiz ends with a final score shown as "X / Y" where X matches the number of correct answers.
- [ ] FT-06: Select a timeline event
  - Action: Open a timeline in a tour and click the second event marker.
  - Expected: That event's date and description display in a detail area, and the marker is shown as selected.
- [ ] FT-07: Bookmark a tour
  - Action: On a tour detail page, click "Bookmark".
  - Expected: The button label changes to "Bookmarked", and the tour appears in the "Bookmarks" list in the user's library.
- [ ] FT-08: Mark a tour as in progress and resume it
  - Action: Start a tour, go to the third room, click "Home", then open the tour's detail page and click "Resume".
  - Expected: The tour appears under "In Progress" in the library, and "Resume" opens the tour directly at the third room.
- [ ] FT-09: Search for a tour by keyword
  - Action: In the search box, type the exact title of an existing tour and press Enter.
  - Expected: The results list shows that tour as the first result, and every result's title or description contains the search term.
- [ ] FT-10: Filter tours by theme, period, culture, and difficulty
  - Action: Set the "Difficulty" filter to "Beginner" and the "Historical Period" filter to any available period, then click "Clear all".
  - Expected: Results show only tours matching both filters, the result count updates, and after "Clear all" the full catalog returns.
- [ ] FT-11: Open a related tour from the end screen
  - Action: Click "Finish Tour" in the last room of any tour.
  - Expected: An end screen shows a "Related Tours" section with at least one tour card, and clicking a card opens that tour's detail page.

## Constraint
- [ ] CS-01: Bookmark toggles without duplicates
  - Action: On a tour detail page, click "Bookmark", then click "Bookmarked" again.
  - Expected: The button returns to "Bookmark", and the "Bookmarks" list contains no entry for that tour.
- [ ] CS-02: Quiz cannot be submitted without an answer
  - Action: Open a quiz question, do not select any option, and click "Submit".
  - Expected: The submit action is blocked, a message "Please select an answer" appears, and the question is not marked as answered.
- [ ] CS-03: Navigation limits at the first and last rooms
  - Action: In the first room of a tour, check the "Previous" button. Then go to the last room and check the navigation control.
  - Expected: "Previous" is disabled in the first room. In the last room, "Next" is replaced by "Finish Tour".

## Interaction
- [ ] IX-01: Hover feedback on exhibit hotspots
  - Action: In any room, move the mouse over an exhibit hotspot without clicking.
  - Expected: The hotspot is visually highlighted and its exhibit name label appears. Moving the mouse away removes both.
- [ ] IX-02: Immediate quiz answer feedback
  - Action: In a quiz, select an incorrect option and click "Submit".
  - Expected: The selected option turns red, the correct option turns green and is labeled, and a "Next Question" button appears.
- [ ] IX-03: Layered panel tab switching
  - Action: With an exhibit panel open, click "Overview", "Deeper Dive", then "Related Items", then click the close (X) button.
  - Expected: The active tab is highlighted at each step, the room view stays visible behind the panel while switching tabs, and closing the panel returns to the room with no change in the current room.

## Content
- [ ] CT-01: Catalog card details match the tour page
  - Action: Note the title, theme, historical period, culture, difficulty, and "Real" or "Imagined" label on any catalog card. Click the card and compare the detail page.
  - Expected: All values match exactly on both pages, and each tour is labeled as either "Real" or "Imagined".
- [ ] CT-02: Exhibit media and text are relevant
  - Action: Open three different exhibits from any tour and read the overview text and view each image.
  - Expected: Each image loads, is relevant to its exhibit name, and the text contains no placeholder or lorem ipsum content.
- [ ] CT-03: Related tours match the completed tour's theme
  - Action: Finish any tour and note its theme, period, and culture. Compare them with the "Related Tours" shown on the end screen.
  - Expected: Each related tour shares at least one of the theme, historical period, or culture of the completed tour.