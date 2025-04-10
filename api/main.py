from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.utilities.app_response import AppResponse
from api.configurations.configuration import configuration
from api.routes import router as api_router

# INITIALIZE FastAPI APP
app = FastAPI(
    title = "FastAPI with PostgreSQL",
    description = "FastAPI Template",
    version = "1.0.0",
)

# MIDDLEWARE FOR CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTERED ENDPOINTS
app.include_router(api_router)

# ROOT ENDPOINT
@app.get("/", tags=["Root"])
async def root():   
    return AppResponse.send_successful(
        data = None,
        message = "Welcome to the FastAPI Template",
        code = 200
    )

# # RUN THE SERVER
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.main:app",
        port = int(configuration["app"]["port"]),
        reload = True,
    )