All testing is complete. I've verified every checklist item. Key findings: core views, filters, schedules, activity, and clamping work correctly; however, settings adjustments do not persist across navigation (revert to defaults), the empty schedule form gives no validation feedback, and no toast appears on schedule creation.

# Test Result

## Functionality

- [X] FT-01: Dashboard loads and lists all smart home devices
  - Action: Open the admin dashboard.
  - Expected: All default devices are listed, each entry showing device name, assigned room, device type, and current status.

- [X] FT-02: View devices by room
  - Action: Switch to the "By Room" view and select a specific room (e.g., "Living Room").
  - Expected: Only devices assigned to that room are displayed; every shown entry belongs to the selected room.

- [X] FT-03: View devices by device type
  - Action: Switch to the "By Type" view and select a type (e.g., "Lights" or "Thermostats").
  - Expected: Only devices of the selected type are displayed; every shown entry is of that type.

- [ ] FT-04: Adjust a light's brightness
  - Action: Open a default light device, set its brightness to a new value (e.g., 75%), and apply/save.
  - Expected: The device shows the new brightness value (75%) and it persists after saving.
  - Bug Report:
    - Issue: Settings Not Persisted (state resets on navigation)
    - Actual: Brightness can be set and displays the new value in real time (verified values 60%, 75%, 80%, 90% on the card), but there is no save mechanism, and the value does NOT persist: after setting Main Ceiling Light to 80% and navigating to another page (Activity) and back, the card reverted to the default 75%. The Dashboard page simultaneously shows its own copy (75%) while the Devices page shows the changed value (90%) — device state is not shared or retained across routes (confirmed client-side routing, no page reload involved).

- [ ] FT-05: Adjust a thermostat's target temperature
  - Action: Open a default thermostat, set its target temperature to a new value (e.g., 72°F / 22°C), and apply/save.
  - Expected: The thermostat shows the new target temperature and it persists after saving.
  - Bug Report:
    - Issue: Settings Not Persisted (state resets on navigation)
    - Actual: Target temperature can be set and displays the new value immediately (verified 72°F on the Smart Thermostat card), but the value does NOT persist: after navigating away (Activity → Devices), the target reverted to the default 70°F. Identical root cause as FT-04 — no save mechanism and per-page state that resets on route change.

- [X] FT-06: Create a schedule for a light
  - Action: On a light device, create a schedule (e.g., 07:00 AM → "Turn On") and save it.
  - Expected: The schedule is created and listed for that light, showing the configured time and state change.

- [X] FT-07: Create a schedule for a thermostat
  - Action: On a thermostat, create a schedule (e.g., 10:00 PM → set to 68°F / "Heat") and save it.
  - Expected: The schedule is created and listed for that thermostat, showing the configured time and state change.

- [X] FT-08: View recent activity
  - Action: Open the "Recent Activity" section (or a device's activity panel).
  - Expected: Activity entries are listed, each showing the device name and when it was last used (timestamp).

- [X] FT-09: Filter devices by status
  - Action: Apply the "Offline" status filter, then switch to the "Idle" filter.
  - Expected: Each filtered view shows only devices labeled with that status — no devices of other statuses appear.

## Constraint

- [X] CS-01: Brightness is limited to the valid range
  - Action: Attempt to set a light's brightness outside 0–100% (e.g., type 150% or -10%).
  - Expected: The invalid value is rejected or clamped to the 0–100% range; the light never displays an out-of-range brightness.

- [X] CS-02: Target temperature is limited to the valid range
  - Action: Attempt to set a thermostat's target temperature beyond the allowed min–max range (e.g., 200°F or -50°F).
  - Expected: The invalid temperature is rejected or clamped; an out-of-range temperature is never saved or displayed.

- [ ] CS-03: Schedule cannot be saved with empty required fields
  - Action: Open the schedule form for a device, leave a required field empty (e.g., time or state), and click Save/Create.
  - Expected: The schedule is not created; a validation message identifies the missing required field.
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: Clicking "Create Schedule" with all fields empty (no device, no action, no time) does correctly block creation (dialog stays open, schedule count unchanged at 4), but no validation message of any kind appears — no error text in the dialog, no field highlighting, no toast, and no `required`/`aria-required` attributes on the inputs. The submission is silently ignored, so the user gets no indication of what is missing.

- [X] CS-04: Settings controls match the device type
  - Action: Open a light device and a thermostat device; compare their settings controls.
  - Expected: The light exposes brightness (no temperature control) and the thermostat exposes target temperature (no brightness control) — no cross-type settings appear.

## Interaction

- [X] IX-01: Brightness slider updates the value in real time
  - Action: Drag the brightness slider on a light device.
  - Expected: The displayed brightness value updates continuously while dragging, without a page reload.

- [X] IX-02: Active status filter is visually indicated
  - Action: Click a status filter option (e.g., "Offline") and observe the filter control.
  - Expected: The selected filter appears highlighted/active while the other filter options remain unhighlighted.

- [ ] IX-03: Toast confirms schedule creation
  - Action: Save a valid schedule for a device.
  - Expected: A success toast/notification appears (e.g., "Schedule created") confirming the action.
  - Bug Report:
    - Issue: Missing Success Notification
    - Actual: After saving three valid schedules (e.g., Main Ceiling Light "Turn on" 07:00 Mon — schedule was created and listed correctly), no toast or notification ever appeared. The app has a toast container (Notifications region, sonner `<ol>`) but it remained empty; polling for up to 3 seconds after each creation detected no toast elements. Toggling a device power switch also produced no toast, so no confirmation feedback is shown for these actions.

## Content

- [X] CT-01: Device icons match device types
  - Action: Inspect the icon shown for each device in the list.
  - Expected: Every device shows an icon appropriate to its type (e.g., bulb icon for lights, thermometer for thermostats); no missing or mismatched icons.

- [X] CT-02: Activity entries contain relevant, complete details
  - Action: Inspect each entry in the Recent Activity list.
  - Expected: Every entry shows a real device name, the action/state involved, and a valid last-used timestamp — no placeholder or irrelevant text.

- [X] CT-03: Status labels match the device's actual state
  - Action: Compare each device's displayed status label with its underlying state (e.g., against its last-used activity info).
  - Expected: Labels come from the expected status set (e.g., On/Active, Off, Idle, Offline), are spelled correctly, and are consistent with the device's real state.

---

**Test summary:** 14 passed, 4 failed. Core viewing/filtering (rooms, types, status), schedule creation, activity logging, input clamping (brightness 0–100%, temperature 60–85°F), type-appropriate controls and icons, and real-time slider feedback all work as expected. The failures cluster around state and feedback: device settings do not persist across page navigation (each page holds its own default-initialized copy of device state, and changes are silently discarded on route change), the schedule form provides no validation messaging for empty required fields, and no success toast is displayed when a schedule is created.