import asyncio
import sys
import uuid
from pathlib import Path

import httpx

URL_BASE = "https://picsum.photos/"


async def download_images(n: int, w: int, h: int) -> None:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        for i in range(n):
            result = await client.get(f"{URL_BASE}/{w}/{h}")
            out = Path(__file__).parent.parent / "images" / f"{w}-{h}--{uuid.uuid4()}.png"
            out.write_bytes(result.content)


def main() -> None:
    asyncio.run(download_images(*map(int, sys.argv[1:4])))


if __name__ == "__main__":
    main()
