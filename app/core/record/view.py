from typing import Union
from datetime import date

from fastapi import APIRouter, Depends, Query

from app.common.security.auth import oauth2_scheme
from app.core.record.payload import Request
from app.core.record.service.charge_record import charge_record
from app.core.record.service.get_approved_list import get_approved_record
from app.core.record.service.my_records import get_my_record
from app.core.record.service.react_record import react_to_request_record

record_router = APIRouter()


@record_router.post('/records')
def request_record(request: Request.ChargeRecord, token: str = Depends(oauth2_scheme)):
    charge_record(token, request)


@record_router.patch('/records')
def react_to_record(request: Request.ReactRecord):
    return react_to_request_record(request)


@record_router.get('/records')
def get_my_required_record_list(token: str = Depends(oauth2_scheme)):
    return get_my_record(token)


@record_router.get('/records/list')
def get_approved_record_list(start_at: date = Query(alias='startAt'), end_at: date = Query(alias='endAt')):
    return get_approved_record(start_at, end_at)
