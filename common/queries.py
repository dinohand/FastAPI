from typing import final

# 쿼리문 모음
QUERIES_STR : final[str]= {
    """실행하고자 하는 쿼리문을 반환한다
       예) QUERIES_STR[데이베이명][테이블 액션]
    """
    "oracle": {
        "tableSelect":"select table from oracle",
        "tableUpdate":"update table from oracle",
        "tableInsert":"Insert table from oracle",
    },
    "sqlite":{
        "tableSelect":"select table from sqlite",
        "tableUpdate":"update table from sqlite",
        "tableInsert":"Insert table from sqlite",
    }
}

# print(QUERIES_STR["oracle"]["tableUpdate"])