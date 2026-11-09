# Test Checklist

## Functionality

- [ ] FT-01: Tour catalog displays tours with descriptive metadata
  - Action: Open the site's tour catalog page.
  - Expected: Multiple tours are listed, each showing its title plus theme, historical period, culture, and difficulty level.

- [ ] FT-02: Keyword search returns matching tours
  - Action: Type a keyword matching an existing tour (e.g., its name or "museum") into the search field and submit.
  - Expected: The catalog shows only tours whose title or description matches the keyword.

- [ ] FT-03: Filters narrow the catalog by each supported dimension
  - Action: Select a value for each filter — theme, historical period, culture, and difficulty level — one at a time.
  - Expected: The catalog updates after each selection to show only tours matching the selected filter value.

- [ ] FT-04: User can start a tour from the catalog
  - Action: Click any tour card, then click the "Start Tour" button.
  - Expected: The tour view opens, displaying the first room/area of that tour.

- [ ] FT-05: User can move between rooms/areas within a tour
  - Action: From the first room, use next/previous controls (or room links) to move to at least two other rooms, then move back.
  - Expected: Each action loads a different room/area with its own exhibits, including backwards navigation.

- [ ] FT-06: Exhibit click opens layered educational content
  - Action: Click an exhibit, read its overview, then open the deeper-dive section and one related item from it.
  - Expected: The overview opens first; the deeper dive and clickable related items are accessible from the overview, each revealing additional content.

- [ ] FT-07: Quiz can be completed and scored
  - Action: Open a quiz inside a tour, answer every question, and click Submit.
  - Expected: The quiz submits and displays a result (e.g., score "3/3" or a pass/fail message).

- [ ] FT-08: Timeline within a tour is viewable and interactive
  - Action: Open the timeline element in a tour and click at least two events.
  - Expected: Events are shown in chronological order, and clicking an event displays its details (date and description).

- [ ] FT-09: Tour resumes where the user left off
  - Action: Start a tour, advance to room 2, then bookmark / mark it "In progress", leave the tour, reload the site, and click Resume/Continue on that tour.
  - Expected: The tour reopens at room 2 (the last visited position), not at the tour start.

- [ ] FT-10: Related tours are suggested at the end of a tour
  - Action: Reach the end of a tour (complete the final room or the tour's end screen).
  - Expected: A "Related Tours" suggestions section lists other tours, and clicking a suggestion opens that tour (its details page or start).

## Constraint

- [ ] CS-01: Search with no matches shows a clear empty state
  - Action: Type a nonsense keyword (e.g., "zzzqqqx") into the search field and submit.
  - Expected: A "No results found" message is shown, no tour cards are listed, and the page does not break.

- [ ] CS-02: Filtered results must match every applied filter
  - Action: Apply a combined filter (e.g., Theme = "Art" AND Difficulty = "Beginner") and inspect each displayed tour card.
  - Expected: Every displayed tour matches all selected values; no off-theme or wrong-difficulty tours appear in the results.

- [ ] CS-03: Quiz cannot be submitted with unanswered questions
  - Action: Open a quiz, leave at least one question unanswered, and click Submit.
  - Expected: Submission is blocked with a message identifying the unanswered question(s), and no score is displayed.

## Interaction

- [ ] IX-01: Bookmark button gives immediate visual feedback
  - Action: Click the bookmark/save button on a tour card or tour page.
  - Expected: The button's state visibly changes (e.g., filled icon, "Bookmarked" label, or a confirmation toast).

- [ ] IX-02: Progress indicator updates as rooms are visited
  - Action: Advance through rooms in a tour and observe the progress UI (e.g., "Room 2 of 5", progress bar, or room dots).
  - Expected: The indicator updates immediately with each room change.

- [ ] IX-03: Quiz answers show selected and correct/incorrect states
  - Action: In a quiz, select an option for a question, then submit the answered quiz.
  - Expected: The chosen option displays a selected highlight before submission, and correct/incorrect answers are visually distinguished in the result.

## Content

- [ ] CT-01: Catalog covers the full tour scope, including imagined places
  - Action: Browse all tour titles and descriptions in the catalog.
  - Expected: Tours span museums, art galleries, historical sites, and cultural landmarks, and include both real locations and fully imagined/fictional places.

- [ ] CT-02: Exhibit content and media are relevant and load correctly
  - Action: Open at least three exhibits across different tours.
  - Expected: Each exhibit's overview/deeper-dive text describes that specific exhibit, and all images/icons are on-topic and fully load (no broken images or placeholder text).

- [ ] CT-03: Quiz and timeline content match the tour's theme and period
  - Action: Review the quiz questions and timeline events within a single tour.
  - Expected: Every question and event relates to that tour's subject, historical period, and culture — no mismatched or off-topic content.