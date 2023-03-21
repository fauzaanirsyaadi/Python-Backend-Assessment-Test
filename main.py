import datetime
from typing import List, Dict, Union
from fastapi import FastAPI
import json

app = FastAPI()

# Create an empty JSON file to store customer data
with open("customer_data.json", "w") as f:
    json.dump({}, f)

# Load customer data from JSON file
def load_data() -> Dict[str, Dict[str, str]]:
    with open("customer_data.json", "r") as f:
        data = json.load(f)
    return data

# Save customer data to JSON file
def save_data(data: Dict[str, Dict[str, str]]) -> None:
    with open("customer_data.json", "w") as f:
        json.dump(data, f)

# Check if a given nik or no_hp is already used by another customer
def is_existing_customer(nik: str, no_hp: str) -> bool:
    data = load_data()
    for customer in data.values():
        if customer["nik"] == nik or customer["no_hp"] == no_hp:
            return True
    return False

# Generate a new account number for a new customer
def generate_account_number() -> str:
    data = load_data()
    max_account_number = 0
    for customer in data.values():
        account_number = int(customer["no_rekening"])
        if account_number > max_account_number:
            max_account_number = account_number
    new_account_number = str(max_account_number + 1).zfill(6)
    return new_account_number

# Register a new customer
@app.post("/daftar")
def register_customer(customer: Dict[str, str]) -> Dict[str, str]:
    nik = customer["nik"]
    no_hp = customer["no_hp"]
    if is_existing_customer(nik, no_hp):
        return {"remark": "NIK atau nomor HP sudah digunakan"}
    new_account_number = generate_account_number()
    customer["no_rekening"] = new_account_number
    customer["saldo"] = 0
    customer["mutasi"] = []
    data = load_data()
    data[new_account_number] = customer
    save_data(data)
    return {"no_rekening": new_account_number}

# Deposit money to a customer's account
@app.post("/tabung")
def deposit(customer_info: Dict[str, str]) -> Dict[str, Union[str, int]]:
    account_number = customer_info["no_rekening"]
    nominal = int(customer_info["nominal"])
    data = load_data()
    if account_number not in data:
        return {"remark": "Nomor rekening tidak ditemukan"}
    data[account_number]["saldo"] += nominal
    mutasi = data[account_number]["mutasi"]
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mutasi.append({
        "waktu": waktu,
        "kode_transaksi": "tabung",
        "nominal": nominal
    })
    data[account_number]["mutasi"] = mutasi

    save_data(data)
    return {"saldo": data[account_number]["saldo"]}

# Withdraw money from a customer's account
@app.post("/tarik")
def withdraw(customer_info: Dict[str, str]) -> Dict[str, Union[str, int]]:
    account_number = customer_info["no_rekening"]
    nominal = int(customer_info["nominal"])
    data = load_data()
    if account_number not in data:
        return {"remark": "Nomor rekening tidak ditemukan"}
    if data[account_number]["saldo"] < nominal:
        return {"remark": "Saldo tidak cukup"}
    data[account_number]["saldo"] -= nominal
    mutasi = data[account_number]["mutasi"]
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mutasi.append({
        "waktu": waktu,
        "kode_transaksi": "tarik",
        "nominal": nominal
    })
    save_data(data)
    return {"saldo": data[account_number]["saldo"]}

# Get the current balance of a customer's account
@app.get("/saldo/{no_rekening}")
def check_balance(no_rekening: str) -> Dict[str, Union[str, int]]:
    data = load_data()
    if no_rekening not in data:
        return {"remark": "Nomor rekening tidak ditemukan"}
    return {"saldo": data[no_rekening]["saldo"]}

# Get the transaction history of a customer's account
@app.get("/mutasi/{no_rekening}")
def check_mutasi(no_rekening: str) -> Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]:
    data = load_data()
    if no_rekening not in data:
        return {"remark": "Nomor rekening tidak ditemukan"}
    mutasi = data[no_rekening]["mutasi"]
    result = []
    for transaksi in mutasi:
        result.append({
            "waktu": transaksi["waktu"],
            "kode_transaksi": transaksi["kode_transaksi"],
            "nominal": transaksi["nominal"]
        })
    return {"mutasi": result}
