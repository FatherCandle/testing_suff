import asyncio
from random import randint
from time import perf_counter
from typing import Any, Awaitable

from req_http import http_get, http_get_sync

# The highest Pokemon id
MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


def get_random_pokemons_sync(count: int):
    result = []
    for _ in range(count):
        result.append(get_random_pokemon_name_sync())
    return result


async def get_random_pokemons(count: int):
    return await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])


async def main() -> None:

    # synchronous call
    time_before = perf_counter()
    result = get_random_pokemons_sync(20)
    print(result)
    print(f"Total time (synchronous): {perf_counter() - time_before}")

    # asynchronous call
    time_before = perf_counter()
    result = await get_random_pokemons(20)
    print(result)
    print(f"Total time (asynchronous): {perf_counter() - time_before}")


asyncio.run(main())
