from fastapi import APIRouter

record_router = APIRouter()


@record_router.post('/')
def request_record():
    pass


@record_router.patch('/')
def react_to_request_record():
    pass


@record_router.get('/')
def get_my_required_record_list():
    pass


@record_router.get('/list')
def get_approved_record_list():
    pass
