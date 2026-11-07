# Test Result

## Functionality

- [X] FT-01: New student can create an account and sign in
  - Action: Open the sign-up page, enter a valid name, email, and password, submit, then sign in with the same credentials.
  - Expected: Account is created, the user is signed in, and the app shows the signed-in home/dashboard with profile setup prompted or accessible.

- [ ] FT-02: Student can set up a profile with subjects, current level, and preferred study times
  - Action: Open profile setup, add at least one subject (e.g., Biology), select a current level (e.g., Beginner/Intermediate/Advanced), select a preferred study time, and save.
  - Expected: Profile saves successfully and the profile page displays the entered subjects, current level, and preferred study times.
  - Bug Report:
    - Issue: Incorrect Form Submission / Data Mismatch
    - Actual: The Academic Level ("Graduate") and the Availability entry (monday 14:00–18:00) saved and displayed correctly, but subjects did not: the subject picker behaves as a single-select (clicking Literature deselected Biology), the selection is cleared whenever the level dropdown is changed, and after saving with "Biology" selected no subject toggle is active and the profile/member list shows "Literature" — a subject never selected. The profile page never renders the saved subjects as display data (only the editor toggles).

- [ ] FT-03: Student can create a focused study group around a topic
  - Action: Go to the groups area, choose "Create Group", enter a topic name (e.g., Calculus), a description, and submit.
  - Expected: The new group is created and appears in the group list and in the creator's "My Groups"; the group page opens showing its shared space and discussion area.
  - Bug Report:
    - Issue: Missing Navigation / Incomplete Listing
    - Actual: "Calculus Problem Solvers" (Mathematics) was created and appeared in "Your Groups", but the app stayed on /groups — the new group's page did not open (no redirect to the shared space/discussion area), and the new group was never added to the "Discover Groups" directory list, so it is not visible to other students.

- [X] FT-04: Student can join an existing study group from the default group list
  - Action: From the groups directory, open a default group the user has not joined (e.g., Biology) and select "Join Group".
  - Expected: The user becomes a member; the group appears in "My Groups" and the join button changes to a member state (e.g., "Leave" or "Joined").

- [ ] FT-05: Members can organize notes, outlines, and reading summaries into labeled sections
  - Action: In a joined group's shared space, create a labeled section (e.g., "Exam Prep"), then add one note, one outline, and one reading summary into that section.
  - Expected: All three items appear inside the "Exam Prep" section, each with its title and content visible and grouped under that section label.
  - Bug Report:
    - Issue: Missing Feature (no user-created sections) / No Grouping
    - Actual: The shared space (Notes tab) has only an "Add Note" button — there is no "Add Section"/"Create Section" control, so a section named "Exam Prep" cannot be created. The only labeling mechanism is a fixed preset "Category" dropdown (Lecture Notes, Formulas, Assignments, Reading List, Study Guides, Practice Problems, Summaries, Resources). Three items were added with the "Study Guides" label ("Exam Prep Note: Cell Structure", "Exam Prep Outline: Unit 1-4", "Exam Prep Reading Summary: Ch. 7"); all three show their title and content with the "Study Guides" badge, but they are rendered in a flat chronological list with a per-item badge rather than grouped under a section heading.

- [X] FT-06: Members can post questions and answers in the group discussion area
  - Action: In the group discussion area, post a question; then open that question and post a reply/answer.
  - Expected: The question appears in the discussion list; opening it shows the posted answer under it, attributed to the member who replied.

- [X] FT-07: Members can schedule an upcoming study session with the time selector
  - Action: In the group, open the scheduling/session area, pick a future date and time using the time selector, add a title, and confirm.
  - Expected: The session is created and appears in the group's "Upcoming Sessions" list with the chosen date, time, and title.

- [ ] FT-08: Members can mark themselves as available for proposed times
  - Action: In the scheduling view, mark yourself as available for at least one proposed time slot and save/confirm.
  - Expected: Your name is recorded as available for that slot and is shown in the availability display for that time slot.
  - Bug Report:
    - Issue: Missing Feature
    - Actual: The group's Sessions tab and the "Schedule a Study Session" dialog contain no proposed time slots and no availability control. The dialog has only Title, Description, Date, Start Time and End Time; the session card shows only title, time range, organizer and RSVP counts. The only availability feature in the app is the personal weekly availability editor on the profile's "Availability" tab (day + from/to times), which is not tied to any proposed group time slot and is not displayed anywhere in the scheduling view.

- [ ] FT-09: Members can RSVP to a scheduled session and appear in the attendee list
  - Action: Open an existing upcoming session in a joined group and select "RSVP"/"Going".
  - Expected: Your name appears in the session's attendee list and the session shows you as attending to all viewers.
  - Bug Report:
    - Issue: Missing Attendee List
    - Actual: RSVP state is recorded (the "Attending" button becomes active and the counter changes: 1 attending → 0 attending after "Can't make it" → 1 attending after "Attending" again), but the session card shows only aggregate counters ("1 attending / 0 maybe"). There is no attendee list — no names or avatars of who is attending are displayed anywhere on the session.

- [X] FT-10: A user can mark their profile as a mentor
  - Action: Open profile settings, enable the "Mentor" option (e.g., "I am available as a mentor"), and save.
  - Expected: The profile displays a mentor indicator/badge and the user is identified as a mentor elsewhere in the app.

- [X] FT-11: A group can invite a mentor and the mentor can accept and join with a mentor role
  - Action: From a group's members area, open "Invite Mentor", select a default user who is marked as a mentor, send the invite; then sign in as that mentor and accept the invite.
  - Expected: The mentor joins the group and is listed in the member list with a distinct mentor role label (different from regular member).

- [X] FT-12: A mentor can pin important posts and highlight recommended resources in the group space
  - Action: Signed in as a mentor member of a group, pin an existing discussion post, and mark an existing resource/item in the shared space as a recommended resource.
  - Expected: The pinned post appears at the top of the discussion area with a "Pinned" indicator, and the resource appears with a "Recommended"/highlighted indicator visible to all members.

## Constraint

- [ ] CS-01: Profile cannot be saved with required profile fields empty
  - Action: Open profile setup, clear/leave subjects, current level, and preferred study times empty, and attempt to save.
  - Expected: Save is blocked; inline validation messages appear for each empty required field and the profile is not updated.
  - Bug Report:
    - Issue: Missing Form Validation
    - Actual: With no subject selected (all subject toggles off), clicking "Save Changes" was accepted — the toast "Profile updated / Your changes have been saved." appeared and no inline validation message was rendered for the empty Subjects field. The Academic Level combobox has no empty option (it always holds a value), and preferred study times are saved separately on the Availability tab with their own "Save Availability" button, which also saves an empty list without any error.

- [X] CS-02: Only users marked as mentors are offered in the "Invite Mentor" list
  - Action: From a group, open the "Invite Mentor" picker/search and review the selectable users.
  - Expected: Every listed user is marked as a mentor; default users without the mentor flag are not selectable.

- [X] CS-03: Non-mentor members cannot pin posts or highlight resources
  - Action: Sign in as a regular (non-mentor) member of a group and look for pin and highlight/recommend controls on a discussion post and a shared-space item.
  - Expected: Pin and highlight controls are not available to the regular member (hidden or disabled/rejected), so no post becomes pinned and no resource becomes highlighted.

- [X] CS-04: A member cannot hold duplicate RSVPs for the same session
  - Action: RSVP "Going" to an upcoming session, then change the RSVP (e.g., to "Not Going" and back to "Going"), and check the attendee list.
  - Expected: The member appears only once in the attendee list and the latest RSVP state is the one displayed; no duplicate entries are created.

## Interaction

- [ ] IX-01: Selecting a proposed time slot reveals who marked themselves available
  - Action: In the scheduling view, click/select each proposed time slot that has availability.
  - Expected: The selected slot immediately displays the list/names of members who marked themselves available for that slot, without a page reload; slots with no availability show an empty state.
  - Bug Report:
    - Issue: Missing Feature / Unresponsive Control
    - Actual: There are no proposed time slots to select. The Sessions tab renders a flat list of scheduled sessions (title, "18:00 - 20:00", date, organizer, "1 attending / 0 maybe" counters and Attending/Maybe/Can't make it buttons). No time-slot selector, no availability-per-slot control and no availability name list exists, so nothing can be revealed on selection. The members' weekly availability set in their profiles is never surfaced in the group scheduling view.

- [X] IX-02: Mentor invite shows pending status and updates to a mentor role after acceptance
  - Action: Send a mentor invite from a group, view the invite/member area before acceptance, then accept as the mentor and refresh the view.
  - Expected: Before acceptance the invite shows a pending state; after acceptance the pending state clears and the member list shows the user with the mentor role label.

## Content

- [X] CT-01: Group directory content is study-topic focused and relevant
  - Action: Browse the groups directory and open at least three default groups.
  - Expected: Groups are centered on study subjects (e.g., Calculus, Biology, Literature) with relevant titles and descriptions; no placeholder text (e.g., "lorem ipsum") or off-theme content is displayed.

- [ ] CT-02: Profile content matches the saved profile data and reflects mentor status
  - Action: Open a default user's profile and your own saved profile.
  - Expected: Displayed subjects, current level, and preferred study times match what was saved (accurate labels, no placeholder or mismatched values); profiles marked as mentors show a mentor badge/label, others do not.
  - Bug Report:
    - Issue: Incorrect Content / Mismatched Values
    - Actual: Level and mentor status display correctly (e.g., "Graduate" for the new account; "Mentor" badge shown for Alex Chen and Sarah Martinez after enabling it, absent for others; saved availability "monday 14:00–18:00" is retained in the Availability tab). However, subjects are wrong: after saving "Biology", the profile/members list rendered "Literature" for Alice Tester, and the profile editor shows no subject toggle selected for any user (Alex Chen, Sarah Martinez, Alice Tester) even though their member cards list subjects — so the profile does not display the saved subject values.
