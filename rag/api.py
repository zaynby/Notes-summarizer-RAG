from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from rag.embedder import embed_text
from rag.vector_store import search, module_stats, count_chunks

app = FastAPI(title="Study Knowledge Base API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str
    module: Optional[str] = None
    top_k: int = 5


class QueryResult(BaseModel):
    text: str
    module: str
    filename: str
    position: str
    label: str
    score: float


class QueryResponse(BaseModel):
    results: list[QueryResult]


class ModuleStat(BaseModel):
    module: str
    chunks: int


class StatsResponse(BaseModel):
    total_chunks: int
    modules: list[ModuleStat]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query_endpoint(req: QueryRequest):
    vec = embed_text(req.question)
    if not vec:
        raise HTTPException(status_code=500, detail="Failed to embed query")
    results = search(vec, top_k=min(req.top_k, 50), module=req.module)
    return QueryResponse(results=[QueryResult(**r) for r in results])


@app.get("/stats", response_model=StatsResponse)
def stats_endpoint():
    return StatsResponse(
        total_chunks=count_chunks(),
        modules=[ModuleStat(**m) for m in module_stats()],
    )
