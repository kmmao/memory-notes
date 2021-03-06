# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     context_processors.py  
   Description :  
   Author :       JHao
   date：          2016/11/19
-------------------------------------------------
   Change Activity:
                   2016/11/19: 
-------------------------------------------------
"""
from .models import Article, Category


def sidebar(request):
    rank_article = Article.objects.order_by("-view")[0:7]
    category = Category.objects.all()
    return {
        "rank_article": rank_article,
        "category": category,
    }
