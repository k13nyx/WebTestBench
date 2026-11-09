# Test Result

## Functionality

- [ ] **FT-01: Tour catalog displays available immersive tours**
  - **Action:** Open the tour catalog and select a listed tour.
  - **Expected:** The selected tour opens with its title, description, and an option to begin or enter the tour.
  - **Bug Report:**
    - **Issue:** Missing tour entry control
    - **Actual:** The selected tour opened with its title and description, but no explicit “Begin” or “Enter Tour” option was displayed.

- [X] **FT-02: User can move between areas within a tour**
  - **Action:** Start a tour and use the available navigation controls or room/area selector.
  - **Expected:** The user can enter each available room or area, and the displayed scene and area label update accordingly.

- [X] **FT-03: User can open exhibit information**
  - **Action:** Click an interactive exhibit within a tour area.
  - **Expected:** An exhibit information panel opens for the selected exhibit.

- [X] **FT-04: Exhibit panel provides layered educational content**
  - **Action:** In an exhibit information panel, open the overview, deeper-dive content, and related-items section.
  - **Expected:** Each layer opens successfully and displays content relevant to the selected exhibit.

- [X] **FT-05: User can complete an interactive quiz**
  - **Action:** Open a quiz within a tour, select an answer, and submit it.
  - **Expected:** The quiz records the selected answer and displays the result or feedback.

- [ ] **FT-06: User can explore an interactive timeline**
  - **Action:** Open a timeline within a tour and select different dates or timeline points.
  - **Expected:** The displayed event or historical information changes to match the selected timeline point.
  - **Bug Report:**
    - **Issue:** Missing interactive timeline
    - **Actual:** No timeline control or timeline content was available in the inspected tour area or exhibit panel. The available exhibit layers were Overview, Deep Dive, and Quiz.

- [X] **FT-07: User can discover tours using search**
  - **Action:** Enter a term matching a tour title or description in the search field and submit the search.
  - **Expected:** The catalog displays tours matching the entered term and does not display unrelated results as matches.

- [ ] **FT-08: User can filter tours by discovery criteria**
  - **Action:** Apply filters for theme, historical period, culture, and difficulty level, individually and in combination.
  - **Expected:** The catalog updates to show only tours matching all currently selected filter values.
  - **Bug Report:**
    - **Issue:** Complete filter behavior not verified
    - **Actual:** Filter controls for theme, period, culture, and difficulty were present, and the theme filter updated the catalog, but the required individual and combined filter scenarios could not all be completed after the application entered an error state.

- [X] **FT-09: User can bookmark a tour**
  - **Action:** Select the bookmark control on a catalog tour or tour detail view.
  - **Expected:** The tour is visibly marked as bookmarked and is available through the bookmarked-tours view or control.

- [X] **FT-10: User can mark a tour as in progress**
  - **Action:** Enter a tour and navigate through at least one area, then leave the tour.
  - **Expected:** The tour is marked “In Progress” and appears in the user’s in-progress tours.

- [X] **FT-11: User can resume an in-progress tour**
  - **Action:** Open an “In Progress” tour after leaving it.
  - **Expected:** The tour resumes at the previously visited room, area, or position rather than restarting from the beginning.

- [X] **FT-12: Related tours are offered at the end of a tour**
  - **Action:** Reach the end of a tour.
  - **Expected:** A related-tours section is displayed with selectable tour suggestions.

## Constraint

- [ ] **CS-01: Combined filters do not return nonmatching tours**
  - **Action:** Select multiple filter values, such as a theme and difficulty level, and inspect every returned tour.
  - **Expected:** Every returned tour matches every selected filter; no tour violating any selected criterion is shown.
  - **Bug Report:**
    - **Issue:** Combined-filter constraint not verified
    - **Actual:** The required combination of multiple filter values and inspection of every returned tour could not be completed before the application entered an error state.

- [X] **CS-02: Search and filters can be cleared**
  - **Action:** Run a search and apply one or more filters, then use the clear-search and clear-filter controls.
  - **Expected:** The search term and filters are removed, and the full unfiltered catalog is restored.

- [ ] **CS-03: Progress state remains consistent after resuming**
  - **Action:** Mark a tour in progress, leave it, resume it, and navigate to another area.
  - **Expected:** The tour remains marked “In Progress,” and the saved position updates to the most recently visited area.
  - **Bug Report:**
    - **Issue:** Progress consistency scenario not fully completed
    - **Actual:** The tour was restored to the previously visited room and displayed “In Progress,” but the complete leave, resume, navigate again, and re-check sequence was not completed.

## Interaction

- [X] **IX-01: Tour navigation provides visible state feedback**
  - **Action:** Move from one room or area to another using the tour navigation controls.
  - **Expected:** The active room or area is visibly indicated, and the new area loads without requiring a page reload.

- [ ] **IX-02: Exhibit selection opens and closes cleanly**
  - **Action:** Click an exhibit, close its information panel, then select a different exhibit.
  - **Expected:** The panel opens for the first exhibit, closes when requested, and then displays the second exhibit’s content without retaining incorrect information.
  - **Bug Report:**
    - **Issue:** Multiple-exhibit switching scenario not completed
    - **Actual:** The first exhibit panel opened and closed successfully, but selecting a different exhibit after closing could not be completed.

- [ ] **IX-03: Bookmark control reflects its current state**
  - **Action:** Bookmark a tour, then select the bookmark control again.
  - **Expected:** The control visibly changes to indicate bookmarked status and then returns to its unbookmarked state when toggled off.
  - **Bug Report:**
    - **Issue:** Bookmark toggle-off behavior not verified
    - **Actual:** The control changed from “Save Tour” to “Saved,” but toggling it again to confirm the unbookmarked state was not completed.

- [X] **IX-04: Catalog updates after discovery actions**
  - **Action:** Enter a search term or change a filter value.
  - **Expected:** The displayed tour results update to reflect the change, and the active search term or filter is visibly indicated.

## Content

- [ ] **CT-01: Catalog includes real and fully imagined places**
  - **Action:** Review the available tours in the catalog.
  - **Expected:** The catalog contains at least one tour based on a real place and at least one tour set in a fully imagined place, with each type clearly identifiable.
  - **Bug Report:**
    - **Issue:** Tour type is not clearly identified
    - **Actual:** The catalog included historically based subjects such as Ancient Egypt and Rome and a mythology-themed tour, but no tour was explicitly labeled as a fully imagined place or clearly categorized as real versus imagined.

- [ ] **CT-02: Tour content matches its cultural or historical subject**
  - **Action:** Open tours covering different museums, galleries, historical sites, or cultural landmarks.
  - **Expected:** Each tour’s rooms, exhibits, educational text, quizzes, and timelines are relevant to that tour’s stated place, culture, theme, or historical period.
  - **Bug Report:**
    - **Issue:** Tour page runtime error
    - **Actual:** Opening the related “Realm of the Greek Gods” tour produced a blank page and a React `TypeError: Cannot read properties of undefined`, preventing validation of its rooms, exhibits, educational content, quizzes, and timelines.

- [X] **CT-03: Related-tour suggestions are relevant**
  - **Action:** Complete or reach the end of multiple tours with different themes, periods, cultures, or difficulty levels.
  - **Expected:** The suggested tours are clearly related to the completed tour’s subject or classification and are not unrelated catalog items.
