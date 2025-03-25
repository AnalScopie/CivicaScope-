
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class IndicatorData(BaseModel):
    territoire: str
    logement_crise: Optional[float]
    taux_chomage_jeunes: Optional[float]
    satisfaction_transport: Optional[float]
    emission_co2: Optional[float]
    note_globale: Optional[float]
    style: Optional[str] = "federateur"

app = FastAPI(title="CivicaScope API")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API CivicaScope - Analyse citoyenne intelligente."}

@app.post("/generer-discours")
def generer_discours(data: IndicatorData):
    try:
        prompt = f"""
Tu es une IA citoyenne chargée de rédiger un discours de style {data.style}.
Voici les données d'un territoire à analyser :

- Taux de chômage des jeunes : {data.taux_chomage_jeunes} %
- Crise du logement : {data.logement_crise} (sur 10)
- Satisfaction transports : {data.satisfaction_transport} / 5
- Émissions de CO2 : {data.emission_co2} t/an
- Note globale citoyenne : {data.note_globale} / 5

Rédige un discours synthétique et percutant de 100 mots maximum, adapté à un public local, en mettant en lumière les problèmes ou les réussites, selon les données.
"""

        discours_simule = {
            "solennel": "Citoyennes, citoyens, notre ville traverse une phase exigeante, mais des indicateurs positifs émergent. La lutte contre le chômage des jeunes reste une priorité, tout comme la réduction de nos émissions.",
            "federateur": "Ensemble, nous avons le pouvoir d'agir. Le taux de chômage des jeunes reste élevé, mais notre énergie collective et les projets locaux montrent que le changement est en marche.",
            "semantique": "Les données révèlent une tension persistante sur le logement et un besoin d’amélioration des transports, mais aussi des progrès en matière environnementale à consolider."
        }

        discours = discours_simule.get(data.style, discours_simule["federateur"])
        return {"territoire": data.territoire, "style": data.style, "discours": discours}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
