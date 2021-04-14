# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:46:45 2021

@author: louis
"""

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    SuperMarket_DB= client['Market_db']
    Produits = SuperMarket_DB['Produits']

    P1 = {"Produit": "Pâtes",
            "Ref": 123,
            "Prix":1,
            }

    P2 = {"Produit": "Eau",
            "Ref": 456,
            "Prix":0.5,
            }

            
    P3 = {"Produit": "Captain Morgan",
            "Ref": 345,
            "Prix":10,
            }

    PN=[P1, P2, P3]
    
    print(Produits)
    print(PN)

    
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    SuperMarket_DB= client['Market_db']
    commandes = SuperMarket_DB['commandes']
    
    C1 = {"com_num": 1,
                 "com_prod": [123, 10],
                    }
    C2 = {"com_num": 2,
                    "com_prod": [123, 9]
                    }
    C3 = {"com_num": 3,
                    "com_prod": [345, 10]
                    }
        
    print(commandes)
    CN=[C1,C2,C3]

    #commandes.insert(Produits)
    
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    SuperMarket_DB= client['Market_db']
    caisses = SuperMarket_DB['caisses']
    
    Caisse_1 = {"com_num": 1,
                 "com_prod": [123, 10],
                    }
    Caisse_2 = {"com_num": 2,
                    "com_prod": [123, 9]
                    }
    Caisse_3 = {"com_num": 3,
                    "com_prod": [345, 10]
                    }
        
    Caisse_N=[Caisse_1,Caisse_2,Caisse_3]
    
    #caisses.insert(Produits)
    print(caisses)
    print(Caisse_N)
    
    
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    SuperMarket_DB= client['Market_db']
    Stock = SuperMarket_DB['Stock']

    Stock_tot={"Stock_tot": [P1, 5, P2, 10, P3, 10000]}
    
    print(Stock_tot)


'''collection_with_newFields = caisse_1.aggregate(
        [
            {
                "$addFields":
                    {
                    "_id": None,
                    "totalReactions": {"$sum": "$com_prod"}
                    }
            }
        ]
    )
    
    
    for agg in collection_with_newFields:
        print(agg)

    print(caisse_1.find_one())   ''' 
    
  