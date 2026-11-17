# Changelog

## 1.0.0 — 2026-11-16

First release.

- **Touch gestures** turned into the mouse events Escoria already handles:
  - first tap on an item hovers it, the second tap acts;
  - tap on the floor walks, double tap runs;
  - long press is a right click;
  - drag moves the cursor;
  - taps on buttons click right away.
- **Touch targets**: tap slop and a minimum touch area for small buttons,
  both in millimeters, with snapping to the nearest small button.
- **Phone layout** (`layout/room_height`, `layout/bottom_panel`):
  - the room fills the screen;
  - on phones the verb panel becomes a drawer that opens on an item tap
    (object, then verb), with a tab to open it by hand;
  - on tablets the panel stays docked when it fits;
  - menus come back in the full design;
  - dialog options slide up over a translucent backdrop.
- **HUD**: a settings button (opens the pause menu) and a button that
  highlights the room's interactive items, with optional names.
- **Web**: fullscreen and landscape lock on the first touch, and a "turn your
  phone" hint while in portrait.
- **Configurable look**: corner, size, margin, colors, border and icons of the
  HUD buttons, the drawer tab, the highlight marks and the dialog backdrop.
- **Popups**: OptionButton lists (embedded windows) receive touches.
- **Debug**: mouse-as-finger simulation on desktop, a gesture log and an
  on-screen log overlay.
- **`tools/serve_https.py`**: serves a web export over HTTPS on the local
  network, to test on a phone.
