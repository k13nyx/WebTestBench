All tests executed. Compiling results.

# Test Result

## Functionality
- [X] FT-01: New student can create an account and log in
  - Action: Open the sign-up form, enter a valid name, email, and password, submit, then log in with those credentials
  - Expected: Account is created and the user lands in the app logged in as the new student
  - Note: Sign-up ("Alice Student") created the account, showed "Welcome to StudyHub! Your account has been created." and landed on /profile logged in; log out → sign-in with the same credentials redirected to /groups as the member. (See "General observations" — accounts do not survive a full page reload.)

- [X] FT-02: Profile includes subjects, current level, and preferred study times
  - Action: Go to Profile, add subjects (e.g., "Biology"), set current level (e.g., "Sophomore / AP"), set preferred study times (e.g., weekday evenings), save, then reopen the profile
  - Expected: All three fields save and are displayed again on the profile page
  - Note: Subjects Biology + Literature selected, level set to "High School" (the app's closest level option; no "Sophomore/AP" choice exists), availability Monday–Friday 18:00–21:00 saved via "Save Availability". After navigating away and reopening the profile, all three persisted (Bio text also persisted: "AP student who loves Biology and Literature").

- [X] FT-03: Student can create a study group around a topic
  - Action: Select "Create Group", enter a topic name (e.g., "Calculus BC – Chapter 4") and submit
  - Expected: The group is created and appears in the creator's group list with the shared space accessible
  - Note: "Calculus BC – Chapter 4" created with toast "Group created!"; it appears under "Your Groups" with an accessible shared space (Notes/Discussions/Sessions/Members tabs, "Open Group" link).

- [X] FT-04: Student can join an existing default study group
  - Action: From the groups list/browse page, select an existing default group (e.g., "Literature") and click Join
  - Expected: The group is added to the student's groups and their membership is reflected in the member list
  - Note: Joined "Victorian Literature Society" (toast "Joined group!"), it appeared under "Your Groups" (1 → 2 members), and the Members tab listed "Alice Student — Member" alongside the owner.

- [ ] FT-05: Members can create labeled sections and file content into them
  - Action: In a group's shared space, create a labeled section (e.g., "Reading Summaries"), then add a note, an outline, and a reading summary into that section
  - Expected: Each item is saved under the correct labeled section and visible to other group members
  - Bug Report:
    - Issue: Missing Feature — no way to create a custom labeled section
    - Actual: The group shared space offers only "Add Note" with a fixed Category dropdown (Lecture Notes, Formulas, Assignments, Reading List, Study Guides, Practice Problems, Summaries, Resources); there is no "create/add section" control anywhere (verified on the group page and the Add Note dialog). Items save correctly under existing categories and are visible to other members (Bob saw Alice's three items), but a user-created section such as "Reading Summaries" cannot be made.

- [X] FT-06: Discussion area supports questions and answers
  - Action: Post a question (e.g., "How do we solve problem 12?") in the group discussion, then post a reply to it as another member
  - Expected: Question and reply both appear in the discussion thread in order, attributed to their authors
  - Note: Question posted by Alice Student (Nov 8, 12:10 PM); after a second member (Bob Reader) joined the group, his reply appeared directly below the question, attributed to "Bob Reader" with its own timestamp.

- [X] FT-07: Members can schedule an upcoming study session via the time selector
  - Action: Open "Schedule Session", choose a future date/time using the simple time selector, and save
  - Expected: The session appears in the group's upcoming sessions list with the chosen date/time
  - Note: "Chapter 4 Review Session" scheduled for Thu Nov 12, 2026 18:00–20:00; toast "Session scheduled!" and the session appeared in the Sessions tab with the exact date/time.

- [ ] FT-08: Members can mark themselves as available for a session time
  - Action: Open the session scheduler/availability view and mark "available" for a proposed time slot
  - Expected: The student is recorded as available for that slot and counted in the availability display
  - Bug Report:
    - Issue: Missing Control — no per-session "available" marking exists
    - Actual: The "Schedule a Study Session" dialog contains only Title/Description/Date/Start/End inputs; the session card shows only RSVP buttons (Attending/Maybe/Can't make it). There is no "Available" toggle for a proposed slot anywhere in the session scheduler or group views (the profile Availability tab holds generic weekly hours, not session-slot availability).

- [ ] FT-09: Group members can RSVP to a scheduled session
  - Action: As a group member, open an upcoming session and click RSVP (e.g., "Attending"), then view the session again
  - Expected: The RSVP is saved and the member shows in the attendee list for that session
  - Bug Report:
    - Issue: Partial implementation — RSVP saves but no attendee list is displayed
    - Actual: Clicking "Maybe"/"Attending" updated counts live ("1 attending" → "0 attending / 1 maybe" → "1 attending") and Bob's "Attending" state persisted across tab switches and a logout/login cycle. However, the session card shows only numeric counts ("1 attending, 0 maybe") — there is no attendee list naming who is attending, so a member cannot be seen "in the attendee list".

- [X] FT-10: A student can mark their profile as a mentor
  - Action: In profile settings, toggle/mark "Mentor" status and save
  - Expected: The profile is flagged as a mentor and the status is visible on the profile page
  - Note: Toggling the "Mentor Status" checkbox and saving showed "Profile updated" and a "Mentor" badge under the name in the profile header.

- [X] FT-11: Groups can invite mentors, who join with a distinct role
  - Action: From a group, invite a default mentor account; accept the invitation and view the group's member list
  - Expected: The mentor appears in the member list labeled with a mentor role distinct from regular members
  - Note: "Invite Mentor" listed default mentors (Alex Chen, Dr. Emily Wong); inviting Alex produced "Invitation sent!". Logging in as Alex, the invitation appeared under a mentor-only "Invites" tab on the profile with Accept/Decline; after Accept the group's member list showed "Alex Chen — Mentor" (distinct from "Owner"/"Member" labels).

- [X] FT-12: Mentors can highlight recommended resources and pin posts
  - Action: As a mentor in a group, add/highlight a recommended resource (e.g., a textbook link or document) and pin an existing discussion post
  - Expected: The resource is marked as mentor-recommended and the post becomes pinned in the group space
  - Note: As mentor Alex Chen, the star ("recommend") control on a note activated (accent-filled star persisted on the card, visible to members) and clicking the pin icon on a discussion post pinned it — the pinned post moved to the top of the discussion list, above unpinned posts. (Labeling shortcomings are reported under IX-02.)

## Constraint
- [ ] CS-01: Required profile/group fields cannot be left empty
  - Action: Submit the profile form with subjects/level left blank, then submit "Create Group" with no topic name
  - Expected: A validation error is shown for each, and nothing is saved (user stays on the form)
  - Bug Report:
    - Issue: Missing Validation — profile form accepts empty subjects
    - Actual: Deselecting all subjects and clicking "Save Changes" showed the success toast "Profile updated — Your changes have been saved." and persisted a profile with zero subjects (no validation error). The Create Group dialog did validate correctly ("Notification: Please fill in all fields", dialog stayed open), so the profile half of the constraint fails.

- [X] CS-02: Pin and resource-highlight controls are restricted to mentors
  - Action: As a regular (non-mentor) group member, look for the "Pin" control on a post and the "Recommend resource" control
  - Expected: These controls are absent or disabled for the regular member; the action cannot be performed
  - Note: As Bob Reader (plain "Member", non-mentor), discussion post cards showed only the reply input/send button — no pin control; note cards showed no star/pin buttons (only the already-starred card retained a static star marker). Actions could not be performed.

## Interaction
- [ ] IX-01: Time selector shows who is available per slot
  - Action: With default members having marked availability, open the session time selector and inspect a proposed slot
  - Expected: The selector displays the list/count of members available for that slot, updating when availability is toggled
  - Bug Report:
    - Issue: Missing Feature — no availability display in the time selector
    - Actual: The "Schedule a Study Session" dialog contains only Title/Description/Date/Start Time/End Time fields. Changing the date (2026-11-19) and time (18:00) produced no availability list, count, or member info; the dialog text remained identical ("…Date, Start Time, End Time, Schedule Session, Close"). No per-slot availability UI exists anywhere in the group session views.

- [ ] IX-02: Pinned posts are visually distinguished and placed at the top
  - Action: After a mentor pins a discussion post, view the discussion area
  - Expected: The pinned post appears at the top with a clear "Pinned" indicator, above unpinned posts
  - Bug Report:
    - Issue: Missing Indicator — no "Pinned" label/badge
    - Actual: Ordering works (pinning Alex's newer post moved it above older unpinned posts; unpinning reverted order). But there is no "Pinned" text or badge: the only signal is the pin icon's subtle color change (text-primary), visible only to the user whose view shows the pin button. A regular member's view of the pinned thread contained no pin icon or "Pinned" label at all.

- [X] IX-03: Session/RSVP actions produce visible confirmation
  - Action: Create a session and submit an RSVP, watching the UI after each action
  - Expected: A success message or immediate state change confirms each action (e.g., session listed, attendee count updates) without needing a manual page reload
  - Note: Session creation raised the toast "Session scheduled!" and immediately listed the session; each RSVP click updated the attending/maybe counts live without any reload.

## Content
- [X] CT-01: Default content is relevant to the study platform theme
  - Action: Browse the default groups, sections, and resources on the home/groups pages
  - Expected: Topics shown are study-related as specified (e.g., calculus, biology, literature); no placeholder/irrelevant content appears
  - Note: Landing page and groups list cover calculus ("Calculus Champions", "Master calculus together! From limits to integrals…"), biology ("Biology Study Circle"), literature ("Victorian Literature Society"); seeded notes include a "Reading List - Fall Semester" with Jane Eyre, Great Expectations, Middlemarch, Tess; members/mentors have real names and subjects. No lorem-ipsum/placeholder content found.

- [X] CT-02: Role labels and mentor content are correctly presented
  - Action: View a mentor's profile and a group's member list and recommended-resources area
  - Expected: The mentor displays a clear mentor badge/label, and mentor-highlighted resources are visibly marked as recommended
  - Note: Alex Chen's profile header displays a "Mentor" badge; member lists show distinct "Owner" / "Mentor" / "Member" labels (also "1 Mentor" chips on the groups page); the mentor-starred resource card displays a persistent filled/accent star marker. (The recommendation mark is icon-only with no text label — see IX-02 for the analogous labeling weakness.)

## General observations (outside checklist scope)
- **Data does not survive a full page reload:** the mock backend is in-memory only; a hard navigation (e.g., typing the URL) wiped the newly created account ("Login failed — No account found with that email"), and all groups/notes/RSVPs reset. All verifications above were performed via in-app SPA navigation, where state persists correctly.
- A non-mentor group **Owner** (Alice, before mentor toggle) saw and could use the pin control on discussion posts — pinning is not restricted to "mentors" for owners, though it is correctly absent for plain members.
- Pin/star/reply icon buttons have no accessible labels (no aria-label/title), and RSVP attendees are count-only (no names).