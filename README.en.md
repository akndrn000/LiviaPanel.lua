<div align="center">

<img src="assets/en/banner.png" alt="Livia Panel: a mobile panel for Roblox executors" width="100%">

<br>

![Lua](https://img.shields.io/badge/Lua-2C2D72?style=flat-square&logo=lua&logoColor=white)
![Roblox](https://img.shields.io/badge/Roblox_executor-000000?style=flat-square&logo=roblox&logoColor=white)
![Mobile](https://img.shields.io/badge/Mobile-friendly-7c5cff?style=flat-square)
![MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

[Bahasa Indonesia](README.md) · [English](README.en.md)

**A simple panel for Roblox executors, built for phone screens.**
Five features in one panel. One Lua file, no dependencies.

[Try it now](#try-it-now) ·
[Features](#features) ·
[How to use](#how-to-use) ·
[Controls](#controls) ·
[Customization](#customization) ·
[Privacy](#privacy-and-security) ·
[Limitations](#known-limitations) ·
[Contributing](#contributing)

</div>

---

## Overview

Mobile executors usually give you a text box and small buttons that are easy to hit by accident while dragging. Livia Panel puts Speed, Jump, Fly, Ghost, and Player ESP into one panel with ON/OFF buttons and number boxes, all from a single Lua file.

Three principles guide the panel:

- **One file, one panel.** Copy one file into your executor and press Execute. No dependencies, no extra setup.
- **Safe to touch.** Buttons only fire on a short tap. A drag of more than 10 px moves the panel, so dragging never toggles a feature on or off.
- **Clean on close.** The `X` button turns off every feature, disconnects every listener, and removes the panel. Running the script again does not create a duplicate panel.

## Try it now

Three steps from zero to a running panel:

1. **Copy** the contents of [`LiviaPanel.lua`](LiviaPanel.lua) into your executor (for example, Delta).
2. Press **Execute**. The **LIVIA PANEL** window appears on screen.
3. Type a number in the box, then press **ON** on the feature you want.

> [!WARNING]
> Using scripts in games can violate Roblox's Terms of Use and put your account at risk of penalties. Read [Known limitations](#known-limitations) before using it.

## Preview

<p align="center">
  <img src="assets/preview.png" alt="Livia panel preview" width="360">
</p>

<p align="center"><sub>The panel is 300×342, each row is 46 tall, and text is size 14, so it is comfortable to tap on a phone. Values in the image are examples.</sub></p>

## Features

| | |
|---|---|
| **Speed** | Walk speed. Number + ON/OFF. Default 50, returns to 16 when OFF. |
| **Jump** | Jump height. Number + ON/OFF. Default 100, returns to 50 when OFF. |
| **Fly** | Flight. The number is the fly speed (default 60). The character hovers when the joystick is released. |
| **Ghost** | Walk through walls (noclip). ON/OFF. |
| **ESP Player** | Other players are visible through walls with a red Highlight and a white outline. ON/OFF. |
| **Tap, not drag** | Buttons only fire on a short tap. A drag of more than 10 px moves the panel. |
| **Drag from anywhere** | The panel can be dragged from the header, the background, a row, or directly from a button. |
| **Values apply live** | Number boxes can be changed while a feature is ON and take effect immediately. |
| **Minimize** | The `-` button shrinks the panel into a draggable **L** bubble. |
| **Clean close** | The `X` button turns off every feature and removes the panel. Running the script again does not create a duplicate panel. |

## How to use

1. **Open** a Roblox game and launch your executor (for example, Delta).
2. **Copy** the contents of [`LiviaPanel.lua`](LiviaPanel.lua) into the executor and press **Execute**, or use loadstring:

   ```lua
   loadstring(game:HttpGet("https://raw.githubusercontent.com/USERNAME/REPO/main/LiviaPanel.lua"))()
   ```

   Replace `USERNAME` and `REPO` with your own account and repository name.
3. **Type a number** in the Speed, Jump, or Fly box if you want a different starting value.
4. **Press ON** on the feature you want. Press OFF to turn it off.
5. For **Fly**, move the joystick to go forward. While moving, aim the camera up or down to rise or descend.
6. Press `-` to hide the panel, or `X` to close it completely.

> [!TIP]
> If the game pulls your speed or jump back, lower the number. Smaller values trigger anti-cheat less often.

> [!NOTE]
> The panel is placed in `CoreGui`, so your executor must allow access to it.

## Controls

| Button | Function |
|---|---|
| `ON` / `OFF` | Turns the feature on that row on or off. |
| Number box | Sets the value (Speed, Jump, Fly). Input that is not a number, or a negative number, is reverted to the previous value. |
| `-` | Collapses the panel into the **L** bubble. |
| **L** (bubble) | Opens the panel again. |
| `X` | Turns off every feature, then closes the panel. |
| Drag | Moves the panel. A drag of more than 10 px counts as dragging, not tapping. |

### Default values

| Feature | Starting value | When turned off |
|---|---|---|
| Speed | 50 | `WalkSpeed` returns to 16 |
| Jump | 100 | `JumpPower` returns to 50 |
| Fly | 60 | Flight stops and the character can walk again |
| Ghost | - | Character collision is switched back on |
| ESP Player | - | All Highlights are removed |

## Customization

Everything is set near the top of `LiviaPanel.lua`.

| What to change | How |
|---|---|
| **Starting values** | Edit the `V` table, for example `local V = {Speed = 50, Jump = 100, Fly = 60}`. |
| **Colors** | Edit the `T` table (`Accent`, `On`, `Off`, `Red`, and so on). |
| **Drag sensitivity** | Change `DRAG_THRESHOLD` (default 10 px). The larger it is, the harder it is to press a button by accident when your touch slides slightly. |
| **Panel size** | Change `Main.Size` and the row height in `createRow`. |

## Privacy and security

- The script **runs on the client side** and sends no data anywhere. There are no network calls inside `LiviaPanel.lua`.
- There are no analytics, trackers, or stored data. Values return to their defaults each time the script is run again.
- Do not run scripts from sources you do not trust. Only run a copy you have read yourself, or one from your own repository.

## Known limitations

- **Anti-cheat.** Some games have anti-cheat. If speed or jump feels pulled back, use a smaller number.
- **Account risk.** Using scripts in games can violate Roblox's Terms of Use and put your account at risk of penalties. Use at your own risk.
- **Fixed restore values.** When OFF, Speed always returns to 16 and Jump to 50, not to the game's own values if it uses different ones.
- **Fly depends on the camera.** Rising and descending only happen while the joystick is moving. Moving backward reverses the rise and descend direction.
- **Nothing is saved.** Values are not remembered after the script is run again.
- **Executor-dependent.** The panel is placed in `CoreGui`, so an executor that does not allow it will not show the panel.
- "Roblox" is a trademark of Roblox Corporation, mentioned only to describe what the script is for. This project is **not affiliated with Roblox**.

## File structure

```
livia-panel/
├── LiviaPanel.lua       # Main script (UI + logic, single file)
├── assets/
│   ├── banner.png       # Banner above the README (1200x630, can be used as a social preview)
│   ├── en/
│   │   └── banner.png   # English banner (used by README.en.md)
│   └── preview.png      # Panel preview
├── LICENSE              # MIT
├── README.md            # Bahasa Indonesia
└── README.en.md         # English
```

`LiviaPanel.lua` is split into blocks:

```
STATE                 S (ON/OFF) and V (values) variables + the color theme T
FEATURE LOGIC         Heartbeat/Stepped for Speed, Jump, Fly, Ghost, ESP
TAP vs DRAG SYSTEM    Tells a drag from a tap (DRAG_THRESHOLD)
UI                    Header, feature rows, minimize/close buttons
CLEANUP               Turns off features, disconnects, removes the GUI
```

## Contributing

Feedback and fixes are welcome through issues or pull requests. Before opening a pull request, test your change in an executor on a real game: toggle each feature on and off, drag the panel, minimize and reopen it, and close it with `X` then run the script again to confirm there is no duplicate panel. Mention the executor and game you used in the PR description.

## License

Released under the [MIT License](LICENSE).

---

<div align="center">
<sub>Livia Panel. A mobile panel for Roblox executors. Runs on the client side.</sub>
</div>
