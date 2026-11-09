# Test Checklist

## Functionality
- [ ] FT-01: User can browse the tour catalog and view the available tours
  - Action: Open the website's catalog/main page
  - Expected: A catalog listing tours of museums, galleries, historical sites, or cultural landmarks is displayed

- [ ] FT-02: User can select a tour from the catalog and enter the tour experience
  - Action: Click on any tour in the catalog
  - Expected: The selected tour opens, showing its first room/area ready for exploration

- [ ] FT-03: User can navigate through different rooms or areas within a tour
  - Action: Use the navigation controls (arrows/buttons/map) inside a tour
  - Expected: The view switches to the next/previous room or area within the same tour

- [ ] FT-04: User can click on an exhibit to open its layered educational content
  - Action: Click on any exhibit (object, painting, artifact, marker) inside a tour
  - Expected: A content panel opens for the clicked exhibit

- [ ] FT-05: User can complete an interactive quiz within a tour
  - Action: Find and interact with a quiz element inside a tour; submit an answer
  - Expected: The quiz accepts input, returns feedback, and tracks completion

- [ ] FT-06: User can interact with a timeline element within a tour
  - Action: Locate a timeline element inside a tour; click a date or scrub through it
  - Expected: The timeline responds to the interaction and displays related historical information

- [ ] FT-07: User can bookmark a tour
  - Action: Click the bookmark/save control on a tour (from catalog or inside a tour)
  - Expected: The tour is added to the user's bookmarked list and is retrievable later

- [ ] FT-08: User can mark a tour as "in progress" and resume from where they left off
  - Action: Begin a tour, leave it partway, return to the catalog and reopen that tour
  - Expected: The tour resumes at the same room/area and exhibit where the user previously stopped

- [ ] FT-09: User can search for tours using a keyword
  - Action: Type a keyword (e.g., "Renaissance", "Louvre", "ancient Egypt") into the search box
  - Expected: The catalog updates to show tours whose title, theme, or content matches the keyword

- [ ] FT-10: User can filter tours by theme, historical period, culture, and difficulty level
  - Action: Apply one or more filters (e.g., theme = "Art", period = "Medieval", culture = "Japanese", difficulty = "Beginner")
  - Expected: The catalog shows only tours matching all selected filter criteria

- [ ] FT-11: User can view suggestions for related tours at the end of a tour
  - Action: Complete a tour (or reach its final screen)
  - Expected: A list of related tours is shown, each one contextually linked to the completed tour

## Constraint
- [ ] CS-01: Catalog must include both real and imagined museums, galleries, or cultural landmarks
  - Action: Browse the full catalog
  - Expected: The catalog contains a mix of tours based on real places AND tours of fully imagined/fictional locations

- [ ] CS-02: User cannot resume a tour that was never started
  - Action: Try to "resume" a tour that has no prior progress
  - Expected: The system does not offer a resume action, or it starts the tour from the beginning instead

## Interaction
- [ ] IX-01: Bookmarked and in-progress tours show a visible status indicator in the catalog
  - Action: Bookmark one tour and mark another as in progress; then return to the catalog
  - Expected: Both tours display a visible badge, icon, or label distinguishing them from unbookmarked/unstarted tours

- [ ] IX-02: A visual transition/feedback occurs when navigating between rooms or areas
  - Action: Move from one room to the next within a tour
  - Expected: A visual transition (animation, fade, slide, or load state) plays between the two rooms

- [ ] IX-03: The exhibit content panel reveals layered sections: overview, deeper dive, and related items
  - Action: Open an exhibit and switch between its content layers/tabs
  - Expected: The panel displays three distinct sections — an overview, a deeper dive, and related items — and the user can switch between them

## Content
- [ ] CT-01: All tours must match the themes of museums, art galleries, historical sites, or cultural landmarks
  - Action: Scan every tour listed in the catalog
  - Expected: Each tour's title, description, and imagery is relevant to museums, galleries, historical sites, or cultural landmarks (no off-topic content)

- [ ] CT-02: Filter results must align strictly with the selected theme, historical period, culture, and difficulty
  - Action: Apply a filter (e.g., theme = "History", period = "18th Century") and inspect every result
  - Expected: Every returned tour matches the selected theme, period, culture, and difficulty criteria

- [ ] CT-03: Related tour suggestions at the end of a tour must be contextually relevant
  - Action: Finish a tour and review its related tour suggestions
  - Expected: Each suggested tour shares a clear contextual link (same theme, period, culture, or subject) with the just-completed tour