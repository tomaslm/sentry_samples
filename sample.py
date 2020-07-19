import asyncio
import logging
import os

import aiohttp
import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

sentry_sdk.init(os.environ["SENTRY_URL"],
integrations=[AioHttpIntegration()])

async def fetch(session, url):
    async with session.get(url) as response:
        a = 1 / 0
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        logging.info(f"{len(html)=}")

if __name__ == "__main__":
    logging.info("starting")
    asyncio.run(main())
