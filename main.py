from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from pathlib import Path
import dataset
import uvicorn
from subprocess import Popen

app = FastAPI()
db = dataset.connect('sqlite:///db.sqlite')

static = {}

for child in Path('static').iterdir():
    if child.is_file():
        static[child.name] = child.read_text()

@app.get('/')
async def home(request: Request):
    return RedirectResponse(url='/query')

@app.get('/query')
async def make_query(request: Request):
    return HTMLResponse(content=static['query.html'], status_code=200)

@app.post('/query')
async def receive_query(contract_id: str = Form(...), network: str = Form(...)):
    print(contract_id, network)
    try:
        print(network)
        return RedirectResponse(url=f'/query/{network}/{contract_id}', status_code=302)
    except ValueError:
        return RedirectResponse(url='/query', status_code=302)

@app.get('/query/{namespace}/{reference}/{contract_id}')
async def display_contract():
    return HTMLResponse(content=static['contract.html'], status_code=200)

@app.post('/query/{namespace}/{reference}/{contract_id}')
async def set_contract(request: Request, namespace: str, reference: str, contract_id: str):
    form_data = dict(await request.form())

    table = db[f'{namespace}:{reference}']
    table.upsert(dict(contract_id=contract_id, **form_data), ['contract_id'])

    print(form_data)

    return RedirectResponse(url=f'/query/{namespace}/{reference}/{contract_id}?success=true', status_code=302)


@app.get('/{namespace}/{reference}/{contract_id}')
async def get_contract(namespace: str, reference: str, contract_id: str):
    table = db[f'{namespace}:{reference}']
    contract = table.find_one(contract_id=contract_id)

    if contract:
        return {
            "@context": "https://daostar.org/schemas",
            "type": "DAO",
            "name": contract["dao_name"],
            "description": contract["dao_description"],
            "membersURI": contract["members_uri"],
            "proposalsURI": contract["proposals_uri"],
            "activityLogURI": contract["activity_log_uri"],
            "governanceURI": contract["governance_uri"]
        }
    
    else:
        return {}

if __name__ == '__main__':
    Popen(['python3', '-m', 'https_redirect'])
    uvicorn.run('main:app', host='0.0.0.0', port=443,
        reload=True, reload_dirs=['static'],
        ssl_keyfile='/etc/letsencrypt/live/api.daostar.org/privkey.pem',
        ssl_certfile='/etc/letsencrypt/live/api.daostar.org/fullchain.pem')