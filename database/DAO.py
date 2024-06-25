from database.DB_connect import DBConnect
from model.prodotto import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getBrand():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.Product_brand as brand
from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(row["brand"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(brand):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gp.*
from go_products gp 
where gp.Product_brand =%s"""

        cursor.execute(query,(brand,))

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(anno, id1, id2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count(distinct t1.r1) as peso
from (select gds.Retailer_code as r1,gds.`Date` as d1 
from go_daily_sales gds 
where gds.Product_number =%s and year(gds.`Date`)=%s )as t1, (select gds.Retailer_code as r2,gds.`Date` as d2
from go_daily_sales gds 
where gds.Product_number =%s and year(gds.`Date`)=%s ) as t2
where t1.r1=t2.r2 and t1.d1=t2.d2

                        """

        cursor.execute(query, (id1, anno, id2, anno,))

        for row in cursor:
            result = row["peso"]

        cursor.close()
        conn.close()
        return result