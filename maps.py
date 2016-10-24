#!/usr/bin/env python3
# -*- coding: utf-8 -*-

maps = [0,1,2,3,4,5,6,7,8,9,10]
maps[0] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
          ^----D----^
"""
maps[1] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
|         |    o    |          |
|         D    r    D          |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
"""
maps[2] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |          |
|  cell   D    r    D          |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
"""
maps[3] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
|         |    o    |  eastern |
|         D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
"""
maps[4] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
"""
maps[5] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
          |         |           
          |  guard  |
          |  room   D 
          |         |
          o----D----o           
"""          
maps[6] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
          |         |           
          |  guard  |----------o 
          |  room   D darkness D   
          |         |----------o                  
          o----D----o           
"""
maps[7] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
          |         |          
          |  guard  |
          |  room   D 
          |         |
          o----D----o           
          |         |
          |  south  | 
          |  room   |
          |         |
          o---------o
"""
maps[8] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
          |         |           
          |  guard  |----------o  
          |  room   D darkness D     
          |         |----------o                  
          o----D----o        
          |         |
          |  south  | 
          |  room   |
          |         |
          o---------o
"""
maps[9] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
          |         |           /^^¨^¨^¨^¨^¨^¨^¨^\
          |  guard  |----------o                  \
          |  room   D darkness D       yard        D  
          |         |----------o                  /
          o----D----o           \_.__.__.__._.__./
          |         |
          |  south  | 
          |  room   |
          |         |
          o---------o
"""
maps[10] = """
           _________
          |         |
          |  your   |
          |  cell   | 
          |         |
o---------^----D----^----------o
|         |    c    |          |
| western |    o    |  eastern |
|  cell   D    r    D   cell   |
|         |    r    |          |
o---------o    i    o----------o
          |    d    |
          |    o    |
          |    r    |
          o----D----o
          |         |           /^^¨^¨^¨^¨^¨^¨^¨^\
          |  guard  |----------o                  \
          |  room   D darkness D       yard        D   __FREEDOM__
          |         |----------o                  /
          o----D----o           \_.__.__.__._.__./
          |         |
          |  south  | 
          |  room   |
          |         |
          o---------o
"""
