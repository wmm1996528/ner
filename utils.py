import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    PER = get_PER_entity(tag_seq, char_seq)
    LOC = get_LOC_entity(tag_seq, char_seq)
    CAR = get_CAR_entity(tag_seq, char_seq)
    WAY = get_WAY_entity(tag_seq, char_seq)
    TIME = get_TIME_entity(tag_seq, char_seq)
    return PER, LOC, CAR, WAY, TIME


def get_PER_entity(tag_seq, char_seq):
    try:
        length = len(char_seq)
        PER = []
        for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
            if tag == 'B-PER':
                if 'per' in locals().keys():
                    PER.append(per)
                    del per
                per = char
                if i+1 == length:
                    PER.append(per)
            if tag == 'I-PER':
                per += char
                if i+1 == length:
                    PER.append(per)
            if tag not in ['I-PER', 'B-PER']:
                if 'per' in locals().keys():
                    PER.append(per)
                    del per
                continue
        return PER
    except:
        pass


def get_LOC_entity(tag_seq, char_seq):
    try:
        length = len(char_seq)
        LOC = []
        for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
            if tag == 'B-LOC':
                if 'loc' in locals().keys():
                    LOC.append(loc)
                    del loc
                loc = char
                if i+1 == length:
                    LOC.append(loc)
            if tag == 'I-LOC':
                loc += char
                if i+1 == length:
                    LOC.append(loc)
            if tag not in ['I-LOC', 'B-LOC']:
                if 'loc' in locals().keys():
                    LOC.append(loc)
                    del loc
                continue
        return LOC
    except:
        pass


def get_CAR_entity(tag_seq, char_seq):
    try:
        length = len(char_seq)
        CAR = []
        for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
            if tag == 'B-CAR':
                if 'car' in locals().keys():
                    CAR.append(car)
                    del car
                car = char
                if i+1 == length:
                    CAR.append(car)
            if tag == 'I-CAR':
                car += char
                if i+1 == length:
                    CAR.append(car)
            if tag not in ['I-CAR', 'B-CAR']:
                if 'car' in locals().keys():
                    CAR.append(car)
                    del car
                continue
        return CAR
    except:
        pass


def get_WAY_entity(tag_seq, char_seq):
    try:
        length = len(char_seq)
        WAY = []
        for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
            if tag == 'B-WAY':
                if 'way' in locals().keys():
                    WAY.append(way)
                    del way
                way = char
                if i+1 == length:
                    WAY.append(way)
            if tag == 'I-WAY':
                way += char
                if i+1 == length:
                    WAY.append(way)
            if tag not in ['I-WAY', 'B-WAY']:
                if 'way' in locals().keys():
                    WAY.append(way)
                    del way
                continue
        return WAY
    except:
       pass
def get_TIME_entity(tag_seq, char_seq):
    try:
        length = len(char_seq)
        TIME = []
        for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
            if tag == 'B-TIME':
                if 'time' in locals().keys():
                    TIME.append(time)
                    del time
                time = char
                if i+1 == length:
                    TIME.append(time)
            if tag == 'I-TIME':
                time += char
                if i+1 == length:
                    TIME.append(time)
            if tag not in ['I-TIME', 'B-TIME']:
                if 'time' in locals().keys():
                    TIME.append(time)
                    del time
                continue
        return TIME
    except:
       pass

def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
