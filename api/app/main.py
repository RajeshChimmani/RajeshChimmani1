from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from .routers import health, advisory, weather, market, pest, profile


app = FastAPI(title="KisanMITRA API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(advisory.router, prefix="/advisory", tags=["advisory"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])
app.include_router(market.router, prefix="/market", tags=["market"])
app.include_router(pest.router, prefix="/pest", tags=["pest"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])

# Minimal static UI at /app
app.mount("/app", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/app/")

