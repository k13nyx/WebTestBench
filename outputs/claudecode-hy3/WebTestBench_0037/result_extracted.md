# Test Result

## Functionality
- [X] FT-01: Search adoptable animals by keyword
  - Action: Enter a keyword (e.g., "Labrador") in the search box and submit.
  - Expected: Results list shows only pets whose name/breed/description match the keyword.
  - Note: Tested with keyword "Luna"; result count dropped from 12 → 1 and only the matching pet (Luna) remained. (No "Labrador" breed exists in the dataset, so "Luna" was used to verify the matching/filtering behavior.)

- [X] FT-02: Filter pets by species, age range, size, good-with-kids, good-with-pets
  - Action: Set filters (e.g., Species=Dog, Age=Young, Size=Medium, Good with Kids=Yes, Good with Pets=Yes) and apply.
  - Expected: A results list of pets matching all selected criteria is displayed across multiple shelters.
  - Note: Applying Dog+Young+Medium+Good-with-kids returned exactly 1 matching pet (Max, from Portland OR shelter). Adding "Good with other pets" correctly yielded 0 (shown as "No pets found"), confirming the AND-combination of criteria across shelters is enforced.

- [X] FT-03: View a clear list of matching pets
  - Action: Apply any search/filter combination.
  - Expected: A list/grid of matching pets appears, each identifiable by name and/or photo.
  - Note: Grid of pet cards, each with photo (img alt = pet name) and name heading, clearly identifiable.

- [X] FT-04: Sort pets by relevance or time listed
  - Action: Select "Sort by: Relevance" then "Sort by: Time Listed".
  - Expected: List reorders to relevance ranking, then to newest-listed-first order.
  - Note: Sort dropdown offers "Relevance" (default) and "Newest First" (= time listed). Switching to "Newest First" reordered the list (e.g., from Luna, Oliver, Max… to Mochi, Cinnamon, Duke…), confirming both sort modes work.

- [X] FT-05: Open a detailed profile for a pet
  - Action: Click a pet's name, photo, or card in the results list.
  - Expected: That pet's detailed profile page opens.
  - Note: Clicking Luna's card navigated to /pets/pet-1 showing the full profile.

- [X] FT-06: Save a pet to favorites
  - Action: On a pet's profile/list item, click "Save to Favorites" (or heart icon).
  - Expected: Pet is added to the favorites list.
  - Note: Clicking the heart on Luna's card updated the nav badge to "Favorites 1"; adding Oliver made it "Favorites 2".

- [X] FT-07: View the saved favorites list
  - Action: Open the Favorites section.
  - Expected: All previously saved pets are shown.
  - Note: /favorites displayed "2 pets saved" and listed both Luna and Oliver.

- [X] FT-08: Send an adoption inquiry via the pet's page form
  - Action: On a pet's profile, fill required fields (name, email, message) and click "Send Inquiry".
  - Expected: Inquiry is submitted and a confirmation is shown.
  - Note: Submitting produced a toast "Inquiry Sent!" and an inline "Inquiry Submitted!" confirmation with shelter follow-up text.

## Constraint
- [X] CS-01: Filter results must not violate any selected criterion
  - Action: Apply filters including "Good with Kids=No" and "Size=Small".
  - Expected: No result contradicts a selected filter value (no kids-friendly or non-small pets appear).
  - Note: Enforced and verified — Size=Small + Good-with-kids returned only small, kid-friendly pets (Biscuit, Mochi, Sunny, Bella); no non-small or non-kid-friendly pet appeared. One caveat: the UI provides only a positive "Good with kids" checkbox; there is no "Good with Kids = No" (negative) option, so that specific sub-value could not be selected. The available criteria are nonetheless strictly enforced with no contradictions.

- [X] CS-02: Inquiry form blocks submission with empty required fields
  - Action: Leave required fields blank and click "Send Inquiry".
  - Expected: Submission is blocked and an error marks the missing required fields.
  - Note: Clearing Name/Email/Message and submitting did NOT navigate or show any success confirmation; the browser's native required-field validation blocked submission and focused the first empty required field. (The app relies on native HTML5 validation rather than a custom inline error message, but the block + field flagging behavior is present.)

- [X] CS-03: Same pet cannot be added to favorites twice
  - Action: Save a pet that is already in the favorites list.
  - Expected: Favorites list shows the pet only once (no duplicate entry).
  - Note: Favorites are keyed by unique pet id. Clicking an already-favorited pet's heart toggles it off (rather than stacking a duplicate), and the /favorites page listed each saved pet exactly once (Luna, Oliver). Duplicates are therefore impossible.

## Interaction
- [X] IX-01: Results update dynamically when filters change
  - Action: Change a filter value (e.g., toggle "Good with Pets").
  - Expected: Pet list immediately reflects updated results without a full page reload.
  - Note: Toggling filters updated the result count and list live (e.g., 12 → 5 → 1 → 0) while the URL stayed on /pets — no navigation/reload occurred.

- [X] IX-02: Visible confirmation when favoriting a pet
  - Action: Click "Save to Favorites" on a pet.
  - Expected: The button/icon changes state (e.g., empty→filled heart) or a success toast appears.
  - Note: The heart button changed to an active/filled state and the nav "Favorites" badge incremented (0 → 1 → 2), providing clear visible confirmation.

- [X] IX-03: Profile page renders photos and description
  - Action: Open a pet's detailed profile.
  - Expected: At least one photo and a text description are visible on the page.
  - Note: Luna's profile rendered a main photo plus 2 thumbnails and an "About Luna" description paragraph.

- [X] IX-04: Sort control visibly changes result order
  - Action: Switch between Relevance and Time Listed.
  - Expected: Pet order changes and matches the selected sort option.
  - Note: Switching Relevance → "Newest First" visibly reordered the pet grid (verified order change).

## Content
- [X] CT-01: Pet listings show accurate adoption attributes
  - Action: Inspect a pet card and its profile.
  - Expected: Each pet displays species, age, size, and good-with-kids/good-with-pets indicators.
  - Note: Cards show species, size, age, and a "Kid-friendly" badge; the full profile additionally shows Gender, Personality, and explicit "Good with kids" / "Good with other pets" + Health indicators. All attributes were accurate. (Minor: the list card surfaces only the "Kid-friendly" badge, not the "good with other pets" indicator — that indicator appears on the detail profile.)

- [X] CT-02: All displayed content aligns with the pet-adoption theme
  - Action: Review site text, images, and shelter information.
  - Expected: Text, photos, and shelter names relate to adoptable pets (no irrelevant/off-topic content).
  - Note: All content is on-theme — brand "PawfectMatch", pet names/breeds/sizes, shelter "Happy Tails Rescue" with real-looking contact info, adoption-focused copy, and pet photos throughout. No off-topic content observed.
