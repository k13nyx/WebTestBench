All verification is complete. The compatibility icons (✓ text-success / ✗ text-destructive) confirm the filters' flags match the profile data — Whiskers is ✗ for kids, Max and Sunny are ✗ for other pets, exactly as the filters excluded them.

# Test Result

## Functionality
- [X] FT-01: Search adoptable animals by keyword
  - Action: Type a search term (e.g., "dog" or a pet name) into the search box and submit.
  - Expected: The list updates to show only pets matching the search term.
- [X] FT-02: Filter by species
  - Action: Select a species filter (e.g., "Dog").
  - Expected: Only pets of the selected species appear in the list.
- [X] FT-03: Filter by age range
  - Action: Select an age range filter (e.g., "Puppy/Kitten (< 1 year)").
  - Expected: Only pets within that age range appear in the list.
- [X] FT-04: Filter by size
  - Action: Select a size filter (e.g., "Small").
  - Expected: Only pets of the selected size appear in the list.
- [X] FT-05: Filter by "good with kids"
  - Action: Enable the "Good with kids" filter.
  - Expected: Only pets flagged as good with kids appear in the list.
- [X] FT-06: Filter by "good with other pets"
  - Action: Enable the "Good with other pets" filter.
  - Expected: Only pets flagged as good with other pets appear in the list.
- [X] FT-07: Sort the result list
  - Action: Select "Relevance" and then "Time listed" in the sort control.
  - Expected: Each selection reorders the list accordingly, with "Time listed" showing newest entries first.
- [X] FT-08: Open a detailed pet profile
  - Action: Click a pet in the result list.
  - Expected: A detailed profile page opens showing the pet's photos and a written description.
- [X] FT-09: Save a pet to favorites
  - Action: Click the save/favorite control on a pet.
  - Expected: The pet is added to the favorites list.
- [X] FT-10: View the favorites list
  - Action: Navigate to the favorites page/list.
  - Expected: All previously saved pets are listed, each with its name and photo.
- [X] FT-11: Send an adoption inquiry
  - Action: On a pet's profile page, fill the adoption inquiry form with valid details and submit it.
  - Expected: The inquiry is submitted successfully for that pet.

## Constraint
- [X] CS-01: Inquiry form rejects empty required fields
  - Action: Leave one or more required fields (e.g., name, email, message) blank and click submit.
  - Expected: The form does not submit and an error is indicated on the blank required field(s).
- [X] CS-02: Multiple active filters combine correctly
  - Action: Apply species + age range + size + "Good with kids" simultaneously.
  - Expected: Every listed pet satisfies ALL active filters; no pet missing any selected criterion is shown.

## Interaction
- [X] IX-01: Result list responds immediately to filter/sort changes
  - Action: Change any filter or the sort option with a result list already displayed.
  - Expected: The list and the displayed result count update immediately without a page reload.
- [X] IX-02: Success confirmation after inquiry submission
  - Action: Submit a valid adoption inquiry form.
  - Expected: A clear success confirmation (e.g., "Inquiry sent" message) is displayed.
- [X] IX-03: Favorite control reflects saved state
  - Action: Click the save/favorite control on a pet, then revisit that pet.
  - Expected: The control visibly changes to a saved/filled state and stays saved.
- [X] IX-04: No-match state is displayed
  - Action: Apply filters that no pet satisfies (e.g., a rare filter combination).
  - Expected: An explicit "no results" message is shown instead of an empty/broken list.

## Content
- [X] CT-01: Pet photos are present and relevant
  - Action: Browse the result list and open several pet profiles.
  - Expected: Each pet shows at least one photo that clearly depicts that pet; no broken or placeholder images.
- [X] CT-02: Pet profile content is relevant and complete
  - Action: Open a pet's detailed profile.
  - Expected: The description includes relevant details for that pet — name, breed/type, age, size, shelter, and kid/other-pet compatibility.
- [X] CT-03: Shelter attribution and multi-shelter coverage
  - Action: Review pets in the list and their profiles.
  - Expected: Each pet displays the name of its originating shelter, and pets from more than one shelter are represented.

---

### Evidence summary
- **FT-01:** search "dog" → count changed 12 → 5, all results were dogs (Luna, Max, Duke, Bella, Charlie).
- **FT-02–FT-06:** Dogs → 5 dogs; "Baby (< 1 year)" → only Mochi (6 months); Small → 4 small pets; Good with kids → 11 (Whiskers excluded, profile shows ✗ for kids); Good with other pets → 10 (Max & Sunny excluded, both show ✗ on profiles).
- **FT-07:** sort control offers Relevance / Newest First / Oldest First / Name A-Z ("Newest First" is the time-listed mode). Relevance → default order; Newest First reordered and placed the two oldest-listed pets (Whiskers, Shadow, "about 2 years ago") last; Relevance restored the original order.
- **FT-08/CT-02:** `/pets/pet-1` shows gallery (main + thumbnails), "About Luna" description, name, breed (Golden Retriever Mix), age (3 years), size (Large), shelter (Happy Tails Rescue), and compatibility rows.
- **CS-01:** submitting with blank name/email, then with blank message, never submitted (URL and form unchanged, no success state); browser reported "Please fill out this field." on the blank required field (native validation, no custom inline error text).
- **CS-02:** Dogs + Adult (4-7) + Small + Good with kids → exactly 1 result, Bella (dog, small, 4 years, kid-friendly) — satisfies all four criteria.
- **IX-01:** every checkbox/sort change updated the list and "N adorable pets available" count synchronously with no navigation/reload.
- **IX-02/FT-11:** valid submit → panel "Inquiry Submitted! … has received your inquiry about Luna" plus toast "Inquiry Sent! …".
- **FT-09/FT-10/IX-03:** heart icon switched from `text-muted-foreground` to `fill-accent text-accent`; `/favorites` showed "1 pet saved to your favorites" with Luna's name and loaded photo; heart still filled on revisit.
- **IX-04:** Birds + Large → "0 adorable pets available" and explicit "No pets found" message.
- **CT-01:** all 12 list images loaded (naturalWidth 600, complete, unique Unsplash sources, no placeholders); profile photos loaded on every profile opened.
- **CT-03:** profiles display originating shelter names — Happy Tails Rescue (Portland) and Second Chance Animal Haven (Seattle) — confirming ≥2 shelters; note list cards show the pet's city rather than the shelter name, with attribution appearing on each pet's profile.