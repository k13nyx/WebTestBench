All tests executed. Here is the complete checklist with results.

# Test Result

## Functionality
- [X] FT-01: Search box returns adoptable pets matching the entered term
  - Action: Type a pet name/keyword (e.g., "Labrador") in the search field and submit.
  - Expected: Results list shows only pets matching the term; previously shown non-matching pets are removed.
- [X] FT-02: User can filter results by species
  - Action: Select a species option (e.g., "Dog") in the species filter.
  - Expected: Results list updates to show only pets of the selected species.
- [ ] FT-03: User can filter results by age range
  - Action: Set/select an age range (e.g., "1–3 years") in the age filter.
  - Expected: Results list shows only pets whose listed age falls within the selected range.
  - Bug Report:
    - Issue: Incorrect Filter Results (age-range boundary misclassification)
    - Actual: Selecting "Adult (4-7 years)" returns Luna and Shadow, both displayed as "3 years" — outside the range. Selecting "Senior (8+ years)" returns Duke, displayed as "7 years" — outside the range. Conversely, "Young (1-3 years)" omits the 3-year-old pets (Luna, Shadow). The age buckets do not align with the displayed/listed age.
- [X] FT-04: User can filter results by size
  - Action: Select a size option (e.g., "Small") in the size filter.
  - Expected: Results list shows only pets matching the selected size.
- [X] FT-05: User can filter by good with kids and good with other pets
  - Action: Select "Good with kids" and separately "Good with other pets".
  - Expected: Results list narrows to only pets tagged as good with kids / good with other pets respectively.
- [X] FT-06: Multiple filters apply together
  - Action: Apply species + age range + size simultaneously.
  - Expected: Results satisfy ALL selected criteria at once (not just the last one applied).
- [ ] FT-07: Results list shows matching pets from multiple shelters
  - Action: Run a broad search that matches pets from different shelters.
  - Expected: Result cards list pets from more than one shelter, each card showing pet name, photo, and shelter name.
  - Bug Report:
    - Issue: Missing Content on Result Cards (shelter name absent)
    - Actual: Cards show pet name and photo, but display the shelter's city ("Portland, OR" / "Seattle, WA" / "San Francisco, CA") in place of the shelter name. No shelter name (e.g., "Happy Tails Rescue", "Second Chance Animal Haven", "Furry Friends Forever") appears anywhere on the results list.
- [X] FT-08: User can sort results by relevance or time listed
  - Action: Choose "Sort by: Relevance" then "Sort by: Newest/Time listed".
  - Expected: Order changes accordingly — relevance keeps best matches first; time listed shows most recently listed first.
- [X] FT-09: User can open a detailed pet profile with photos and description
  - Action: Click a pet in the results list.
  - Expected: A detail page opens showing at least one pet photo and a written description for that specific pet.
- [X] FT-10: User can save a pet to a favorites list
  - Action: Click "Save"/"Favorite" on a pet, then open the favorites list.
  - Expected: The pet appears in the favorites list and is viewable there.
- [X] FT-11: User can send an adoption inquiry from the pet's page
  - Action: On a pet's profile page, fill the inquiry form and click "Send Inquiry".
  - Expected: Form submits successfully and a confirmation is shown.

## Constraint
- [X] CS-01: No-match search/filter combination shows an empty state
  - Action: Apply filters that match no pets (e.g., species + size with zero overlap).
  - Expected: A clear "no pets found" message is shown; no unrelated or stale pets remain listed.
- [X] CS-02: Inquiry form blocks submission with missing required fields
  - Action: Click "Send Inquiry" with required fields (e.g., name, email, message) empty.
  - Expected: Form is not submitted; each missing required field shows a validation error.
- [X] CS-03: Inquiry is tied to the specific pet being viewed
  - Action: Open Pet A, submit an inquiry, then open Pet B's page.
  - Expected: The submitted inquiry references Pet A (not the wrong pet); Pet B's form is blank/unrelated.
- [X] CS-04: Favorites list does not create duplicates for the same pet
  - Action: Save the same pet twice (from list and/or detail page).
  - Expected: The pet appears only once in the favorites list.

## Interaction
- [X] IX-01: Confirmation is shown after a successful inquiry submission
  - Action: Submit a valid adoption inquiry form.
  - Expected: A success message/toast (e.g., "Your inquiry has been sent") is displayed to the user.
- [X] IX-02: Favorite toggle reflects saved/unsaved state
  - Action: Click the favorite control on a pet, then click it again.
  - Expected: Icon/label switches to a visible "saved" state on first click and back to "unsaved" on second click, consistent with the favorites list.

## Content
- [X] CT-01: Pet photos are relevant to the pet and its species
  - Action: Open several pet profiles across different species.
  - Expected: Each profile's main photo depicts a real animal of the stated species/breed (no placeholders, unrelated, or broken images).
- [X] CT-02: Each pet profile contains a specific, present description
  - Action: Open multiple pet profiles.
  - Expected: Every profile has a written description with pet-specific details (not empty, not generic filler).
- [ ] CT-03: Shelter origin is identified on each pet
  - Action: Review pet cards and profiles.
  - Expected: Each pet displays its source shelter name so the user can confirm listings come from multiple shelters.
  - Bug Report:
    - Issue: Missing Content (shelter name not shown on pet cards)
    - Actual: Shelter name is displayed only on the profile page ("Shelter Information" → e.g., "Happy Tails Rescue", "Second Chance Animal Haven"). On the results/favorites cards, only the city ("Portland, OR") is shown; the source shelter name is absent from cards, so shelter origin cannot be confirmed from the card view.

---

### Verification Notes (evidence)
- **FT-01:** Search "Golden" → only `Luna` (Golden Retriever Mix) remained.
- **FT-02:** Species "Dogs" → exactly the 5 dogs (Luna, Max, Duke, Bella, Charlie).
- **FT-03:** Bucket results — Baby→Mochi(6mo); Young(1-3)→Oliver(2), Max(1), Biscuit(1), Sunny(2), Cinnamon(2); Adult(4-7)→Luna(3), Whiskers(5), Bella(4), Shadow(3), Charlie(5); Senior(8+)→Duke(7). Underlying data confirms Luna=3, Shadow=3, Duke=7.
- **FT-04:** "Small" → Biscuit, Mochi, Sunny, Bella (all small).
- **FT-05:** "Good with kids" → 11 pets (excludes Whiskers, the only `goodWithKids:false`); "Good with other pets" → 10 pets (excludes Max and Sunny, the only `goodWithPets:false`).
- **FT-06:** Dogs + Young(1-3) + Medium → `Max` (satisfies all three; not just last-applied).
- **FT-08:** "Newest First" order matched `listedAt` descending exactly (Mochi 2024-12-10 → Shadow 2024-10-15); "Oldest First" matched ascending exactly; "Relevance" returned default order.
- **FT-09 / CT-01 / CT-02:** Profile shows main photo + thumbnails, "About <pet>" description; all 12 card images loaded (naturalWidth=600, 0 broken, 12 distinct sources); all 12 pets have specific descriptions (~169–215 chars).
- **FT-11 / IX-01 / CS-03:** Submitting Luna's form produced toast "Inquiry Sent! Happy Tails Rescue will contact you soon about Luna."; Oliver's page showed "Interested in Oliver?" with message "Hi! I'm interested in adopting Oliver…".
- **CS-01:** Birds + Large → "No pets found — Try adjusting your search or filters to find more pets." with a "Clear all filters" action; 0 cards.
- **CS-02:** Name/Email/Message are `required`; submitting empty kept the user on the page (no submission) with browser validation messages.
- **CS-04 / IX-02:** Favorites badge 2→1→2 on toggle; favorites list contained Luna and Oliver exactly once; list heart icons matched favorites (only Luna & Oliver filled).

**Summary: 18 PASS / 3 FAIL** — Failures: FT-03 (age filter boundary bug), FT-07 (shelter name missing on result cards), CT-03 (shelter origin not shown on cards).