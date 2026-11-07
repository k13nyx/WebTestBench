# Test Result

## Functionality

- [X] FT-01: Dashboard displays the full inventory of smart home devices
  - Action: Open the admin dashboard and read the main device list.
  - Expected: Every default device is listed, each row showing its name, room, device type (e.g. light, thermostat), and current status. No device is missing.

- [X] FT-02: Devices can be viewed grouped by room
  - Action: Select the "By Room" view/grouping option, then expand or select a room such as "Living Room".
  - Expected: All devices assigned to that room are shown under it; devices from other rooms are not shown under that room. Every room present in the data is listed.

- [X] FT-03: Devices can be viewed filtered by device type
  - Action: Use the device type filter and select "Lights" (then repeat with "Thermostats").
  - Expected: Only devices of the selected type are displayed; selecting "Thermostats" shows only thermostats.

- [ ] FT-04: Brightness of a light device can be adjusted and applied
  - Action: Open an online light device and set its brightness to a new valid value (e.g. 40%), then save/apply.
  - Expected: The device's displayed brightness value changes to 40% and persists after re-opening the device.
  - Bug Report:
    - Issue: Setting does not persist (state lost on navigation)
    - Actual: Dragging the "Main Ceiling Light" brightness slider updates the card in place (75% → 55%, and 75% → 70% on a second attempt), but after leaving the Devices page (Dashboard or Rooms) and returning, the value is back to the default "75%". The Dashboard card simultaneously displayed "75%" while the Devices page showed "55%". No save/apply control exists, and localStorage is empty, so the change is never persisted or shared.

- [ ] FT-05: Target temperature of a thermostat can be adjusted and applied
  - Action: Open an online thermostat and change its target temperature to a new valid value (e.g. 22°C), then save/apply.
  - Expected: The thermostat's displayed target temperature updates to 22°C and persists after re-opening the device.
  - Bug Report:
    - Issue: Setting does not persist; also target temperature cannot be entered in °C / values below 60
    - Actual: "Smart Thermostat" target changed in place from 70°F to 82°F, but after navigating away (Dashboard) and back it reverted to "70°F". Additionally the app is °F-only (slider aria-valuemin=60, aria-valuemax=85), so "22°C" cannot be entered — a literal 22 is out of the allowed range.

- [X] FT-06: A schedule can be created for a light
  - Action: Open a light device, choose "Add Schedule", set a time (e.g. 18:00) and an action (turn on), then save.
  - Expected: The new schedule is saved and appears in that device's schedule list with the correct time and action.

- [X] FT-07: A schedule can be created for a thermostat
  - Action: Open a thermostat, choose "Add Schedule", set a time (e.g. 22:00), a target temperature/action, then save.
  - Expected: The new schedule is saved and appears in the thermostat's schedule list with the correct time and target state.

- [X] FT-08: Recent activity shows when each device was last used
  - Action: Open the "Recent Activity" panel on the dashboard.
  - Expected: The panel lists activity entries that include the device name and a last-used time (timestamp or relative time such as "2 hours ago") for default devices.

## Constraint

- [X] CS-01: Status filter "Offline" shows only offline devices
  - Action: Apply the status filter and select "Offline".
  - Expected: Every displayed device has status "Offline"; no online or idle device appears in the list.

- [X] CS-02: Status filter "Idle" shows only idle devices
  - Action: Apply the status filter and select "Idle".
  - Expected: Every displayed device has status "Idle"; no online or offline device appears in the list.

- [X] CS-03: Brightness is restricted to the valid range
  - Action: Open a light device and attempt to set brightness to 150% (and to a negative value), then save.
  - Expected: The out-of-range value is rejected — either blocked from entry or refused on save with a validation message — and the device brightness remains unchanged.

- [ ] CS-04: Incomplete schedules cannot be saved
  - Action: Open "Add Schedule" for a device and attempt to save without specifying a time and without specifying an action/state.
  - Expected: Save is blocked and a validation message is shown; no schedule is added to the device's schedule list.
  - Bug Report:
    - Issue: Missing validation feedback (silent failure)
    - Actual: Clicking "Create Schedule" with Device = "Select a device", Action empty and Time empty produced no validation message of any kind — no inline error text, no toast, no `role="alert"`/`aria-live` content. The dialog simply stayed open and the schedule list stayed at "Active Schedules (4)". Save is blocked, but the user receives no explanation that time/action/device are required (the form inputs have no `required` attribute either).

- [X] CS-05: Settings cannot be changed on an offline device
  - Action: Apply "Offline" filter, open an offline light or thermostat, and attempt to change brightness/target temperature.
  - Expected: The control is disabled or the change is refused with a message indicating the device is offline; the stored value does not change.

## Interaction

- [ ] IX-01: Selecting a device opens its detail and settings panel
  - Action: Click any device row/card in the list.
  - Expected: A detail panel or view for that device opens showing its name, current status, its adjustable settings, and its schedules.
  - Bug Report:
    - Issue: Unresponsive / no detail view for devices
    - Actual: Clicking the "Main Ceiling Light" card (heading and card body) produces no result: URL stays "/devices", no dialog, drawer, or route change occurs (`[role="dialog"]` count = 0). The card has no click handler (cursor: auto, no onclick) and contains only the power switch and brightness slider — there is no per-device detail panel and no per-device schedule list anywhere in the app.

- [X] IX-02: Switching room or device type view updates the list in place
  - Action: Click a different room grouping and then a different device type filter.
  - Expected: The device list refreshes to the new selection without a full page reload, and the currently selected room/type is visibly highlighted as active.

- [ ] IX-03: Saving a schedule gives confirmation feedback
  - Action: Complete and save a valid new schedule for a device.
  - Expected: A confirmation message/notification appears (e.g. "Schedule saved"), and the schedule is immediately visible in the device's schedule list.
  - Bug Report:
    - Issue: Missing confirmation feedback
    - Actual: After saving valid schedules ("Main Ceiling Light / Turn on / 18:00", "Smart Thermostat / Set to 72°F / 22:00", "Desk Lamp / Turn on / 19:30") the new row does appear in the list, but no confirmation message or notification is ever shown. Sampling the full page text at 150 ms/300 ms/600 ms/1200 ms after save showed only the new schedule row and the "Active Schedules (n)" count change; the notification regions ("Notifications (F8)", "Notifications alt+T") and all `[role="status"]`/`[role="alert"]`/`aria-live` nodes remained empty.

- [X] IX-04: Clearing the status filter restores the full device list
  - Action: With "Offline" filter active, clear or deselect the status filter (e.g. select "All").
  - Expected: The full device inventory is shown again, including online and idle devices, and the filter no longer shows "Offline" as active.

## Content

- [X] CT-01: Page heading identifies it as a smart home device admin dashboard
  - Action: Read the dashboard title/heading and main navigation labels.
  - Expected: Text clearly identifies smart home device management (e.g. "Smart Home Devices" / "Device Management"); no template or placeholder branding such as "Lorem" or "Untitled".

- [X] CT-02: Device rows show relevant names, types, and icons
  - Action: Inspect 5 device entries in the list including their icons/images.
  - Expected: Each device has a meaningful name and a type-appropriate icon/image (light icon for lights, thermostat icon for thermostats); no broken images and no placeholder text.

- [X] CT-03: Activity entries reference real devices with readable times
  - Action: Read at least 3 entries in the Recent Activity panel.
  - Expected: Each entry names a device that exists in the device list, describes a real action (e.g. "turned on", "set to 21°C"), and shows a valid readable time; no "undefined", "NaN", or empty values.
