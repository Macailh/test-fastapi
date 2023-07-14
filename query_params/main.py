from fastapi import FastAPI, params

app = FastAPI()

query_params = params.Query(None, min_length=1, max_length=50)


@app.get("/")
def params(query: str = query_params):
    return query
