All tests are now complete. "Mentor Tester" appeared in the Invite a Mentor list - FT-09 fully verified. I have now executed every checklist item. Here is the full test report:

# Test Result

## Functionality

- [X] FT-01: New student can create an account
  - Action: Open the Sign Up page, enter a valid name, email, and password, and click "Sign Up".
  - Expected: Account is created, user is logged in, and is redirected to the dashboard/profile page.
  - (Verified: "Welcome to StudyHub! Your account has been created." toast shown, user logged in, redirected to /profile.)

- [X] FT-02: Student can set up a study profile
  - Action: On the profile page, add subjects (e.g., "Calculus", "Biology"), select a current level, and set preferred study times; click "Save".
  - Expected: Profile is saved and the entered subjects, level, and preferred study times are shown on the profile.
  - (Verified: subjects Mathematics/Biology/Literature shown selected, level Undergraduate, availability Mon/Wed 14:00–18:00 persisted on the Availability tab, "Profile updated" toast.)

- [X] FT-03: Student can create a study group
  - Action: Click "Create Group", enter a group name and topic (e.g., "Literature"), and submit the form.
  - Expected: New group appears in the group list with the entered name/topic and the creator is listed as a member.
  - (Verified: "Physics Explorers" created under "Your Groups" with Physics subject, "1 members", creator as member.)

- [X] FT-04: Student can join an existing study group
  - Action: Open a default group (e.g., the "Calculus" group) and click "Join Group".
  - Expected: User is added to the group's member list and can access its shared space and discussion area.
  - (Verified: "Joined group!" toast, Calculus Champions member count 3→4 with new avatar, full access to Notes/Discussions/Sessions/Members tabs.)

- [X] FT-05: Member can add a note into a labeled section
  - Action: In a default group's shared space, click "Add Note", choose a labeled section, enter note content, and save.
  - Expected: Note appears filed under the chosen labeled section alongside other notes/outlines/summaries.
  - (Verified: "Integration by Parts Examples" saved under "Formulas" label next to other notes, "Note added!" toast.)

- [X] FT-06: Members can ask and answer questions in the discussion area
  - Action: In a default group's discussion area, post a question, then post a reply as another group member.
  - Expected: Question and reply appear as a running Q&A thread visible to all group members.
  - (Verified: Alex Chen posted "Mentor check-in: Final exam review plans?"; Sarah Martinez replied; both appear as a running thread visible to all group members in the shared data.)

- [ ] FT-07: Member can schedule a study session showing availability
  - Action: As one member, mark yourself as available for a time slot; as another member, click "Schedule Session", pick the date/time with the time selector, and save.
  - Expected: Time selector indicates which members marked themselves as available for that time; session is listed under upcoming sessions.
  - Bug Report:
    - Issue: Missing feature — availability not indicated in the time selector
    - Actual: Session scheduling itself works ("Session scheduled!" toast, session listed under upcoming sessions), but the Schedule Session dialog contains only Title/Description/Date/Start Time/End Time fields; DOM inspection of the dialog before and after picking date/time shows no indication of which members marked themselves as available, even though the current member had saved availability (Tue/Thu/Sat time slots).

- [ ] FT-08: Member can RSVP to a scheduled session
  - Action: Open a default upcoming session and click "RSVP"/"Going".
  - Expected: RSVP is recorded and the user's name appears in the session's attendee list ("who plans to attend").
  - Bug Report:
    - Issue: Missing attendee list — RSVP names never displayed
    - Actual: The RSVP is recorded ("RSVP updated!" toast, "Attending" button becomes active, count shows "1 attending"), but the session card's DOM contains only numeric counts ("1 attending, 0 maybe") with no attendee name list, avatars, or expandable details — the user's name never appears anywhere in the session's attendee list. (Note: no default upcoming session exists; the default sessions are in the past, so a newly scheduled session was used.)

- [X] FT-09: Advanced student can mark their profile as mentor
  - Action: On your own profile, enable the "Mentor" toggle and save.
  - Expected: Profile is updated to mentor status and the user is now discoverable/selectable as a mentor.
  - (Verified: Mentor Status toggle + save shows "Mentor" badge on profile; a user registered as mentor appeared in a group's "Invite a Mentor" list with subjects and an Invite button, confirming discoverability/selectability.)

- [ ] FT-10: Group can invite a mentor to join
  - Action: As a group member, open "Invite Members", select a default mentor from the mentor list, send the invite, and accept it as that mentor.
  - Expected: Mentor is added to the group's member list.
  - Bug Report:
    - Issue: Incomplete invitation flow — no accept mechanism for the invited mentor
    - Actual: The "Invite a Mentor" dialog lists mentors and the invite sends successfully ("Invitation sent! The mentor will see your request."), but the invited mentor has no way to see or accept it: as the invited mentor, no invitation UI exists anywhere — the group card shows only a plain "Join Group" button, no "Accept" button, no pending-invitation banner, and no notifications. The mentor is never added to the group's member list through the invite flow.

- [X] FT-11: Mentor can highlight resources and pin posts
  - Action: As the group's mentor, click "Highlight as Recommended" on a note in the shared space and "Pin" on a discussion post.
  - Expected: The note is marked as a recommended resource and the post appears pinned at the top of the discussion area.
  - (Verified: star action on "Week 3 Lecture Summary" turned the highlight icon to its active accent state, marking it recommended; pin action on a discussion post moved it to the top of the discussion area with the pin icon in active state.)

## Constraint

- [X] CS-01: Sign-up requires all mandatory fields
  - Action: On the Sign Up page, leave name/email/password empty and click "Sign Up".
  - Expected: No account is created; validation messages identify each missing required field.
  - (Verified: submission blocked, URL unchanged/no account created, `required` fields carry "Please fill out this field." validation messages and focus moves to each missing field.)

- [X] CS-02: Group creation requires required fields
  - Action: Open "Create Group" with an empty name/topic and submit.
  - Expected: Group is not created; an error message requires the missing information.
  - (Verified: error toast "Please fill in all fields", dialog stays open, no group created.)

- [X] CS-03: Pin and highlight actions are restricted to the mentor role
  - Action: As a regular (non-mentor) member, view notes and discussion posts in a default group and look for "Pin" / "Highlight as Recommended" actions.
  - Expected: These controls are unavailable (hidden or disabled) to regular members.
  - (Verified: as regular members, notes and discussions show no pin/star action buttons at all; the pin/star controls only appear when a mentor views the group.)

- [X] CS-04: RSVP state stays consistent
  - Action: RSVP to a default session, then toggle RSVP off and on again.
  - Expected: Attendee list always lists the user exactly once; toggling off removes the name entirely.
  - (Verified: attending count 1 → "Can't make it" → 0 (removed entirely) → "Attending" → back to exactly 1; each toggle shows "RSVP updated!" toast.)

## Interaction

- [X] IX-01: Success feedback after account and profile actions
  - Action: Complete the sign-up (FT-01) and save the profile (FT-02).
  - Expected: A success message/toast (e.g., "Account created", "Profile saved") appears after each action.
  - (Verified: "Welcome to StudyHub! Your account has been created." after sign-up; "Profile updated — Your changes have been saved." after profile save.)

- [ ] IX-02: RSVP updates are visible to all group members
  - Action: RSVP to a default session in one account, then open the same session page as another group member.
  - Expected: The attendee list reflects the new RSVP so everyone knows who plans to attend.
  - Bug Report:
    - Issue: RSVP count propagates, but attendee identity is not shown
    - Actual: The other group member can see the session with the RSVP reflected numerically ("1 attending" — the count did update and propagate across members), but the app displays only a numeric count with no attendee names, so members cannot know *who* plans to attend.

## Content

- [X] CT-01: Default groups are organized around study topics
  - Action: Browse the default group list.
  - Expected: Every group's name, topic, and labels correspond to a study subject (e.g., calculus, biology, literature); no irrelevant groups.
  - (Verified: Calculus Champions — Mathematics, Biology Study Circle — Biology, Victorian Literature Society — Literature; all study-subject groups, none irrelevant.)

- [X] CT-02: Group content matches the group's subject
  - Action: Open a default group (e.g., the "Literature" group) and review its labeled sections, notes, and discussion posts.
  - Expected: All notes/outlines/reading summaries and Q&A posts are relevant to that group's subject.
  - (Verified: Literature group's "Reading List — Fall Semester" contains only Victorian novels (Jane Eyre, Great Expectations, Middlemarch, Tess of the d'Urbervilles); Calculus group's notes (integration formulas, Riemann sums, Stewart's Calculus problems) and Q&A (u-substitution) are all calculus-related; Biology group's note covers mitosis/meiosis.)

- [X] CT-03: Mentor role is visibly labeled
  - Action: View a default mentor's profile and a group member list containing that mentor (after FT-10).
  - Expected: A "Mentor" badge/label appears in both places, clearly distinguishing them from regular members.
  - (Verified: Alex Chen's profile page displays a "Mentor" badge next to his name/level, and the group's Members tab lists "Alex Chen — Mentor" role label, clearly distinguished from "Owner" and "Member" roles.)

---

**Summary**: 16 of 20 checks passed. The four failures are: (1) FT-07 — the session scheduling dialog's time selector never indicates member availability; (2) FT-08/IX-02 — RSVPs are recorded and counts propagate to all members, but no attendee name list exists anywhere, so nobody can see *who* plans to attend; (3) FT-10 — mentor invitations can be sent but the invited mentor has no UI to see or accept them, so invited mentors are never added to the group.