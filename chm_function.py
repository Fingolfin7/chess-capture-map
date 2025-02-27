#acm_function.py

import requests, re

def getGamesFromLichess(data):
    BASE_URL = 'https://lichess.org/api/games/user/'
    response = requests.get(BASE_URL + data, timeout=50) # response will time out after 50 seconds
    return response

def write_games(data, user):
    file = open(user +'.pgn', 'wb')
    file.write(data.content)
    file.close


def captureFinder(data):
    captureRegex = re.compile(r'(x([a-hA-H][1-8]))', re.VERBOSE)
    matches = []
    for groups in captureRegex.findall(data):
        matches.append(groups[1])
    return matches

def mateFinder(data):
    # regex pattern to find checkmates e.g. Qxg2# or Qee7# or Rb8#
    captureRegex = re.compile(r'(x?([a-hA-H][1-8])\#)', re.VERBOSE)
    matches = []
    for groups in captureRegex.findall(data):
        matches.append(groups[1])
    return matches

def captureCounter(data):
    '''Returns a dictionary counting captures for each square coordinate'''
    captureCounts = {
    "a8": 0, "b8": 0, "c8": 0, "d8": 0, "e8": 0, "f8":0, "g8": 0, "h8": 0,
    "a7": 0, "b7": 0, "c7": 0, "d7": 0, "e7": 0, "f7":0, "g7": 0, "h7": 0,
    "a6": 0, "b6": 0, "c6": 0, "d6": 0, "e6": 0, "f6":0, "g6": 0, "h6": 0,
    "a5": 0, "b5": 0, "c5": 0, "d5": 0, "e5": 0, "f5":0, "g5": 0, "h5": 0,
    "a4": 0, "b4": 0, "c4": 0, "d4": 0, "e4": 0, "f4":0, "g4": 0, "h4": 0,
    "a3": 0, "b3": 0, "c3": 0, "d3": 0, "e3": 0, "f3":0, "g3": 0, "h3": 0,
    "a2": 0, "b2": 0, "c2": 0, "d2": 0, "e2": 0, "f2":0, "g2": 0, "h2": 0,
    "a1": 0, "b1": 0, "c1": 0, "d1": 0, "e1": 0, "f1":0, "g1": 0, "h1": 0
    }
    for capture in data:
        captureCounts[capture.lower()] += 1
    return captureCounts

