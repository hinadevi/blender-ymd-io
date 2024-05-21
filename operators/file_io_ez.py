import os
from Crypto.Cipher import AES
from zipfile import ZipFile
from .ymd import *


def file_io_open_ez(context, filepath):
    input_file = filepath
    filename = os.path.splitext(os.path.basename(input_file))[0]
    directory = os.path.dirname(input_file)
    print("Load", filename)
    
    # Decrypt and extract file
    try:
        decrypt_file(key, input_file)    
        zf = ZipFile(directory + '/' + filename + '.zip', 'r')
        zf.extractall(directory + '/' + filename)
        zf.close()
    except:
        pass


    directory2 = os.path.dirname(os.path.abspath(input_file))
    
    # Convert .ymd to .obj
    to_obj(directory + '/' + filename + '/' + filename + '.ymd',directory2 + '/' + filename )

    return {'FINISHED'}

key = b'\x2a\xb5\x11\xf4\x77\x97\x7d\x25\xcf\x6f\x7a\x8a\xe0\x49\xa1\x25'
def decrypt_file(key, input_file, output_file=None, chunksize=64*1024):
    if not output_file:
        output_file = os.path.splitext(input_file)[0] + '.zip'

    filesize = os.path.getsize(input_file)

    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')

    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(cipher.decrypt(chunk))

            outfile.truncate(filesize)