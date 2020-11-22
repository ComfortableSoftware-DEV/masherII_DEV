

from datetime import datetime as DT
from typing import List, Dict, Any, Tuple, TypedDict, TextIO, BinaryIO


CMNTLNLEN = 70
constMakerConstFilename = "constMakerNew.py"
currentTS = DT.strftime(DT.now(), "%Y%m%d.%H%M%S")
DEBUGME = 0x20
FDconstants = None
FDconstMaker = None
mainConstFilename = "constantsNew.py"
NEWTHINGS = True
profileFilename = "currentProfileNew.py"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CMconstantsNew.py 20200819.003108
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-


DBGLVL = "DBGLVL"
WriteAllThings = "WriteAllThings"


DBGPD_: Dict[str, Any] = {
	DBGLVL: 10,  # 0 print nothing to 10 print everything
	WriteAllThings: True,
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CHR_ defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


BKQT = "`"
BKSLSH = "\\"
CBRCE = "}"
CBRKT = "]"
CPAREN = ")"
DBLQT = "\""
DQTSTR = "\""
NEWLINE = "\n"
OBRCE = "{"
OBRKT = "["
OPAREN = "("
TABSTR = "\t"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of STR_ defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

CMNT_MRKR = "# * " + "#*" * 70
EMPTY_STR_LIST = [None, "", '"', '""', "'", "''", "`", "None", "\r", "\n", "\r\n", "\n\r", ]
FOLD0ENDHERE = "# fold here " + "⟰" * 150
FOLD0STARTHERE = "# fold here " + "⟱" * 150
FOLD1ENDHERE = "# fold here " + "⥣" * 150
FOLD1STARTHERE = "# fold here " + "⥥" * 150
FOLD2ENDHERE = "# fold here " + "⨇" * 150
FOLD2STARTHERE = "# fold here " + "⨈" * 150
IMPORTANTSTR = '# * ' + "!-" * 70
INDENTIN = " -=> "
INDENTOUT = " <=- "
INFOSTR = "# * " + "%_" * 70
NTAB = lambda NUM: "\t" * NUM
QT_SET = ['"', "'", "`"]
TRIQT = DBLQT + DBLQT + DBLQT
ZD3STR_ = lambda PFX__, DB__, AX__, FLD__, NM__: f'''"{PFX__}": {OBRCE}"DB_": "{DB__}", "AX_": "{AX__}", "FLD_": "{FLD__}", "NM_": "{NM__}"{CBRCE},'''
_DFLT_CHR_ = "''"
_DFLT_DEC_ = "0.0"
_DFLT_DICT_ = "{}"
_DFLT_DT_ = "'1870-01-01 00:00:01'"
_DFLT_FLOAT_ = "0.0"
_DFLT_INT_ = "0"
_DFLT_LAT_ = "41.0"
_DFLT_LON_ = "-112.0"
_DFLT_POINT_ = "'point(0,0)'"
_DFLT_STR_ = "''"
_EMPTY_DICT_ = {}
_EMPTY_LIST_ = []
_EMPTY_STR_ = ""
_EMPTY_TUPLE_ = ()


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of TYPE defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

ARRAY_ = "list"  # used to maintain wording between apps
AX_ = "AX_"  # action
BB_ = "bbox"  # bounding box in all uses
CHR_ = "varchar"  # character
CM_ = "CM_"  # constMaker related
CONST_ = "CONST_"  # constant in all uses
COORDS_ = "coordinates"  # coordinates in all uses
CRNT_ = "CRNT_"  # current in all uses
DATETIME = "datetime"
DB_ = "DB_"  # database in all uses
DEC = "decimal"
DECIMAL = "decimal"
DFN_ = "DFN_"  # define in all uses
DICT = "dict"
DPB_ = "DPB_"  # destination progress bar
EQ_ = "EQ_"  # earthquake in all uses
EV_ = "EV_"  # event in all uses
FEATCOL_ = "FeatureCollection"
FEATS_ = "features"  # features in all uses
FEAT_ = "Feature"  # feature in all uses
FLD_ = "varchar"  # field name
FLOAT = "float"
GEO_ = "geometry"  # geometry in all uses
GRP_ = "GRP_"  # group in all uses
IDS_ = "ids"  # IDs in all uses
IDX_ = "IDX_"  # index in all uses
ID_ = "id"  # id identification in all uses
INT = "int"
IN_ = "IN_"  # in in all uses
JOB_ = "JOB_"  # job in all uses
KEY = "key"
LCN_ = "LCN_"  # location in all uses
LD_ = "LD_"  # load in all uses
LIST = "list"
LMT_ = "LMT_"  # limit in all uses
LST_ = "LST"  # list in all uses
META_ = "metadata"  # metadata in all uses
NM_ = "NM_"  # name in all uses
NOP_ = "NOP_"  # no operation in all uses
NUM_ = "number"  # number in all uses
OT_ = "output type in all uses, also type of CM output standalone, standaloneClass, etc."
PFX_ = "PFX_"  # prefix in all uses
PKL_ = "PKL_"  # pickle in any use
POINT = "point"  # geometric point
PRODS_ = "products"  # products in all uses
PROD_ = "PROD_"  # product in all uses
PROPS_ = "properties"  # properties in all uses
PT_ = "PT_"  # point
RTN_ = "RTN_"  # return in all uses
SRCS_ = "sources"  # sources in all uses
SRC_ = "source"  # source in all uses
STR_ = "varchar"
TBL_ = "TBL_"  # table in all uses
timeZ_ = "time"  # quick trans for time
TUP = "tuple"
TUPLE = "tuple"
TYPES_ = "types"  # types in all uses
TYPE_ = "type"  # type in all uses
UPD_ = "updated"  # update(d) in all uses
VARCHAR = "varchar"
_n = "_n"  # indirectly new copy of all input
_N = "_N"  # new copy of all input


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * CM_ strings defines
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

CM_AXDFN_str = ''
CM_AXLST_str = ''
CM_CHR_str = ''
CM_CMBLDFN_str = ''
CM_CMDFN_str = ''
CM_ORGD3DICTDICT_: Dict[str, str] = {}
CM_ORGD3LSTDICT_: Dict[str, str] = {}
CM_ORGDFLT_str = ''
CM_ORGDFN_str = ''
CM_ORGDICTCMNT_: Dict[str, str] = {}
CM_ORGDICTLSTDICTCMNT_: Dict[str, str] = {}
CM_ORGDICTLSTDICTOT_: Dict[str, str] = {}
CM_ORGDICTLSTDICTTYPES_: Dict[str, str] = {}
CM_ORGDICTLSTDICT_: Dict[str, str] = {}
CM_ORGDICTLSTLSTDICTCMNT_: Dict[str, str] = {}
CM_ORGDICTLSTLSTDICTOT_: Dict[str, str] = {}
CM_ORGDICTLSTLSTDICTTYPES_: Dict[str, str] = {}
CM_ORGDICTLSTLSTDICT_: Dict[str, str] = {}
CM_ORGDICTOT_: Dict[str, str] = {}
CM_ORGDICTTYPES_: Dict[str, str] = {}
CM_ORGDICT_: Dict[str, str] = {}
CM_ORGLSTCLSDICTCMNT_: Dict[str, str] = {}
CM_ORGLSTCLSDICTOT_: Dict[str, str] = {}
CM_ORGLSTCLSDICTTYPES_: Dict[str, str] = {}
CM_ORGLSTCLSDICT_: Dict[str, str] = {}
CM_ORGLSTDICTCMNT_: Dict[str, str] = {}
CM_ORGLSTDICTOT_: Dict[str, str] = {}
CM_ORGLSTDICTTYPES_: Dict[str, str] = {}
CM_ORGLSTDICT_: Dict[str, str] = {}
CM_ORGTBLDFN_str = ''
CM_ORGTBLDICTCMNT_: Dict[str, str] = {}
CM_ORGTBLDICTOT_: Dict[str, str] = {}
CM_ORGTBLDICTTYPES_: Dict[str, str] = {}
CM_ORGTBLDICT_: Dict[str, str] = {}
CM_ORGTBLnoWRTLST_str = ''
CM_ORGTBLTUPDICTCMNT_: Dict[str, str] = {}
CM_ORGTBLTUPDICTOT_: Dict[str, str] = {}
CM_ORGTBLTUPDICTTYPES_: Dict[str, str] = {}
CM_ORGTBLTUPDICT_: Dict[str, str] = {}
CM_ORGTUPDICTDICTCMNT_: Dict[str, str] = {}
CM_ORGTUPDICTDICTOT_: Dict[str, str] = {}
CM_ORGTUPDICTDICTTYPES_: Dict[str, str] = {}
CM_ORGTUPDICTDICT_: Dict[str, str] = {}
CM_ORGTUPDICTTUPDICTCMNT_: Dict[str, str] = {}
CM_ORGTUPDICTTUPDICTOT_: Dict[str, str] = {}
CM_ORGTUPDICTTUPDICTTYPES_: Dict[str, str] = {}
CM_ORGTUPDICTTUPDICT_: Dict[str, str] = {}
CM_ORGTUPLSTDICTCMNT_: Dict[str, str] = {}
CM_ORGTUPLSTDICTOT_: Dict[str, str] = {}
CM_ORGTUPLSTDICTTYPES_: Dict[str, str] = {}
CM_ORGTUPLSTDICT_: Dict[str, str] = {}
CM_ORGTUP_DICTCMNT_: Dict[str, str] = {}
CM_ORGTUP_DICTOT_: Dict[str, str] = {}
CM_ORGTUP_DICTTYPES_: Dict[str, str] = {}
CM_ORGTUP_DICT_: Dict[str, str] = {}
CM_ORGTYPE_str = ''
CM_PDCMNT_: Dict[str, str] = {}
CM_PDDFN_str = ''
CM_PD_: Dict[str, str] = {}
CM_PD_str = ''
CM_PODGODICTCMNT_: Dict[str, str] = {}
CM_PODGODICT_: Dict[str, str] = {}
CM_PODGRPDICTCMNT_: Dict[str, str] = {}
CM_PODGRPDICT_: Dict[str, str] = {}
CM_PODPDCMNT_: Dict[str, str] = {}
CM_PODPD_: Dict[str, str] = {}
CM_PODTUPDICTCMNT_: Dict[str, str] = {}
CM_PODTUPDICT_: Dict[str, str] = {}
CM_PODTUPOT_: Dict[str, str] = {}
CM_PODTUPTYPES_: Dict[str, str] = {}
CM_STRDFN_str = ''
CM_STR_str = ''
CM_TYPEDFN_str = ''
CM_VALSTR = ''


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * _D3BLKSTR PFX block returned
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

_D3BLKSTR = lambda PFX__, DB__, AX__, FLD__, NM__: f"""{NTAB(3)}"{PFX__}": {OBRCE}
{NTAB(4)}{FOLD0STARTHERE}
{NTAB(4)}"DB_": "{DB__}",
{NTAB(4)}"AX_": "{AX__}",
{NTAB(4)}"FLD_": "{FLD__}",
{NTAB(4)}"NM_": "{NM__}", {CBRCE},
{NTAB(4)}{FOLD0ENDHERE}"""


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * CMSTR strings
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
CMS_ALL = "all"
CMS_CLASS = "class"
CMS_STANDALONE = "standalone"
CMS_STANDALONECLASS = "standaloneClass"
CMS_STANDALONECLASSPKL = "standalone class plus pkl save/restore/with support"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * CMAX_ stuff
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

CMAX_AX = "CMAX_AX"  # <NM_><AX_><..>
CMAX_CHRDFN = "CMAX_CHRDFN"  # <NM_><AX_><CHR_>
CMAX_CMBL = "CMAX_CMBL"  # <NM_><AX_><VAL_>
CMAX_CMDICTVALEMPTY = "CMAX_CMDICTVALEMPTY"  # <NM_><AX_><TYPE_>
CMAX_CMLSTDFN = "CMAX_CMLSTDFN"  # <NM_><AX_><GRP_><OT_>
CMAX_CMLSTSTR = "CMAX_CMLSTSTR"  # <NM_><AX_><GRP_><VARNM_><STR>
CMAX_CMLSTVAL = "CMAX_CMLSTVAL"  # <NM_><AX_><GRP_><VARNM_><VAL>
CMAX_CMLSTVALEMPTY = "CMAX_CMLSTVALEMPTY"  # <NM_><AX_><TYPE_>
CMAX_CMSTR = "CMAX_CMSTR"  # <NM_><AX_><STR_>
CMAX_CMVAL = "CMAX_CMVAL"  # <NM_><AX_><VAL_>
CMAX_D3DFN = "CMAX_D3DFN"  # <NM_><AX_><GRP_>
CMAX_D3STR = "CMAX_D3STR"  # <NM_><AX_><GRP_><PFX><VAL1><VAL2><VAL3>
CMAX_DICTDFN = "CMAX_DICTDFN"  # <NM_><AX_><GRP_><OT_><TYPE_>
CMAX_DICTLSTDFN = "CMAX_DICTLSTDFN"  # <NM><AX><GRP><OT><TYPE_>
CMAX_DICTLSTSTR = "CMAX_DICTLSTSTR"  # <NM><AX><GRP><VALNM><STR>
CMAX_DICTLSTSTRnoDFN = "CMAX_DICTLSTSTRnoDFN"  # <NM><AX><GRP><VALNM><STR>
CMAX_DICTLSTVAL = "CMAX_DICTLSTVAL"  # <NM><AX><GRP><VALNM><VAL>
CMAX_DICTSTR = "CMAX_DICTSTR"  # <NM_><AX_><GRP_><VARNM_><STR_>
CMAX_DICTSTRnoDFN = "CMAX_DICTSTRnoDFN"  # <NM_><AX_><GRP_><VARNM_><STR_>
CMAX_DICTVAL = "CMAX_DICTVAL"  # <NM_><AX_><GRP_><VARNM_><STR_>
CMAX_LSTDFN = "CMAX_LSTDFN"  # <NM_><AX_><GRP_><OT_><TYPE_>
CMAX_LSTSTR = "CMAX_LSTSTR"  # <NM_><AX_><GRP_><STR_>
CMAX_LSTVAL = "CMAX_LSTVAL"  # <NM_><AX_><GRP_><VAL_>
CMAX_NOP = "CMAX_NOP"  # <NM_><AX_><..>
CMAX_PD = "CMAX_PD"  # <NM_><AX_><VARNM_><VAL_>
CMAX_PODDFN = "CMAX_PODDFN"  # <NM_><AX_><GRP_><OT_><TYPE_>
CMAX_PODSTR = "CMAX_PODSTR"  # <NM_><AX_><GRP_><VARNM_><VAL>
CMAX_PODVAL = "CMAX_PODVAL"  # <NM_><AX_><GRP_><VARNUM_><VAL>
CMAX_STRDFN = "CMAX_STRDFN"  # <NM><AX><STR>
CMAX_TBLDFN = "CMAX_TBLDFN"  # <NM><AX><GRP>
CMAX_TBLFLD = "CMAX_TBLFLD"  # <NM><AX><GRP><TYPE><DFLT>
CMAX_TBLFLDnoDFN = "CMAX_TBLFLDnoDFN"  # <NM><AX><GRP><TYPE><DFLT>
CMAX_TBLFLDnoWRT = "CMAX_TBLFLDnoWRT"  # <NM><AX><GRP><TYPE><DFLT>
CMAX_TUPDFN = "CMAX_TUPDFN"  # <NM><AX><GRP><OT_><TYPE_>
CMAX_TUPDICTDFN = "CMAX_TUPDICTDFN"  # <NM><AX><GRP><OT_><TYPE_>
CMAX_TUPDICTSTR = "CMAX_TUPDICTSTR"  # <NM><AX><GRP><VALNM><STR>
CMAX_TUPDICTVAL = "CMAX_TUPDICTVAL"  # <NM><AX><GRP><VALNM><VAL>
CMAX_TUPSTR = "CMAX_TUPSTR"  # <NM><AX><GRP><VALNM><STR>
CMAX_TUPVAL = "CMAX_TUPVAL"  # <NM><AX><GRP><VALNM><VAL>
CMAX_TYPEDFN = "CMAX_TYPEDFN"  # <NM><AX><TYPE>
CMAX_VALDFN = "CMAX_VALDFN"  # <NM><AX><VAL>


CMAX_LST_: List[str] = [
# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	CMAX_AX,  # <NM_><AX_><..>
	CMAX_CHRDFN,  # <NM_><AX_><CHR_>
	CMAX_CMBL,  # <NM_><AX_><VAL_>
	CMAX_CMDICTVALEMPTY,  # <NM_><AX_><TYPE_>
	CMAX_CMLSTDFN,  # <NM_><AX_><GRP_><OT_>
	CMAX_CMLSTSTR,  # <NM_><AX_><GRP_><VARNM_><STR>
	CMAX_CMLSTVAL,  # <NM_><AX_><GRP_><VARNM_><VAL>
	CMAX_CMLSTVALEMPTY,  # <NM_><AX_><TYPE_>
	CMAX_CMSTR,  # <NM_><AX_><STR_>
	CMAX_CMVAL,  # <NM_><AX_><VAL_>
	CMAX_D3DFN,  # <NM_><AX_><GRP_>
	CMAX_D3STR,  # <NM_><AX_><GRP_><PFX><VAL1><VAL2><VAL3>
	CMAX_DICTDFN,  # <NM_><AX_><GRP_><OT_><TYPE_>
	CMAX_DICTLSTDFN,  # <NM><AX><GRP><OT><TYPE_>
	CMAX_DICTLSTSTR,  # <NM><AX><GRP><VALNM><STR>
	CMAX_DICTLSTSTRnoDFN,  # <NM><AX><GRP><VALNM><STR>
	CMAX_DICTLSTVAL,  # <NM><AX><GRP><VALNM><VAL>
	CMAX_DICTSTR,  # <NM_><AX_><GRP_><VARNM_><STR_>
	CMAX_DICTSTRnoDFN,  # <NM_><AX_><GRP_><VARNM_><STR_>
	CMAX_DICTVAL,  # <NM_><AX_><GRP_><VARNM_><STR_>
	CMAX_LSTDFN,  # <NM_><AX_><GRP_><OT_><TYPE_>
	CMAX_LSTSTR,  # <NM_><AX_><GRP_><STR_>
	CMAX_LSTVAL,  # <NM_><AX_><GRP_><VAL_>
	CMAX_NOP,  # <NM_><AX_><..>
	CMAX_PD,  # <NM_><AX_><VARNM_><VAL_>
	CMAX_PODDFN,  # <NM_><AX_><GRP_><OT_><TYPE_>
	CMAX_PODSTR,  # <NM_><AX_><GRP_><VARNM_><VAL>
	CMAX_PODVAL,  # <NM_><AX_><GRP_><VARNUM_><VAL>
	CMAX_STRDFN,  # <NM><AX><STR>
	CMAX_TBLDFN,  # <NM><AX><GRP>
	CMAX_TBLFLD,  # <NM><AX><GRP><TYPE><DFLT>
	CMAX_TBLFLDnoDFN,  # <NM><AX><GRP><TYPE><DFLT>
	CMAX_TBLFLDnoWRT,  # <NM><AX><GRP><TYPE><DFLT>
	CMAX_TUPDFN,  # <NM><AX><GRP><OT_><TYPE_>
	CMAX_TUPDICTDFN,  # <NM><AX><GRP><OT_><TYPE_>
	CMAX_TUPDICTSTR,  # <NM><AX><GRP><VALNM><STR>
	CMAX_TUPDICTVAL,  # <NM><AX><GRP><VALNM><VAL>
	CMAX_TUPSTR,  # <NM><AX><GRP><VALNM><STR>
	CMAX_TUPVAL,  # <NM><AX><GRP><VALNM><VAL>
	CMAX_TYPEDFN,  # <NM><AX><TYPE>
	CMAX_VALDFN,  # <NM><AX><VAL>
]
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CMBL_ struct
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


CMBL_AX1 = 1
CMBL_CHR2 = 2
CMBL_CMDICTTYPE2 = 2
CMBL_CMLSTTYPE2 = 2
CMBL_CMNT2 = 2
CMBL_CMNT3 = 3
CMBL_CMNT4 = 4
CMBL_CMNT5 = 5
CMBL_CMNT6 = 6
CMBL_CMNT7 = 7
CMBL_CMNT8 = 8
CMBL_D3AX5 = 5
CMBL_D3DB4 = 4
CMBL_D3FLD6 = 6
CMBL_D3PFX3 = 3
CMBL_GRPNM2 = 2
CMBL_NM0 = 0
CMBL_OT3 = 3
CMBL_PDNM2 = 2
CMBL_PDVAL3 = 3
CMBL_STR2 = 2
CMBL_TBLDFLT4 = 4
CMBL_TBLNM2 = 2
CMBL_TBLTYPE3 = 3
CMBL_TPRTYPE4 = 4
CMBL_TYPE2 = 2
CMBL_VAL2 = 2
CMBL_VAL4 = 4
CMBL_VARNM3 = 3


# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * end of CMconstantsNew.py cut 20200819.003108
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of the big list
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!


theBigList: List[Tuple] = [
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	("ARRAY_", CMAX_TYPEDFN, "list", "used to maintain wording between apps",),
	("AX_", CMAX_TYPEDFN, "AX_", "action",),
	("BB_", CMAX_TYPEDFN, "bbox", "bounding box in all uses",),
	("BKQT", CMAX_CHRDFN, "`",),
	("BKSLSH", CMAX_CHRDFN, "\\\\",),
	("BULKMODES_GRP_", CMAX_LSTDFN, "BULKMODESLST", CMS_STANDALONE, "str", "list of modes which will have PROP_ filled and waiting when EQEV__ID is learned",),
	("BULKMODES__day", CMAX_LSTSTR, "BULKMODESLST", "day",),
	("BULKMODES__hour", CMAX_LSTSTR, "BULKMODESLST", "hour",),
	("BULKMODES__month", CMAX_LSTSTR, "BULKMODESLST", "month",),
	("BULKMODES__query", CMAX_LSTSTR, "BULKMODESLST", "query",),
	("BULKMODES__week", CMAX_LSTSTR, "BULKMODESLST", "week",),
	("CBRCE", CMAX_CHRDFN, "}",),
	("CBRKT", CMAX_CHRDFN, "]",),
	("CHR_", CMAX_TYPEDFN, "varchar", "character",),
	("CMAX_AX", CMAX_AX, "<NM_><AX_><..>",),
	("CMAX_CHRDFN", CMAX_AX, "<NM_><AX_><CHR_>",),
	("CMAX_CMBL", CMAX_AX, "<NM_><AX_><VAL_>",),
	("CMAX_CMDICTVALEMPTY", CMAX_AX, "<NM_><AX_><TYPE_>"),
	("CMAX_CMLSTDFN", CMAX_AX, "<NM_><AX_><GRP_><OT_>",),
	("CMAX_CMLSTSTR", CMAX_AX, "<NM_><AX_><GRP_><VARNM_><STR>",),
	("CMAX_CMLSTVAL", CMAX_AX, "<NM_><AX_><GRP_><VARNM_><VAL>",),
	("CMAX_CMLSTVALEMPTY", CMAX_AX, "<NM_><AX_><TYPE_>"),
	("CMAX_CMSTR", CMAX_AX, "<NM_><AX_><STR_>",),
	("CMAX_CMVAL", CMAX_AX, "<NM_><AX_><VAL_>",),
	("CMAX_D3DFN", CMAX_AX, "<NM_><AX_><GRP_>",),
	("CMAX_D3STR", CMAX_AX, "<NM_><AX_><GRP_><PFX><VAL1><VAL2><VAL3>",),
	("CMAX_DICTDFN", CMAX_AX, "<NM_><AX_><GRP_><OT_><TYPE_>",),
	("CMAX_DICTLSTDFN", CMAX_AX, "<NM><AX><GRP><OT><TYPE_>",),
	("CMAX_DICTLSTSTR", CMAX_AX, "<NM><AX><GRP><VALNM><STR>",),
	("CMAX_DICTLSTSTRnoDFN", CMAX_AX, "<NM><AX><GRP><VALNM><STR>",),
	("CMAX_DICTLSTVAL", CMAX_AX, "<NM><AX><GRP><VALNM><VAL>",),
	("CMAX_DICTSTR", CMAX_AX, "<NM_><AX_><GRP_><VARNM_><STR_>",),
	("CMAX_DICTSTRnoDFN", CMAX_AX, "<NM_><AX_><GRP_><VARNM_><STR_>",),
	("CMAX_DICTVAL", CMAX_AX, "<NM_><AX_><GRP_><VARNM_><STR_>",),
	("CMAX_LSTDFN", CMAX_AX, "<NM_><AX_><GRP_><OT_><TYPE_>",),
	("CMAX_LSTSTR", CMAX_AX, "<NM_><AX_><GRP_><STR_>",),
	("CMAX_LSTVAL", CMAX_AX, "<NM_><AX_><GRP_><VAL_>",),
	("CMAX_NOP", CMAX_AX, "<NM_><AX_><..>",),
	("CMAX_PD", CMAX_AX, "<NM_><AX_><VARNM_><VAL_>",),
	("CMAX_PODDFN", CMAX_AX, "<NM_><AX_><GRP_><OT_><TYPE_>",),
	("CMAX_PODSTR", CMAX_AX, "<NM_><AX_><GRP_><VARNM_><VAL>",),
	("CMAX_PODVAL", CMAX_AX, "<NM_><AX_><GRP_><VARNUM_><VAL>",),
	("CMAX_STRDFN", CMAX_AX, "<NM><AX><STR>",),
	("CMAX_TBLDFN", CMAX_AX, "<NM><AX><GRP>",),
	("CMAX_TBLFLD", CMAX_AX, "<NM><AX><GRP><TYPE><DFLT>",),
	("CMAX_TBLFLDnoDFN", CMAX_AX, "<NM><AX><GRP><TYPE><DFLT>",),
	("CMAX_TBLFLDnoWRT", CMAX_AX, "<NM><AX><GRP><TYPE><DFLT>",),
	("CMAX_TUPDFN", CMAX_AX, "<NM><AX><GRP><OT_><TYPE_>",),
	("CMAX_TUPDICTDFN", CMAX_AX, "<NM><AX><GRP><OT_><TYPE_>",),
	("CMAX_TUPDICTSTR", CMAX_AX, "<NM><AX><GRP><VALNM><STR>",),
	("CMAX_TUPDICTVAL", CMAX_AX, "<NM><AX><GRP><VALNM><VAL>",),
	("CMAX_TUPLSTDFN", CMAX_NOP, "<NM><AX><GRP><OT_><TYPE_>",),
	("CMAX_TUPLSTSTR", CMAX_NOP, "<NM><AX><GRP><STR>",),
	("CMAX_TUPLSTVAL", CMAX_NOP, "<NM><AX><GRP><VAL>",),
	("CMAX_TUPSTR", CMAX_AX, "<NM><AX><GRP><VALNM><STR>",),
	("CMAX_TUPVAL", CMAX_AX, "<NM><AX><GRP><VALNM><VAL>",),
	("CMAX_TYPEDFN", CMAX_AX, "<NM><AX><TYPE>",),
	("CMAX_VALDFN", CMAX_AX, "<NM><AX><VAL>",),
	("CMBL_AX1", CMAX_CMBL, 1,),
	("CMBL_CHR2", CMAX_CMBL, 2,),
	("CMBL_CMDICTTYPE2", CMAX_CMBL, 2),
	("CMBL_CMLSTTYPE2", CMAX_CMBL, 2),
	("CMBL_CMNT2", CMAX_CMBL, 2,),
	("CMBL_CMNT3", CMAX_CMBL, 3,),
	("CMBL_CMNT4", CMAX_CMBL, 4,),
	("CMBL_CMNT5", CMAX_CMBL, 5,),
	("CMBL_CMNT6", CMAX_CMBL, 6,),
	("CMBL_CMNT7", CMAX_CMBL, 7,),
	("CMBL_CMNT8", CMAX_CMBL, 8,),
	("CMBL_D3AX5", CMAX_CMBL, 5,),
	("CMBL_D3DB4", CMAX_CMBL, 4,),
	("CMBL_D3FLD6", CMAX_CMBL, 6,),
	("CMBL_D3PFX3", CMAX_CMBL, 3,),
	("CMBL_GRPNM2", CMAX_CMBL, 2,),
	("CMBL_NM0", CMAX_CMBL, 0,),
	("CMBL_OT3", CMAX_CMBL, 3,),
	("CMBL_PDNM2", CMAX_CMBL, 2,),
	("CMBL_PDVAL3", CMAX_CMBL, 3,),
	("CMBL_STR2", CMAX_CMBL, 2,),
	("CMBL_TBLDFLT4", CMAX_CMBL, 4,),
	("CMBL_TBLNM2", CMAX_CMBL, 2,),
	("CMBL_TBLTYPE3", CMAX_CMBL, 3,),
	("CMBL_TPRTYPE4", CMAX_CMBL, 4,),
	("CMBL_TYPE2", CMAX_CMBL, 2,),
	("CMBL_VAL2", CMAX_CMBL, 2,),
	("CMBL_VAL4", CMAX_CMBL, 4,),
	("CMBL_VARNM3", CMAX_CMBL, 3,),
	("CMNT_MRKR", CMAX_VALDFN, '"# * " + "#*" * 70',),
	("CMS_ALL", CMAX_CMSTR, "all",),
	("CMS_CLASS", CMAX_CMSTR, "class",),
	("CMS_STANDALONE", CMAX_CMSTR, "standalone",),
	("CMS_STANDALONECLASS", CMAX_CMSTR, "standaloneClass",),
	("CMS_STANDALONECLASSPKL", CMAX_CMSTR, "standalone class plus pkl save/restore/with support",),
	("CM_", CMAX_TYPEDFN, "CM_", "constMaker related",),
	("CM_AXDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_AXLST_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_CHR_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_CMBLDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_CMDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_ORGD3DICTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGD3LSTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDFLT_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_ORGDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_ORGDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTLSTDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTLSTDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTLSTDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTLSTLSTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTCLSDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTCLSDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTCLSDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTCLSDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGLSTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_ORGTBLDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLnoWRTLST_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_ORGTBLTUPDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLTUPDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLTUPDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTBLTUPDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTTUPDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTTUPDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTTUPDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPDICTTUPDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPLSTDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPLSTDICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPLSTDICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUPLSTDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUP_DICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUP_DICTOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUP_DICTTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTUP_DICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_ORGTYPE_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_PDCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PDDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_PD_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PD_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_PODGODICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODGODICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODGRPDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODGRPDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODPDCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODPD_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODTUPDICTCMNT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODTUPDICT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODTUPOT_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_PODTUPTYPES_", CMAX_CMDICTVALEMPTY, "str, str",),
	("CM_STRDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_STR_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_TYPEDFN_str", CMAX_CMVAL, _DFLT_STR_,),
	("CM_VALSTR", CMAX_CMVAL, _DFLT_STR_,),
	("CNTS_TBL", CMAX_TBLDFN, "CNTS_",),
	("CNTS__EQEVID", CMAX_TBLFLD, "CNTS_", "VARCHAR", _DFLT_STR_,),
	("CNTS__EQEVRID", CMAX_TBLFLD, "CNTS_", "INT", _DFLT_INT_,),
	("CNTS__len", CMAX_TBLFLD, "CNTS_", "INT", _DFLT_INT_,),
	("CNTS__name", CMAX_TBLFLD, "CNTS_", "VARCHAR", _DFLT_STR_,),
	("CNTS__timeR", CMAX_TBLFLDnoWRT, "CNTS_", "DATETIME", _DFLT_DT_,),
	("CNTS__type", CMAX_TBLFLD, "CNTS_", "VARCHAR", _DFLT_STR_,),
	("CNTS__updatedR", CMAX_TBLFLDnoWRT, "CNTS_", "DATETIME", _DFLT_DT_,),
	("CNTS__updatedZ", CMAX_TBLFLD, "CNTS_", "DATETIME", _DFLT_DT_,),
	("CNTS__URL", CMAX_TBLFLD, "CNTS_", "VARCHAR", _DFLT_STR_,),
	("CONST_", CMAX_TYPEDFN, "CONST_", "constant in all uses",),
	("COORDS_", CMAX_TYPEDFN, "coordinates", "coordinates in all uses",),
	("CPAREN", CMAX_CHRDFN, ")",),
	("CRNT_", CMAX_TYPEDFN, "CRNT_", "current in all uses",),
	("D01_GRP_point", CMAX_DICTDFN, "D01_", CMS_STANDALONE, "int, str", "DICT of GEO PT IDX",),
	("D01__depth", CMAX_DICTVAL, "D01_", 2, "PROP__depth",),
	("D01__lat", CMAX_DICTVAL, "D01_", 1, "PROP__lat",),
	("D01__lon", CMAX_DICTVAL, "D01_", 0, "PROP__lon",),
	("D02_GRP_rect", CMAX_DICTDFN, "D02_", CMS_STANDALONE, "int, str", "DICT of GEO BBOX and RECT IDX",),
	("D02__bottom", CMAX_DICTVAL, "D02_", 5, "FILE__BBbottom",),
	("D02__east", CMAX_DICTVAL, "D02_", 3, "FILE__BBeast",),
	("D02__north", CMAX_DICTVAL, "D02_", 4, "FILE__BBnorth",),
	("D02__south", CMAX_DICTVAL, "D02_", 1, "FILE__BBsouth",),
	("D02__top", CMAX_DICTVAL, "D02_", 2, "FILE__BBtop",),
	("D02__west", CMAX_DICTVAL, "D02_", 0, "FILE__BBwest",),
	("D03_GRP_EQEVPROP1", CMAX_DICTDFN, "D03_", CMS_STANDALONE, "str, str", "dictionary translating PROP_ values to EQEV_ values",),
	("D03__EQEVtimeZ", CMAX_DICTVAL, "D03_", "PROP__timeZ", "EQEV__timeZ",),
	("D03__EQEVupdatedZ", CMAX_DICTVAL, "D03_", "PROP__updatedZ", "EQEV__updatedZ",),
	("D3PFX_", CMAX_D3DFN, "PFXD3_",),
	("DATETIME", CMAX_TYPEDFN, "datetime",),
	("DBG_fillPFXOnly", CMAX_PD, "fillPFXOnly", "True",),
	("DBG__DBGLVL", CMAX_PD, "DBGLVL", "10", "0 print nothing to 10 print everything",),
	("DBG__FTS", CMAX_PD, "FTS", 'DT.strftime(DT.now(), "%Y%m%d.%H%M%S")',),
	("DBG__TS", CMAX_PD, "TS", 'DT.strftime(DT.now(), "%Y-%m-%d %H:%M:%S")',),
	("DBG__writeAllThings", CMAX_PD, "WriteAllThings", "True",),
	("DBG__writeNewPFX", CMAX_PD, "writeNewPFX", "True",),
	("DBLQT", CMAX_CHRDFN, '\\"',),
	("DB_", CMAX_TYPEDFN, "DB_", "database in all uses",),
	("DEC", CMAX_TYPEDFN, "decimal",),
	("DECIMAL", CMAX_TYPEDFN, "decimal",),
	("DFN_", CMAX_TYPEDFN, "DFN_", "define in all uses",),
	("DICT", CMAX_TYPEDFN, "dict",),
	("DPB_", CMAX_TYPEDFN, "DPB_", "destination progress bar",),
	("DQTSTR", CMAX_CHRDFN, '\\"',),
	("EMPTY_STR_LIST", CMAX_VALDFN, """[None, "", '"', '""', "'", "''", "`", "None", "\\r", "\\n", "\\r\\n", "\\n\\r", ]""",),
	("EQEV_TBL_", CMAX_TBLDFN, "EQEV_", "earthquake event one per EQ table to rule the others",),
	("EQEV__assocIDs", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__CNTSRIDs", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__GEORIDs", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__ID", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__PRODRIDs", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__PROPRIDs", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__timeR", CMAX_TBLFLDnoWRT, "EQEV_", "DATETIME", _DFLT_DT_,),
	("EQEV__timeZ", CMAX_TBLFLD, "EQEV_", "DATETIME", _DFLT_DT_,),
	("EQEV__updatedR", CMAX_TBLFLDnoWRT, "EQEV_", "DATETIME", _DFLT_DT_,),
	("EQEV__updatedTimesR", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__updatedTimesZ", CMAX_TBLFLD, "EQEV_", "VARCHAR", _DFLT_STR_,),
	("EQEV__updatedZ", CMAX_TBLFLD, "EQEV_", "DATETIME", _DFLT_DT_,),
	("EQ_", CMAX_TYPEDFN, "EQ_", "earthquake in all uses",),
	("EV_", CMAX_TYPEDFN, "EV_", "event in all uses",),
	("FEATCOL_", CMAX_TYPEDFN, "FeatureCollection",),
	("FEATS_", CMAX_TYPEDFN, "features", "features in all uses",),
	("FEAT_", CMAX_TYPEDFN, "Feature", "feature in all uses",),
	("FILE_TBL", CMAX_TBLDFN, "FILE_",),
	("FILE__BBbottom", CMAX_TBLFLD, "FILE_", "DECIMAL", _DFLT_DEC_,),
	("FILE__BBeast", CMAX_TBLFLD, "FILE_", "DECIMAL", _DFLT_DEC_,),
	("FILE__BBnorth", CMAX_TBLFLD, "FILE_", "DECIMAL", _DFLT_DEC_,),
	("FILE__BBsouth", CMAX_TBLFLD, "FILE_", "DECIMAL", _DFLT_DEC_,),
	("FILE__BBtop", CMAX_TBLFLD, "FILE_", "DECIMAL", _DFLT_DEC_,),
	("FILE__BBwest", CMAX_TBLFLD, "FILE_", "DECIMAL", _DFLT_DEC_,),
	("FILE__METAAPI", CMAX_TBLFLD, "FILE_", "VARCHAR", _DFLT_STR_,),
	("FILE__METAcount", CMAX_TBLFLD, "FILE_", "INT", _DFLT_INT_,),
	("FILE__METAlimit", CMAX_TBLFLD, "FILE_", "INT", _DFLT_INT_,),
	("FILE__METAoffset", CMAX_TBLFLD, "FILE_", "INT", _DFLT_INT_,),
	("FILE__METAstatus", CMAX_TBLFLD, "FILE_", "INT", _DFLT_INT_,),
	("FILE__METAtimeZ", CMAX_TBLFLD, "FILE_", "DATETIME", _DFLT_DT_,),
	("FILE__METAtitle", CMAX_TBLFLD, "FILE_", "VARCHAR", _DFLT_STR_,),
	("FILE__METAURL", CMAX_TBLFLD, "FILE_", "VARCHAR", _DFLT_STR_,),
	("FILE__name", CMAX_TBLFLD, "FILE_", "VARCHAR", _DFLT_STR_,),
	("FILE__timeR", CMAX_TBLFLDnoWRT, "FILE_", "DATETIME", _DFLT_DT_,),
	("FILE__timeZ", CMAX_TBLFLD, "FILE_", "DATETIME", _DFLT_DT_,),
	("FILE__type", CMAX_TBLFLD, "FILE_", "VARCHAR", _DFLT_STR_,),
	("FILE__updatedR", CMAX_TBLFLDnoWRT, "FILE_", "DATETIME", _DFLT_DT_,),
	("FILE__updatedZ", CMAX_TBLFLD, "FILE_", "DATETIME", _DFLT_DT_,),
	("FLD_", CMAX_TYPEDFN, "varchar", "field name",),
	("FLOAT", CMAX_TYPEDFN, "float",),
	("FOLD0ENDHERE", CMAX_VALDFN, '"# fold here " + "⟰" * 150',),
	("FOLD0STARTHERE", CMAX_VALDFN, '"# fold here " + "⟱" * 150',),
	("FOLD1ENDHERE", CMAX_VALDFN, '"# fold here " + "⥣" * 150',),
	("FOLD1STARTHERE", CMAX_VALDFN, '"# fold here " + "⥥" * 150',),
	("FOLD2ENDHERE", CMAX_VALDFN, '"# fold here " + "⨇" * 150',),
	("FOLD2STARTHERE", CMAX_VALDFN, '"# fold here " + "⨈" * 150',),
	("GEO_", CMAX_TYPEDFN, "geometry", "geometry in all uses",),
	("getDeetsLST", CMAX_LSTDFN, "getDeets", CMS_STANDALONE, "str", "holds the EQEVID that will be detailed",),
	("GRP_", CMAX_TYPEDFN, "GRP_", "group in all uses",),
	("IDS_", CMAX_TYPEDFN, "ids", "IDs in all uses",),
	("IDX_", CMAX_TYPEDFN, "IDX_", "index in all uses",),
	("ID_", CMAX_TYPEDFN, "id", "id identification in all uses",),
	("IMPORTANTSTR", CMAX_VALDFN, f"""'# * ' + "!-" * {CMNTLNLEN}""",),
	("INDENTIN", CMAX_VALDFN, '" -=> "',),
	("INDENTOUT", CMAX_VALDFN, '" <=- "',),
	("INFOSTR", CMAX_VALDFN, f'''"# * " + "%_" * {CMNTLNLEN}''',),
	("INT", CMAX_TYPEDFN, "int",),
	("IN_", CMAX_TYPEDFN, "IN_", "in in all uses",),
	("JOB_", CMAX_TYPEDFN, "JOB_", "job in all uses",),
	("KEY", CMAX_TYPEDFN, "key",),
	("LCN_", CMAX_TYPEDFN, "LCN_", "location in all uses",),
	("LD_", CMAX_TYPEDFN, "LD_", "load in all uses",),
	("LIST", CMAX_TYPEDFN, "list",),
	("LMT_", CMAX_TYPEDFN, "LMT_", "limit in all uses",),
	("LST_", CMAX_TYPEDFN, "LST", "list in all uses",),
	("META_", CMAX_TYPEDFN, "metadata", "metadata in all uses",),
	("NEWLINE", CMAX_CHRDFN, "\\n",),
	("NM_", CMAX_TYPEDFN, "NM_", "name in all uses",),
	("NOP_", CMAX_TYPEDFN, "NOP_", "no operation in all uses",),
	("NTAB", CMAX_VALDFN, 'lambda NUM: "\\t" * NUM',),
	("NUM_", CMAX_TYPEDFN, "number", "number in all uses",),
	("OBRCE", CMAX_CHRDFN, "{",),
	("OBRKT", CMAX_CHRDFN, "[",),
	("OPAREN", CMAX_CHRDFN, "(",),
	("OT_", CMAX_TYPEDFN, "output type in all uses, also type of CM output standalone, standaloneClass, etc.",),
	("PD01_initPD_", CMAX_TUPDICTDFN, "PD01_", CMS_STANDALONE, "str, str",),
	("PD01__cachePFX", CMAX_TUPDICTSTR, "PD01_", "cachePFX", _DFLT_STR_,),
	("PD01__codeLCN", CMAX_TUPDICTSTR, "PD01_", "codeLCN", _DFLT_STR_,),
	("PD01__CRNTKEY", CMAX_TUPDICTSTR, "PD01_", "CRNTKEY", _DFLT_STR_,),
	("PD01__DFLTAX", CMAX_TUPDICTSTR, "PD01_", "DFLTAX", _DFLT_STR_,),
	("PD01__DFLTDB", CMAX_TUPDICTSTR, "PD01_", "DFLTDB", _DFLT_STR_,),
	("PD01__DFLTFLD", CMAX_TUPDICTSTR, "PD01_", "DFLTFLD", _DFLT_STR_,),
	("PD01__DFLTNM", CMAX_TUPDICTSTR, "PD01_", "DFLTNM", _DFLT_STR_,),
	("PD01__EQEVID", CMAX_TUPDICTSTR, "PD01_", "EQEVID", _DFLT_STR_,),
	("PD01__EQEVRID", CMAX_TUPDICTVAL, "PD01_", "EQEVRID", _DFLT_INT_,),
	("PD01__fileDate", CMAX_TUPDICTSTR, "PD01_", "fileDate", _DFLT_STR_,),
	("PD01__GJfilename", CMAX_TUPDICTSTR, "PD01_", "GJfilename", _DFLT_STR_,),
	("PD01__isNew", CMAX_TUPDICTVAL, "PD01_", "isNew", True,),
	("PD01__mode", CMAX_TUPDICTSTR, "PD01_", "mode", _DFLT_STR_,),
	("PD01__myHash", CMAX_TUPDICTSTR, "PD01_", "myHash", _DFLT_STR_,),
	("PD01__recsSeen", CMAX_TUPDICTVAL, "PD01_", "recsSeen", _DFLT_INT_,),
	("PD01__recsUpd", CMAX_TUPDICTVAL, "PD01_", "recsUpd", _DFLT_INT_,),
	("PD01__SQLDate", CMAX_TUPDICTSTR, "PD01_", "SQLDate", _DFLT_STR_,),
	("PD01__THISAX", CMAX_TUPDICTSTR, "PD01_", "THISAX", _DFLT_STR_,),
	("PD01__THISFILETYPE", CMAX_TUPDICTSTR, "PD01_", "THISFILETYPE", _DFLT_STR_,),
	("PD01__THISPFX", CMAX_TUPDICTSTR, "PD01_", "THISPFX", _DFLT_STR_,),
	("PD01__THISTYPE", CMAX_TUPDICTSTR, "PD01_", "THISTYPE", _DFLT_STR_,),
	("PD01__THISVAL", CMAX_TUPDICTSTR, "PD01_", "THISVAL", _DFLT_STR_,),
	("PD01__TUPfilename", CMAX_TUPDICTSTR, "PD01_", "TUPfilename", _DFLT_STR_,),
	("PD01__URL", CMAX_TUPDICTSTR, "PD01_", "URL", _DFLT_STR_,),
	("PFXD3_GRP_", CMAX_D3DFN, "PFXD3_",),
	("PFXSTACK_GRP_", CMAX_LSTDFN, "PFXSTACK_", CMS_STANDALONE, "str",),
	("PFX_", CMAX_TYPEDFN, "PFX_", "prefix in all uses",),
	("PFX_dyfiCNTSEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents|end_map", "CNTS_", "ENDPRODCNTS", ""),
	("PFX_dyfiCNTSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents|map_key", "", "MAPKEY", ""),
	("PFX_dyfiCNTSSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents|start_map", "PROD_", "STARTCNTS", ""),
	("PFX_dyfiCode", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.code|string", "PROD_", "GETPROD", "PROD__code"),
	("PFX_dyfiDepth", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.depth|string", "PROD_", "GETPROD", "PROD__depth"),
	("PFX_dyfiENDARRAY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi|end_array", "CNTS_", "ENDCNTSARRAY", ""),
	("PFX_dyfiEventSource", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.eventsource|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_dyfigeoMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt|map_key", "", "MAPKEY", ""),
	("PFX_dyfiIndexID", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.indexid|string", "PROD_", "GETPROD", "PROD__indexID"),
	("PFX_dyfiLat", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.latitude|string", "PROD_", "GETPROD", "PROD__lat"),
	("PFX_dyfiLon", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.longitude|string", "PROD_", "GETPROD", "PROD__lon"),
	("PFX_dyfiMag", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.magnitude|string", "PROD_", "GETPROD", "PROD__mag"),
	("PFX_dyfiMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item|map_key", "PROD_", "MAPKEY", ""),
	("PFX_dyfiMaxMMI", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.maxmmi|string", "PROD_", "GETPROD", "PROD__maxmmi"),
	("PFX_dyfiNumResp", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.numResp|string", "PROD_", "GETPROD", "PROD__numResp"),
	("PFX_dyfiPDLClientV", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.pdl-client-version|string", "PROD_", "GETPROD", "PROD__PDLClientV"),
	("PFX_dyfiPfdWgt", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.preferredWeight|number", "PROD_", "GETPROD", "PROD__pfdWgt"),
	("PFX_dyfiPRODPROPSEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties|end_map", "PROD_", "ENDPRODPROPS", ""),
	("PFX_dyfiPROPSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties|map_key", "PROD_", "MAPKEY", ""),
	("PFX_dyfiPROPSSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties|start_map", "PROD_", "STARTPRODPROPS", ""),
	("PFX_dyfiResponseCount", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.num-responses|string", "PROD_", "GETPROD", "PROD__responseCount"),
	("PFX_dyfiSource", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.source|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_dyfiSourceCode", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.eventsourcecode|string", "PROD_", "GETPROD", "PROD__sourceCode"),
	("PFX_dyfiStatus", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.status|string", "PROD_", "GETPROD", "PROD__status"),
	("PFX_dyfiTimeZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.properties.eventtime|string", "PROD_", "GETPROD", "PROD__timeZ"),
	("PFX_dyfiType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.type|string", "PROD_", "GETPROD", "PROD__type"),
	("PFX_dyfiUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.updateTime|number", "PROD_", "GETPROD", "PROD__updatedZ"),
	("PFX_EQEVEND", CMAX_D3STR, "PFXD3_", "features.item|end_map", "", "ENDEQEV", ""),
	("PFX_EQEVID", CMAX_D3STR, "PFXD3_", "features.item.id|string", "EQEV_", "GETEQEV", "EQEV__ID"),
	("PFX_EQEVSTART", CMAX_D3STR, "PFXD3_", "features.item|start_map", "EQEV_", "STARTEQEV", ""),
	("PFX_FEATCOLSTART", CMAX_D3STR, "PFXD3_", "type|string", "", "STARTFEATCOL", ""),
	("PFX_FEATMAPKEY", CMAX_D3STR, "PFXD3_", "features.item|map_key", "", "MAPKEY", ""),
	("PFX_FEATsEND", CMAX_D3STR, "PFXD3_", "features|end_array", "FILE_", "ENDFEATS", ""),
	("PFX_FEATSSTART", CMAX_D3STR, "PFXD3_", "features|start_array", "FILE_", "STARTFEATS", ""),
	("PFX_FEATSTART", CMAX_D3STR, "PFXD3_", "features.item.type|string", "EQEV_", "STARTFEAT", ""),
	("PFX_FILEAPI", CMAX_D3STR, "PFXD3_", "metadata.api|string", "FILE_", "GETFILE", "FILE__METAAPI"),
	("PFX_FILEBBOX", CMAX_D3STR, "PFXD3_", "bbox.item|number", "FILE_", "GETBBOX", ""),
	("PFX_FILEBBOXEND", CMAX_D3STR, "PFXD3_", "bbox|end_array", "FILE_", "ENDBBOX", ""),
	("PFX_FILEBBOXSTART", CMAX_D3STR, "PFXD3_", "bbox|start_array", "FILE_", "STARTBBOX", ""),
	("PFX_FILEcount", CMAX_D3STR, "PFXD3_", "metadata.count|number", "FILE_", "GETFILE", "FILE__METAcount"),
	("PFX_FILEEND", CMAX_D3STR, "PFXD3_", "|end_map", "FILE_", "ENDFILE", ""),
	("PFX_FILEMAPKEY", CMAX_D3STR, "PFXD3_", "|map_key", "", "MAPKEY", ""),
	("PFX_FILEMETAEND", CMAX_D3STR, "PFXD3_", "metadata|end_map", "FILE_", "ENDMETA", ""),
	("PFX_FILEMETAMAPKEY", CMAX_D3STR, "PFXD3_", "metadata|map_key", "", "MAPKEY", ""),
	("PFX_FILEMETASTART", CMAX_D3STR, "PFXD3_", "metadata|start_map", "FILE_", "STARTMETA", ""),
	("PFX_FILESTART", CMAX_D3STR, "PFXD3_", "|start_map", "FILE_", "STARTFILE", ""),
	("PFX_FILEstatus", CMAX_D3STR, "PFXD3_", "metadata.status|number", "FILE_", "GETFILE", "FILE__METAstatus"),
	("PFX_FILEtimeZ", CMAX_D3STR, "PFXD3_", "metadata.generated|number", "FILE", "GETFILE", "FILE__METAtimeZ"),
	("PFX_FILEtitle", CMAX_D3STR, "PFXD3_", "metadata.title|string", "FILE_", "GETFILE", "FILE__METAtitle"),
	("PFX_FILEURL", CMAX_D3STR, "PFXD3_", "metadata.url|string", "FILE", "GETFILE", "FILE__METAURL"),
	("PFX_genLnkCNTSEND", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.contents|end_array", "PROD_", "ENDCNTSARRAY", ""),
	("PFX_genLnkCNTSSTART", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.contents|start_array", "PROD_", "STARTCNTSARRAY", ""),
	("PFX_genLnkCode", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.code|string", "PROD_", "GETPROD", "PROD__code"),
	("PFX_genLnkEND", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item|end_map", "PROD_", "ENDPRODITEM", ""),
	("PFX_genLnkENDARRAY", CMAX_D3STR, "PFXD3_", "properties.products.general-link|end_array", "PROD_", "ENDARRAY", ""),
	("PFX_genLnkEventSource", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties.eventsource|string", "PROD_", "GETPROD", "PROD__eventSource"),
	("PFX_genLnkID", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.id|string", "PROD_", "GETPROD", "PROD__ID"),
	("PFX_genLnkIndexID", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.indexid|string", "PROD_", "GETPROD", "PROD__indexID"),
	("PFX_genLnkIndexTime", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.indexTime|number", "PROD_", "GETPROD", "PROD__indexTime"),
	("PFX_genLnkMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item|map_key", "PROD_", "MAPKEY", ""),
	("PFX_genLnkPfdWgt", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.preferredWeight|number", "PROD_", "GETPROD", "PROD__pfdWgt"),
	("PFX_genLnkPROPSEND", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties|end_map", "PROD_", "ENDPRODPROPS", ""),
	("PFX_genLnkPROPSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties|map_key", "PROD_", "MAPKEY", ""),
	("PFX_genLnkPROPSPDLClientV", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties.pdl-client-version|string", "PROD_", "GETPROD", "PROD__PDLClientV"),
	("PFX_genLnkPROPSPropsTxt", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties.text|string", "PROD_", "GETPROD", "PROD__propsTxt"),
	("PFX_genLnkPROPSSTART", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties|start_map", "PROD_", "STARTPRODPROPS", ""),
	("PFX_genLnkPROPSURL", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties.url|string", "PROD_", "GETPROD", "PROD__propsURL"),
	("PFX_genLnkSource", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.source|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_genLnkSourceCode", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.properties.eventsourcecode|string", "PROD_", "GETPROD", "PROD__sourceCode"),
	("PFX_genLnkSTART", CMAX_D3STR, "PFXD3_", "properties.products.general-link|start_array", "PROD_", "STARTCNTSARRAY", ""),
	("PFX_genLnkSTARTITEMs", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item|start_map", "PROD_", "STARTCNTSITEMS", ""),
	("PFX_genLnkStatus", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.status|string", "PROD_", "GETPROD", "PROD__status"),
	("PFX_genLnkType", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.type|string", "PROD_", "GETPROD", "PROD__type"),
	("PFX_genLnkUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.general-link.item.updateTime|number", "PROD_", "GETPROD", "PROD__updatedZ"),
	("PFX_genTxtCode", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.code|string", "PROD_", "GETPROD", "PROD__code"),
	("PFX_genTxtENDITEM", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item|end_map", "PROD_", "ENDPRODITEM", ""),
	("PFX_genTxtENDITEMCNTS", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents|end_map", "CNTS_", "ENDITEMCNTS", ""),
	("PFX_genTxtENDITEMPROPS", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties|end_map", "PROD_", "ENDPRODPROPS", ""),
	("PFX_genTxtEventSource", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties.eventsource|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_genTxtEventSourceCode", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties.eventsourcecode|string", "PROD_", "GETPROD", "PROD__sourceCode"),
	("PFX_genTxtIndexID", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.indexid|string", "PROD_", "GETPROD", "PROD__indexID"),
	("PFX_genTxtIndexTime", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.indexTime|number", "PROD_", "GETPROD", "PROD__indexTime"),
	("PFX_genTxtItemID", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.id|string", "PROD_", "GETPROD", "PROD__ID"),
	("PFX_genTxtItemSTART", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item|start_map", "PROD_", "STARTITEM", ""),
	("PFX_genTxtMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item|map_key", "PROD_", "MAPKEY", ""),
	("PFX_genTxtPDLClientV", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties.pdl-client-version|string", "PROD_", "GETPROD", "PROD__PDLClientV"),
	("PFX_genTxtPfdWgt", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.preferredWeight|number", "PROD_", "GETPROD", "PROD__pfdWgt"),
	("PFX_genTxtPROPMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties|map_key", "PROD_", "MAPKEY", ""),
	("PFX_genTxtPROPSTART", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties|start_map", "PROD_", "STARTPROPS", ""),
	("PFX_genTxtRvuStatus", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.properties.review-status|string", "PROD_", "GETPROD", "PROD__rvuStatus"),
	("PFX_genTxtSource", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.source|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_genTxtSTART", CMAX_D3STR, "PFXD3_", "properties.products.general-text|start_array", "PROD_", "STARTARRAY", ""),
	("PFX_genTxtSTARTITEMCNTS", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents|start_map", "CNTS_", "STARTITEMCNTS", ""),
	("PFX_genTxtSTART_CNTS", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents.|start_map", "CNTS_", "STARTITEMCNTS", ""),
	("PFX_genTxtStatus", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.status|string", "PROD_", "GETPROD", "PROD__status"),
	("PFX_genTxtType", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.type|string", "PROD_", "GETPROD", "PROD__type"),
	("PFX_genTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.updateTime|number", "PROD_", "GETPROD", "PROD__updatedZ"),
	("PFX_geoserveCode", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.code|string", "PROD_", "GETPROD", "PROD__code"),
	("PFX_geoserveEND", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item|end_map", "PROD_", "ENDPRODITEM", ""),
	("PFX_geoserveENDARRAY", CMAX_D3STR, "PFXD3_", "properties.products.geoserve|end_array", "PROD_", "ENDCNTSARRAY", ""),
	("PFX_geoserveENDPRODPROPS", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties|end_map", "PROD_", "ENDPRODPROPS", ""),
	("PFX_geoserveEventSource", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties.eventsource|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_geoserveEventSourceCode", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties.eventsourcecode|string", "PROD_", "GETPROD", "PROD__sourceCode"),
	("PFX_geoserveID", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.id|string", "PROD_", "GETPROD", "PROD__ID"),
	("PFX_geoserveIndexID", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.indexid|string", "PROD_", "GETPROD", "PROD__indexID"),
	("PFX_geoserveIndexTime", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.indexTime|number", "PROD_", "GETPROD", "PROD__indexTime"),
	("PFX_geoserveLcn", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties.location|string", "PROD_", "GETPROD", "PROD__lcn"),
	("PFX_geoserveMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item|map_key", "PROD_", "MAPKEY", ""),
	("PFX_geoservePDLClientV", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties.pdl-client-version|string", "PROD_", "GETPROD", "PROD__PDLClientV"),
	("PFX_geoservePfdWgt", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.preferredWeight|number", "PROD_", "GETPROD", "PROD__pfdWgt"),
	("PFX_geoservePROPSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties|map_key", "PROD_", "MAPKEY", ""),
	("PFX_geoserveSource", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.source|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_geoserveSTART", CMAX_D3STR, "PFXD3_", "properties.products.geoserve|start_array", "PROD_", "STARTPROD", ""),
	("PFX_geoserveSTARTITEM", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item|start_map", "PROD_", "STARTITEM", ""),
	("PFX_geoserveSTARTPROPS", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties|start_map", "PROD_", "STARTPROPS", "PFX__geoserveSTARTPROPS1"),
	("PFX_geoserveStatus", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.status|string", "PROD_", "GETPROD", "PROD__status"),
	("PFX_geoserveTsunamiFlg", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties.tsunamiFlag|string", "PROD_", "GETPROD", "PROD__tsunamiFlg"),
	("PFX_geoserveType", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.type|string", "PROD_", "GETPROD", "PROD__type"),
	("PFX_geoserveUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.updateTime|number", "PROD_", "GETPROD", "PROD__updatedZ"),
	("PFX_geoserveUtcOffset", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.properties.utcOffset|string", "PROD_", "GETPROD", "PROD__utcOffset"),
	("PFX_groundFailureandslideHazardAlertColor", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-hazard-alert-color|string", "PROD_", "GETPROD", "PROD__landslideAlertColor"),
	("PFX_groundFailureCode", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.code|string", "PROD_", "GETPROD", "PROD__code"),
	("PFX_groundFailureDepth", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.depth|string", "PROD_", "GETPROD", "PROD__depth"),
	("PFX_groundFailureENDPROPS", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties|end_map", "PROD_", "ENDPRODPROPS", ""),
	("PFX_groundFailureEventSource", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.eventsource|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_groundFailureEventSourceCode", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.eventsourcecode|string", "PROD_", "GETPROD", "PROD__sourceCode"),
	("PFX_groundFailureHazardAlertPARM", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-hazard-alert-parameter|string", "PROD_", "GETPROD", "PROD__landslideHazardAlertPARM"),
	("PFX_groundFailureID", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.id|string", "PROD_", "GETPROD", "PROD__ID"),
	("PFX_groundFailureIndexID", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.indexid|string", "PROD_", "GETPROD", "PROD__indexID"),
	("PFX_groundFailureIndexTime", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.indexTime|number", "PROD_", "GETPROD", "PROD__indexTime"),
	("PFX_groundFailureLandslideAlert", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-alert|string", "PROD_", "GETPROD", "PROD__landslideAlert"),
	("PFX_groundFailureLandslideHazardAlertVal", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-hazard-alert-value|string", "PROD_", "GETPROD", "PROD__landslideHazardAlertVal"),
	("PFX_groundFailureLandslideMaxLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-maximum-latitude|string", "PROD_", "GETPROD", "PROD__landslideMaxLat"),
	("PFX_groundFailureLandslideMaxLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-maximum-longitude|string", "PROD_", "GETPROD", "PROD__landslideMaxLon"),
	("PFX_groundFailureLandslideMinLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-minimum-latitude|string", "PROD_", "GETPROD", "PROD__landslideMinLat"),
	("PFX_groundFailureLandslideMinLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-minimum-longitude|string", "PROD_", "GETPROD", "PROD__landslideMinLon"),
	("PFX_groundFailureLandslideOverlay", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-overlay|string", "PROD_", "GETPROD", "PROD__landslideOverlay"),
	("PFX_groundFailureLandslidePopAlertColor", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-population-alert-color|string", "PROD_", "GETPROD", "PROD__landslideAlertColor"),
	("PFX_groundFailureLandslidePopAlertPARM", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-population-alert-parameter|string", "PROD_", "GETPROD", "PROD__landslidePopAlertPARM"),
	("PFX_groundFailureLandslidePopAlertVal", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.landslide-population-alert-value|string", "PROD_", "GETPROD", "PROD__landslidePopAlertVal"),
	("PFX_groundFailureLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.latitude|string", "PROD_", "GETPROD", "PROD__lat"),
	("PFX_groundFailureLiqAlert", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-alert|string", "PROD_", "GETPROD", "PROD__liqAlert"),
	("PFX_groundFailureLiqHazardAlert", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-hazard-alert-color|string", "PROD_", "GETPROD", "PROD__liqHazardAlertColor"),
	("PFX_groundFailureLiqHazardAlertPARM", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-hazard-alert-parameter|string", "PROD_", "GETPROD", "PROD__liqHazardAlertPARM"),
	("PFX_groundFailureLiqHazardAlertVal", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-hazard-alert-value|string", "PROD_", "GETPROD", "PROD__liqHazardAlertVal"),
	("PFX_groundFailureLiqMaxLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-maximum-latitude|string", "PROD_", "GETPROD", "PROD__maxLat"),
	("PFX_groundFailureLiqMaxLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-maximum-longitude|string", "PROD_", "GETPROD", "PROD__maxLon"),
	("PFX_groundFailureLiqMinLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-minimum-latitude|string", "PROD_", "GETPROD", "PROD__minLat"),
	("PFX_groundFailureLiqMinLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-minimum-longitude|string", "PROD_", "GETPROD", "PROD__minLon"),
	("PFX_groundFailureLiqOverlay", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-overlay|string", "PROD_", "GETPROD", "PROD__overlay"),
	("PFX_groundFailureLiqPopAlertColor", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-population-alert-color|string", "PROD_", "GETPROD", "PROD__popAlertColor"),
	("PFX_groundFailureLiqPopAlertPARM", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-population-alert-parameter|string", "PROD_", "GETPROD", "PROD__popAlertPARM"),
	("PFX_groundFailureLiqPopAlertVal", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.liquefaction-population-alert-value|string", "PROD_", "GETPROD", "PROD__popAlertVal"),
	("PFX_groundFailureLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.longitude|string", "PROD_", "GETPROD", "PROD__lon"),
	("PFX_groundFailureMag", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.magnitude|string", "PROD_", "PROD__mag", "PROD__mag"),
	("PFX_groundFailureMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item|map_key", "PROD_", "MAPKEY", ""),
	("PFX_groundFailureMaxLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.maximum-latitude|string", "PROD_", "GETPROD", "PROD__maxLat"),
	("PFX_groundFailureMaxLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.maximum-longitude|string", "PROD_", "GETPROD", "PROD__maxLon"),
	("PFX_groundFailureMinLat", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.minimum-latitude|string", "PROD_", "GETPROD", "PROD__minLat"),
	("PFX_groundFailureMinLon", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.minimum-longitude|string", "PROD_", "GETPROD", "PROD__minLon"),
	("PFX_groundFailurePDLClientV", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.pdl-client-version|string", "PROD_", "GETPROD", "PROD__PDLClientV"),
	("PFX_groundFailurePfdWgt", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.preferredWeight|number", "PROD_", "GETPROD", "PROD__pfdWgt"),
	("PFX_groundFailurePROPSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties|map_key", "PROD_", "MAPKEY", ""),
	("PFX_groundFailureRuptWarn", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.rupture-warning|string", "PROD_", "GETPROD", "PROD__ruptWarn"),
	("PFX_groundFailureShakemapV", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.shakemap-version|string", "PROD_", "GETPROD", "PROD__shakemapV"),
	("PFX_groundFailureSource", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.source|string", "PROD_", "GETPROD", "PROD__source"),
	("PFX_groundFailureSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure|start_array", "PROD_", "STARTARRAY", ""),
	("PFX_groundFailureSTARTCNTS", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item|start_map", "PROD_", "STARTCNTS", ""),
	("PFX_groundFailureSTARTPROPS", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties|start_map", "PROD_", "STARTPRODPROPS", ""),
	("PFX_groundFailureStatus", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.status|string", "PROD_", "GETPROD", "PROD__status"),
	("PFX_groundFailureTimeZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.eventtime|string", "PROD_", "GETPROD", "PROD__timeZ"),
	("PFX_groundFailureType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.type|string", "PROD_", "GETPROD", "PROD__type"),
	("PFX_groundFailureUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.updateTime|number", "PROD_", "GETPROD", "PROD__updatedZ"),
	("PFX_groundFailureV", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.properties.version|string", "PROD_", "GETPROD", "PROD__V"),
	("PFX_PRODDyfiIndexTime", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.indexTime|number", "PROD_", "GETPROD", "PROD__indexTime"),
	("PFX_PRODID", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.id|string", "PROD_", "GETPROD", "PROD__ID"),
	("PFX_PRODITEMSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item|start_map", "PROD_", "STARTPRODITEM", ""),
	("PFX_PRODMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products|map_key", "", "MAPKEY", ""),
	("PFX_PRODSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi|start_array", "PROD_", "STARTPROD", ""),
	("PFX_PROPalert", CMAX_D3STR, "PFXD3_", "features.item.properties.alert|string", "PROP_", "GETPROP", "PROP__alert"),
	("PFX_PROPalert0", CMAX_D3STR, "PFXD3_", "features.item.properties.alert|null", "PROP_", "GETPROP", "PROP__alert"),
	("PFX_PROPalertD", CMAX_D3STR, "PFXD3_", "properties.alert|string", "PROP_", "GETPROP", "PROP__alert"),
	("PFX_PROPCDI", CMAX_D3STR, "PFXD3_", "features.item.properties.cdi|number", "PROP_", "GETPROP", "PROP__CDI"),
	("PFX_PROPCDI0", CMAX_D3STR, "PFXD3_", "features.item.properties.cdi|null", "PROP_", "GETPROP", "PROP__CDI"),
	("PFX_PROPCDID", CMAX_D3STR, "PFXD3_", "properties.cdi|number", "PROP_", "GETPROP", "PROP__CDI"),
	("PFX_PROPcode", CMAX_D3STR, "PFXD3_", "features.item.properties.code|string", "PROP_", "GETPROP", "PROP__code"),
	("PFX_PROPcodeD", CMAX_D3STR, "PFXD3_", "properties.code|string", "PROP_", "GETPROP", "PROP__code"),
	("PFX_PROPCOORDS", CMAX_D3STR, "PFXD3_", "features.item.geometry.coordinates.item|number", "PROP_", "GETCOORDS", ""),
	("PFX_PROPCOORDSEND", CMAX_D3STR, "PFXD3_", "features.item.geometry.coordinates|end_array", "PROP_", "ENDCOORDS", ""),
	("PFX_PROPCOORDSSTART", CMAX_D3STR, "PFXD3_", "features.item.geometry.coordinates|start_array", "PROP_", "STARTCOORDS", ""),
	("PFX_PROPdetail", CMAX_D3STR, "PFXD3_", "features.item.properties.detail|string", "PROP_", "GETPROP", "PROP__detailURL"),
	("PFX_PROPDMIN", CMAX_D3STR, "PFXD3_", "features.item.properties.dmin|number", "PROP_", "GETPROP", "PROP__DMIN"),
	("PFX_PROPDMIN0", CMAX_D3STR, "PFXD3_", "features.item.properties.dmin|null", "PROP_", "GETPROP", "PROP__DMIN"),
	("PFX_PROPDMIND", CMAX_D3STR, "PFXD3_", "properties.dmin|number", "PROP_", "GETPROP", "PROP__DMIN"),
	("PFX_PROPeventType", CMAX_D3STR, "PFXD3_", "features.item.properties.type|string", "PROP_", "GETPROP", "PROP__eventType"),
	("PFX_PROPeventTypeD", CMAX_D3STR, "PFXD3_", "properties.type|string", "PROP_", "GETPROP", "PROP__eventType"),
	("PFX_PROPfelt", CMAX_D3STR, "PFXD3_", "features.item.properties.felt|number", "PROP_", "GETPROP", "PROP__felt"),
	("PFX_PROPfelt0", CMAX_D3STR, "PFXD3_", "features.item.properties.felt|null", "PROP_", "GETPROP", "PROP__felt"),
	("PFX_PROPfeltD", CMAX_D3STR, "PFXD3_", "properties.felt|number", "PROP_", "GETPROP", "PROP__felt"),
	("PFX_PROPGEOEND", CMAX_D3STR, "PFXD3_", "features.item.geometry|end_map", "PROP_", "ENDGEO", ""),
	("PFX_PROPGEOMAPKEY", CMAX_D3STR, "PFXD3_", "features.item.geometry|map_key", "", "MAPKEY", ""),
	("PFX_PROPGEOSTART", CMAX_D3STR, "PFXD3_", "features.item.geometry|start_map", "PROP_", "STARTGEO", ""),
	("PFX_PROPGEOtype", CMAX_D3STR, "PFXD3_", "features.item.geometry.type|string", "PROP_", "GETPROP", "PROP__GEOType"),
	("PFX_PROPIDsUsed", CMAX_D3STR, "PFXD3_", "features.item.properties.ids|string", "PROP_", "GETPROP", "PROP__IDsUsed"),
	("PFX_PROPIDsUsedD", CMAX_D3STR, "PFXD3_", "properties.ids|string", "PROP_", "GETPROP", "PROP__IDsUsed"),
	("PFX_PROPmag", CMAX_D3STR, "PFXD3_", "features.item.properties.mag|number", "PROP_", "GETPROP", "PROP__mag"),
	("PFX_PROPMag0", CMAX_D3STR, "PFXD3_", "features.item.properties.mag|null", "PROP_", "GETPROP", "PROP__mag"),
	("PFX_PROPmagD", CMAX_D3STR, "PFXD3_", "properties.mag|number", "PROP_", "GETPROP", "PROP__mag"),
	("PFX_PROPMagType", CMAX_D3STR, "PFXD3_", "features.item.properties.magType|null", "PROP_", "GETPROP", "PROP__magType"),
	("PFX_PROPmagType", CMAX_D3STR, "PFXD3_", "features.item.properties.magType|string", "PROP_", "GETPROP", "PROP__magType"),
	("PFX_PROPmagTypeD", CMAX_D3STR, "PFXD3_", "properties.magType|string", "PROP_", "GETPROP", "PROP__magType"),
	("PFX_PROPMAPKEY", CMAX_D3STR, "PFXD3_", "properties|map_key", "", "MAPKEY", ""),
	("PFX_PROPmaxAzmGap", CMAX_D3STR, "PFXD3_", "features.item.properties.gap|number", "PROP_", "GETPROP", "PROP__maxAzmGap"),
	("PFX_PROPmaxAzmGap0", CMAX_D3STR, "PFXD3_", "features.item.properties.gap|null", "PROP_", "GETPROP", "PROP__maxAzmGap"),
	("PFX_PROPmaxAzmGapD", CMAX_D3STR, "PFXD3_", "properties.gap|number", "PROP_", "GETPROP", "PROP__maxAzmGap"),
	("PFX_PROPMMI", CMAX_D3STR, "PFXD3_", "features.item.properties.mmi|number", "PROP_", "GETPROP", "PROP__MMI"),
	("PFX_PROPMMI0", CMAX_D3STR, "PFXD3_", "features.item.properties.mmi|null", "PROP_", "GETPROP", "PROP__MMI"),
	("PFX_PROPMMID", CMAX_D3STR, "PFXD3_", "properties.mmi|number", "PROP_", "GETPROP", "PROP__MMI"),
	("PFX_PROPnet", CMAX_D3STR, "PFXD3_", "features.item.properties.net|string", "PROP_", "GETPROP", "PROP__net"),
	("PFX_PROPnetD", CMAX_D3STR, "PFXD3_", "properties.net|string", "PROP_", "GETPROP", "PROP__net"),
	("PFX_PROPNST", CMAX_D3STR, "PFXD3_", "features.item.properties.nst|number", "PROP_", "GETPROP", "PROP__NST"),
	("PFX_PROPNST0", CMAX_D3STR, "PFXD3_", "features.item.properties.nst|null", "PROP_", "GETPROP", "PROP__NST"),
	("PFX_PROPNSTD", CMAX_D3STR, "PFXD3_", "properties.nst|number", "PROP_", "GETPROP", "PROP__NST"),
	("PFX_PROPplace", CMAX_D3STR, "PFXD3_", "features.item.properties.place|string", "PROP_", "GETPROP", "PROP__place"),
	("PFX_PROPplaceD", CMAX_D3STR, "PFXD3_", "properties.place|string", "PROP_", "GETPROP", "PROP__place"),
	("PFX_PROPPRODSSTART", CMAX_D3STR, "PFXD3_", "properties.products|start_map", "PROP_", "STARTPROPPRODS", ""),
	("PFX_PROPRMS", CMAX_D3STR, "PFXD3_", "features.item.properties.rms|number", "PROP_", "GETPROP", "PROP__RMS"),
	("PFX_PROPRMS0", CMAX_D3STR, "PFXD3_", "features.item.properties.rms|null", "PROP_", "GETPROP", "PROP__RMS"),
	("PFX_PROPRMSD", CMAX_D3STR, "PFXD3_", "properties.rms|number", "PROP_", "GETPROP", "PROP__RMS"),
	("PFX_PROPRODTypes", CMAX_D3STR, "PFXD3_", "features.item.properties.types|string", "PROP_", "GETPROP", "PROP__PRODTypes"),
	("PFX_PROPRODTypesD", CMAX_D3STR, "PFXD3_", "properties.types|string", "PROP_", "GETPROP", "PROP__PRODTypes"),
	("PFX_PROPSEND", CMAX_D3STR, "PFXD3_", "features.item.properties|end_map", "PROP_", "ENDPROPS", ""),
	("PFX_PROPSIG", CMAX_D3STR, "PFXD3_", "features.item.properties.sig|number", "PROP_", "GETPROP", "PROP__SIG"),
	("PFX_PROPSIGD", CMAX_D3STR, "PFXD3_", "properties.sig|number", "PROP_", "GETPROP", "PROP__SIG"),
	("PFX_PROPSMAPKEY", CMAX_D3STR, "PFXD3_", "features.item.properties|map_key", "", "MAPKEY", ""),
	("PFX_PROPSourcesUSed", CMAX_D3STR, "PFXD3_", "features.item.properties.sources|string", "PROP_", "GETPROP", "PROP__sourcesUsed"),
	("PFX_PROPSourcesUsedD", CMAX_D3STR, "PFXD3_", "properties.sources|string", "PROP_", "GETPROP", "PROP__sourcesUsed"),
	("PFX_PROPSSTART", CMAX_D3STR, "PFXD3_", "properties|start_map", "PROP_", "STARTPROP", ""),
	("PFX_PROPSTART", CMAX_D3STR, "PFXD3_", "features.item.properties|start_map", "PROP_", "STARTPROP", ""),
	("PFX_PROPStatus", CMAX_D3STR, "PFXD3_", "features.item.properties.status|string", "PROP_", "GETPROP", "PROP__status"),
	("PFX_PROPStatusD", CMAX_D3STR, "PFXD3_", "properties.status|string", "PROP_", "GETPROP", "PROP__status"),
	("PFX_PROPtimeZ", CMAX_D3STR, "PFXD3_", "features.item.properties.time|number", "PROP_", "GETPROP", "PROP__timeZ"),
	("PFX_PROPtimeZD", CMAX_D3STR, "PFXD3_", "properties.time|number", "PROP_", "GETPROP", "PROP__timeZ"),
	("PFX_PROPtitle", CMAX_D3STR, "PFXD3_", "features.item.properties.title|string", "PROP_", "GETPROP", "PROP__title"),
	("PFX_PROPtitleD", CMAX_D3STR, "PFXD3_", "properties.title|string", "PROP_", "GETPROP", "PROP__title"),
	("PFX_PROPtsunami", CMAX_D3STR, "PFXD3_", "features.item.properties.tsunami|number", "PROP_", "GETPROP", "PROP__tsunami"),
	("PFX_PROPtsunamiD", CMAX_D3STR, "PFXD3_", "properties.tsunami|number", "PROP_", "GETPROP", "PROP__tsunami"),
	("PFX_PROPTZLM", CMAX_D3STR, "PFXD3_", "features.item.properties.tz|number", "PROP_", "GETPROP", "PROP__TZLM"),
	("PFX_PROPTZLM0", CMAX_D3STR, "PFXD3_", "features.item.properties.tz|null", "PROP_", "GETPROP", "PROP__TZLM"),
	("PFX_PROPTZLMD", CMAX_D3STR, "PFXD3_", "properties.tz|number", "PROP_", "GETPROP", "PROP__TZLM"),
	("PFX_PROPupdatedZ", CMAX_D3STR, "PFXD3_", "features.item.properties.updated|number", "PROP_", "GETPROP", "PROP__updatedZ"),
	("PFX_PROPupdatedZD", CMAX_D3STR, "PFXD3_", "properties.updated|number", "PROP_", "GETPROP", "PROP__updatedZ"),
	("PFX_PROPURL", CMAX_D3STR, "PFXD3_", "features.item.properties.url|string", "PROP_", "GETPROP", "PROP__URL"),
	("PFX_PROPURLD", CMAX_D3STR, "PFXD3_", "properties.url|string", "PROP_", "GETPROP", "PROP__URL"),
	("PFX__dyfi10kmGJEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiCIIMGeoImapHTMEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiCIIMGeoImapHTMLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiCIIMGeoImapHTMMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiCIIMGeoImapHTMSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiCIIMGeoImapHTMType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiCIIMGeoImapHTMUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiCIIMGeoImapHTMURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo_imap.html.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiCIIMGeoPdfEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf|end_map", "CNTS_", "ENDCNTS", "CNTS__URL"),
	("PFX__dyfiCIIMGeoPdfLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiCIIMGeoPdfMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiCIIMGeoPdfSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiCIIMGeoPdfType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiCIIMGeoPdfUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiCIIMGeoPdfURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.pdf.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiCIIMGeoPsEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiCIIMGeoPsLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiCIIMGeoPsMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiCIIMGeoPsSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiCIIMGeoPsType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiCIIMGeoPsUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiCIIMGeoPsURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.ps.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiCIIMImapHTMEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiCIIMImapHTMLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiCIIMImapHTMMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiCIIMImapHTMSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiCIIMImapHTMType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiCIIMImapHTMUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiCIIMImapHTMURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_imap.html.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiEVCIIMGeoJpgEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiEVCIIMGeoJpgLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiEVCIIMGeoJpgMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiEVCIIMGeoJpgSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiEVCIIMGeoJpgType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiEVCIIMGeoJpgUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiEVCIIMGeoJpgURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim_geo.jpg.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiEVCIIMJpgEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiEVCIIMJpgLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiEVCIIMJpgMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiEVCIIMJpgSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiEVCIIMJpgType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiEVCIIMJpgUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiEVCIIMJpgURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.jpg.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiEVCIIMPdfEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiEVCIIMPdfLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiEVCIIMPdfMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiEVCIIMPdfSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiEVCIIMPdfType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiEVCIIMPdfUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiEVCIIMPdfURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.pdf.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiEVCIIMPsEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiEVCIIMPsLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiEVCIIMPsMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiEVCIIMPsSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiEVCIIMPsType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiEVCIIMPsUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiEVCIIMPsURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_ciim.ps.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiEVDataXmlEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiEVDataXmlLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiEVDataXmlMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiEVDataXmlSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiEVDataXmlType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiEVDataXmlUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiEVDataXmlURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.event_data.xml.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiGeo10kmGJLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiGeo10kmGJMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiGeo10kmGJSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiGeo10kmGJType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiGeo10kmGJUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiGeo10kmGJURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_10km.geojson.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiGeo1kmGJEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiGeo1kmGJLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiGeo1kmGJMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiGeo1kmGJSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiGeo1kmGJType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiGeo1kmGJUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiGeo1kmGJURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo_1km.geojson.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiGeo1kmTxtEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiGeo1kmTxtLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiGeo1kmTxtMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiGeo1kmTxtSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiGeo1kmTxtType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiGeo1kmTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiGeo1kmTxtURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo_1km.txt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiGeoKmzEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiGeoKmzLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiGeoKmzMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiGeoKmzSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiGeoKmzType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiGeoKmzUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiGeoKmzURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_geo.kmz.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiGeoTxtEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiGeoTxtLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiGeoTxtSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt|start_map", "", "STARTCNTS", ""),
	("PFX__dyfiGeoTxtType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiGeoTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiGeoTxtURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.txt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiGeoXmlEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiGeoXmlLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiGeoXmlMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml|map_key", "", "MAPKEY", ""),
	("PFX__dyfiGeoXmlSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiGeoXmlType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiGeoXmlUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiGeoXmlURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_geo.xml.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiItemEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item|end_map", "CNTS_", "ENDPRODITEM", ""),
	("PFX__dyfiKmzEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiKmzLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiKmzMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiKmzSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiKmzType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz.contentType|string", "CNTS_", "GETCNTS", ""),
	("PFX__dyfiKmzUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiKmzURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi.kmz.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltAttenJpgEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltAttenJpgLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltAttenJpgMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltAttenJpgSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltAttenJpgType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltAttenJpgUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltAttenJpgURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.jpg.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltAttennJsonEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltAttennJsonLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltAttennJsonMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltAttennJsonSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltAttennJsonType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltAttennJsonUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltAttennJsonURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_atten.json.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltAttenPsEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltAttenPsLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltAttenPsMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltAttenPsSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltAttenPsType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltAttenPsUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltAttenPsURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.ps.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltAttenTxtEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltAttenTxtLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltAttenTxtMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltAttenTxtSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltAttenTxtType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltAttenTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltAttenTxtURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_atten.txt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltNumRespJpgEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltNumRespJpgLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltNumRespJpgMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltNumRespJpgSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltNumRespJpgType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltNumRespJpgUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltNumRespJpgURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.jpg.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltNumRespPsEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltNumRespPsLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltNumRespPsMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltNumRespPsSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltNumRespPsType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltNumRespPsUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltNumRespPsURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.ps.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltNumRespTxtEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltNumRespTxtLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltNumRespTxtMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltNumRespTxtSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltNumRespTxtType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltNumRespTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltNumRespTxtURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.%EQEVID%_plot_numresp.txt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiPltNumRspJsonEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiPltNumRspJsonLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiPltNumRspJsonMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiPltNumRspJsonSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiPltNumRspJsonType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiPltNumRspJsonUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiPltNumRspJsonURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_plot_numresp.json.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiXMLEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiXMLlen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiXMLMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiXMLSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiXMLtype", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiXMLupdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiXMLURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.contents.xml.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiZipGJEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiZipGJLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfiZipGJMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiZipGJSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiZipGJType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiZipGJUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiZipGJURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.geojson.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfiZipKmzEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfiZipKmzLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz.length|number", "CNTS_", "GETCNTS", "CNTA__len"),
	("PFX__dyfiZipKmzMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfiZipKmzSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfiZipKmzType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfiZipKmzUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfiZipKmzURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.dyfi_zip.kmz.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfizipTxtEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfizipTxtLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfizipTxtMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfizipTxtSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfizipTxtType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfizipTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfizipTxtURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.txt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__dyfizipXmlEND", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__dyfizipXmlLen", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__dyfizipXmlMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__dyfizipXmlSTART", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__dyfizipXmlType", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__dyfizipXmlUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__dyfizipXmlURL", CMAX_D3STR, "PFXD3_", "properties.products.dyfi.item.contents.cdi_zip.xml.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__genTxtBytes", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents..bytes|string", "CNTS_", "GETCNTS", "CNTS__bytes"),
	("PFX__genTxtCNTSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__genTxtENDARRAY", CMAX_D3STR, "PFXD3_", "properties.products.general-text|end_array", "PROD_", "ENDCNTSARRAY", ""),
	("PFX__genTxtENDCNTS", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents.|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__genTxtLen", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents..length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__genTxtType", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents..contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__genTxtUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents..lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__genTxt_CNTSMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.general-text.item.contents.|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__geoserveCntsMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__geoserveENDCNTS", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__geoserveGeoserveJsonSTART", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__geoserveGeoservJsonMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__geoserveJsonENDCNTS", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__geoserveJsonLen", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__geoserveJsonType", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__geoserveJsonUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__geoserveJsonURL", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents.geoserve.json.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__geoserveSTARTCNTS", CMAX_D3STR, "PFXD3_", "properties.products.geoserve.item.contents|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureCntsMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureCntsSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents|start_map", "CNTS_", "STARTPRODCNTS", ""),
	("PFX__groundFailureCntsXmlEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureCntsXmlLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureCntsXmlMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureCntsXmlSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureCntsXmlType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureCntsXmlUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureCntsXmlURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.contents.xml.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureGodt2008Hdf5END", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureGodt2008Hdf5Len", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureGodt2008Hdf5MAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureGodt2008Hdf5START", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureGodt2008Hdf5Type", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureGodt2008Hdf5UpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureGodt2008Hdf5URL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.hdf5.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureGodt2008MdlFltEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureGodt2008MdlFltLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureGodt2008MdlFltMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureGodt2008MdlFltSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureGodt2008MdlFltType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureGodt2008MdlFltUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureGodt2008MdlFltURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.flt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureGodt2008ModelHdrEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureGodt2008ModelHdrLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureGodt2008ModelHdrMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureGodt2008ModelHdrSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureGodt2008ModelHdrType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureGodt2008ModelHdrUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureGodt2008ModelHdrURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.hdr.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureGodt2008ModelTifEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureGodt2008ModelTifLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureGodt2008ModelTifMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureGodt2008ModelTifSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureGodt2008ModelTifType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureGodt2008ModelTifUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureGodt2008ModelTifURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008_model.tif.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureGodt2008PngEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureGodt2008PngLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureGodt2008PngMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureGodt2008PngSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureGodt2008PngType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureGodt2008PngUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updaatedZ"),
	("PFX__groundFailureGodt2008PngURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.godt_2008.png.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureInfoJsonEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureInfoJsonLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureInfoJsonMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureInfoJsonSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureInfoJsonType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureInfoJsonUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureInfoJsonURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.info.json.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureJessee2017FltEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureJessee2017FltLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureJessee2017FltMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureJessee2017FltSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureJessee2017FltType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureJessee2017FltUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureJessee2017FltURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.flt.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureJessee2017Hdf5END", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureJessee2017Hdf5Len", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureJessee2017Hdf5MAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureJessee2017Hdf5START", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureJessee2017Hdf5Type", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureJessee2017Hdf5UpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureJessee2017Hdf5URL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.hdf5.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureJessee2017ModelHdrEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureJessee2017ModelHdrLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureJessee2017ModelHdrMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureJessee2017ModelHdrSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureJessee2017ModelHdrType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureJessee2017ModelHdrUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureJessee2017ModelHdrURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.hdr.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureJessee2017ModelTifEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureJessee2017ModelTifLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureJessee2017ModelTifMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureJessee2017ModelTifSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureJessee2017ModelTifType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureJessee2017ModelTifUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureJessee2017ModelTifURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017_model.tif.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PFX__groundFailureJessee2017PngEND", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png|end_map", "CNTS_", "ENDCNTS", ""),
	("PFX__groundFailureJessee2017PngLen", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png.length|number", "CNTS_", "GETCNTS", "CNTS__len"),
	("PFX__groundFailureJessee2017PngMAPKEY", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png|map_key", "CNTS_", "MAPKEY", ""),
	("PFX__groundFailureJessee2017PngSTART", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png|start_map", "CNTS_", "STARTCNTS", ""),
	("PFX__groundFailureJessee2017PngType", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png.contentType|string", "CNTS_", "GETCNTS", "CNTS__type"),
	("PFX__groundFailureJessee2017PngUpdatedZ", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png.lastModified|number", "CNTS_", "GETCNTS", "CNTS__updatedZ"),
	("PFX__groundFailureJessee2017PngURL", CMAX_D3STR, "PFXD3_", "properties.products.ground-failure.item.contents.jessee_2017.png.url|string", "CNTS_", "GETCNTS", "CNTS__URL"),
	("PKL_", CMAX_TYPEDFN, "PKL_", "pickle in any use",),
	("POD01_GRP", CMAX_PODDFN, "POD01_", "standaloneNC", "pod for geojson stuffs",),
	("POD01__day", CMAX_PODSTR, "POD01_", "-d", "day",),
	("POD01__detail", CMAX_PODSTR, "POD01_", "-D", "detail",),
	("POD01__detailQ_", CMAX_PODSTR, "POD01_", "-Q", "detailQuery",),
	("POD01__file", CMAX_PODSTR, "POD01_", "-f", "file",),
	("POD01__hour", CMAX_PODSTR, "POD01_", "-h", "hour",),
	("POD01__link", CMAX_PODSTR, "POD01_", "-L", "link",),
	("POD01__list", CMAX_PODSTR, "POD01_", "-l", "list",),
	("POD01__month", CMAX_PODSTR, "POD01_", "-m", "month",),
	("POD01__query", CMAX_PODSTR, "POD01_", "-q", "query",),
	("POD01__week", CMAX_PODSTR, "POD01_", "-w", "week",),
	("POINT", CMAX_TYPEDFN, "point", "geometric point",),
	("PRODS_", CMAX_TYPEDFN, "products", "products in all uses",),
	("PROD_", CMAX_TYPEDFN, "PROD_", "product in all uses",),
	("PROMPT1_str", CMAX_VALDFN, 'lambda FLDIN_, PFXIN_, DFLTIN_: f"""enter the {FLDIN_} ("" = "{DFLTIN_}" ::  " " = ""){NEWLINE}{PFXIN_}{NEWLINE}"""',),
	("PROPS_", CMAX_TYPEDFN, "properties", "properties in all uses",),
	("PROP_TBL_", CMAX_TBLDFN, "PROP_", "all the PROPS, PRODS will have their own",),
	("PROP__alert", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__CDI", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__code", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__depth", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__depthErr", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__detailURL", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__DMIN", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__EQEVID", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__EQEVRID", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__eventType", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__felt", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__GEOType", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__horzErr", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__IDsUsed", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__lat", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__locnSrc", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__lon", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__mag", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__magErr", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__magNST", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__magSrc", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__magType", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__maxAzmGap", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__MMI", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__net", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__NST", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__PFDWT", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__place", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__point", CMAX_TBLFLDnoWRT, "PROP_", "POINT", _DFLT_STR_,),
	("PROP__PRODs", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__PRODTypes", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__RMS", CMAX_TBLFLD, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PROP__SIG", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__source", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__sourcesUsed", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__status", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__timeR", CMAX_TBLFLDnoWRT, "PROP_", "DATETIME", _DFLT_STR_,),
	("PROP__timeZ", CMAX_TBLFLD, "PROP_", "DATETIME", _DFLT_STR_,),
	("PROP__title", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__toPoint", CMAX_TBLFLDnoWRT, "PROP_", "POINT", _DFLT_STR_,),
	("PROP__tsunami", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__type", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__TZLM", CMAX_TBLFLD, "PROP_", "INT", _DFLT_INT_,),
	("PROP__updatedR", CMAX_TBLFLDnoWRT, "PROP_", "DATETIME", _DFLT_STR_,),
	("PROP__updatedZ", CMAX_TBLFLD, "PROP_", "DATETIME", _DFLT_STR_,),
	("PROP__URL", CMAX_TBLFLD, "PROP_", "VARCHAR", _DFLT_STR_,),
	("PROP__Zdistance", CMAX_TBLFLDnoWRT, "PROP_", "DECIMAL", _DFLT_DEC_,),
	("PT_", CMAX_TYPEDFN, "PT_", "point",),
	("PYDEW_PYErrWrnCodes", CMAX_DICTDFN, "PYDEW_", CMS_STANDALONE, "str, str", "list of python lint tools codes",),
	("PYDEW__D100", CMAX_DICTSTR, "PYDEW_", "D100", "Missing docstring in public module",),
	("PYDEW__D101", CMAX_DICTSTR, "PYDEW_", "D101", "Missing docstring in public class",),
	("PYDEW__D102", CMAX_DICTSTR, "PYDEW_", "D102", "Missing docstring in public method",),
	("PYDEW__D103", CMAX_DICTSTR, "PYDEW_", "D103", "Missing docstring in public function",),
	("PYDEW__D104", CMAX_DICTSTR, "PYDEW_", "D104", "Missing docstring in public package",),
	("PYDEW__D105", CMAX_DICTSTR, "PYDEW_", "D105", "Missing docstring in magic method",),
	("PYDEW__D106", CMAX_DICTSTR, "PYDEW_", "D106", "Missing docstring in public nested class",),
	("PYDEW__D107", CMAX_DICTSTR, "PYDEW_", "D107", "Missing docstring in __init__",),
	("PYDEW__D200", CMAX_DICTSTR, "PYDEW_", "D200", "One-line docstring should fit on one line with quotes",),
	("PYDEW__D201", CMAX_DICTSTR, "PYDEW_", "D201", "No blank lines allowed before function docstring",),
	("PYDEW__D202", CMAX_DICTSTR, "PYDEW_", "D202", "No blank lines allowed after function docstring",),
	("PYDEW__D203", CMAX_DICTSTR, "PYDEW_", "D203", "1 blank line required before class docstring",),
	("PYDEW__D204", CMAX_DICTSTR, "PYDEW_", "D204", "1 blank line required after class docstring",),
	("PYDEW__D205", CMAX_DICTSTR, "PYDEW_", "D205", "1 blank line required between summary line and description",),
	("PYDEW__D206", CMAX_DICTSTR, "PYDEW_", "D206", "Docstring should be indented with spaces, not tabs",),
	("PYDEW__D207", CMAX_DICTSTR, "PYDEW_", "D207", "Docstring is under-indented",),
	("PYDEW__D208", CMAX_DICTSTR, "PYDEW_", "D208", "Docstring is over-indented",),
	("PYDEW__D209", CMAX_DICTSTR, "PYDEW_", "D209", "Multi-line docstring closing quotes should be on a separate line",),
	("PYDEW__D210", CMAX_DICTSTR, "PYDEW_", "D210", "No whitespaces allowed surrounding docstring text",),
	("PYDEW__D211", CMAX_DICTSTR, "PYDEW_", "D211", "No blank lines allowed before class docstring",),
	("PYDEW__D212", CMAX_DICTSTR, "PYDEW_", "D212", "Multi-line docstring summary should start at the first line",),
	("PYDEW__D213", CMAX_DICTSTR, "PYDEW_", "D213", "Multi-line docstring summary should start at the second line",),
	("PYDEW__D214", CMAX_DICTSTR, "PYDEW_", "D214", "Section is over-indented",),
	("PYDEW__D215", CMAX_DICTSTR, "PYDEW_", "D215", "Section underline is over-indented",),
	("PYDEW__D300", CMAX_DICTSTR, "PYDEW_", "D300", "Use “”“triple double quotes”“”",),
	("PYDEW__D301", CMAX_DICTSTR, "PYDEW_", "D301", "Use r”“” if any backslashes in a docstring",),
	("PYDEW__D302", CMAX_DICTSTR, "PYDEW_", "D302", "Use u”“” for Unicode docstrings",),
	("PYDEW__D400", CMAX_DICTSTR, "PYDEW_", "D400", "First line should end with a period",),
	("PYDEW__D401", CMAX_DICTSTR, "PYDEW_", "D401", "First line should be in imperative mood",),
	("PYDEW__D401", CMAX_DICTSTR, "PYDEW_", "D401", "First line should be in imperative mood; try rephrasing",),
	("PYDEW__D402", CMAX_DICTSTR, "PYDEW_", "D402", "First line should not be the function’s “signature”",),
	("PYDEW__D403", CMAX_DICTSTR, "PYDEW_", "D403", "First word of the first line should be properly capitalized",),
	("PYDEW__D404", CMAX_DICTSTR, "PYDEW_", "D404", "First word of the docstring should not be This",),
	("PYDEW__D405", CMAX_DICTSTR, "PYDEW_", "D405", "Section name should be properly capitalized",),
	("PYDEW__D406", CMAX_DICTSTR, "PYDEW_", "D406", "Section name should end with a newline",),
	("PYDEW__D407", CMAX_DICTSTR, "PYDEW_", "D407", "Missing dashed underline after section",),
	("PYDEW__D408", CMAX_DICTSTR, "PYDEW_", "D408", "Section underline should be in the line following the section’s name",),
	("PYDEW__D409", CMAX_DICTSTR, "PYDEW_", "D409", "Section underline should match the length of its name",),
	("PYDEW__D410", CMAX_DICTSTR, "PYDEW_", "D410", "Missing blank line after section",),
	("PYDEW__D411", CMAX_DICTSTR, "PYDEW_", "D411", "Missing blank line before section",),
	("PYDEW__D412", CMAX_DICTSTR, "PYDEW_", "D412", "No blank lines allowed between a section header and its content",),
	("PYDEW__D413", CMAX_DICTSTR, "PYDEW_", "D413", "Missing blank line after last section",),
	("PYDEW__D414", CMAX_DICTSTR, "PYDEW_", "D414", "Section has no content",),
	("PYDEW__D415", CMAX_DICTSTR, "PYDEW_", "D415", "First line should end with a period, question mark, or exclamation point",),
	("PYDEW__D416", CMAX_DICTSTR, "PYDEW_", "D416", "Section name should end with a colon",),
	("PYDEW__D417", CMAX_DICTSTR, "PYDEW_", "D417", "Missing argument descriptions in the docstring",),
	("PYDEW__E1", CMAX_DICTSTR, "PYDEW_", "E1", "indentation",),
	("PYDEW__E101", CMAX_DICTSTR, "PYDEW_", "E101", "indentation contains mixed spaces and tabs",),
	("PYDEW__E111", CMAX_DICTSTR, "PYDEW_", "E111", "indentation is not a multiple of four",),
	("PYDEW__E112", CMAX_DICTSTR, "PYDEW_", "E112", "expected an indented block",),
	("PYDEW__E113", CMAX_DICTSTR, "PYDEW_", "E113", "unexpected indentation",),
	("PYDEW__E114", CMAX_DICTSTR, "PYDEW_", "E114", "indentation is not a multiple of four (comment)",),
	("PYDEW__E115", CMAX_DICTSTR, "PYDEW_", "E115", "expected an indented block (comment)",),
	("PYDEW__E116", CMAX_DICTSTR, "PYDEW_", "E116", "unexpected indentation (comment)",),
	("PYDEW__E117", CMAX_DICTSTR, "PYDEW_", "E117", "over-indented",),
	("PYDEW__E121", CMAX_DICTSTR, "PYDEW_", "E121", "(*^) continuation line under-indented for hanging indent",),
	("PYDEW__E122", CMAX_DICTSTR, "PYDEW_", "E122", "(^) continuation line missing indentation or outdented",),
	("PYDEW__E123", CMAX_DICTSTR, "PYDEW_", "E123", "(*) closing bracket does not match indentation of opening bracket’s line",),
	("PYDEW__E124", CMAX_DICTSTR, "PYDEW_", "E124", "(^) closing bracket does not match visual indentation",),
	("PYDEW__E125", CMAX_DICTSTR, "PYDEW_", "E125", "(^) continuation line with same indent as next logical line",),
	("PYDEW__E126", CMAX_DICTSTR, "PYDEW_", "E126", "(*^) continuation line over-indented for hanging indent",),
	("PYDEW__E127", CMAX_DICTSTR, "PYDEW_", "E127", "(^) continuation line over-indented for visual indent",),
	("PYDEW__E128", CMAX_DICTSTR, "PYDEW_", "E128", "(^) continuation line under-indented for visual indent",),
	("PYDEW__E129", CMAX_DICTSTR, "PYDEW_", "E129", "(^) visually indented line with same indent as next logical line",),
	("PYDEW__E131", CMAX_DICTSTR, "PYDEW_", "E131", "(^) continuation line unaligned for hanging indent",),
	("PYDEW__E133", CMAX_DICTSTR, "PYDEW_", "E133", "(*) closing bracket is missing indentation",),
	("PYDEW__E2", CMAX_DICTSTR, "PYDEW_", "E2", "Whitespace",),
	("PYDEW__E201", CMAX_DICTSTR, "PYDEW_", "E201", "whitespace after ‘(‘",),
	("PYDEW__E202", CMAX_DICTSTR, "PYDEW_", "E202", "whitespace before ‘)’",),
	("PYDEW__E203", CMAX_DICTSTR, "PYDEW_", "E203", "whitespace before ‘:’",),
	("PYDEW__E211", CMAX_DICTSTR, "PYDEW_", "E211", "whitespace before ‘(‘",),
	("PYDEW__E221", CMAX_DICTSTR, "PYDEW_", "E221", "multiple spaces before operator",),
	("PYDEW__E222", CMAX_DICTSTR, "PYDEW_", "E222", "multiple spaces after operator",),
	("PYDEW__E223", CMAX_DICTSTR, "PYDEW_", "E223", "tab before operator",),
	("PYDEW__E224", CMAX_DICTSTR, "PYDEW_", "E224", "tab after operator",),
	("PYDEW__E225", CMAX_DICTSTR, "PYDEW_", "E225", "missing whitespace around operator",),
	("PYDEW__E226", CMAX_DICTSTR, "PYDEW_", "E226", "(*) missing whitespace around arithmetic operator",),
	("PYDEW__E227", CMAX_DICTSTR, "PYDEW_", "E227", "missing whitespace around bitwise or shift operator",),
	("PYDEW__E228", CMAX_DICTSTR, "PYDEW_", "E228", "missing whitespace around modulo operator",),
	("PYDEW__E231", CMAX_DICTSTR, "PYDEW_", "E231", "missing whitespace after ‘,’, ‘;’, or ‘:’",),
	("PYDEW__E241", CMAX_DICTSTR, "PYDEW_", "E241", "(*) multiple spaces after ‘,’",),
	("PYDEW__E242", CMAX_DICTSTR, "PYDEW_", "E242", "(*) tab after ‘,’",),
	("PYDEW__E251", CMAX_DICTSTR, "PYDEW_", "E251", "unexpected spaces around keyword / parameter equals",),
	("PYDEW__E261", CMAX_DICTSTR, "PYDEW_", "E261", "at least two spaces before inline comment",),
	("PYDEW__E262", CMAX_DICTSTR, "PYDEW_", "E262", "inline comment should start with ‘# ‘",),
	("PYDEW__E265", CMAX_DICTSTR, "PYDEW_", "E265", "block comment should start with ‘# ‘",),
	("PYDEW__E266", CMAX_DICTSTR, "PYDEW_", "E266", "too many leading ‘#’ for block comment",),
	("PYDEW__E271", CMAX_DICTSTR, "PYDEW_", "E271", "multiple spaces after keyword",),
	("PYDEW__E272", CMAX_DICTSTR, "PYDEW_", "E272", "multiple spaces before keyword",),
	("PYDEW__E273", CMAX_DICTSTR, "PYDEW_", "E273", "tab after keyword",),
	("PYDEW__E274", CMAX_DICTSTR, "PYDEW_", "E274", "tab before keyword",),
	("PYDEW__E275", CMAX_DICTSTR, "PYDEW_", "E275", "missing whitespace after keyword",),
	("PYDEW__E3", CMAX_DICTSTR, "PYDEW_", "E3", "Blank line",),
	("PYDEW__E301", CMAX_DICTSTR, "PYDEW_", "E301", "expected 1 blank line, found 0",),
	("PYDEW__E302", CMAX_DICTSTR, "PYDEW_", "E302", "expected 2 blank lines, found 0",),
	("PYDEW__E303", CMAX_DICTSTR, "PYDEW_", "E303", "too many blank lines (3)",),
	("PYDEW__E304", CMAX_DICTSTR, "PYDEW_", "E304", "blank lines found after function decorator",),
	("PYDEW__E305", CMAX_DICTSTR, "PYDEW_", "E305", "expected 2 blank lines after end of function or class",),
	("PYDEW__E306", CMAX_DICTSTR, "PYDEW_", "E306", "expected 1 blank line before a nested definition",),
	("PYDEW__E4", CMAX_DICTSTR, "PYDEW_", "E4", "Import",),
	("PYDEW__E401", CMAX_DICTSTR, "PYDEW_", "E401", "multiple imports on one line",),
	("PYDEW__E402", CMAX_DICTSTR, "PYDEW_", "E402", "module level import not at top of file",),
	("PYDEW__E5", CMAX_DICTSTR, "PYDEW_", "E5", "Line length",),
	("PYDEW__E501", CMAX_DICTSTR, "PYDEW_", "E501", "(^) line too long (82 > 79 characters)",),
	("PYDEW__E502", CMAX_DICTSTR, "PYDEW_", "E502", "the backslash is redundant between brackets",),
	("PYDEW__E7", CMAX_DICTSTR, "PYDEW_", "E7", "Statement",),
	("PYDEW__E701", CMAX_DICTSTR, "PYDEW_", "E701", "multiple statements on one line (colon)",),
	("PYDEW__E702", CMAX_DICTSTR, "PYDEW_", "E702", "multiple statements on one line (semicolon)",),
	("PYDEW__E703", CMAX_DICTSTR, "PYDEW_", "E703", "statement ends with a semicolon",),
	("PYDEW__E704", CMAX_DICTSTR, "PYDEW_", "E704", "(*) multiple statements on one line (def)",),
	("PYDEW__E711", CMAX_DICTSTR, "PYDEW_", "E711", "(^) comparison to None should be ‘if cond is None:’",),
	("PYDEW__E712", CMAX_DICTSTR, "PYDEW_", "E712", "(^) comparison to True should be ‘if cond is True:’ or ‘if cond:’",),
	("PYDEW__E713", CMAX_DICTSTR, "PYDEW_", "E713", "test for membership should be ‘not in’",),
	("PYDEW__E714", CMAX_DICTSTR, "PYDEW_", "E714", "test for object identity should be ‘is not’",),
	("PYDEW__E721", CMAX_DICTSTR, "PYDEW_", "E721", "(^) do not compare types, use ‘isinstance()’",),
	("PYDEW__E722", CMAX_DICTSTR, "PYDEW_", "E722", "do not use bare except, specify exception instead",),
	("PYDEW__E731", CMAX_DICTSTR, "PYDEW_", "E731", "do not assign a lambda expression, use a def",),
	("PYDEW__E741", CMAX_DICTSTR, "PYDEW_", "E741", "do not use variables named ‘l’, ‘O’, or ‘I’",),
	("PYDEW__E742", CMAX_DICTSTR, "PYDEW_", "E742", "do not define classes named ‘l’, ‘O’, or ‘I’",),
	("PYDEW__E743", CMAX_DICTSTR, "PYDEW_", "E743", "do not define functions named ‘l’, ‘O’, or ‘I’",),
	("PYDEW__E9", CMAX_DICTSTR, "PYDEW_", "E9", "Runtime",),
	("PYDEW__E901", CMAX_DICTSTR, "PYDEW_", "E901", "SyntaxError or indentationError",),
	("PYDEW__E902", CMAX_DICTSTR, "PYDEW_", "E902", "IOError",),
	("PYDEW__F401", CMAX_DICTSTR, "PYDEW_", "F401", "module imported but unused",),
	("PYDEW__F402", CMAX_DICTSTR, "PYDEW_", "F402", "import module from line N shadowed by loop variable",),
	("PYDEW__F403", CMAX_DICTSTR, "PYDEW_", "F403", "‘from module import *’ used; unable to detect undefined names",),
	("PYDEW__F404", CMAX_DICTSTR, "PYDEW_", "F404", "future import(s) name after other statements",),
	("PYDEW__F405", CMAX_DICTSTR, "PYDEW_", "F405", "name may be undefined, or defined from star imports: module",),
	("PYDEW__F406", CMAX_DICTSTR, "PYDEW_", "F406", "‘from module import *’ only allowed at module level",),
	("PYDEW__F407", CMAX_DICTSTR, "PYDEW_", "F407", "an undefined __future__ feature name was imported",),
	("PYDEW__F501", CMAX_DICTSTR, "PYDEW_", "F501", "invalid % format literal",),
	("PYDEW__F502", CMAX_DICTSTR, "PYDEW_", "F502", "% format expected mapping but got sequence",),
	("PYDEW__F503", CMAX_DICTSTR, "PYDEW_", "F503", "% format expected sequence but got mapping",),
	("PYDEW__F504", CMAX_DICTSTR, "PYDEW_", "F504", "% format unused named arguments",),
	("PYDEW__F505", CMAX_DICTSTR, "PYDEW_", "F505", "% format missing named arguments",),
	("PYDEW__F506", CMAX_DICTSTR, "PYDEW_", "F506", "% format mixed positional and named arguments",),
	("PYDEW__F507", CMAX_DICTSTR, "PYDEW_", "F507", "% format mismatch of placeholder and argument count",),
	("PYDEW__F508", CMAX_DICTSTR, "PYDEW_", "F508", "% format with * specifier requires a sequence",),
	("PYDEW__F509", CMAX_DICTSTR, "PYDEW_", "F509", "% format with unsupported format character",),
	("PYDEW__F521", CMAX_DICTSTR, "PYDEW_", "F521", ".format(...) invalid format string",),
	("PYDEW__F522", CMAX_DICTSTR, "PYDEW_", "F522", ".format(...) unused named arguments",),
	("PYDEW__F523", CMAX_DICTSTR, "PYDEW_", "F523", ".format(...) unused positional arguments",),
	("PYDEW__F524", CMAX_DICTSTR, "PYDEW_", "F524", ".format(...) missing argument",),
	("PYDEW__F525", CMAX_DICTSTR, "PYDEW_", "F525", ".format(...) mixing automatic and manual numbering",),
	("PYDEW__F541", CMAX_DICTSTR, "PYDEW_", "F541", "f-string without any placeholders",),
	("PYDEW__F601", CMAX_DICTSTR, "PYDEW_", "F601", "dictionary key name repeated with different values",),
	("PYDEW__F602", CMAX_DICTSTR, "PYDEW_", "F602", "dictionary key variable name repeated with different values",),
	("PYDEW__F621", CMAX_DICTSTR, "PYDEW_", "F621", "too many expressions in an assignment with star-unpacking",),
	("PYDEW__F622", CMAX_DICTSTR, "PYDEW_", "F622", "two or more starred expressions in an assignment (a, *b, *c = d)",),
	("PYDEW__F631", CMAX_DICTSTR, "PYDEW_", "F631", "assertion test is a tuple, which is always True",),
	("PYDEW__F632", CMAX_DICTSTR, "PYDEW_", "F632", "use ==/!= to compare str, bytes, and int literals",),
	("PYDEW__F633", CMAX_DICTSTR, "PYDEW_", "F633", "use of >> is invalid with print function",),
	("PYDEW__F634", CMAX_DICTSTR, "PYDEW_", "F634", "if test is a tuple, which is always True",),
	("PYDEW__F701", CMAX_DICTSTR, "PYDEW_", "F701", "a break statement outside of a while or for loop",),
	("PYDEW__F702", CMAX_DICTSTR, "PYDEW_", "F702", "a continue statement outside of a while or for loop",),
	("PYDEW__F703", CMAX_DICTSTR, "PYDEW_", "F703", "a continue statement in a finally block in a loop",),
	("PYDEW__F704", CMAX_DICTSTR, "PYDEW_", "F704", "a yield or yield from statement outside of a function",),
	("PYDEW__F705", CMAX_DICTSTR, "PYDEW_", "F705", "a return statement with arguments inside a generator",),
	("PYDEW__F706", CMAX_DICTSTR, "PYDEW_", "F706", "a return statement outside of a function/method",),
	("PYDEW__F707", CMAX_DICTSTR, "PYDEW_", "F707", "an except: block as not the last exception handler",),
	("PYDEW__F721", CMAX_DICTSTR, "PYDEW_", "F721", "syntax error in doctest",),
	("PYDEW__F722", CMAX_DICTSTR, "PYDEW_", "F722", "syntax error in forward annotation",),
	("PYDEW__F723", CMAX_DICTSTR, "PYDEW_", "F723", "syntax error in type comment",),
	("PYDEW__F811", CMAX_DICTSTR, "PYDEW_", "F811", "redefinition of unused name from line N",),
	("PYDEW__F812", CMAX_DICTSTR, "PYDEW_", "F812", "list comprehension redefines name from line N",),
	("PYDEW__F821", CMAX_DICTSTR, "PYDEW_", "F821", "undefined name name",),
	("PYDEW__F822", CMAX_DICTSTR, "PYDEW_", "F822", "undefined name name in __all__",),
	("PYDEW__F823", CMAX_DICTSTR, "PYDEW_", "F823", "local variable name … referenced before assignment",),
	("PYDEW__F831", CMAX_DICTSTR, "PYDEW_", "F831", "duplicate argument name in function definition",),
	("PYDEW__F841", CMAX_DICTSTR, "PYDEW_", "F841", "local variable name is assigned to but never used",),
	("PYDEW__F901", CMAX_DICTSTR, "PYDEW_", "F901", "raise NotImplemented should be raise NotImplementedError",),
	("PYDEW__W001", CMAX_DICTSTR, "PYDEW_", "W001", "indentation warning",),
	("PYDEW__W002", CMAX_DICTSTR, "PYDEW_", "W002", "Whitespace warning",),
	("PYDEW__W003", CMAX_DICTSTR, "PYDEW_", "W003", "Blank line warning",),
	("PYDEW__W005", CMAX_DICTSTR, "PYDEW_", "W005", "Line break warning",),
	("PYDEW__W006", CMAX_DICTSTR, "PYDEW_", "W006", "Deprecation warning",),
	("PYDEW__W191", CMAX_DICTSTR, "PYDEW_", "W191", "indentation contains tabs",),
	("PYDEW__W291", CMAX_DICTSTR, "PYDEW_", "W291", "trailing whitespace",),
	("PYDEW__W292", CMAX_DICTSTR, "PYDEW_", "W292", "no newline at end of file",),
	("PYDEW__W293", CMAX_DICTSTR, "PYDEW_", "W293", "blank line contains whitespace",),
	("PYDEW__W312", CMAX_DICTSTR, "PYDEW_", "W312", "",),
	("PYDEW__W391", CMAX_DICTSTR, "PYDEW_", "W391", "blank line at end of file",),
	("PYDEW__W503", CMAX_DICTSTR, "PYDEW_", "W503", "(*) line break before binary operator",),
	("PYDEW__W504", CMAX_DICTSTR, "PYDEW_", "W504", "(*) line break after binary operator",),
	("PYDEW__W505", CMAX_DICTSTR, "PYDEW_", "W505", "(*^) doc line too long (82 > 79 characters)",),
	("PYDEW__W601", CMAX_DICTSTR, "PYDEW_", "W601", ".has_key() is deprecated, use ‘in’",),
	("PYDEW__W602", CMAX_DICTSTR, "PYDEW_", "W602", "deprecated form of raising exception",),
	("PYDEW__W603", CMAX_DICTSTR, "PYDEW_", "W603", "‘<>’ is deprecated, use ‘!=’",),
	("PYDEW__W604", CMAX_DICTSTR, "PYDEW_", "W604", "backticks are deprecated, use ‘repr()’",),
	("PYDEW__W605", CMAX_DICTSTR, "PYDEW_", "W605", "invalid escape sequence ‘x’",),
	("PYDEW__W606", CMAX_DICTSTR, "PYDEW_", "W606", "‘async’ and ‘await’ are reserved keywords starting with Python 3.7",),
	("QT_SET", CMAX_VALDFN, """['"', "'", "`"]""",),
	("Q_TBL_", CMAX_TBLDFN, "Q_", "preset local queries",),
	("Q__R0DESC", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_DEC_,),
	("Q__R0EST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R0KMFROM", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R0NM", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R0NTH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R0STH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R0WST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R1DESC", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R1EST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R1KMFROM", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R1NM", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R1NTH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R1STH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R1WST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R2DESC", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R2EST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R2KMFROM", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R2NM", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R2NTH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R2STH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R2WST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R3DESC", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R3EST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R3KMFROM", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R3NM", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__R3NTH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R3STH", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__R3WST", CMAX_TBLFLD, "Q_", "DECIMAL", _DFLT_DEC_,),
	("Q__RTS", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__SQLGROUPBY", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__SQLHAVING", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__SQLLIMIT", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__SQLORDERBY", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__SQLSELECT", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__SQLWHERE", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__timeZ", CMAX_TBLFLD, "Q_", "DATETIME", _DFLT_DT_,),
	("Q__TITLE", CMAX_TBLFLD, "Q_", "VARCHAR", _DFLT_STR_,),
	("Q__updatedZ", CMAX_TBLFLD, "Q_", "DATETIME", _DFLT_DT_,),
	("Q___endTime", CMAX_VALDFN, 'lambda DT_: f"endtime={DT_}"',),
	("Q___EVtypeRoot", CMAX_VALDFN, 'lambda EVTypeLST: f"eventtype={EVTypeLST}"'),
	("Q___minMag", CMAX_VALDFN, 'lambda MINmag: f"minmagnitude={MINmag}"',),
	("Q___orderby", CMAX_VALDFN, 'lambda orderBy: f"orderby={orderBy}"',),
	("Q___startTime", CMAX_VALDFN, 'lambda DT_: f"starttime={DT_}"',),
	("Q___URL", CMAX_VALDFN, 'lambda resultType: f"https://earthquake.usgs.gov/fdsnws/event/1/query.{resultType}?"',),
	("RID", CMAX_TBLFLD, "_TBL_SPLAT_", "INT", _DFLT_INT_, "the same in all tables",),
	("RID", CMAX_TBLFLDnoDFN, "CNTS_", "INT", _DFLT_INT_,),
	("RID", CMAX_TBLFLDnoDFN, "EQEV_", "INT", _DFLT_INT_,),
	("RID", CMAX_TBLFLDnoDFN, "FILE_", "INT", _DFLT_INT_,),
	("RID", CMAX_TBLFLDnoDFN, "PROP_", "INT", _DFLT_INT_,),
	("RID", CMAX_TBLFLDnoDFN, "Q_", "INT", _DFLT_INT_,),
	("RTN_", CMAX_TYPEDFN, "RTN_", "return in all uses",),
	("SQLLMTSTR", CMAX_VALDFN, "' limit 0, 150'", "used by the web server in web??.py",),
	("SRCS_", CMAX_TYPEDFN, "sources", "sources in all uses",),
	("SRC_", CMAX_TYPEDFN, "source", "source in all uses",),
	("STR_", CMAX_TYPEDFN, "varchar",),
	("TABSTR", CMAX_CHRDFN, "\\t",),
	("TBL_", CMAX_TYPEDFN, "TBL_", "table in all uses",),
	("timeZ_", CMAX_TYPEDFN, "time", "quick trans for time",),
	("TRIQT", CMAX_VALDFN, "DBLQT + DBLQT + DBLQT",),
	("TUP", CMAX_TYPEDFN, "tuple",),
	("TUPLE", CMAX_TYPEDFN, "tuple",),
	("TYPES_", CMAX_TYPEDFN, "types", "types in all uses",),
	("TYPE_", CMAX_TYPEDFN, "type", "type in all uses",),
	("UPD_", CMAX_TYPEDFN, "updated", "update(d) in all uses",),
	("URL_CACHEDIR", CMAX_VALDFN, 'lambda filename_: f"/home/will/.cache/earthquakesUSGS/{filename_}"',),
	("URL_CSVFEEDALL", CMAX_VALDFN, 'lambda term_: f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{term_}.csv"',),
	("URL_CSVQUERY", CMAX_VALDFN, 'lambda query_: f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv{query_}"',),
	("URL_GEOJSONALLSMRY", CMAX_VALDFN, 'lambda term_: f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{term_}.geojson"',),
	("URL_GEOJSONDETAIL", CMAX_VALDFN, 'lambda ID__: f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/{ID__}.geojson"',),
	("URL_GEOJSONDETAILQUERY", CMAX_VALDFN, 'lambda ID__: f"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid={ID__}&format=geojson"',),
	("URL_GEOJSONQUERY", CMAX_VALDFN, 'lambda query_: f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson{query_}"',),
	("VARCHAR", CMAX_TYPEDFN, "varchar",),
	("ZD3STR_", CMAX_VALDFN, f"""lambda PFX__, DB__, AX__, FLD__, NM__: f'''{DBLQT}{OBRCE}PFX__{CBRCE}{DBLQT}: {OBRCE}OBRCE{CBRCE}"DB_": "{OBRCE}DB__{CBRCE}", "AX_": "{OBRCE}AX__{CBRCE}", "FLD_": "{OBRCE}FLD__{CBRCE}", "NM_": "{OBRCE}NM__{CBRCE}"{OBRCE}CBRCE{CBRCE},'''""",),
	("_DFLT_CHR_", CMAX_STRDFN, "''",),
	("_DFLT_DEC_", CMAX_STRDFN, "0.0",),
	("_DFLT_DICT_", CMAX_STRDFN, "{}",),
	("_DFLT_DT_", CMAX_STRDFN, "'1870-01-01 00:00:01'",),
	("_DFLT_FLOAT_", CMAX_STRDFN, "0.0",),
	("_DFLT_INT_", CMAX_STRDFN, "0",),
	("_DFLT_LAT_", CMAX_STRDFN, "41.0",),
	("_DFLT_LON_", CMAX_STRDFN, "-112.0",),
	("_DFLT_POINT_", CMAX_STRDFN, "'point(0,0)'",),
	("_DFLT_STR_", CMAX_STRDFN, "''",),
	("_EMPTY_DICT_", CMAX_VALDFN, '{}',),
	("_EMPTY_LIST_", CMAX_VALDFN, '[]',),
	("_EMPTY_STR_", CMAX_VALDFN, '""',),
	("_EMPTY_TUPLE_", CMAX_VALDFN, '()',),
	("_n", CMAX_TYPEDFN, "_n", "indirectly new copy of all input",),
	("_N", CMAX_TYPEDFN, "_N", "new copy of all input",),
	("_TBL_SPLAT_TBL_", CMAX_TBLDFN, "_TBL_SPLAT_", "the default table for things like RID ",),
]
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * end of of theBigList
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of getCMNT
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def getCMNT(TUPIN_, CMNTIDX_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	THIS_LEN_ = len(TUPIN_)
	if THIS_LEN_ > CMNTIDX_:
		CMNTtoRTN = f"  # {TUPIN_[CMNTIDX_]}"
	else:
		CMNTtoRTN = ""
	return CMNTtoRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of importantLines
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def importantLines(HOW_MANY_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRTN = ""
	for TI in range(0, HOW_MANY_):
		strToRTN += IMPORTANTSTR
		if HOW_MANY_ > 1 and TI < HOW_MANY_ - 1:
			strToRTN += NEWLINE
	return strToRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of infoLines
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def infoLines(HOW_MANY_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRTN = ""
	for TI in range(0, HOW_MANY_):
		strToRTN += INFOSTR
		if HOW_MANY_ > 1 and TI < HOW_MANY_ - 1:
			strToRTN += NEWLINE
	return strToRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of commentLines
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def commentLines(HOW_MANY_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRTN = ""
	for TI in range(0, HOW_MANY_):
		strToRTN += CMNT_MRKR
		if HOW_MANY_ > 1 and TI < HOW_MANY_ - 1:
			strToRTN += NEWLINE
	return strToRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of textCommentLine
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def textCommentLine(THIS_CMNT_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	return f"# * {THIS_CMNT_}"
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of commentBlock
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def commentBlock(THIS_CMNT_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRTN = f"""{commentLines(1)}
{textCommentLine(f"{THIS_CMNT_}")}
{commentLines(1)}"""
	return strToRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of START_SECT_str
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
def START_SECT_str(THIS_CMNT_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRtn = ""
	strToRtn += f"""{commentLines(1)}
{textCommentLine(f"{THIS_CMNT_}")}
{commentLines(3)}
{importantLines(6)}"""
	return strToRtn
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of END_SECT_str
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def END_SECT_str(THIS_CMNT_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRtn = ""
	strToRtn += f"""{importantLines(6)}
{commentLines(3)}
{textCommentLine(f"{THIS_CMNT_}")}
{commentLines(1)}
"""
	return strToRtn
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of TUPDICTblock
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def TUPDICTblock(GRPNM, TUP_str, DICT_str, THIS_CMNT_, OBJTYPE="all"):
	# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
	strToRTN = ""
	if OBJTYPE == "all":
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""{commentBlock(f"all the bits for TUPDICT/TBL {GRPNM}")}

class {GRPNM}_C:
{TABSTR}{FOLD2STARTHERE}
{TABSTR}{GRPNM}EMPTY_TUP = None
{TABSTR}{GRPNM}PD_ = None
{TABSTR}FD{GRPNM}PD_ = None

{TABSTR}def __init__(self):
{NTAB(2)}self.{GRPNM}EMPTY_TUP = {OPAREN}{THIS_CMNT_}
{TUP_str}{NTAB(2)}{CPAREN}

{NTAB(2)}self.{GRPNM}PD_ = {OBRCE}{THIS_CMNT_}
{DICT_str}{NTAB(2)}{CBRCE}

{TABSTR}def __enter__(self):
{NTAB(2)}self.FD{GRPNM}PD_ = open({DBLQT}{GRPNM}PD_.py{DBLQT}, {DBLQT}tw{DBLQT})
{NTAB(2)}return self

{TABSTR}def append(self, itemToAppend, valueToAppend):
{NTAB(2)}if itemToAppend not in self.{GRPNM}PD_.keys():
{NTAB(3)}self.{GRPNM}PD_[itemToAppend] = valueToAppend

{TABSTR}def {GRPNM}EMPTY_DICT_N(self):
{NTAB(2)}return dict((x, y) for x, y in self.{GRPNM}EMPTY_TUP)

{TABSTR}def __exit__(self, exc_type, exc_val, exc_tb):
		OUTSTR = f{DBLQT}{OBRCE}repr(self.{GRPNM}PD_){CBRCE}{DBLQT}
		self.FD{GRPNM}PD_.write(OUTSTR)
		self.FD{GRPNM}PD_.flush()
		self.FD{GRPNM}PD_.close()

{TABSTR}{FOLD2ENDHERE}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	elif OBJTYPE == CMS_STANDALONECLASS:
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""{commentBlock(f"all the bits for TUPDICT/TBL {GRPNM}")}

class {GRPNM}_C:
{TABSTR}{FOLD2STARTHERE}
{TABSTR}{GRPNM}EMPTY_TUP = None
{TABSTR}{GRPNM}PD_ = None
{TABSTR}FD{GRPNM}PD_ = None

{TABSTR}def __init__(self):
{NTAB(2)}self.{GRPNM}EMPTY_TUP = {OPAREN}{THIS_CMNT_}
{TUP_str}{NTAB(2)}{CPAREN}

{NTAB(2)}self.{GRPNM}PD_ = {OBRCE}{THIS_CMNT_}
{DICT_str}{NTAB(2)}{CBRCE}

{TABSTR}def {GRPNM}EMPTY_DICT_N(self):
{NTAB(2)}return dict((x, y) for x, y in self.{GRPNM}EMPTY_TUP)

{TABSTR}{FOLD2ENDHERE}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	elif OBJTYPE == CMS_STANDALONECLASSPKL:
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""{commentBlock(f"all the bits for TUPDICT/TBL {GRPNM}")}

class {GRPNM}_C:
{TABSTR}{GRPNM}EMPTY_TUP = None
{TABSTR}{GRPNM}PD_ = None
{TABSTR}FD{GRPNM}PD_ = None

{TABSTR}def __init__(self):
{NTAB(2)}self.{GRPNM}EMPTY_TUP = {OPAREN}{THIS_CMNT_}
{TUP_str}{NTAB(2)}{CPAREN}

{NTAB(2)}self.{GRPNM}PD_ = {OBRCE}{THIS_CMNT_}
{DICT_str}{NTAB(2)}{CBRCE}

{TABSTR}def {GRPNM}EMPTY_DICT_N(self):
{NTAB(2)}return dict((x, y) for x, y in self.{GRPNM}EMPTY_TUP)


{TABSTR}def savePKL(self):
{NTAB(2)}self.FDPFXD3_DICT = open("PFXD3_DICT.pkl", "wb")
{NTAB(2)}PD.dump(self.PFXD3_DICT, self.FDPFXD3_DICT)
{NTAB(2)}self.FDPFXD3_DICT.close()
{NTAB(2)}self.FDPFXD3_LST = open("PFXD3_LST.pkl", "wb")
{NTAB(2)}PD.dump(self.PFXD3_LST, self.FDPFXD3_LST)
{NTAB(2)}self.FDPFXD3_LST.close()

{TABSTR}def loadPKL(self):
{NTAB(2)}if PATH.isfile("PFXD3_DICT.pkl")and PATH.isfile("PFXD3_LST.pkl"):
{NTAB(3)}self.FDPFXD3_DICT = open("PFXD3_DICT.pkl", "rb")
{NTAB(3)}self.PFXD3_DICT = PD.load(self.FDPFXD3_DICT)
{NTAB(3)}self.FDPFXD3_LST = open("PFXD3_LST.pkl", "rb")
{NTAB(3)}self.PFXD3_LST = PD.load(self.FDPFXD3_LST)
{NTAB(2)}else:
{NTAB(3)}self.savePKL()

{TABSTR}def __enter__(self):
{NTAB(2)}# self.loadPKL()
{NTAB(2)}pass

{TABSTR}def __exit__(self, exc_type, exc_val, exc_tb):
{NTAB(2)}self.savePKL()
{NTAB(2)}with open("TUP.txt", "tw") as FDOut:
{NTAB(3)}for thisKey, thisEntry in self.PFXD3_DICT.items():
{NTAB(3)}{TABSTR}FDOut.write(f" " "{TABSTR}("{OBRCE}thisEntry['NM_']{CBRCE}", CMAX_D3STR, "PFXD3_", "{OBRCE}thisKey{CBRCE}", "{OBRCE}thisEntry['DB_']{CBRCE}", "{OBRCE}thisEntry['AX_']{CBRCE}", "{OBRCE}thisEntry['FLD_']{CBRCE}",),
" " ",),

"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	elif OBJTYPE == CMS_STANDALONE:
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""{commentBlock(f"all the bits for TUPDICT/TBL {GRPNM}")}
{GRPNM}EMPTY_TUP = {OPAREN}{THIS_CMNT_}
{TABSTR}{FOLD0STARTHERE}
{TUP_str}{CPAREN}
{FOLD0ENDHERE}

{GRPNM}PD_ = {OBRCE}{THIS_CMNT_}
{TABSTR}{FOLD0STARTHERE}
{DICT_str}{CBRCE}
{FOLD0ENDHERE}


def {GRPNM}EMPTY_DICT_N():
{TABSTR}return dict((x, y) for x, y in {GRPNM}EMPTY_TUP)


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	return strToRTN
	# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make a TUP block and return it
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def TUPblock(GRPNM, TUP_str, OBJTYPE, suffix, THIS_CMNT_):
	# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
	strToRTN = ""
	if OBJTYPE == "standaloneClass":
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""# not currently implemented fully
class {GRPNM}_C:
{TABSTR}{FOLD0STARTHERE}
{TABSTR}{GRPNM}TUP{suffix} = None
{TABSTR}FD{GRPNM}TUP{suffix} = None

{NTAB(2)}{GRPNM}TUP{suffix} = {OPAREN}{THIS_CMNT_}
{TUP_str}{NTAB(2)}{CPAREN}
{FOLD0ENDHERE}
"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	elif OBJTYPE == "class":
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""{NTAB(2)}self.{GRPNM}TUP{suffix} = {OPAREN}{THIS_CMNT_}
{TUP_str}{NTAB(2)}{CPAREN}

"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	return strToRTN
	# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make a DICT block and return it
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def DICTblock(GRPNM, DICT_str, OBJTYPE, suffix, THISTYPE, THIS_CMNT_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	strToRTN = ""
	if OBJTYPE == CMS_STANDALONECLASS:
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		strToRTN = f"""class {GRPNM}{suffix}_C:{THIS_CMNT_}
{TABSTR}{FOLD0STARTHERE}
{TABSTR}{GRPNM}DICT{suffix} = None
{TABSTR}FD{GRPNM}DICT{suffix} = None

{TABSTR}def __init__(self):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}self.{GRPNM}DICT{suffix} = {OBRCE}
{DICT_str}{NTAB(2)}{CBRCE}
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def __enter__(self):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}self.FD{GRPNM}DICT{suffix} = open({DBLQT}{GRPNM}DICT{suffix}.py{DBLQT}, {DBLQT}tw{DBLQT})
{NTAB(2)}return self

{TABSTR}def append(self, itemToAppend, valueToAppend):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}if itemToAppend not in self.{GRPNM}DICT{suffix}.keys():
{NTAB(3)}self.{GRPNM}DICT{suffix}[itemToAppend] = valueToAppend

{TABSTR}def __exit__(self, exc_type, exc_val, exc_tb):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}OUTSTR = f{DBLQT}{OBRCE}repr(self.{GRPNM}DICT){CBRCE}{DBLQT}
{NTAB(2)}self.FD{GRPNM}DICT.write(OUTSTR)
{NTAB(2)}self.FD{GRPNM}DICT.flush()
{NTAB(2)}self.FD{GRPNM}DICT.close()

{TABSTR}{FOLD0ENDHERE}

"""
# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif OBJTYPE == CMS_STANDALONE:
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		strToRTN = f"""{GRPNM}DICT{suffix}: Dict[{THISTYPE}] = {OBRCE}{THIS_CMNT_}
{FOLD0STARTHERE}
{DICT_str}{CBRCE}
{FOLD0ENDHERE}
"""
# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	elif OBJTYPE == CMS_CLASS:
		# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
		strToRTN = f"""{NTAB(2)}self.{GRPNM}{suffix} = {OBRCE}{THIS_CMNT_}
{NTAB(3)}{FOLD1STARTHERE}
{DICT_str}{NTAB(2)}{CBRCE}
{NTAB(2)}{FOLD1ENDHERE}

"""
# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣
	return strToRTN
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * make a LST block and return it
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def LSTblock(GRPNM, LST_str, OBJTYPE, suffix, itemType, THIS_CMNT_):
	# fold here ⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥⥥
	strToRTN = ""
	if OBJTYPE == "standaloneClass":
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""class {GRPNM}_C:{THIS_CMNT_}
{TABSTR}{FOLD0STARTHERE}
{TABSTR}{GRPNM}LST{suffix}: List[itemType] = None
{TABSTR}FD{GRPNM}LST{suffix}: = None

{TABSTR}def __init__(self):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}self.{GRPNM}LST{suffix}: List[Any] = {OBRKT}{THIS_CMNT_}
{LST_str}{NTAB(2)}{CBRKT}
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def __enter__(self):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}self.FD{GRPNM}LST{suffix}: List[Any] = open({DBLQT}{GRPNM}LST{suffix}.py{DBLQT}, {DBLQT}tw{DBLQT})
{NTAB(2)}return self
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def append(self, valueToAppend):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}if valueToAppend not in self.{GRPNM}LST{suffix}:
{NTAB(3)}self.{GRPNM}LST{suffix}.append(valueToAppend)
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def __exit__(self, exc_type, exc_val, exc_tb):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}OUTSTR = f{DBLQT}{OBRCE}repr(self.{GRPNM}LST{suffix}){CBRCE}{DBLQT}
{NTAB(2)}self.FD{GRPNM}LST{suffix}.write(OUTSTR)
{NTAB(2)}self.FD{GRPNM}LST{suffix}.flush()
{NTAB(2)}self.FD{GRPNM}LST{suffix}.close()
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}{FOLD0ENDHERE}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	elif OBJTYPE == "standalone":
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		strToRTN = f"""{GRPNM}LST{suffix}: List[{itemType}] = {OBRKT}{THIS_CMNT_}
{TABSTR}{FOLD0STARTHERE}
{LST_str}{CBRKT}
{FOLD0ENDHERE}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
	return strToRTN
	# fold here ⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣⥣


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of main
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!


def __main__():
	# @auto-fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	global CM_AXDFN_str, CM_AXLST_str, CM_CHR_str, CM_CMBLDFN_str, CM_CMDFN_str, CM_ORGD3DICTDICT_, CM_ORGD3LSTDICT_, CM_ORGDFLT_str, CM_ORGDFN_str, \
		CM_ORGDICTCMNT_, CM_ORGDICTLSTDICTCMNT_, CM_ORGDICTLSTDICTOT_, CM_ORGDICTLSTDICT_, CM_ORGDICTLSTLSTDICTCMNT_, CM_ORGDICTLSTLSTDICTOT_, \
		CM_ORGDICTLSTLSTDICT_, CM_ORGDICTOT_, CM_ORGDICT_, CM_ORGLSTCLSDICTCMNT_, CM_ORGLSTCLSDICTOT_, CM_ORGLSTCLSDICT_, CM_ORGLSTDICTCMNT_, \
		CM_ORGLSTDICTOT_, CM_ORGLSTDICT_, CM_ORGTBLDFN_str, CM_ORGTBLDICTCMNT_, CM_ORGTBLDICT_, CM_ORGTBLnoWRTLST_str, CM_ORGTBLTUPDICTCMNT_, \
		CM_ORGTBLTUPDICTOT_, CM_ORGTBLTUPDICT_, CM_ORGTUPDICTDICTCMNT_, CM_ORGTUPDICTDICTOT_, CM_ORGTUPDICTDICT_, CM_ORGTUPDICTTUPDICTCMNT_, \
		CM_ORGTUPDICTTUPDICTOT_, CM_ORGTUPDICTTUPDICT_, CM_ORGTUPLSTDICTCMNT_, CM_ORGTUPLSTDICTOT_, CM_ORGTUPLSTDICT_, CM_ORGTUP_DICTCMNT_, \
		CM_ORGTUP_DICTOT_, CM_ORGTUP_DICT_, CM_ORGTYPE_str, CM_PD_, CM_PDCMNT_, CM_PDDFN_str, CM_PD_str, CM_PODGODICTCMNT_, CM_PODGODICT_, \
		CM_PODGRPDICTCMNT_, CM_PODGRPDICT_, CM_PODPDCMNT_, CM_PODPD_, CM_PODTUPDICTCMNT_, CM_PODTUPDICT_, CM_STRDFN_str, CM_STR_str, \
		CM_TYPEDFN_str, CM_VALSTR, FDconstants, FDconstMaker, CM_ORGTUP_DICTOT_, CM_PODTUPOT_

	# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
	# * start of __main__ code proper
	# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
	# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
	# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
	with open(mainConstFilename, "tw") as FDconstants, \
			open(constMakerConstFilename, "tw") as FDconstMaker:
		for THIS_entry in theBigList:
			if DBGPD_[DBGLVL] > 5:
				print(f"""this entry: {THIS_entry}
""")
			THIS_name = THIS_entry[CMBL_NM0]
			THIS_CMAX_ = THIS_entry[CMBL_AX1]
			if THIS_CMAX_ == CMAX_NOP or THIS_CMAX_ not in CMAX_LST_:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_AX:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT2)
				CM_AXDFN_str += f"""{THIS_name} = {DBLQT}{THIS_name}{DBLQT}{THIS_CMNT_}
"""
				CM_AXLST_str += f"""{TABSTR}{THIS_name},{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_CHRDFN, CMAX_STRDFN, CMAX_VALDFN]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_VAL_ = THIS_entry[CMBL_STR2]
				if THIS_CMAX_ == CMAX_CHRDFN:
					CM_CHR_str += f"""{THIS_name} = {DBLQT}{THIS_VAL_}{DBLQT}{THIS_CMNT_}
"""
				else:
					if THIS_CMAX_ == CMAX_VALDFN:
						LQT_str = ""
					else:
						LQT_str = DBLQT
					CM_STR_str += f"""{THIS_name} = {LQT_str}{THIS_VAL_}{LQT_str}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_CMBL:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_VAL_ = THIS_entry[CMBL_VAL2]
				CM_CMBLDFN_str += f"""{THIS_name} = {THIS_VAL_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_CMSTR:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_VAL_ = THIS_entry[CMBL_VAL2]
				CM_CMDFN_str += f"""{THIS_name} = {DBLQT}{THIS_VAL_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_CMVAL:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_VAL_ = THIS_entry[CMBL_VAL2]
				CM_STRDFN_str += f"""{THIS_name} = {THIS_VAL_}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_DICTDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_OT_ = THIS_entry[CMBL_OT3]
				THIS_TYPE_ = THIS_entry[CMBL_TPRTYPE4]
				if THIS_GRP_ not in CM_ORGDICT_.keys():
					CM_ORGDICT_[THIS_GRP_] = ""
				CM_ORGDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				CM_ORGDICTOT_[THIS_GRP_] = f"{THIS_OT_}"
				CM_ORGDICTTYPES_[THIS_GRP_] = f"{THIS_TYPE_}"
				CM_ORGDFN_str += f"""{THIS_GRP_} = {DBLQT}{THIS_GRP_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_DICTSTR, CMAX_DICTSTRnoDFN, CMAX_DICTVAL]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_VARNM_ = THIS_entry[CMBL_VARNM3]
				THIS_VAL_ = THIS_entry[CMBL_VAL4]
				THIS_OT_ = CM_ORGDICTOT_[THIS_GRP_]
				if THIS_GRP_ not in CM_ORGDICT_.keys():
					CM_ORGDICT_[THIS_GRP_] = ""
				if THIS_CMAX_ in [CMAX_DICTSTR, CMAX_DICTSTRnoDFN]:
					LQT_str = DBLQT
				else:
					LQT_str = ""
				if THIS_OT_ in [CMS_CLASS, CMS_STANDALONECLASS]:
					LTABSTR = NTAB(3)
				elif THIS_OT_ == CMS_STANDALONE:
					LTABSTR = TABSTR
				CM_ORGDICT_[THIS_GRP_] += f"""{LTABSTR}{LQT_str}{THIS_VARNM_}{LQT_str}: {LQT_str}{THIS_VAL_}{LQT_str},{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_name} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				if THIS_CMAX_ == CMAX_DICTSTR:
					CM_ORGDFN_str += f"""{THIS_VARNM_} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_LSTDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_TYPE_ = THIS_entry[CMBL_TPRTYPE4]
				if THIS_GRP_ not in CM_ORGLSTDICT_.keys():
					CM_ORGLSTDICT_[THIS_GRP_] = ""
				CM_ORGLSTDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				CM_ORGLSTDICTOT_[THIS_GRP_] = "standalone"
				CM_ORGLSTDICTTYPES_[THIS_GRP_] = f"{THIS_TYPE_}"
				CM_ORGDFN_str += f"""{THIS_GRP_} = {DBLQT}{THIS_GRP_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_LSTSTR, CMAX_LSTVAL]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT4)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_VARNM_ = THIS_entry[CMBL_VARNM3]
				THIS_OT_ = CM_ORGLSTDICTOT_[THIS_GRP_]
				if THIS_GRP_ not in CM_ORGLSTDICT_.keys():
					CM_ORGLSTDICT_[THIS_GRP_] = ""
				if THIS_CMAX_ == CMAX_LSTSTR:
					LQT_str = DBLQT
				else:
					LQT_str = ""
				if THIS_OT_ == CMS_STANDALONE:
					LTABSTR = TABSTR
				else:  # if THIS_OT_ in [CMS_CLASS, CMS_STANDALONECLASS, ]:
					LTABSTR = NTAB(3)
				CM_ORGLSTDICT_[THIS_GRP_] += f"""{LTABSTR}{LQT_str}{THIS_VARNM_}{LQT_str},{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_VARNM_} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_PD:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT4)
				THISPDNM_ = THIS_entry[CMBL_PDNM2]
				THIS_VAL_ = THIS_entry[CMBL_PDVAL3]
				CM_PD_str += f"""{TABSTR}{THISPDNM_}: {THIS_VAL_},{THIS_CMNT_}
"""
				CM_PDDFN_str += f"""{THISPDNM_} = {DBLQT}{THISPDNM_}{DBLQT}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_TBLDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				CM_ORGTBLDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_ORGTBLDICT_.keys():
					CM_ORGTBLDICT_[THIS_GRP_] = ""
				CM_ORGTBLDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_ORGTBLTUPDICT_.keys():
					CM_ORGTBLTUPDICT_[THIS_GRP_] = ""
				CM_ORGTBLTUPDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				CM_ORGTBLDFN_str += f"""{THIS_name} = {DBLQT}{THIS_GRP_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_TBLFLD, CMAX_TBLFLDnoWRT, CMAX_TBLFLDnoDFN]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				if THIS_GRP_ not in CM_ORGTBLDICT_.keys():
					CM_ORGTBLDICT_[THIS_GRP_] = ""
				CM_ORGTBLDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_ORGTBLTUPDICT_.keys():
					CM_ORGTBLTUPDICT_[THIS_GRP_] = ""
				CM_ORGTBLTUPDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				THIS_TYPE_ = THIS_entry[CMBL_TBLTYPE3]
				THIS_DFLT_ = THIS_entry[CMBL_TBLDFLT4]
				if THIS_CMAX_ != CMAX_TBLFLDnoDFN:
					CM_ORGTBLDFN_str += f"""{THIS_name} = {DBLQT}{THIS_name}{DBLQT}{THIS_CMNT_}
"""
					CM_ORGDFLT_str += f"""{TABSTR}{THIS_name}: {THIS_DFLT_},{THIS_CMNT_}
"""
					CM_ORGTYPE_str += f"""{TABSTR}{THIS_name}: {THIS_TYPE_},{THIS_CMNT_}
"""
				CM_ORGTBLDICT_[THIS_GRP_] += f"""{NTAB(3)}{THIS_name}: {THIS_DFLT_},{THIS_CMNT_}
"""
				CM_ORGTBLTUPDICT_[THIS_GRP_] += f"""{NTAB(3)}{OPAREN}{THIS_name}, {THIS_DFLT_},{CPAREN},{THIS_CMNT_}
"""
				if THIS_CMAX_ == CMAX_TBLFLDnoWRT:
					CM_ORGTBLnoWRTLST_str += f"""{TABSTR}{THIS_name},{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_TUPDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_name, CMBL_CMNT4)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_OT_ = THIS_entry[CMBL_OT3]
				if THIS_GRP_ not in CM_ORGTUP_DICT_.keys():
					CM_ORGTUP_DICT_[THIS_GRP_] = ""
				CM_ORGTUP_DICTOT_[THIS_GRP_] = f"{THIS_OT_}"
				CM_ORGTUP_DICT_[THIS_GRP_] = f"{THIS_CMNT_}"
				CM_ORGDFN_str += f"""{THIS_name} = {DBLQT}{THIS_GRP_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_TUPSTR, CMAX_TUPVAL]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_VARNM_ = THIS_entry[CMBL_VARNM3]
				THIS_VAL_ = THIS_entry[CMBL_VAL4]
				if THIS_GRP_ not in CM_ORGTUP_DICT_.keys():
					CM_ORGTUP_DICT_[THIS_GRP_] = ""
				if THIS_CMAX_ == CMAX_TUPSTR:
					LQT_str = DBLQT
				else:
					LQT_str = ""
				CM_ORGTUP_DICT_[THIS_GRP_] += f"""{NTAB(3)}{OPAREN}{THIS_VARNM_}, {LQT_str}{THIS_VAL_}{LQT_str}{CPAREN}{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_VARNM_} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_name} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_TUPDICTDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT4)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_OT_ = THIS_entry[CMBL_OT3]
				if THIS_GRP_ not in CM_ORGTUPDICTDICT_.keys():
					CM_ORGTUPDICTDICT_[THIS_GRP_] = ""
				CM_ORGTUPDICTDICTOT_[THIS_GRP_] = f"{THIS_OT_}"
				CM_ORGTUPDICTDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_ORGTUPDICTTUPDICT_.keys():
					CM_ORGTUPDICTTUPDICT_[THIS_GRP_] = ""
				CM_ORGTUPDICTTUPDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				CM_ORGTUPDICTTUPDICTOT_[THIS_GRP_] = f"{THIS_OT_}"
				CM_ORGDFN_str += f"""{THIS_GRP_} = {DBLQT}{THIS_GRP_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_TUPDICTSTR, CMAX_TUPDICTVAL]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_VARNM_ = THIS_entry[CMBL_VARNM3]
				THIS_VAL_ = THIS_entry[CMBL_VAL4]
				if THIS_GRP_ not in CM_ORGTUPDICTDICT_.keys():
					CM_ORGTUPDICTDICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGTUPDICTTUPDICT_.keys():
					CM_ORGTUPDICTTUPDICT_[THIS_GRP_] = ""
				if CM_ORGTUPDICTTUPDICTOT_[THIS_GRP_] == CMS_STANDALONE:
					LTABSTR = f"{TABSTR}"
				elif CM_ORGTUP_DICTOT_[THIS_GRP_] == CMS_CLASS:
					LTABSTR = f"{NTAB(3)}"
				if THIS_CMAX_ == CMAX_TUPSTR:
					LQT_str = DBLQT
				else:
					LQT_str = ""
				CM_ORGTUPDICTDICT_[THIS_GRP_] += f"""{LTABSTR}{THIS_VARNM_}: {LQT_str}{THIS_VAL_}{LQT_str},{THIS_CMNT_}
"""
				CM_ORGTUPDICTTUPDICT_[THIS_GRP_] += f"""{LTABSTR}{OPAREN}{THIS_VARNM_}, {LQT_str}{THIS_VAL_}{LQT_str},{CPAREN},{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_VARNM_} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_name} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_TYPEDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_TYPE_ = THIS_entry[CMBL_TYPE2]
				CM_TYPEDFN_str += f"""{THIS_name} = {DBLQT}{THIS_TYPE_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_PODDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT4)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_OT_ = THIS_entry[CMBL_OT3]
				if THIS_GRP_ not in CM_PODGRPDICT_:
					CM_PODGRPDICT_[THIS_GRP_] = ""
				CM_PODGRPDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_PODPD_:
					CM_PODPD_[THIS_GRP_] = ""
				CM_PODPDCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_PODGODICT_:
					CM_PODGODICT_[THIS_GRP_] = ""
				CM_PODGODICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				if THIS_GRP_ not in CM_PODTUPDICT_.keys():
					CM_PODTUPOT_[THIS_GRP_] = f"{THIS_OT_}"
				CM_PODTUPDICTCMNT_[THIS_GRP_] = f"{THIS_CMNT_}"
				CM_ORGDFN_str += f"""{THIS_GRP_} = {DQTSTR}{THIS_GRP_}{DQTSTR}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_PODSTR, CMAX_PODVAL]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				CRNT_VAL_ = THIS_entry[CMBL_VAL4]
				THIS_VARNM_ = THIS_entry[CMBL_VARNM3]
				if THIS_GRP_ not in CM_PODGRPDICT_:
					CM_PODGRPDICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_PODPD_:
					CM_PODPD_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_PODGODICT_:
					CM_PODGODICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_PODTUPDICT_.keys():
					CM_PODTUPDICT_[THIS_GRP_] = ""
				if THIS_CMAX_ == CMAX_PODSTR:
					LQT_str = DBLQT
				else:
					LQT_str = _EMPTY_STR_
				CM_PODGRPDICT_[THIS_GRP_] += f"""{NTAB(3)}{LQT_str}{THIS_VARNM_}{LQT_str}: "{CRNT_VAL_}",{THIS_CMNT_}
"""
				CM_PODPD_[THIS_GRP_] += f"""{NTAB(3)}{LQT_str}{THIS_VARNM_}{LQT_str}: None,{THIS_CMNT_}
"""
				CM_PODTUPDICT_[THIS_GRP_] += f"""{NTAB(3)}{OPAREN}{LQT_str}{THIS_VARNM_}{LQT_str}, None,{CPAREN},{THIS_CMNT_}
"""
				if THIS_VARNM_[0] == "-":
					CM_PODGODICT_[THIS_GRP_] += f"{THIS_VARNM_[1]}:"
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_DICTLSTDFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				if THIS_GRP_ not in CM_ORGDICTLSTDICT_.keys():
					CM_ORGDICTLSTDICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGDICTLSTLSTDICT_.keys():
					CM_ORGDICTLSTLSTDICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGDICTLSTDICTCMNT_.keys():
					CM_ORGDICTLSTDICTCMNT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGDICTLSTLSTDICTCMNT_.keys():
					CM_ORGDICTLSTLSTDICT_[THIS_GRP_] = ""
				CM_ORGDFN_str += f"""{THIS_GRP_} = {DBLQT}{THIS_GRP_}{DBLQT}{THIS_CMNT_}
"""
				CM_ORGDICTLSTDICTCMNT_[THIS_GRP_] = THIS_CMNT_
				CM_ORGDICTLSTLSTDICTCMNT_[THIS_GRP_] = THIS_CMNT_
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_DICTLSTSTR, CMAX_DICTLSTVAL]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT5)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_VARNM_ = THIS_entry[CMBL_VARNM3]
				THIS_VAL_ = THIS_entry[CMBL_VAL4]
				if THIS_GRP_ not in CM_ORGDICTLSTDICT_.keys():
					CM_ORGDICTLSTDICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGDICTLSTLSTDICT_.keys():
					CM_ORGDICTLSTLSTDICT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGDICTLSTDICTCMNT_.keys():
					CM_ORGDICTLSTDICTCMNT_[THIS_GRP_] = ""
				if THIS_GRP_ not in CM_ORGDICTLSTLSTDICTCMNT_.keys():
					CM_ORGDICTLSTLSTDICT_[THIS_GRP_] = ""
				if THIS_CMAX_ in [CMAX_DICTSTR, CMAX_DICTSTRnoDFN]:
					LQT_str = DBLQT
				else:
					LQT_str = ""
				CM_ORGDICTLSTDICT_[THIS_GRP_] += f"""{NTAB(3)}{LQT_str}{THIS_VARNM_}{LQT_str}: {LQT_str}{THIS_VAL_}{LQT_str},{THIS_CMNT_}
"""
				CM_ORGDICTLSTLSTDICT_[THIS_GRP_] += f"""{NTAB(3)}{THIS_VARNM_},{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_name} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				if THIS_CMAX_ == CMAX_DICTLSTSTR:
					CM_ORGDFN_str += f"""{THIS_VARNM_} = {DBLQT}{THIS_VARNM_}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_D3DFN:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				# THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				if THIS_GRP_ not in CM_ORGD3DICTDICT_.keys():
					CM_ORGD3DICTDICT_[THIS_GRP_] = ""
					CM_ORGD3LSTDICT_[THIS_GRP_] = ""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ in [CMAX_D3STR]:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT7)
				THIS_GRP_ = THIS_entry[CMBL_GRPNM2]
				THIS_PFX = THIS_entry[CMBL_D3PFX3]
				THIS_DB = THIS_entry[CMBL_D3DB4]
				THIS_AX = THIS_entry[CMBL_D3AX5]
				THIS_FLD = THIS_entry[CMBL_D3FLD6]
				if THIS_GRP_ not in CM_ORGD3DICTDICT_.keys():
					CM_ORGD3DICTDICT_[THIS_GRP_] = ""
					CM_ORGD3LSTDICT_[THIS_GRP_] = ""
				CM_ORGD3DICTDICT_[THIS_GRP_] += f"""{_D3BLKSTR(THIS_PFX, THIS_DB, THIS_AX, THIS_FLD, THIS_name)}
"""
				CM_ORGD3LSTDICT_[THIS_GRP_] += f"""{NTAB(3)}{DBLQT}{THIS_AX}{DBLQT},{THIS_CMNT_}
"""
				CM_ORGDFN_str += f"""{THIS_name} = {DBLQT}{THIS_AX}{DBLQT}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			elif THIS_CMAX_ == CMAX_CMDICTVALEMPTY:
				# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
				THIS_CMNT_ = getCMNT(THIS_entry, CMBL_CMNT3)
				THIS_TYPE_ = THIS_entry[CMBL_VAL2]
				CM_STRDFN_str += f"""{THIS_name}: Dict[{THIS_TYPE_}] = {OBRCE}{CBRCE}{THIS_CMNT_}
"""
				continue
				# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		# for THIS_entry in theBigList:
	# with open(mainConstFilename, "tw") as FDconstants, \



# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# %_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_
# * end of __main__ code proper
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of write constantsNew.py
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!

		# for THIS_entry in theBigList:
	# with open(mainConstFilename, "tw") as FDconstants, \

		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{START_SECT_str(f"start of constants.py cut {currentTS}")}


{commentBlock(f"start of DBGPD block")}


{CM_PDDFN_str}

DBGPD_: Dict[str, Any] = {OBRCE}
{CM_PD_str}{CBRCE}


{commentBlock("start of CHR_ defines")}


{CM_CHR_str}

{commentBlock("start of STR_ defines")}


{CM_STR_str}

{commentBlock("_D3BLKSTR PFX block returned")}

_D3BLKSTR = lambda PFX__, DB__, AX__, FLD__, NM__: f{TRIQT}{OBRCE}NTAB(3){CBRCE}{DBLQT}{OBRCE}PFX__{CBRCE}{DBLQT}: {OBRCE}OBRCE{CBRCE}
{OBRCE}NTAB(4){CBRCE}{OBRCE}FOLD0STARTHERE{CBRCE}
{OBRCE}NTAB(4){CBRCE}{DBLQT}DB_{DBLQT}: {DBLQT}{OBRCE}DB__{CBRCE}{DBLQT},
{OBRCE}NTAB(4){CBRCE}{DBLQT}AX_{DBLQT}: {DBLQT}{OBRCE}AX__{CBRCE}{DBLQT},
{OBRCE}NTAB(4){CBRCE}{DBLQT}FLD_{DBLQT}: {DBLQT}{OBRCE}FLD__{CBRCE}{DBLQT},
{OBRCE}NTAB(4){CBRCE}{DBLQT}NM_{DBLQT}: {DBLQT}{OBRCE}NM__{CBRCE}{DBLQT}, {OBRCE}CBRCE{CBRCE},
{OBRCE}NTAB(4){CBRCE}{OBRCE}FOLD0ENDHERE{CBRCE}{TRIQT}


{commentBlock("type defines")}


{CM_TYPEDFN_str}

{commentBlock("TBL defines")}


{CM_ORGTBLDFN_str}

TBLnoWRTLST = {OBRCE}
{CM_ORGTBLnoWRTLST_str}{CBRCE}


TYPE_DICT_ = {OBRCE}
{CM_ORGTYPE_str}{CBRCE}


DFLT_DICT_ = {OBRCE}
{CM_ORGDFLT_str}{CBRCE}


{commentBlock("start normal defines")}


{CM_ORGDFN_str}

{commentBlock("start of all things TBL")}


"""
		# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		for THIS_GRP_, THIS_VAL_ in CM_ORGTBLDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			OUT_STR_ = TUPDICTblock(THIS_GRP_, CM_ORGTBLTUPDICT_[THIS_GRP_], THIS_VAL_, CM_ORGTBLTUPDICTCMNT_[THIS_GRP_], "all")
			FDconstants.write(OUT_STR_)
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{commentBlock("start all of the TUPDICT")}


"""
		# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		for THIS_GRP_, THIS_VAL_ in CM_ORGTUPDICTDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			THIS_OT_ = CM_ORGTUPDICTDICTOT_[THIS_GRP_]
			OUT_STR_ = TUPDICTblock(THIS_GRP_, CM_ORGTUPDICTTUPDICT_[THIS_GRP_], THIS_VAL_, CM_ORGTUPDICTTUPDICTCMNT_[THIS_GRP_], THIS_OT_)
			FDconstants.write(OUT_STR_)
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{commentBlock("start all of the TUP")}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		OUT_STR_ = ""
		for THIS_GRP_, THIS_VAL_ in CM_ORGTUP_DICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			THIS_OT_ = CM_ORGTUP_DICTOT_[THIS_GRP_]
			THIS_TYPE_ = CM_ORGTUP_DICTTYPES_[THIS_GRP_]
			OUT_STR_ = TUPblock(THIS_GRP_, THIS_VAL_, THIS_OT_, "", CM_ORGTUP_DICTCMNT_[THIS_GRP_])
			FDconstants.write(OUT_STR_)
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{commentBlock("start all of the DICT")}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		for THIS_GRP_, THIS_VAL_ in CM_ORGDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			THIS_OT_ = CM_ORGDICTOT_[THIS_GRP_]
			THIS_TYPE_ = CM_ORGDICTTYPES_[THIS_GRP_]
			OUT_STR_ = DICTblock(THIS_GRP_, THIS_VAL_, THIS_OT_, "", THIS_TYPE_, CM_ORGDICTCMNT_[THIS_GRP_]) + NEWLINE
			FDconstants.write(OUT_STR_)
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{commentBlock("start all of the LST")}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		for THIS_GRP_, THIS_VAL_ in CM_ORGLSTDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			OUT_STR_ = LSTblock(THIS_GRP_, THIS_VAL_, CM_ORGLSTDICTOT_[THIS_GRP_], "", CM_ORGLSTDICTTYPES_[THIS_GRP_], CM_ORGLSTDICTCMNT_[THIS_GRP_])
			FDconstants.write(OUT_STR_)
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{commentBlock("start all of the DICTLST")}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		for THIS_GRP_, value in CM_ORGDICTLSTDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			OUT_STR_ = ""
			THIS_CMNT_ = CM_ORGDICTLSTDICT_[THIS_GRP_]
			# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
			OUT_STR_ += f"""class {THIS_GRP_}_C:
{TABSTR}{THIS_GRP_}DLD_ = None
{TABSTR}{THIS_GRP_}DLL = None
{TABSTR}FD{THIS_GRP_} = None

{TABSTR}def __init__(self):
{NTAB(2)}self.{THIS_GRP_}DLD_ = {OBRCE}{THIS_CMNT_}
{value}{NTAB(2)}{CBRCE}
"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			FDconstants.write(OUT_STR_)
			OUT_STR_ = ""
			value = CM_ORGDICTLSTLSTDICT_[THIS_GRP_]
			THIS_CMNT_ = CM_ORGDICTLSTLSTDICTCMNT_[THIS_GRP_]
			# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
			OUT_STR_ += f"""
{NTAB(2)}self.{THIS_GRP_}DLL_ = {OBRKT}{THIS_CMNT_}
{value}{NTAB(2)}{CBRKT}

{TABSTR}def __enter__(self):
{NTAB(2)}self.FD{THIS_GRP_} = open({DBLQT}{THIS_GRP_}DL.py{DBLQT}, {DBLQT}tw{DBLQT})
{NTAB(2)}return self

{TABSTR}def append(self, itemToAppend, valueToAppend):
{NTAB(2)}if itemToAppend not in self.{THIS_GRP_}DLD_.keys():
{NTAB(3)}self.{THIS_GRP_}DLD_[itemToAppend] = valueToAppend
{NTAB(3)}self.{THIS_GRP_}DLL_.append(valueToAppend)

{TABSTR}def __exit__(self, exc_type, exc_val, exc_tb):
{NTAB(2)}OUTSTR = f{DBLQT}{OBRCE}repr(self.{THIS_GRP_}DLD_){CBRCE}{DBLQT}
{NTAB(2)}self.FD{THIS_GRP_}.write(OUTSTR)
{NTAB(2)}OUTSTR = f{DBLQT}{OBRKT}repr(self.{THIS_GRP_}DLL_){CBRKT}{DBLQT}
{NTAB(2)}self.FD{THIS_GRP_}.write(OUTSTR)
{NTAB(2)}self.FD{THIS_GRP_}.flush()
{NTAB(2)}self.FD{THIS_GRP_}.close()

"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			FDconstants.write(OUT_STR_)
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{commentBlock("start all of the POD")}


"""
		# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstants.write(OUT_STR_)
		OUT_STR_ = ""
		for THIS_GRP_, value in CM_PODGRPDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			OUT_STR_ = ""
			# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
			OUT_STR_ += f"""class {THIS_GRP_}_C:
{TABSTR}{THIS_GRP_}DICTPOD_ = None
{TABSTR}{THIS_GRP_}DICTPODPD_ = None
{TABSTR}{THIS_GRP_}TUPEMPTY = None

{TABSTR}def __init__(self):
"""
			# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			THIS_CMNT_ = CM_PODGRPDICTCMNT_[THIS_GRP_]
			OUT_STR_ += DICTblock(THIS_GRP_, value, CMS_CLASS, "POD_", "Any, Any", THIS_CMNT_)
			FDconstants.write(OUT_STR_)
			value = CM_PODPD_[THIS_GRP_]
			OUT_STR_ = ""
			OUT_STR_ += DICTblock(THIS_GRP_, value, CMS_CLASS, "PODPD_", "Any, Any", THIS_CMNT_)
			FDconstants.write(OUT_STR_)
			OUT_STR_ = ""
			value = CM_PODTUPDICT_[THIS_GRP_]
			OUT_STR_ += TUPblock(THIS_GRP_, value, CMS_CLASS, "EMPTY", THIS_CMNT_)
			# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
			OUT_STR_ += f"""{NTAB(2)}self.{THIS_GRP_}GO_ = {DBLQT}{CM_PODGODICT_[THIS_GRP_]}{DBLQT}


{commentBlock("start of D3 stuff")}


"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
		FDconstants.write(OUT_STR_)
		for THIS_GRP_, value in CM_ORGD3DICTDICT_.items():
			# fold here ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈
			value2 = CM_ORGD3LSTDICT_[THIS_GRP_]
			# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
			OUT_STR_ = f"""class {THIS_GRP_}_D3:
{TABSTR}{FOLD0STARTHERE}
{TABSTR}def __init__(self):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}self.{THIS_GRP_}DICT = {OBRCE}
{NTAB(3)}{FOLD2STARTHERE}
{value}{NTAB(2)}{CBRCE}
{NTAB(3)}{FOLD2ENDHERE}
{NTAB(2)}self.{THIS_GRP_}LST = {OBRKT}
{NTAB(3)}{FOLD2STARTHERE}
{value2}{NTAB(2)}{CBRKT}
{NTAB(2)}{FOLD2ENDHERE}
{NTAB(2)}self.AX_ = "AX_"
{NTAB(2)}self.DB_ = "DB_"
{NTAB(2)}self.FLD_ = "FLD_"
{NTAB(2)}self.NM_ = "NM_"
{NTAB(2)}self.FD{THIS_GRP_}DICT = None
{NTAB(2)}self.FD{THIS_GRP_}LST = None
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def append(self, PFX, DB, AX, FLD, NM):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}if PFX not in self.{THIS_GRP_}DICT.keys():
{NTAB(3)}self.{THIS_GRP_}DICT[PFX] = {OBRCE}
{NTAB(4)}self.AX_: AX,
{NTAB(4)}self.DB_: DB,
{NTAB(4)}self.FLD_: FLD,
{NTAB(4)}self.NM_: NM,
{NTAB(3)}{CBRCE}
{NTAB(3)}self.{THIS_GRP_}LST.append(AX)
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def __enter__(self):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}# {THIS_GRP_}DICT = unPickleIt({DBLQT}{THIS_GRP_}DICT.pkl{DBLQT})
{NTAB(2)}# {THIS_GRP_}LST = unPickleIt()
{NTAB(2)}pass
{NTAB(2)}{FOLD1ENDHERE}

{TABSTR}def __exit__(self, exc_type, exc_val, exc_tb):
{NTAB(2)}{FOLD1STARTHERE}
{NTAB(2)}# pickleIt("PFXD3_DICT.pkl", self.PFXD3_DICT)
{NTAB(2)}# pickleIt("PFXD3_LST.pkl", self.PFXD3_LST)
{NTAB(2)}FDTupOut = open("TUP.txt", "tw")
{NTAB(2)}for thisKey, thisEntry in self.PFXD3_DICT.items():
{NTAB(3)}FDTupOut.write(f{TRIQT}{TABSTR}("{OBRCE}thisEntry['NM_']{CBRCE}", CMAX_D3STR, "PFXD3_", "{OBRCE}thisKey{CBRCE}", "{OBRCE}thisEntry['DB_']{CBRCE}", "{OBRCE}thisEntry['AX_']{CBRCE}", "{OBRCE}thisEntry['FLD_']{CBRCE}"),{TRIQT})
{NTAB(2)}FDTupOut.flush()
{NTAB(2)}FDTupOut.close()
{NTAB(2)}FDDICTOUT = open("DICT.py", "tw")
{NTAB(2)}FDPRODD3LST = open("PROD.py", "tw")
{NTAB(2)}FDPRODD3LST.write(f{TRIQT}PROD_LST_ = {OBRKT}
{TRIQT})
{NTAB(2)}FDDICTOUT.write(f{TRIQT}{NTAB(2)}self.PFXD3_DICT = {OBRCE}{NEWLINE}{TRIQT})
{NTAB(2)}for thisHash, thisEntry in self.PFXD3_DICT.items():
{NTAB(3)}# FDDICTOUT.write(f{TRIQT}{OBRCE}thisEntry["FLD_"]{CBRCE}, {OBRCE}thisEntry["AX_"]{CBRCE}{TRIQT})
{NTAB(3)}FDDICTOUT.write(f{TRIQT}{OBRCE}_D3BLKSTR(f"{OBRCE}thisHash{CBRCE}", {OBRCE}thisEntry["DB_"]{CBRCE}, {OBRCE}thisEntry["AX_"]{CBRCE}, {OBRCE}thisEntry["FLD_"]{CBRCE}, {OBRCE}thisEntry["NM_"]{CBRCE}){TRIQT})
{NTAB(3)}if thisEntry["FLD_"].find("PROD__") > -1:
{NTAB(4)}FDPRODD3LST.write(f{TABSTR}("{OBRCE}thisEntry["FLD_"]{CBRCE}", "{OBRCE}thisEntry["NM_"]{CBRCE}", "{OBRCE}thisHash{CBRCE}",),
{TRIQT})
{NTAB(2)}FDDICTOUT.write(f"{NTAB(2)}{CBRCE}{NEWLINE}{NEWLINE}")
{NTAB(2)}FDDICTOUT.flush()
{NTAB(2)}FDDICTOUT.close()
{NTAB(2)}FDPRODD3LST.write(f{TRIQT}{CBRKT}{NEWLINE}{TRIQT})
{NTAB(2)}FDPRODD3LST.flush()
{NTAB(2)}FDPRODD3LST.close()
{NTAB(2)}{FOLD1ENDHERE}

{NTAB(2)}{FOLD0ENDHERE}

"""
			# fold here ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
			FDconstants.write(OUT_STR_)
		OUT_STR_ = ""
		OUT_STR_ += f"""{END_SECT_str(f"end of constants.py cut {currentTS}")}
"""
		FDconstants.write(OUT_STR_)


# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * end of of write constantsNew.py
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

		# for THIS_entry in theBigList:
	# with open(mainConstFilename, "tw") as FDconstants, \

# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * start of write CMConstantsNew.py
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!

		# for THIS_entry in theBigList:
	# with open(mainConstFilename, "tw") as FDconstants, \

		OUT_STR_ = ""
		# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
		OUT_STR_ += f"""{START_SECT_str(f"start of CMconstantsNew.py {currentTS}")}


{CM_PDDFN_str}

DBGPD_: Dict[str, Any] = {OBRCE}
{CM_PD_str}{CBRCE}


{commentBlock("start of CHR_ defines")}


{CM_CHR_str}

{commentBlock("start of STR_ defines")}

{CM_STR_str}

{commentBlock("start of TYPE defines")}

{CM_TYPEDFN_str}

{commentBlock("CM_ strings defines")}

{CM_STRDFN_str}

{commentBlock("_D3BLKSTR PFX block returned")}

_D3BLKSTR = lambda PFX__, DB__, AX__, FLD__, NM__: f{TRIQT}{OBRCE}NTAB(3){CBRCE}{DBLQT}{OBRCE}PFX__{CBRCE}{DBLQT}: {OBRCE}OBRCE{CBRCE}
{OBRCE}NTAB(4){CBRCE}{OBRCE}FOLD0STARTHERE{CBRCE}
{OBRCE}NTAB(4){CBRCE}{DBLQT}DB_{DBLQT}: {DBLQT}{OBRCE}DB__{CBRCE}{DBLQT},
{OBRCE}NTAB(4){CBRCE}{DBLQT}AX_{DBLQT}: {DBLQT}{OBRCE}AX__{CBRCE}{DBLQT},
{OBRCE}NTAB(4){CBRCE}{DBLQT}FLD_{DBLQT}: {DBLQT}{OBRCE}FLD__{CBRCE}{DBLQT},
{OBRCE}NTAB(4){CBRCE}{DBLQT}NM_{DBLQT}: {DBLQT}{OBRCE}NM__{CBRCE}{DBLQT}, {OBRCE}CBRCE{CBRCE},
{OBRCE}NTAB(4){CBRCE}{OBRCE}FOLD0ENDHERE{CBRCE}{TRIQT}


{commentBlock("CMSTR strings")}
{CM_CMDFN_str}

{commentBlock("CMAX_ stuff")}

{CM_AXDFN_str}

CMAX_LST_: List[str] = {OBRKT}
{FOLD0STARTHERE}
{CM_AXLST_str}{CBRKT}
{FOLD0ENDHERE}


{commentBlock("start of CMBL_ struct")}


{CM_CMBLDFN_str}

{END_SECT_str(f"end of CMconstantsNew.py cut {currentTS}")}"""
# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰
		FDconstMaker.write(OUT_STR_)


# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# -!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * end of of CMConstantsNew.py
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
		# for THIS_entry in theBigList:
	# with open(mainConstFilename, "tw") as FDconstants, \


if __name__ == "__main__":
	__main__()
	with open("SVD_currentTS.txt", "w") as FDOut1:
		FDOut1.write(currentTS)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
