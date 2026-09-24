from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Mahasiswa(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None
    
db_mahasiswa = {}
    
@app.get("/")
def selamat_datang():
    return {"Selamat Datang di Data mahasiswa"}
    
# POST : TAMBAH DATA MAHASISWA
@app.post("/mahasiswa/{mahasiswa_id}")
async def add_mahasiswa(mahasiswa_id: int, mahasiswa: Mahasiswa):
    if mahasiswa_id in db_mahasiswa:
        return {"error": "mahasiswa sudah ada"}
    
    db_mahasiswa[mahasiswa_id] = mahasiswa.model_dump()
    return {"pesan": "data mahasiswa berhasil ditambahkan", "mahasiswa": db_mahasiswa[mahasiswa_id]}

# TAMPILKAN DATA MAHASISWA
@app.get("/mahasiswa/{mahasiswa_id}")
async def get_mahasiswa(mahasiswa_id: int):
    if mahasiswa_id not in db_mahasiswa:
        raise HTTPException(status_code=404, detail="mahasiswa tidak ditemukan")
    return {"mahasiswa_id": mahasiswa_id, "mahasiswa": db_mahasiswa[mahasiswa_id]}

# UPDATE DATA MAHASISWA
@app.put("/mahasiswa/{mahasiswa_id}")
async def update_mahasiswa(mahasiswa_id: int, mahasiswa: Mahasiswa):
    if mahasiswa_id in db_mahasiswa:
        return {"error": "mahasiswa tidak ditemukan"}
    db_mahasiswa[mahasiswa_id] = mahasiswa.model_dump()
    return {"pesan": "data mahasiswa berhasil diupdate", "mahasiswa": db_mahasiswa[mahasiswa_id]}

# HAPUS DATA MAHASISWA
@app.delete("/mahasiswa/{mahasiswa_id}")
async def delete_mahasiswa(mahasiswa_id: int):
    if mahasiswa_id not in db_mahasiswa:
        return {"error": "mahasiswa tidak ditemukan"}
    deleted_mahasiswa = db_mahasiswa.pop(mahasiswa_id)
    return {"pesan": "mahasiswa berhasil dihapus", "ID mahasiswa": mahasiswa_id, "data dihapus": deleted_mahasiswa}