# EPIC FHIR Simulation API

This Simulation API responds with synthetic patient data in FHIR format.

A full patient data JSON can be generated locally by running `python collate_jsons.py`

---
## How to Use

- Run `pip install -r requirements.txt` to install required packages (recommend using [venv](https://docs.python.org/3/library/venv.html))
- Run `python collate_jsons.py` to build a singular patient data JSON from Patient JSONs in `Synthea/` Directory
- Run `python main.py` to start Simulation API (Flask API Server)

## API Endpoints

- [Postman](https://www.postman.com/) recommended for API queries
- Flask Server found locally at `http://127.0.0.1:5000/`
- Retrieve specific Patient data = `http://127.0.0.1:5000/api/v1/patient/<patient_id>`

## Sample Patient ID and Request

- Sample ID: `d667bfac-fdc8-4e16-baea-ca11513bf2da`
- Sample Request: `http://127.0.0.1:5000/api/v1/patient/d667bfac-fdc8-4e16-baea-ca11513bf2da`
