from ctypes import *
import os

dll = cdll.LoadLibrary(os.getcwd()+"/modules/jieba.dll")
cut = dll.cut
cut.argtypes = [c_char_p]
cut.restype = c_char_p

cutall = dll.cutall
cutall.argtypes = [c_char_p]
cutall.restype = c_char_p


def jieba_cut(text):
    text = bytes(text, encoding='utf-8')
    return cut(text).decode().split(' ')[:-1]


def jieba_cutall(text):
    text = bytes(text, encoding='utf-8')
    return cutall(text).decode().split(' ')[:-1]
