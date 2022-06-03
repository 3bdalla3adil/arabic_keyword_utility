# Harf holds the Arabic character with its different representation forms {glyphs).
class Harf:

    def __init__(self,**kwagrs):
        self.unicodee   = kwagrs['unicodee']
        self.isolated   = kwagrs['isolated']
        self.beggining  = kwagrs['beggining']
        self.medium     = kwagrs['medium']
        self.final      = kwagrs['final']


# Vowels (Tashkeel) characters.
tashkeel = {
	'FATHA'     : '\u064e',
	'FATHATAN'  : '\u064b',
	'DAMMA '    : '\u064f',
	'DAMMATAN'  : '\u064c',
	'KASRA'     : '\u0650',
	'KASRATAN'  : '\u064d',
	'SHADDA'    : '\u0651',
	'SUKUN'     : '\u0652'
}

# Arabic Alphabet using the new Harf_type.
harf_type = dict(# أ
	ALEF_HAMZA_ABOVE = Harf( 
		unicodee=   '\u0623',
		isolated=  '\ufe83',
		beggining= '\u0623',
		medium=    '\ufe84',
		final=     '\ufe84'),

	ALEF = Harf( # ا
		unicodee=   '\u0627',
		isolated=  '\ufe8d',
		beggining= '\u0627',
		medium=    '\ufe8e',
		final=     '\ufe8e'),

	ALEF_MADDA_ABOVE = Harf( # آ
		unicodee=   '\u0622',
		isolated=  '\ufe81',
		beggining= '\u0622',
		medium=    '\ufe82',
		final=     '\ufe82'),

	HAMZA = Harf( # ء
		unicodee=   '\u0621',
		isolated=  '\ufe80',
		beggining= '\u0621',
		medium=    '\u0621',
		final=     '\u0621'),

	WAW_HAMZA_ABOVE = Harf( # ؤ
		unicodee=   '\u0624',
		isolated=  '\ufe85',
		beggining= '\u0624',
		medium=    '\ufe86',
		final=     '\ufe86'),

	ALEF_HAMZA_BELOW = Harf( # إ
		unicodee=   '\u0625',
		isolated=  '\ufe87',
		beggining= '\u0625',
		medium=    '\ufe88',
		final=     '\ufe88'),

	YEH_HAMZA_ABOVE = Harf( # ئ
		unicodee=   '\u0626',
		isolated=  '\ufe89',
		beggining= '\ufe8b',
		medium=    '\ufe8c',
		final=     '\ufe8a'),

	BEH = Harf( # ب
		unicodee=   '\u0628',
		isolated=  '\ufe8f',
		beggining= '\ufe91',
		medium=    '\ufe92',
		final=     '\ufe90'),

	PEH = Harf( # پ
		unicodee=   '\u067e',
		isolated=  '\ufb56',
		beggining= '\ufb58',
		medium=    '\ufb59',
		final=     '\ufb57'),

	TEH = Harf( # ت
		unicodee=   '\u062A',
		isolated=  '\ufe95',
		beggining= '\ufe97',
		medium=    '\ufe98',
		final=     '\ufe96'),

	TEH_MARBUTA = Harf( # ة
		unicodee=   '\u0629',
		isolated=  '\ufe93',
		beggining= '\u0629',
		medium=    '\u0629',
		final=     '\ufe94'),

	THEH = Harf( # ث
		unicodee=   '\u062b',
		isolated=  '\ufe99',
		beggining= '\ufe9b',
		medium=    '\ufe9c',
		final=     '\ufe9a'),

	JEEM = Harf( # ج
		unicodee=   '\u062c',
		isolated=  '\ufe9d',
		beggining= '\ufe9f',
		medium=    '\ufea0',
		final=     '\ufe9e'),

	TCHEH = Harf( # چ
		unicodee=   '\u0686',
		isolated=  '\ufb7a',
		beggining= '\ufb7c',
		medium=    '\ufb7d',
		final=     '\ufb7b'),

	HAH = Harf( # ح
		unicodee=   '\u062d',
		isolated=  '\ufea1',
		beggining= '\ufea3',
		medium=    '\ufea4',
		final=     '\ufea2'),

	KHAH = Harf( # خ
		unicodee=   '\u062e',
		isolated=  '\ufea5',
		beggining= '\ufea7',
		medium=    '\ufea8',
		final=     '\ufea6'),

	DAL = Harf( # د
		unicodee=   '\u062f',
		isolated=  '\ufea9',
		beggining= '\u062f',
		medium=    '\ufeaa',
		final=     '\ufeaa'),

	THAL = Harf( # ذ
		unicodee=   '\u0630',
		isolated=  '\ufeab',
		beggining= '\u0630',
		medium=    '\ufeac',
		final=     '\ufeac'),

	REH = Harf( # ر
		unicodee=   '\u0631',
		isolated=  '\ufead',
		beggining= '\u0631',
		medium=    '\ufeae',
		final=     '\ufeae'),

	JEH = Harf(
		unicodee=   '\u0698',
		isolated=  '\ufb8a',
		beggining= '\u0698',
		medium=    '\ufb8b',
		final=     '\ufb8b',),

	ZAIN = Harf( # ز
		unicodee=   '\u0632',
		isolated=  '\ufeaf',
		beggining= '\u0632',
		medium=    '\ufeb0',
		final=     '\ufeb0'),

	SEEN = Harf( # س
		unicodee=   '\u0633',
		isolated=  '\ufeb1',
		beggining= '\ufeb3',
		medium=    '\ufeb4',
		final=     '\ufeb2'),

	SHEEN = Harf( # ش
		unicodee=   '\u0634',
		isolated=  '\ufeb5',
		beggining= '\ufeb7',
		medium=    '\ufeb8',
		final=     '\ufeb6'),

	SAD = Harf( # ص
		unicodee=   '\u0635',
		isolated=  '\ufeb9',
		beggining= '\ufebb',
		medium=    '\ufebc',
		final=     '\ufeba'),

	DAD = Harf( # ض
		unicodee=   '\u0636',
		isolated=  '\ufebd',
		beggining= '\ufebf',
		medium=    '\ufec0',
		final=     '\ufebe'),

	TAH = Harf( # ط
		unicodee=   '\u0637',
		isolated=  '\ufec1',
		beggining= '\ufec3',
		medium=    '\ufec4',
		final=     '\ufec2'),

	ZAH = Harf( # ظ
		unicodee=   '\u0638',
		isolated=  '\ufec5',
		beggining= '\ufec7',
		medium=    '\ufec8',
		final=     '\ufec6'),

	AIN = Harf( # ع
		unicodee=   '\u0639',
		isolated=  '\ufec9',
		beggining= '\ufecb',
		medium=    '\ufecc',
		final=     '\ufeca'),

	GHAIN = Harf( # غ
		unicodee=   '\u063a',
		isolated=  '\ufecd',
		beggining= '\ufecf',
		medium=    '\ufed0',
		final=     '\ufece'),

	FEH = Harf( # ف
		unicodee=   '\u0641',
		isolated=  '\ufed1',
		beggining= '\ufed3',
		medium=    '\ufed4',
		final=     '\ufed2'),

	QAF = Harf( # ق
		unicodee=   '\u0642',
		isolated=  '\ufed5',
		beggining= '\ufed7',
		medium=    '\ufed8',
		final=     '\ufed6'),

	KAF = Harf( # ك
		unicodee=   '\u0643',
		isolated=  '\ufed9',
		beggining= '\ufedb',
		medium=    '\ufedc',
		final=     '\ufeda'),

	KEHEH = Harf( # ک
		unicodee=   '\u06a9',
		isolated=  '\ufb8e',
		beggining= '\ufb90',
		medium=    '\ufb91',
		final=     '\ufb8f',),	

	GAF = Harf( # گ
		unicodee=   '\u06af',
		isolated=  '\ufb92',
		beggining= '\ufb94',
		medium=    '\ufb95',
		final=     '\ufb93'),

	LAM = Harf( # ل
		unicodee=   '\u0644',
		isolated=  '\ufedd',
		beggining= '\ufedf',
		medium=    '\ufee0',
		final=     '\ufede'),

	MEEM = Harf( # م
		unicodee=   '\u0645',
		isolated=  '\ufee1',
		beggining= '\ufee3',
		medium=    '\ufee4',
		final=     '\ufee2'),

	NOON = Harf( # ن
		unicodee=   '\u0646',
		isolated=  '\ufee5',
		beggining= '\ufee7',
		medium=    '\ufee8',
		final=     '\ufee6'),

	HEH = Harf( # ه
		unicodee=   '\u0647',
		isolated=  '\ufee9',
		beggining= '\ufeeb',
		medium=    '\ufeec',
		final=     '\ufeea'),

	WAW = Harf( # و
		unicodee=   '\u0648',
		isolated=  '\ufeed',
		beggining= '\u0648',
		medium=    '\ufeee',
		final=     '\ufeee'),

	YEH = Harf( # ی
		unicodee=   '\u06cc',
		isolated=  '\ufbfc',
		beggining= '\ufbfe',
		medium=    '\ufbff',
		final=     '\ufbfd'),

	ARABICYEH = Harf( # ي
		unicodee=   '\u064a',
		isolated=  '\ufef1',
		beggining= '\ufef3',
		medium=    '\ufef4',
		final=     '\ufef2'),

	ALEF_MAKSURA = Harf( # ى
		unicodee=   '\u0649',
		isolated=  '\ufeef',
		beggining= '\u0649',
		medium=    '\ufef0',
		final=     '\ufef0'),

	TATWEEL = Harf( # ـ
		unicodee=   '\u0640',
		isolated=  '\u0640',
		beggining= '\u0640',
		medium=    '\u0640',
		final=     '\u0640'),

	LAM_ALEF = Harf( # لا
		unicodee=   '\ufefb',
		isolated=  '\ufefb',
		beggining= '\ufefb',
		medium=    '\ufefc',
		final=     '\ufefc'),

	LAM_ALEF_HAMZA_ABOVE = Harf( # ﻷ
		unicodee=   '\ufef7',
		isolated=  '\ufef7',
		beggining= '\ufef7',
		medium=    '\ufef8',
		final=     '\ufef8'),
)

#list of alphabet character
alphabet = [
	harf_type['ALEF_HAMZA_ABOVE'],
	harf_type['ALEF'],
	harf_type['ALEF_MADDA_ABOVE'],
	harf_type['HAMZA'],
	harf_type['WAW_HAMZA_ABOVE'],
	harf_type['ALEF_HAMZA_BELOW'],
	harf_type['YEH_HAMZA_ABOVE'],
	harf_type['BEH'],
	harf_type['PEH'],
	harf_type['TEH'],
	harf_type['TEH_MARBUTA'],
	harf_type['THEH'],
	harf_type['JEEM'],
	harf_type['TCHEH'],
	harf_type['HAH'],
	harf_type['KHAH'],
	harf_type['DAL'],
	harf_type['THAL'],
	harf_type['REH'],
	harf_type['JEH'],
	harf_type['ZAIN'],
	harf_type['SEEN'],
	harf_type['SHEEN'],
	harf_type['SAD'],
	harf_type['DAD'],
	harf_type['TAH'],
	harf_type['ZAH'],
	harf_type['AIN'],
	harf_type['GHAIN'],
	harf_type['FEH'],
	harf_type['QAF'],
	harf_type['KAF'],
	harf_type['KEHEH'],
	harf_type['GAF'],
	harf_type['LAM'],
	harf_type['MEEM'],
	harf_type['NOON'],
	harf_type['HEH'],
	harf_type['WAW'],
	harf_type['YEH'],
	harf_type['ARABICYEH'],
	harf_type['ALEF_MAKSURA'],
	harf_type['TATWEEL'],
	harf_type['LAM_ALEF'],
	harf_type['LAM_ALEF_HAMZA_ABOVE']
]

ALEF_HAMZA_ABOVE= harf_type['ALEF']
ALEF_MADDA_ABOVE= harf_type['ALEF_MADDA_ABOVE']
ALEF=             harf_type['ALEF']
HAMZA=            harf_type['HAMZA']
WAW_HAMZA_ABOVE=  harf_type['WAW_HAMZA_ABOVE']
ALEF_HAMZA_BELOW= harf_type['ALEF_HAMZA_BELOW']
TEH_MARBUTA=      harf_type['TEH']
TATWEEL=          harf_type['TATWEEL']
DAL=              harf_type['DAL']
THAL=             harf_type['THAL']
REH=              harf_type['REH']
ZAIN=             harf_type['ZAIN']
WAW=              harf_type['WAW']
ALEF_MAKSURA=     harf_type['ALEF_MAKSURA']

# use dictionary for faster lookups.
tashkeel = dict(FATHA= True, FATHATAN= True, DAMMA= True,
	DAMMATAN= True, KASRA= True, KASRATAN= True,
	SHADDA= True, SUKUN= True)

# use dictionary for faster lookups. Disclaimer dict in python is the corresponding to map in go
beggining_after = dict(
	ALEF_HAMZA_ABOVE= True,
	ALEF_MADDA_ABOVE= True,
	ALEF=             True,
	HAMZA=            True,
	WAW_HAMZA_ABOVE=  True,
	ALEF_HAMZA_BELOW= True,
	TEH_MARBUTA=      True,
	DAL=              True,
	THAL=             True,
	REH=              True,
	ZAIN=             True,
	WAW=              True,
	ALEF_MAKSURA=     True)


