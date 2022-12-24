from fastapi import APIRouter, Depends

from app.common.security.auth import oauth2_scheme
from app.core.record.payload import Request
from app.core.record.service.charge_record import charge_record

record_router = APIRouter()


@record_router.post('/records')
def request_record(request: Request.ChargeRecord, token: str = Depends(oauth2_scheme)):
    charge_record(token, request)

    # record 생성


@record_router.patch('/')
def approve_to_request_record():
    pass

    # record update
    # schedule update


@record_router.get('/')
def get_my_required_record_list():
    pass

    # query(Record).filter(


@record_router.get('/list')
def get_approved_record_list():
    pass
