from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict
from dateutil.relativedelta import relativedelta
import calendar


app = FastAPI()


class DepositRequest(BaseModel):
    date: str = Field(..., pattern=r"\d{2}\.\d{2}\.\d{4}", description="Дата заявки в формате dd.mm.YYYY")
    periods: int = Field(..., ge=1, le=60, description="Количество месяцев по вкладу (от 1 до 60)")
    amount: int = Field(..., ge=10000, le=3000000, description="Сумма вклада (от 10,000 до 3,000,000)")
    rate: float = Field(..., ge=1, le=8, description="Процент по вкладу (от 1 до 8)")

def calculate_deposit(date: str, periods: int, amount: int, rate: float) -> Dict[str, float]:
    result = {}
    current_amount = amount
    current_date = datetime.strptime(date, '%d.%m.%Y')
    primary_day = current_date.day
    monthly_rate = rate / 100 / 12  # Месячная процентная ставка

    for _ in range(periods):
        # Рассчитываем доход за месяц
        current_amount += current_amount * monthly_rate
        result[current_date.strftime('%d.%m.%Y')] = round(current_amount, 2)
        # Переходим на следующий месяц
        current_date = current_date + relativedelta(months=1)
        # Проверка корректности установленного дня относительно начального
        if primary_day != current_date.day and calendar.monthrange(current_date.year, current_date.month)[1] > current_date.day:
            current_date = current_date.replace(day=primary_day - max(primary_day - calendar.monthrange(current_date.year, current_date.month)[1], 0))

    return result

@app.post("/calculate", response_model=Dict[str, float])
async def calculate(request: DepositRequest):
    try:
        deposit_result = calculate_deposit(request.date, request.periods, request.amount, request.rate)
        return deposit_result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

