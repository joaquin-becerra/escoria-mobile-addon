# Escoria Mobile

A Godot 4 addon that makes [Escoria](https://github.com/godot-escoria/escoria-core)
point-and-click adventures playable on phones and tablets.

It sits between the touch screen and Escoria: touch gestures become the mouse
events Escoria and its UIs already handle, so a game needs no code changes.
You add the addon, enable it and set a few Project Settings.

## Features

- **Touch gestures**:

  | Gesture | Becomes |
  |---|---|
  | 1st tap on an item | hover: its name and default verb show, as with a mouse |
  | 2nd tap on the same item | left click: the action |
  | tap on the floor | walk |
  | double tap on the floor | run (double click) |
  | long press | right click |
  | drag | the cursor follows the finger |
  | tap on a button | click right away |

- **Big enough touch targets**: small buttons get a minimum touch area (in
  millimeters, so it's the same on any screen), and a tap near one snaps to it.
- **Phone layout** (optional): the room fills the screen instead of being
  letterboxed with the verb panel below it.
  - On phones the panel becomes a drawer. It opens when you tap an item, so
    you can tap the object first and then the verb, and closes after the
    action. A tab opens and closes it by hand.
  - On tablets, if the panel fits under the room, it stays as designed.
  - Menus (pause, options, save) switch back to the full design while they
    are shown.
  - Dialog options slide up over the bottom of the room on a translucent
    backdrop.
- **HUD buttons**: a gear that opens the pause menu (the same as Esc), and a
  star that highlights the room's interactive items for a few seconds.
- **Web**:
  - the first touch puts the page in fullscreen and locks it to landscape
    (where the browser allows it);
  - a "turn your phone" hint covers the game while the phone is in portrait.
- **Configurable look**: the position, size, colors and icons of everything
  the addon draws.
- Made to work with any Escoria UI; tested with
  [OpenQuest Enhanced](https://github.com/joaquin-becerra/openquest-enhanced)
  (a SCUMM-style 9-verb interface).
- Pure GDScript, no native code.

## Requirements

- Godot 4.7 (it should work with any Godot 4.x that runs Escoria).
- Escoria 1.0 (escoria-core).

## Installation

1. Copy `addons/escoria-mobile` into your game's `addons/` folder.
2. Enable **Escoria Mobile** in Project > Project Settings > Plugins. This
   adds the `EscoriaMobile` autoload and registers the settings.
3. Turn on "Advanced Settings" in Project Settings and adjust the settings
   under `escoria/mobile/` (below).

By default the addon switches itself on with the first touch on the screen,
so on desktop with a mouse the game is unchanged.

### Phone layout

The phone layout needs to know where the room ends and where the panel is.
For a 1280x800 game with a 1280x576 room and the verbs/inventory panel below
it:

```ini
[escoria]

mobile/layout/room_height=576
mobile/layout/bottom_panel="ui/Control/panel_down"
```

- `room_height` is the height of the room area, at the top of the design.
- `bottom_panel` is the panel's node path inside the game scene
  (`escoria.game_scene`).

Without `room_height` (0) the game keeps its letterboxed design, and only the
gestures and the HUD are added.

## Settings

All of them are under `escoria/mobile/` in Project Settings.

### Input

| Setting | Default | |
|---|---|---|
| `enabled` | Auto | Auto (on with the first touch), Always, Never |
| `double_tap_ms` | 300 | max time between the taps of a double tap |
| `long_press_ms` | 500 | press time for a right click |
| `tap_slop_mm` | 3 | finger travel still counted as a tap |
| `min_target_mm` | 9 | minimum touch area of small buttons |
| `two_tap_action` | on | 1st tap shows the item, 2nd acts; off = one tap acts |

### Phone layout

| Setting | Default | |
|---|---|---|
| `layout/room_height` | 0 | room area height in the design; 0 = keep the design letterboxed |
| `layout/bottom_panel` | "" | the panel's node path in the game scene |
| `layout/tab_side` | Right | side of the drawer tab |
| `layout/tab_size` | 88 x 44 | |
| `layout/tab_icon` | (drawn chevron) | an image pointing up; it's flipped when the drawer is open |

### HUD buttons

| Setting | Default | |
|---|---|---|
| `hud` | on | show the gear and star buttons |
| `hud_hint_names` | on | names next to the highlighted items |
| `hud_buttons/corner` | Top left | Top left, Top right, Bottom left, Bottom right (the gear in the corner, the star next to it) |
| `hud_buttons/size` | 64 | button side, in game pixels |
| `hud_buttons/margin` | 12 | from the screen edge and between the buttons |
| `hud_buttons/settings_icon` | (drawn gear) | an image instead of the drawn icon |
| `hud_buttons/highlight_icon` | (drawn star) | an image; tinted with `style/accent` while active |
| `hud_buttons/highlight_seconds` | 3 | how long the items stay highlighted |

The buttons only show while the player can act in the room: not in menus,
cutscenes or dialogs. In a bottom corner they stay above the game's panel and
the drawer tab.

### Style

| Setting | Default | |
|---|---|---|
| `style/background` | dark blue, 85% | buttons and tab |
| `style/foreground` | light grey | icons, borders, the "turn your phone" hint |
| `style/accent` | yellow | the star while active |
| `style/border_width` | 2 | 0 = no border |
| `style/mark_fill` | dark blue, 35% | circle on each highlighted item |
| `style/mark_ring` | dark blue, 90% | its outline |
| `style/mark_radius` | 18 | |
| `style/backdrop` | black, 70% | behind the dialog options when they slide up |

### Web

| Setting | Default | |
|---|---|---|
| `web/fullscreen_on_first_touch` | on | the first touch puts the page in fullscreen |
| `web/landscape` | on | lock landscape in fullscreen; "turn your phone" hint in portrait |

### Debug

| Setting | Default | |
|---|---|---|
| `debug/simulate_with_mouse` | off | desktop: the mouse acts as a finger (not in web exports) |
| `debug/log` | off | print what each gesture became |
| `debug/overlay` | off | the last log lines on screen (useful on a phone) |

To see the phone layout on desktop, turn on `simulate_with_mouse` and give the
window a phone's shape with `display/window/size/window_width_override` and
`window_height_override` (e.g. 650x293).

## Testing on a phone

A Godot web export only runs in a secure context, and plain `http://` counts
as secure only on `localhost`. To open the game from a phone on the same
network, serve the export over HTTPS:

```sh
python3 tools/serve_https.py path/to/web/export [port]
```

It creates a self-signed certificate once, in `~/.cache/escoria-mobile/`, and
prints the address to open, e.g. `https://192.168.0.10:8443/`. The phone's
browser will warn about the certificate: choose Advanced > continue to the
site.

## How it works

- `mobile_input.gd` (the `EscoriaMobile` autoload) reads touches and sends
  synthetic mouse events with `Input.parse_input_event`.
  - Godot's mouse emulation from touch is turned off while the addon is
    active, and so is physics picking: on desktop, picking would keep
    following the real mouse pointer.
  - Hover is driven by calling the same `ESCItem` handlers that picking calls.
- `layout.gd` switches the window's content scale. In the phone layout the
  base size becomes the room, with the "expand" aspect, so the view takes the
  screen's shape. It also moves the panel and lowers the camera's bottom limit
  to the room. It checks the visible buttons to tell menus from dialog
  options.
- `hud.gd` and `rotate_hint.gd` are CanvasLayers drawn in code, with no
  scenes or assets to import.

## Notes

- Fullscreen and orientation lock need a real user gesture, and the
  orientation lock only works in some browsers (Android Chrome). On iPhone
  the "turn your phone" hint is the fallback.
- Games that draw their own effects over the whole design height may need a
  small fix to use the visible view instead. Room transitions made with a
  full-screen overlay are an example.
- With the phone layout, a menu whose buttons all fit in the room area stays
  in the room's scale.
- "Use X with Y" still works the classic way: choose the verb in the drawer,
  then the two objects.

## Contributing

Suggestions, bug reports and pull requests are welcome: open an issue to talk
about an idea or a problem. Reports of games or Escoria UIs that don't work
well with the addon are especially useful.

If you find it useful, you can support its development with a
[donation via PayPal](https://www.paypal.com/donate/?hosted_button_id=AGB8C4H72NQMJ).

## License

MIT, see [LICENSE](LICENSE).
