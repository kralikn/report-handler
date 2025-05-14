from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

router = APIRouter(prefix="/report", tags=["report"])


@router.post("/upload")
async def upload_report(report: UploadFile = File(...)):

    # 1) Ellenőrizzük a MIME-típust
    if (
        report.content_type
        != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        raise HTTPException(
            status_code=400, detail="Érvénytelen típus, kérlek .xlsx fájlt tölts fel."
        )

    # 2) Beolvassuk a feltöltött fájl tartalmát
    contents = await report.read()
    try:
        df = pd.read_excel(BytesIO(contents), engine="openpyxl")
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Nem sikerült beolvasni az Excel-fájlt: {e}"
        )

    # 3) Példa: visszaküldjük a beolvasott sorok számát és az oszlopneveket
    return {
        "message": "Sikeres report feldolgozás",
        "rows": len(df),
        "columns": df.columns.tolist(),
    }
