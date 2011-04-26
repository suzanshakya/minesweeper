# -*- coding: utf-8 -*- 

@service.jsonrpc
def add_score(player, level, sec, click):
    db.Scores.insert(player=player,
                     level=level,
                     sec=sec,
                     click=click)
    return 1

@service.jsonrpc
def get_scores():
    results = []
    for i in xrange(1, 4):
        rows = db(db.Scores.level==i).select(db.Scores.player, db.Scores.sec,
                    orderby=[db.Scores.sec, db.Scores.click],
                    limitby=(0,20))
        results.append([(row.player, row.sec) for row in rows])
    return results

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @service.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()

def index():
    return "helo" 
