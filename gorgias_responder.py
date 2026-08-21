from fastapi import FastAPI, HTTPException, Request

import json

app = FastAPI(title="GorgiasGrowth Responder")

with open("orders_mock.json", encoding="utf-8") as f:
    ORDERS = {o["order_id"].upper(): o for o in json.load(f)}

STATUS_MSG = {
    "shipped": "{name}, order {oid} is shipped and arriving in 2 days.",
    "delivered": "{name}, order {oid} was delivered. Enjoy! Returns open for 7 days.",
    "processing": "{name}, your order {oid} is packed and ships today.",
    "delayed": "{name}, sorry — order {oid} is delayed by the courier. Rs. 100 credit applied automatically.",
}


@app.post("/gorgias-webhook")
async def gorgias_webhook(request: Request):
    payload = await request.json()
    message = str(payload.get("message", ""))
    words = [w.strip("!.,?").upper() for w in message.split()]
    oid = next((w for w in words if w.startswith("OD")), None)

    if not oid:
        return {"reply": "Please share your order ID (e.g. OD9001) and I'll check right away."}
    order = ORDERS.get(oid)
    if not order:
        raise HTTPException(status_code=200, detail={"reply": f"Order ID {oid} not found. Please double-check."})
    reply = STATUS_MSG[order["status"]].format(name=order["customer"].split()[0], oid=oid)
    return {"reply": reply, "order": order}


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8077)
