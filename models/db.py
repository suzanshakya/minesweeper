# -*- coding: utf-8 -*- 

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db = db) # and store sessions and tickets there
else:                                         # else use a normal relational database
    db = DAL('sqlite://storage.sqlite')       # if not, use SQLite or other DB

from gluon.tools import *
service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc

db.define_table('Scores',
    db.Field('player'), # name of the player
    db.Field('level', 'integer'), # 1 for Beginner, 2 for Intermedieate, 3 for Expert
    db.Field('sec', 'integer'), # seconds player took to win
    db.Field('click', 'integer'), # no of click
    db.Field('scored_on', 'datetime', default=request.now) # datetime when the player scored
)
