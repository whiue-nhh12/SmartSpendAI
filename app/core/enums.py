from enum import Enum
class Status(str,Enum):
    ACTIVE = "active"
    FINISHED = "finished"
class Role(str,Enum):
    BASIC = "Basic_User"
    VIP = "Vip"
    ADMIN = "Admin"
class Screen_Mode(str,Enum):
    lightmode = "lightmode"
    darkmode = "darkmode"

class Background_Color(str,Enum):
    green = "green"
    black = "black"
    yellow = "yellow"
    red = "red"

class Transaction_Types(str,Enum):
    WITHDRAW = "withdraw"
    DEPOSITE = "Deposite"