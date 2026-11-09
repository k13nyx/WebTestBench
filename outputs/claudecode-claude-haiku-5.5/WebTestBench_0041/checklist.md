# Test Checklist

## Functionality
- [ ] FT-01: Devices can be viewed grouped by room
  - Action: Open the device dashboard and select the "By Room" view.
  - Expected: Each room heading (e.g., "Living Room") lists its devices, and every device appears under exactly one room.
- [ ] FT-02: Devices can be viewed grouped by device type
  - Action: Select the "By Type" view.
  - Expected: Devices are grouped under type headings (Lights, Thermostats, etc.), and every device appears under its correct type.
- [ ] FT-03: Light brightness can be adjusted and saved
  - Action: Open a light device, drag the "Brightness" slider to 50, click "Save".
  - Expected: Brightness shows 50% and still reads 50% after a page reload.
- [ ] FT-04: Thermostat target temperature can be adjusted and saved
  - Action: Open a thermostat, set "Target Temperature" to 22 using the + / - buttons, click "Save".
  - Expected: Target temperature shows 22°C and still reads 22°C after a page reload.
- [ ] FT-05: A schedule can be created for a light
  - Action: Open "Schedules", click "New Schedule", choose a light, set action "On", time 18:00, days Mon–Fri, click "Save".
  - Expected: The new schedule appears in the schedule list with the chosen light, action, time, and days.
- [ ] FT-06: A schedule can be created for a thermostat
  - Action: Click "New Schedule", choose a thermostat, set target temperature 20°C, time 07:00, days Daily, click "Save".
  - Expected: The new schedule appears in the list with the chosen thermostat, target temperature, time, and days.
- [ ] FT-07: Recent activity records device use
  - Action: Toggle a light's power off, then open the "Recent Activity" panel.
  - Expected: A new top entry shows that light's name, the "Off" action, and the current time.
- [ ] FT-08: Status filter shows only offline devices
  - Action: In the "Status" filter, select "Offline".
  - Expected: Only devices with the "Offline" status are listed, and the count matches the number shown.
- [ ] FT-09: Status filter shows only idle devices
  - Action: In the "Status" filter, select "Idle".
  - Expected: Only devices with the "Idle" status are listed, and the count matches the number shown.

## Constraint
- [ ] CS-01: Brightness outside 0–100 is rejected
  - Action: Enter 150 in the "Brightness" field and click "Save".
  - Expected: Save is blocked, the message "Brightness must be between 0 and 100" appears, and the previous value remains.
- [ ] CS-02: Target temperature outside the allowed range is rejected
  - Action: Enter 50 in the "Target Temperature" field of a thermostat and click "Save".
  - Expected: Save is blocked, a validation message stating the allowed range appears, and the previous value remains.
- [ ] CS-03: A schedule cannot be saved without a device and time
  - Action: Click "New Schedule", leave the device and time empty, click "Save".
  - Expected: Save is blocked, and the message "Device and time are required" appears next to the empty fields.
- [ ] CS-04: Settings of an offline device cannot be changed
  - Action: Open an device with the "Offline" status, attempt to change its brightness or target temperature, and click "Save".
  - Expected: Controls are disabled or Save is rejected with "Device is offline", and the device's setting is unchanged.

## Interaction
- [ ] IX-01: Success message appears after saving a setting
  - Action: Change a light's brightness to 75 and click "Save".
  - Expected: A "Settings saved" toast appears within 1 second and disappears automatically within about 5 seconds.
- [ ] IX-02: Slider value label updates while dragging
  - Action: Press and drag the "Brightness" slider slowly from 0 to 100.
  - Expected: The numeric label beside the slider changes continuously to match the slider position without requiring a save.
- [ ] IX-03: Active status filter is visually highlighted with a count
  - Action: Select the "Offline" status filter.
  - Expected: The "Offline" chip is highlighted as active, and the text "Showing X of Y devices" updates to reflect the filtered count.

## Content
- [ ] CT-01: Device cards show complete data without placeholder text
  - Action: Review every device card in the "By Room" and "By Type" views.
  - Expected: Each card shows a real device name, room, and type; no text such as "undefined", "null", "NaN", "Device 1", or "TBD" appears.
- [ ] CT-02: Last-used timestamps are valid and readable
  - Action: Review the "Last Used" value on several device cards and in "Recent Activity".
  - Expected: Each value is a readable date/time or relative time (e.g., "2 hours ago"), not "Invalid Date", and no value is in the future.
- [ ] CT-03: Status badges match the device's actual status
  - Action: Compare the status badge of an offline device, an idle device, and an online device with the status shown on its detail page.
  - Expected: Each badge reads "Online", "Offline", or "Idle", and matches the status on the detail page.
- [ ] CT-04: Device icons match the device type
  - Action: Review the icons in the "By Type" view for lights and thermostats.
  - Expected: Lights display a light icon and thermostats display a thermostat icon; no icon is broken or missing.