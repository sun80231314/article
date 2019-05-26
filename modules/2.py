# -*- coding: utf-8 -*-
from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer,  Completion, Keyword, Text, Integer
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])


class ArticleType(DocType):
    #伯乐在线文章类型
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    url_object_id = Keyword()
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"


if __name__ == "__main__":
    ArticleType.init()
