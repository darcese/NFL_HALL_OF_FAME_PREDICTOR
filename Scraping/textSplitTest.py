
text = "14x Pro Bowl7x All-Pro2x SB Champ5x MVP2003 Bert Bell Award (Player of the Year)2004 AP Off. PoY2004 Bert Bell Award (Player of the Year)2005 Walter Payton Man of the Year2012 AP Comeback Player2013 AP Off. PoY2013 Bert Bell Award (Player of the Year)"
a = [int(s) for s in text.split() if s.isdigit()]
print(a)

import re
print(re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd"))
