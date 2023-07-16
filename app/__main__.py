from jsonrpcserver import serve, method, Result, Success, Error

from app.vms import get_vms_statistic


@method
def get_vm_statistic_rpc() -> Result:
    try:
        statistics = get_vms_statistic()
    except Exception as e:
        return Error(code=1, message=str(e))
    return Success(statistics)


if __name__ == '__main__':
    serve(port=8000)
