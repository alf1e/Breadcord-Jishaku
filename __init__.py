from discord.ext.commands import ExtensionNotLoaded

import breadcord


class JishakuBreadcord(breadcord.module.ModuleCog):
    def __init__(self, module_id: str, /):
        super().__init__(module_id)

    async def cog_load(self) -> None:
        self.logger.info("Loading Jishaku...")
        try:
            await self.bot.load_extension("jishaku")
            self.logger.info("Jishaku successfully loaded!")
        except Exception as error:
            self.logger.error(f"Failed to load Jishaku: {error}")

    async def cog_unload(self) -> None:
        self.logger.info("Unloading Jishaku...")
        try:
            await self.bot.unload_extension("jishaku")
            self.logger.info("Jishaku successfully unloaded!")
        except ExtensionNotLoaded:
            self.logger.info("Jishaku already unloaded.")
            pass
        except Exception as error:
            self.logger.error(f"Failed to unload Jishaku: {error}")


async def setup(bot: breadcord.Bot):
    await bot.add_cog(JishakuBreadcord("breadcord_jishaku"))
