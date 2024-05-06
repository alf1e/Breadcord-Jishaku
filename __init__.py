import asyncio

from discord.ext import commands
from discord.ext.commands import ExtensionNotLoaded
from jishaku.features.baseclass import Feature
from jishaku.cog import STANDARD_FEATURES, OPTIONAL_FEATURES

import breadcord


class JishakuBreadcord(breadcord.module.ModuleCog):
    def __init__(self, module_id: str, /):
        super().__init__(module_id)

    async def cog_load(self) -> None:
        self.logger.info("Loading Jishaku...")
        try:
            await self.bot.add_cog(CustomManagementCog(bot=self.bot))
            self.logger.info("Jishaku successfully loaded!")
        except Exception as error:
            self.logger.error(f"Failed to load Jishaku: {error}")
            raise error

    async def cog_unload(self) -> None:
        self.logger.info("Unloading Jishaku...")
        try:
            await self.bot.remove_cog("CustomManagementCog")
            self.logger.info("Jishaku successfully unloaded!")
        except ExtensionNotLoaded:
            self.logger.info("Jishaku already unloaded.")
            pass
        except Exception as error:
            self.logger.error(f"Failed to unload Jishaku: {error}")
            raise error


class CustomManagementCog(*STANDARD_FEATURES, *OPTIONAL_FEATURES):
    @Feature.Command(parent="jsk", name="load", aliases=["reload"])
    async def jsk_load(self, ctx: commands.Context):
        "Please use the `module_manager` core module!"
        await ctx.send("Please use the `module_manager` core module!")

    @Feature.Command(parent="jsk", name="unload")
    async def jsk_unload(self, ctx: commands.Context):
        "Please use the `module_manager` core module!"
        await ctx.send("Please use the `module_manager` core module!")


async def setup(bot: breadcord.Bot):
    await bot.add_cog(JishakuBreadcord("breadcord_jishaku"))
