# from fastapi import APIRouter
# from app.schemas.retrieval import RetrievalRequest, RetrievalResponse
# from app.services.retrieval_service import retrieve_similar_chunks

# router = APIRouter(tags=["retrieval"])


# @router.post("/retrieve", response_model=RetrievalResponse)
# def retrieve(request: RetrievalRequest):
#     result = retrieve_similar_chunks(
#         query=request.query,
#         k=request.k
#     )
#     return RetrievalResponse(**result)
from fastapi import APIRouter
from app.schemas.retrieval import RetrievalRequest, RetrievalResponse
from app.services.retrieval_service import retrieve_similar_chunks

router = APIRouter(tags=["retrieval"])


@router.post("/retrieve", response_model=RetrievalResponse)
def retrieve(request: RetrievalRequest):
    result = retrieve_similar_chunks(
        query=request.query,
        k=request.k
    )
    return RetrievalResponse(**result)