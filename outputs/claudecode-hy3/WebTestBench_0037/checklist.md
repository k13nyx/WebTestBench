# Test Checklist

## Functionality
- [ ] FT-01: Search adoptable animals by keyword
  - Action: Enter a keyword (e.g., "Labrador") in the search box and submit.
  - Expected: Results list shows only pets whose name/breed/description match the keyword.

- [ ] FT-02: Filter pets by species, age range, size, good-with-kids, good-with-pets
  - Action: Set filters (e.g., Species=Dog, Age=Young, Size=Medium, Good with Kids=Yes, Good with Pets=Yes) and apply.
  - Expected: A results list of pets matching all selected criteria is displayed across multiple shelters.

- [ ] FT-03: View a clear list of matching pets
  - Action: Apply any search/filter combination.
  - Expected: A list/grid of matching pets appears, each identifiable by name and/or photo.

- [ ] FT-04: Sort pets by relevance or time listed
  - Action: Select "Sort by: Relevance" then "Sort by: Time Listed".
  - Expected: List reorders to relevance ranking, then to newest-listed-first order.

- [ ] FT-05: Open a detailed profile for a pet
  - Action: Click a pet's name, photo, or card in the results list.
  - Expected: That pet's detailed profile page opens.

- [ ] FT-06: Save a pet to favorites
  - Action: On a pet's profile/list item, click "Save to Favorites" (or heart icon).
  - Expected: Pet is added to the favorites list.

- [ ] FT-07: View the saved favorites list
  - Action: Open the Favorites section.
  - Expected: All previously saved pets are shown.

- [ ] FT-08: Send an adoption inquiry via the pet's page form
  - Action: On a pet's profile, fill required fields (name, email, message) and click "Send Inquiry".
  - Expected: Inquiry is submitted and a confirmation is shown.

## Constraint
- [ ] CS-01: Filter results must not violate any selected criterion
  - Action: Apply filters including "Good with Kids=No" and "Size=Small".
  - Expected: No result contradicts a selected filter value (no kids-friendly or non-small pets appear).

- [ ] CS-02: Inquiry form blocks submission with empty required fields
  - Action: Leave required fields blank and click "Send Inquiry".
  - Expected: Submission is blocked and an error marks the missing required fields.

- [ ] CS-03: Same pet cannot be added to favorites twice
  - Action: Save a pet that is already in the favorites list.
  - Expected: Favorites list shows the pet only once (no duplicate entry).

## Interaction
- [ ] IX-01: Results update dynamically when filters change
  - Action: Change a filter value (e.g., toggle "Good with Pets").
  - Expected: Pet list immediately reflects updated results without a full page reload.

- [ ] IX-02: Visible confirmation when favoriting a pet
  - Action: Click "Save to Favorites" on a pet.
  - Expected: The button/icon changes state (e.g., empty→filled heart) or a success toast appears.

- [ ] IX-03: Profile page renders photos and description
  - Action: Open a pet's detailed profile.
  - Expected: At least one photo and a text description are visible on the page.

- [ ] IX-04: Sort control visibly changes result order
  - Action: Switch between Relevance and Time Listed.
  - Expected: Pet order changes and matches the selected sort option.

## Content
- [ ] CT-01: Pet listings show accurate adoption attributes
  - Action: Inspect a pet card and its profile.
  - Expected: Each pet displays species, age, size, and good-with-kids/good-with-pets indicators.

- [ ] CT-02: All displayed content aligns with the pet-adoption theme
  - Action: Review site text, images, and shelter information.
  - Expected: Text, photos, and shelter names relate to adoptable pets (no irrelevant/off-topic content).