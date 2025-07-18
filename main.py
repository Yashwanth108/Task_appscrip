from fastapi import FastAPI, Depends, HTTPException
from data_collector import fetch_sector_data
from ai_analyzer import analyze_with_gemini
from utils import format_markdown
from auth import validate_token

app = FastAPI()


# "pharmaceuticals", "technology", "agriculture"
@app.get("/analyze/{sector}")
async def analyze(sector: str, token: str = Depends(validate_token)):
    try:
        # fetching the data of the particular sector 
        raw_data = await fetch_sector_data(sector)

        report = await analyze_with_gemini(raw_data, sector)

        final_result = format_markdown(report)
        with open("final_result.md", "w", encoding="utf-8") as f:
            f.write(f"News for {sector} sector:\n\n")
            f.write(final_result)

        # returns markdown format of the data (user friendly response)
        return {
            "raw_data": raw_data,
            "report": final_result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
