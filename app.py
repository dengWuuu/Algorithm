from AlgorithmWorld import create_app

app = create_app()


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.after_request(after_request)
if __name__ == '__main__':
    app.run('development')