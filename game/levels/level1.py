import asyncio
import mechanics as mech


SCREEN_WIDTH = mech.SCREEN_WIDTH
SCREEN_HEIGHT = mech.SCREEN_HEIGHT
BG_COLOR = mech.BG_COLOR
TEXT_COLOR = mech.TEXT_COLOR


async def run_level(screen):
    return await mech.run_level(
        screen,
        level_name="Level 1",
        background_color=BG_COLOR,
        text_color=TEXT_COLOR,
    )