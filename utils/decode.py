import base64

def image_to_data_url(path):

    prefix = f'data:image/jpg;base64,'
    with open(path, 'rb') as f:
        img = f.read()
    print('returning base 64')
    return prefix + base64.b64encode(img).decode('utf-8')
