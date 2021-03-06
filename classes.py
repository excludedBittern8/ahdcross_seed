from guessit import guessit
from imdb import IMDb, IMDbError
import logging
import re
"""
General Classes
"""


class guessitinfo():
    """
    A class for guessit parse on a file
    """
    def __init__(self,file):
        self.info=guessit(file)
        self.name=""
        self.resolution=""
        self.encode=""
        self.source=""
        self.group=""
        self.season_num=""
        self.season=""
    def set_values(self):
        self.set_name()
        self.set_resolution()
        self.set_season_num()
        self.set_season()
        self.set_group()
        self.set_source()
        self.set_encode()
    def get_info(self):
        return self.info
    def set_name(self):
        self.name=self.get_info().get('title',"")
        try:
            self.name=self.name.lower()
        except:
            pass
    def set_resolution(self):
        self.resolution=self.get_info().get('screen_size',"")
    def set_encode(self):
        self.encode=self.get_info().get('video_codec',"")
    def set_source(self):
        self.source=self.get_info().get('source',"")
        try:
            self.source=self.source.lower()
        except:
            pass
        if self.source== "ultra hd blu-ray" or self.source == "hd-dvd":
            self.source="blu-ray"
    def set_group(self):
        self.group=self.get_info().get('release_group',"")
        if type(self.group)==list:
            self.group=""
        if re.search("\(",self.group)!=None or re.search("\)",self.group)!=None:
            self.group=re.sub("\(","",self.group)
            self.group=re.sub("\)","",self.group)

        if re.search("\[",self.group)!=None or re.search("\]",self.group)!=None:
            self.group=re.sub("\[","",self.group)
            self.group=re.sub("\]","",self.group)        
        try:
            self.group=self.group.lower()
        except:
            pass
    def set_season_num(self):
        self.season_num=self.get_info().get('season',"")
    def set_season(self):
        season_num=self.get_season_num()
        if type(season_num) is list or season_num=="":
            self.season=""
        elif(season_num<10):
            self.season="season " + "0" + str(season_num)
        else:
            self.season="season " + str(season_num)
    def get_season_num(self):
        return self.season_num
    def get_season(self):
        return self.season
    def get_group(self):
        return self.group
    def get_resolution(self):
        return self.resolution
    def get_name(self):
        return self.name
    def get_encode(self):
        return self.encode
    def get_source(self):
        return self.source
class filter(logging.Filter):
    def __init__(self, arguments):
        super(filter, self).__init__()
        self._arguments = arguments

    def filter(self, rec):
        if rec.msg==None:
            return 1
        if type(rec.msg)==dict and rec.msg.get("--api")!=None:
            rec.msg['--api']=="your_apikey"
        if  self._arguments['--api'] in rec.msg:
            rec.msg=re.sub(self._arguments['--api'],"your_apikey",rec.msg)
        return 1
