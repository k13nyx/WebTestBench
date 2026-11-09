# Test Checklist

## Functionality
- [ ] FT-01: New student can create an account and log in
  - Action: Open the sign-up form, enter a valid name, email, and password, submit, then log in with those credentials
  - Expected: Account is created and the user lands in the app logged in as the new student

- [ ] FT-02: Profile includes subjects, current level, and preferred study times
  - Action: Go to Profile, add subjects (e.g., "Biology"), set current level (e.g., "Sophomore / AP"), set preferred study times (e.g., weekday evenings), save, then reopen the profile
  - Expected: All three fields save and are displayed again on the profile page

- [ ] FT-03: Student can create a study group around a topic
  - Action: Select "Create Group", enter a topic name (e.g., "Calculus BC – Chapter 4") and submit
  - Expected: The group is created and appears in the creator's group list with the shared space accessible

- [ ] FT-04: Student can join an existing default study group
  - Action: From the groups list/browse page, select an existing default group (e.g., "Literature") and click Join
  - Expected: The group is added to the student's groups and their membership is reflected in the member list

- [ ] FT-05: Members can create labeled sections and file content into them
  - Action: In a group's shared space, create a labeled section (e.g., "Reading Summaries"), then add a note, an outline, and a reading summary into that section
  - Expected: Each item is saved under the correct labeled section and visible to other group members

- [ ] FT-06: Discussion area supports questions and answers
  - Action: Post a question (e.g., "How do we solve problem 12?") in the group discussion, then post a reply to it as another member
  - Expected: Question and reply both appear in the discussion thread in order, attributed to their authors

- [ ] FT-07: Members can schedule an upcoming study session via the time selector
  - Action: Open "Schedule Session", choose a future date/time using the simple time selector, and save
  - Expected: The session appears in the group's upcoming sessions list with the chosen date/time

- [ ] FT-08: Members can mark themselves as available for a session time
  - Action: Open the session scheduler/availability view and mark "available" for a proposed time slot
  - Expected: The student is recorded as available for that slot and counted in the availability display

- [ ] FT-09: Group members can RSVP to a scheduled session
  - Action: As a group member, open an upcoming session and click RSVP (e.g., "Attending"), then view the session again
  - Expected: The RSVP is saved and the member shows in the attendee list for that session

- [ ] FT-10: A student can mark their profile as a mentor
  - Action: In profile settings, toggle/mark "Mentor" status and save
  - Expected: The profile is flagged as a mentor and the status is visible on the profile page

- [ ] FT-11: Groups can invite mentors, who join with a distinct role
  - Action: From a group, invite a default mentor account; accept the invitation and view the group's member list
  - Expected: The mentor appears in the member list labeled with a mentor role distinct from regular members

- [ ] FT-12: Mentors can highlight recommended resources and pin posts
  - Action: As a mentor in a group, add/highlight a recommended resource (e.g., a textbook link or document) and pin an existing discussion post
  - Expected: The resource is marked as mentor-recommended and the post becomes pinned in the group space

## Constraint
- [ ] CS-01: Required profile/group fields cannot be left empty
  - Action: Submit the profile form with subjects/level left blank, then submit "Create Group" with no topic name
  - Expected: A validation error is shown for each, and nothing is saved (user stays on the form)

- [ ] CS-02: Pin and resource-highlight controls are restricted to mentors
  - Action: As a regular (non-mentor) group member, look for the "Pin" control on a post and the "Recommend resource" control
  - Expected: These controls are absent or disabled for the regular member; the action cannot be performed

## Interaction
- [ ] IX-01: Time selector shows who is available per slot
  - Action: With default members having marked availability, open the session time selector and inspect a proposed slot
  - Expected: The selector displays the list/count of members available for that slot, updating when availability is toggled

- [ ] IX-02: Pinned posts are visually distinguished and placed at the top
  - Action: After a mentor pins a discussion post, view the discussion area
  - Expected: The pinned post appears at the top with a clear "Pinned" indicator, above unpinned posts

- [ ] IX-03: Session/RSVP actions produce visible confirmation
  - Action: Create a session and submit an RSVP, watching the UI after each action
  - Expected: A success message or immediate state change confirms each action (e.g., session listed, attendee count updates) without needing a manual page reload

## Content
- [ ] CT-01: Default content is relevant to the study platform theme
  - Action: Browse the default groups, sections, and resources on the home/groups pages
  - Expected: Topics shown are study-related as specified (e.g., calculus, biology, literature); no placeholder/irrelevant content appears

- [ ] CT-02: Role labels and mentor content are correctly presented
  - Action: View a mentor's profile and a group's member list and recommended-resources area
  - Expected: The mentor displays a clear mentor badge/label, and mentor-highlighted resources are visibly marked as recommended