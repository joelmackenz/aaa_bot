import state
import json
import os

message = {}
awaiting = False

def init_state():
    state.message = {}
    state.awaiting = False
