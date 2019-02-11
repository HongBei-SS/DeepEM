from __future__ import print_function
import numpy as np
import os

import dataprovider3.emio as emio


# Minnie dataset
minnie_dir = 'minnie/ground_truth/mip1/padded_x512_y512_z0'
minnie_info = {
    'minnie001':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie002':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie002':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie003':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie004':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie005':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie006':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie007':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie008':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'loc': True,
    },
    'minnie009':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie010':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie011':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'minnie012':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'minnie013':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'fld': 'fld.h5',
        'loc': True,
    },
    'minnie014':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'minnie015':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
}


# Basil dataset
basil_dir = 'basil/ground_truth/mip1/padded_x512_y512_z32'
basil_info = {
    'vol001':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.d128.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
    'vol001a':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
    'vol002':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.d128.h5',
        'loc': True,
    },
    'vol002a':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol003':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'loc': True,
    },
    'vol004':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol005':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'loc': True,
    },
    'vol006':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol008':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol011':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
}


# Pinky dataset
pinky_dir = 'pinky/ground_truth/mip1/padded_x512_y512_z32'
pinky_info = {
    'stitched_vol19-vol34':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'stitched_vol40-vol41':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol101':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
    'vol102':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol103':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol104':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol401':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
    'vol501':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.d128.h5',
        'loc': True,
    },
    'vol501a':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'loc': True,
    },
    'vol502':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'mye': 'mye.h5',
        'loc': True,
    },
    'vol503':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
    'vol201':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.d128.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
    'vol201a':{
        'img': 'img.h5',
        'seg': 'seg.h5',
        'msk': 'msk.h5',
        'blv': 'blv.h5',
        'loc': True,
    },
}


def load_data(data_dir, data_ids=None, **kwargs):
    if data_ids is None:
        data_ids = minnie_info.keys() + basil_info.keys() + pinky_info.keys()

    data = dict()
    base = os.path.expanduser(data_dir)

    for data_id in data_ids:
        # Minnie
        if data_id in minnie_info:
            dpath = os.path.join(base, minnie_dir)
            info = minnie_info[data_id]
            data[data_id] = load_dataset(dpath, data_id, info, **kwargs)
        # Basil
        if data_id in basil_info:
            dpath = os.path.join(base, basil_dir)
            info = basil_info[data_id]
            data[data_id] = load_dataset(dpath, data_id, info, **kwargs)
        # Pinky
        if data_id in pinky_info:
            dpath = os.path.join(base, pinky_dir)
            info = pinky_info[data_id]
            data[data_id] = load_dataset(dpath, data_id, info, **kwargs)

    return data


def load_dataset(dpath, tag, info, class_keys=[], **kwargs):
    assert len(class_keys) > 0
    dset = dict()

    # Image
    dname = tag[:-1] if tag[-1] == 'a' else tag
    fpath = os.path.join(dpath, dname, info['img'])
    print(fpath)
    dset['img']  = emio.imread(fpath).astype('float32')
    dset['img'] /= 255.0

    # Mask
    if dname == 'stitched_vol19-vol34':
        fpath = os.path.join(dpath, dname, 'msk_train.h5')
        print(fpath)
        dset['msk_train'] = emio.imread(fpath).astype('uint8')
        fpath = os.path.join(dpath, dname, 'msk_val.h5')
        print(fpath)
        dset['msk_val'] = emio.imread(fpath).astype('uint8')
    else:
        fpath = os.path.join(dpath, dname, info['msk'])
        print(fpath)
        dset['msk'] = emio.imread(fpath).astype('uint8')

    # Segmentation
    if 'aff' in class_keys or 'long' in class_keys:
        fpath = os.path.join(dpath, dname, info['seg'])
        print(fpath)
        dset['seg'] = emio.imread(fpath).astype('uint32')

    # Myelin
    if 'mye' in class_keys:
        if 'mye' in info:
            fpath = os.path.join(dpath, dname, info['mye'])
            print(fpath)
            mye = emio.imread(fpath).astype('uint8')
        else:
            mye = np.zeros(dset['img'].shape, dtype='uint8')
        dset['mye'] = mye

    # Blood vessel
    if 'blv' in class_keys:
        if 'blv' in info:
            fpath = os.path.join(dpath, dname, info['blv'])
            print(fpath)
            blv = emio.imread(fpath).astype('uint8')
        else:
            blv = np.zeros(dset['img'].shape, dtype='uint8')
        dset['blv'] = blv

    # Fold mask
    if 'fld' in info:
        fpath = os.path.join(dpath, dname, info['fld'])
        print(fpath)
        fld = emio.imread(fpath).astype('uint8')
        if 'msk' in dset:
            dset['msk'][fld > 0] = 0
        if 'msk_train' in dset:
            dset['msk_train'][fld > 0] = 0
        if 'msk_val' in dset:
            dset['msk_val'][fld > 0] = 0

    # Additoinal info
    dset['loc'] = info['loc']

    return dset
