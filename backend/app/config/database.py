from fastapi import Request

async def get_wordle_db(request: Request):
    async with request.app.state.wordle_pool.acquire() as connection:
        yield connection

async def get_books_db(request: Request):
    async with request.app.state.books_pool.acquire() as connection:
        yield connection