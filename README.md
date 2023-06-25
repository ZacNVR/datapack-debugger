# Datapack Debugger
A tool to create a debug version of Minecraft data packs. Specifically, it converts player-based target selectors to `@e[tag=fake_player]` in order to debug player functionality.

In order to use the program, run `python datapack-debugger.py <path-to-datapack> [-o <path-to-output-pack>]`. If the `-o` flag is not specified, it will output a pack in the folder `<path-to-datapack>-debug`.
