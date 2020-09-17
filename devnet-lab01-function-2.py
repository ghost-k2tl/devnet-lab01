# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:02:30 2020

@author: admin
"""


router1 = {"Name": "R1", "IP": "10.10.10.1", "Vendor": "Cisco"}
router2 = {"Name": "R2", "IP": "10.10.11.1", "Vendor": "Juniper"}
router3 = {"Name": "R3", "IP": "10.10.12.1", "Vendor": "Huwei"}
router4 = {"Name": "R4", "IP": "10.10.13.1", "Vendor": "ZTE"}
router5 = {"Name": "R5", "IP": "10.10.14.1", "Vendor": "Erricson"}


list_routers = (router1, router2, router3, router4, router5)


def search_router(_list_routers, _name_router):
    for _i_router in _list_routers:
        if _i_router["Name"] == _name_router:
            print(_i_router)
            
search_router(list_routers,"R2")


