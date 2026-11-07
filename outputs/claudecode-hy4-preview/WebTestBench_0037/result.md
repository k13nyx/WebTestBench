# Test Result

## Functionality

- [X] FT-01: Keyword search returns matching pets
  - Action: On the search/browse page, type a name or breed that exists in the default pet list (e.g. "Luna") into the search box and submit.
  - Expected: A list of pets whose name/breed matches the query is displayed; every result contains the query term in its name or breed.

- [X] FT-02: Filter by species narrows results correctly
  - Action: Open the Species filter, select one species (e.g. "Dog"), and apply it.
  - Expected: All displayed pets show that species on their card; no pet of another species (e.g. Cat) appears in the list.

- [X] FT-03: Filter by age range narrows results correctly
  - Action: Open the Age filter, select one age range (e.g. "Young" / 1–3 years), and apply it.
  - Expected: All displayed pets have an age falling inside the selected range; no pet outside that range appears.

- [X] FT-04: Filter by size narrows results correctly
  - Action: Open the Size filter, select one size (e.g. "Small"), and apply it.
  - Expected: All displayed pets show the selected size; pets of other sizes are absent from the list.

- [X] FT-05: "Good with kids" and "Good with other pets" filters each narrow results
  - Action: Apply the "Good with kids" filter; note results. Clear it, then apply "Good with other pets"; note results.
  - Expected: With each filter applied, every displayed pet is marked as good with kids (resp. good with other pets); pets not marked are excluded.

- [ ] FT-06: Filters combine, and results are drawn from multiple shelters
  - Action: Search empty (no keyword), apply Species = "Dog" together with Size = "Small", and inspect the shelter name shown on the result cards.
  - Expected: The list contains only pets matching both criteria, and at least two different shelter names appear across the results (default data spans multiple shelters).
  - Bug Report:
    - Issue: Expected result set too small to span multiple shelters; shelter provenance not exposed in the list
    - Actual: Filters combine correctly — Species = Dog + Size = Small returns exactly 1 pet ("Bella", French Bulldog, small, dog), so only one shelter ("Furry Friends Forever") is represented and two different shelter names cannot appear. Additionally, no result card renders a shelter name at all: cards display only the location city/state (e.g. "San Francisco, CA"); the shelter name ("Furry Friends Forever") appears only on the pet detail page. (Underlying data does span 3 shelters: Happy Tails Rescue, Second Chance Animal Haven, Furry Friends Forever.)

- [X] FT-07: Sort by relevance and by time listed both reorder the list
  - Action: Enter a keyword search, select sort option "Relevance", record the first 3 pet names; then select "Time Listed" (or "Newest"), record the first 3 names again.
  - Expected: Both options return a valid ordered list for the same result set, and switching between them changes the ordering (or, at minimum, each option keeps its own stable, non-empty order with the newest-listed pet first under "Time Listed").

- [X] FT-08: Pet detail profile opens with photos and description
  - Action: From the results list, click one pet's card/name.
  - Expected: A detail page for that exact pet opens showing at least one photo, a non-empty description, and its attributes (species, breed, age, size, shelter).

- [X] FT-09: Save a pet to favorites and remove it from the favorites list
  - Action: On a pet's detail page click the "Favorite"/"Save" control; then open the Favorites list. Then remove that pet from the list.
  - Expected: The pet appears in the Favorites list after saving, and disappears from the list after removal.

- [X] FT-10: Submit an adoption inquiry from the pet's page
  - Action: On a pet's detail page, fill the inquiry form with name, a valid email, and a message, then submit.
  - Expected: The inquiry for that specific pet is accepted (confirmation shown, and the form is no longer in an unsent state).

## Constraint

- [X] CS-01: No-match filters show an explicit empty state
  - Action: Apply a filter combination that cannot match any default pet (e.g. Species = "Cat" + Size = "Large" if no such pet exists, or a nonsense search keyword).
  - Expected: The list area shows a "no pets found" / empty-results message; no pet cards are displayed and the page does not error.

- [X] CS-02: Inquiry form blocks submission with empty required fields
  - Action: On a pet's detail page, click the inquiry submit button with all fields left empty.
  - Expected: Submission is blocked, no confirmation appears, and required-field error messages are shown (e.g. name, email, message).

- [X] CS-03: Inquiry form rejects an invalid email address
  - Action: Fill the inquiry form with a valid name and message but an invalid email (e.g. "notanemail"), then submit.
  - Expected: Submission is blocked and an email-format error is displayed; no confirmation appears.

- [X] CS-04: A pet cannot be added to favorites twice
  - Action: Favorite a pet, then favorite the exact same pet again (re-click the control / re-save from its page), then open Favorites.
  - Expected: The pet appears exactly once in the Favorites list (no duplicate entries).

## Interaction

- [X] IX-01: Favorite control reflects saved state immediately
  - Action: On a pet's detail page, click the favorite/heart control once; then click it again.
  - Expected: The control visibly toggles to a "saved" state on the first click and back to an "unsaved" state on the second, without reloading the page.

- [X] IX-02: Confirmation appears after a successful inquiry submission
  - Action: Submit a fully valid inquiry form on a pet's detail page.
  - Expected: A success message (e.g. "Inquiry sent") appears on the page.

- [X] IX-03: Result count updates as filters are applied
  - Action: Note the displayed result count (e.g. "24 pets") with no filters, then apply Species = "Dog".
  - Expected: The displayed count updates immediately to match the number of cards shown and is lower than the unfiltered count.

## Content

- [ ] CT-01: Result cards show the info needed to compare pets
  - Action: Inspect three pet cards in the unfiltered results list.
  - Expected: Each card shows the pet's photo, name, shelter name, and at least species/age/size attributes; no card has a missing or broken image (no broken-image icon).
  - Bug Report:
    - Issue: Missing shelter name on result cards
    - Actual: All three inspected cards (Luna, Oliver, Max) show a working photo (naturalWidth 600, `complete=true`), the pet name, breed, size, age, species badge and listing date — but **no shelter name**. Cards render only the shelter's city/state location, e.g. "Luna | Golden Retriever Mix | Large | 3 years | Portland, OR". The shelter name ("Happy Tails Rescue") is shown only on the pet detail page, so pets from different shelters cannot be compared by shelter in the list.

- [X] CT-02: Detail page photos render and relate to the pet
  - Action: Open any pet's detail page and view its photo gallery.
  - Expected: At least one photo loads as a real image (not a broken-image placeholder) and depicts the animal, not an unrelated subject or a generic icon.

- [X] CT-03: Filter controls use pet-adoption-relevant options
  - Action: Open each filter control (Species, Age, Size, Good with kids, Good with other pets).
  - Expected: Species options are animal species/breed groups (e.g. Dog, Cat), Age options are animal age ranges (e.g. Baby/Young/Adult/Senior), Size options are animal size classes (e.g. Small/Medium/Large) — no placeholder or unrelated options.

---

### Notes on verified evidence

- **Data set**: 12 pets across 3 shelters — Happy Tails Rescue (Luna, Max, Duke, Shadow), Second Chance Animal Haven (Oliver, Biscuit, Sunny, Charlie), Furry Friends Forever (Whiskers, Mochi, Bella, Cinnamon).
- **FT-05 verification**: the "Good with other pets" filter excluded Max and Sunny; Max's profile shows a red-X "Good with other pets" marker while Whiskers (included) shows a green check — exclusion matches the underlying data. Card badges surface "Kid-friendly" but not the other-pets marker.
- **CS-02 / CS-03**: validation is browser-native HTML5 (`required` on name/email/message, `type="email"`). Submission was blocked with no confirmation, and the browser reported per-field messages (e.g. *"Please include an '@' in the email address. 'notanemail' is missing an '@'."*). The app renders no custom inline error text.
- **FT-07**: sort options are Relevance / Newest First / Oldest First / Name A‑Z. For keyword "mix": Relevance → Luna, Whiskers, Charlie; Newest First → Charlie, Luna, Whiskers. Unfiltered, Newest First places the "about 2 years ago" listings (Whiskers, Shadow) last.