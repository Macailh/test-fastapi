from fastapi import FastAPI, params, Query

app = FastAPI()

query_params_optional = params.Query(None, min_length=1, max_length=50)
query_param_required = params.Query(..., min_length=1, max_length=50)


@app.get("/")
def query_params_test(query: str = query_param_required,
                      optional_query: str = query_params_optional):
    if optional_query is None:
        return {"The first param is": query}
    else:
        return {"The first param is: " + query + " and the second param is: " + optional_query}


@app.get("/query")
def query_param_with_query(query: str = Query(None, min_length=1, max_length=50)):
    return {"query param": query}


@app.get("/query2")
def query_params_validations(query: str = Query(None, min_length=1, max_length=43),
                             query2: str = Query("default", min_length=1, max_length=40)):
    return {"The firs query param is: ": query, "The second query param is: ": query2}
