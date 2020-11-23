from ikeoClass import Product
import mysql.connector


class BDD():

    @classmethod
    def connect(cls):
        cls.link = mysql.connector.connect(**{
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'ikeo'
            })
        cls.cursor=cls.link.cursor()
        
    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.link.close()

    @classmethod
    def getAllProducts(cls):
        cls.connect()
        productList=[]
        query="SELECT * FROM produits"
        cls.cursor.execute(query)
        liste=cls.cursor.fetchall()
        for row in liste:
            id=int(row[0])
            name=str(row[1])
            ref=str(row[2])
            description=str(row[3])
            aband=str(row[4])
            product=Product(id,name,ref,description,aband)
            productList.append(product)
        cls.close()
        return productList

    @classmethod
    def getFournisseurForProducts(cls):
        products=cls.getAllProducts()
        cls.connect()
        productWithFournisseur=[]
        
        for product in products:
            query="SELECT site_de_production.nom FROM site_de_production JOIN produit_site ON site_de_production.id_site=produit_site.id_site where produit_site.id_produit="+str(product.id)
            cls.cursor.execute(query)
            liste=cls.cursor.fetchall()
            listeFournisseur=[]
            for row in liste:
                name=str(row[0])
                listeFournisseur.append(name)
            product.fournisseur=listeFournisseur
            productWithFournisseur.append(product)

        return productWithFournisseur
