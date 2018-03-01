from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()

# ElasticSearch "model" mapping out what fields to index
class MeetingIndex(DocType):
    title = Text()
    slug = Text()
    description = Text()
    committee = Text()
    category = Text()

    class Meta:
        index = 'meeting-index'

# Bulk indexing function, run in shell
def bulk_indexing():
    MeetingIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Meeting.objects.all().iterator()))

# Simple search function
def search(commitee):
    s = Search().filter('term', commitee=commitee)
    response = s.execute()
    return response
