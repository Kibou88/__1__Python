#!/usr/bin/env python3
# countasync.py

import asyncio
import keyboard
async def count():
    if keyboard.read_key() == "p":
        print("Active fonction 1")
    elif keyboard.read_key() == "q":
        print("Active fonction 2")

async def main():
    await asyncio.gather(count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")