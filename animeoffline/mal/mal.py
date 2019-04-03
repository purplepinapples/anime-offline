from animeoffline.mal import *

BASE_TYPES = [
    'anime',
    'manga',
    'person',
    'character',
    'producer',
    'magazine'
    ]

# sets to keep track of discovered vertices
sets = {_type: set() for _type in BASE_TYPES}


def test_jikan():
    try:
        jikan.anime(1)
        utils.wait()
    except requests.exceptions.ConnectionError as connection_failed:
        base_jikan_url = jikan.base.rstrip("{endpoint}/{id}")
        print(f"Could not connect to jikan-rest server at {base_jikan_url}")
        sys.exit(1)


def discover():
    """use the top rated anime as a root for BFS"""
    test_jikan()
    pprint.pprint(sets)
    top_anime = jikan.top(type='anime')["top"]
    utils.wait()
    queues = {_type: set() for _type, s in sets.items()}
    queues["anime"].add(top_anime[0]["mal_id"])
    bfs(queues)


def queues_has_items(queues):
    """helper function for checking if queue still has items"""
    for q in queues.values():
        if len(q):
            return True
    else:
        return False


def pop_item_from_queues(queues):
    """helper function for returning the first item from the queue"""
    for t, q in queues.items():
        for _ in q: # if this queue has more than one item
            return t, q.pop() # pops the first item off the set


def process(_type, resp, queues):
    # add entries we find in resp to relevant queues
    if _type == 'anime':
        pass
    elif _type == 'manga':
        pass
    elif _type == 'person':
        pass
    elif _type == 'character':
        pass
    elif _type == 'producer':
        pass
    elif _type == 'magazine':
        pass
    else:
        raise ValueError(f"Unrecognized request type: {_type}")


def bfs(queues):
    while queues_has_items(queues):
        _type, id = pop_item_from_queues(queues)
        resp = getattr(jikan, _type)(id)
        utils.wait()
        print(resp["title"])
        process(_type, resp, queues)
