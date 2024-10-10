#!/usr/bin/env python
import tcod

from actions import EscapeAction, MovementAction
from input_handler import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x: int = screen_width // 2
    player_y: int = screen_height // 2

    tileset: tcod.tileset.Tileset = tcod.tileset.load_tilesheet(
        "tileset.png", 32, 9, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    context: tcod.context.Context
    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Rougelike Game",
        vsync=True,
    ) as context:
        root_console: tcod.console.Console = tcod.console.Console(
            screen_width, screen_height, order="F"
        )
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)
            
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
