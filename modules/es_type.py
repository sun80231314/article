# -*- coding: utf-8 -*-
from elasticsearch_dsl import DocType,Date,Keyword,Text,analyzer
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

class ArticleType(DocType):
    title =Text(analyzer="ik_max_word")
    url = Keyword()
    url_object_id = Keyword()
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole111"
        doc_type = "article111"

if __name__ == "__main__":
    ArticleType.init()