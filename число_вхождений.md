```python
words = ''
lib = dict()
```


```python
with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        words += line
        print(line)
```

    XdcXXTdTU TYXX ZTdUYbpU bbU apUXTdb YaTcX XdcXXTdTU Yd ZTdUYbpU UZbYUpXp ZTTYpbYYb ZbaXXdpcY TTdZUbU UTaYdTp UTaYdTp ZbaXXdpcY aZYcYTU UTcUdbUa bX UaTUb bbU XdcXpTdXb UZbYUpXp ZbaXXdpcY XYZZTp caYpdU cUT bX XYpUbapdd ZdTd pUTdZ aZYcYTU UTaYdTp UTcUdbUa UZ UZXaT dU dddZadc XYpUbapdd ad
    bZ UYpYTYaYT UYpYTYaYT dab UYpYTYaYT dab dab YXbTcZ bcdbbbd caYp Ypca UYpYTYaYT bcc Ypca bcc dab cZpZT ZZcTZUc X TcX XYYa cbbUcbdZb UcX dUdTYZ dab apapdbXTT apapdbXTT YdZb bZ TZ UYpYTYaYT UYpYTYaYT apapdbXTT a UTY badUZ adT bTXbUX UYbaZUXd aXbbTUTZU adT Ypca YdaUbUpUc Ypca bcc
    Ucd Ucd TYpTdXZbX ZXcUd ZXcUd UYbZa TUXdcX YaUUX Y p Ucd dp UYbZa ZTUa ccYbTXX Ucd
    Z c c c a TXpXUcdTZ TYZZ c Z YddYap YUpd c c TXpXUcdTZ
    cX cX U TXdUU U c TZap YacdZa T TT dYT daYUdc
    bcTbXpXTa bcTbXpXTa paT TpZaUT c ZXZTZY cXp aUXY ccXUppU aUXY cXaYcZY bcTbXpXTa ZZTdU Tcb TYdXXpY XXcac bcTbXpXTa c bcTbXpXTa paT YYX aUdZa Tcb c aTTdYYUYX dYbTd bcTbXpXTa Udb YdcXUcab bXdbcUZY Z aT bcTbXpXTa bcTbXpXTa aUXY ca XZTX bcTbXpXTa b bcTbXpXTa dX bTZapcdZb aTbb TcTbYpUad XUTUU bcTbXpXTa YacYXdYUc bXYXaUUZa ZaTdcUpb bdZZZUX YZd TYdXXpY aXbdaZd TYXTYY
    UdUccTpd apUX aYZbc UdUccTpd aZYZX apUX U UdUccTpd TTYTacbXT aYZbc apUX UdUccTpd UdUccTpd aTYTc apUX TbXbZp UdUccTpd cpapXZTaX ac XZaTYcXZb YdTdYUbdd baXXXTYp YaZXYb paaa dbUc dX ddZZTpaba UdUccTpd UdUccTpd bbYYUTbb TdTca pUZ cb pTcdUd dpbpY baXXXTYp ppTTZTU ZY pTb aT
    dTb UYT c UbpbTYppX UYT UYT aXTabcYYa ddZTXp cdZZXZp UbpbTYppX dZpaTTTU Ub c UbpbTYppX UbpbTYppX aXTabcYYa c UbpbTYppX ppbXT apd cZcbZTUT UbpbTYppX XcaZTb bXbYZXXT aU XcaZTb aXTabcYYa pbZXpYZp aU TZpYTdXT TZ TXYZUdUZZ YYUaXUTX c ZbpY ZbUaUU cUbYUd XbUZXaY ba dZpaTTTU YXXTZXTZ ZbbdUb Xbp aaYUTdTUU dZpaTTTU XbUZXaY Yb p UYa YTTTpT cdZZXZp YXXTZXTZ b XUZpZT
    aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ X acaaXUY YppbdbUXY YTcdYXZdU YppbdbUXY ZbaUp a XZUYccbUX UcTZ aYdcUdXap aYUTccTaZ XdXXT c XdXXT pXZcUUYT XUTbXTTUc cpZY cdacX aYdcUdXap pYppbaTUa X YpdXpdd X aYdcUdXap ZpXZ dTba aYUTccTaZ pTZpTTYY a Xc a Xc Zcb dTUbY ddZ bTaUdba ddZ YpX
    X YXT ZdUpdX YXT bTd aXXbpY Ycbdbdacc bca YXT ZdUpdX pdpcZ bYbU paabTU ZdUpdX cXpUY Ycbdbdacc paUUc caUY paabTU Xpc bdcXXX cbYbYZba ZdUpdX acUp dTp dTp
    aadXXXT d dZppTapa dZppTapa aT dYpXab TZcaTTdac b TdpcZUY TT YpcaUpTdY aabYcZZd aT XdTUd cTUa d XbbZYZT abddZYcbX Ycacp
    ZUdTXUccY adXpUddTU UY dXdXU dXdXU XZbYXU bcTbYpp UY Tp UY aYZpYddTb U bcTbYpp UZ dpUX dXXT UZ dUZUZYXp dp ZUdTXUccY Tp aYYcTYcT UbpXTUUY abUpUadXT TZcaaYaZd XY dpXX UY dp YUZUc ZUc dYc dbaZYb apXdpcX dX U dbcpX pUUba UY dTcbTUbYY UY Tp cZZUZbc a UY YaUU pZZc Tp cTYU aYbpYXTaY UY
    TYTZbbdca ZZcc ZZcc ZZcc ZZ ZTbYTXcZa dYc dYc T bUabb Y UY ZZcc addbUppaX UpaU TYTZbbdca XT TUZpX bUabb TT ZU XU TcZp abp Zd dZaZbZpXU ZddpcZX adTTTTba bcbdaaT XTdU ZZcc
    XdpaY aaTbZc aaTbZc XdpaY bdXp dYbYYbTda aaTbZc aaTbZc dYbYYbTda Ud TZUpTaa XdpaY dc aaTbZc aaUZcTTa ZUa pUbYdZXbc XdpaY
    dTZY aTadY bpbpT aTadY aadTUda YYpc bpXTZb dXXYcbYX aTpXpdacU bUcYp Y UXTXUpdU cpX aTpXpdacU Xadd TUdbZZabZ YYpc YU T YYcTZbXa aTpXpdacU YYpc bbU ZUbUd TUdZ Up YYpc bXXbpcTc TUdZ UcbUbpX dXZZ YpXUZd c UTcUa UcbbTYdp TTUpUc XYpbbXd ZdTpaZTUT aTadY Xd T aacZUXY dXZZ YaappUb X b aapbbddbX aapbbddbX
    TdXXdXZp c c UTTaZpca cdZbYUZcc X UbUad aYYcZYU YUba X YddTdapU cbTU XYaUdcZYZ cpdXaU X pcYpcT XUpXUa aZbaUpaaU cpdXaU ZcppY aYYcZYU c cpdXaU YUcbaZUZ
    XdYUd ad cZT cZT b bZXp ZYdTbc bZXp cdcbXaYaT bTa
    YadcdUdb X pX X X ZXd U aUTZTUY X bcU Ud aUTZTUY Ud X paTabaUd aUTZTUY
    


```python
print(words)
type(words)
```

    XdcXXTdTU TYXX ZTdUYbpU bbU apUXTdb YaTcX XdcXXTdTU Yd ZTdUYbpU UZbYUpXp ZTTYpbYYb ZbaXXdpcY TTdZUbU UTaYdTp UTaYdTp ZbaXXdpcY aZYcYTU UTcUdbUa bX UaTUb bbU XdcXpTdXb UZbYUpXp ZbaXXdpcY XYZZTp caYpdU cUT bX XYpUbapdd ZdTd pUTdZ aZYcYTU UTaYdTp UTcUdbUa UZ UZXaT dU dddZadc XYpUbapdd adbZ UYpYTYaYT UYpYTYaYT dab UYpYTYaYT dab dab YXbTcZ bcdbbbd caYp Ypca UYpYTYaYT bcc Ypca bcc dab cZpZT ZZcTZUc X TcX XYYa cbbUcbdZb UcX dUdTYZ dab apapdbXTT apapdbXTT YdZb bZ TZ UYpYTYaYT UYpYTYaYT apapdbXTT a UTY badUZ adT bTXbUX UYbaZUXd aXbbTUTZU adT Ypca YdaUbUpUc Ypca bccUcd Ucd TYpTdXZbX ZXcUd ZXcUd UYbZa TUXdcX YaUUX Y p Ucd dp UYbZa ZTUa ccYbTXX UcdZ c c c a TXpXUcdTZ TYZZ c Z YddYap YUpd c c TXpXUcdTZcX cX U TXdUU U c TZap YacdZa T TT dYT daYUdcbcTbXpXTa bcTbXpXTa paT TpZaUT c ZXZTZY cXp aUXY ccXUppU aUXY cXaYcZY bcTbXpXTa ZZTdU Tcb TYdXXpY XXcac bcTbXpXTa c bcTbXpXTa paT YYX aUdZa Tcb c aTTdYYUYX dYbTd bcTbXpXTa Udb YdcXUcab bXdbcUZY Z aT bcTbXpXTa bcTbXpXTa aUXY ca XZTX bcTbXpXTa b bcTbXpXTa dX bTZapcdZb aTbb TcTbYpUad XUTUU bcTbXpXTa YacYXdYUc bXYXaUUZa ZaTdcUpb bdZZZUX YZd TYdXXpY aXbdaZd TYXTYYUdUccTpd apUX aYZbc UdUccTpd aZYZX apUX U UdUccTpd TTYTacbXT aYZbc apUX UdUccTpd UdUccTpd aTYTc apUX TbXbZp UdUccTpd cpapXZTaX ac XZaTYcXZb YdTdYUbdd baXXXTYp YaZXYb paaa dbUc dX ddZZTpaba UdUccTpd UdUccTpd bbYYUTbb TdTca pUZ cb pTcdUd dpbpY baXXXTYp ppTTZTU ZY pTb aTdTb UYT c UbpbTYppX UYT UYT aXTabcYYa ddZTXp cdZZXZp UbpbTYppX dZpaTTTU Ub c UbpbTYppX UbpbTYppX aXTabcYYa c UbpbTYppX ppbXT apd cZcbZTUT UbpbTYppX XcaZTb bXbYZXXT aU XcaZTb aXTabcYYa pbZXpYZp aU TZpYTdXT TZ TXYZUdUZZ YYUaXUTX c ZbpY ZbUaUU cUbYUd XbUZXaY ba dZpaTTTU YXXTZXTZ ZbbdUb Xbp aaYUTdTUU dZpaTTTU XbUZXaY Yb p UYa YTTTpT cdZZXZp YXXTZXTZ b XUZpZTaYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ aYUTccTaZ X acaaXUY YppbdbUXY YTcdYXZdU YppbdbUXY ZbaUp a XZUYccbUX UcTZ aYdcUdXap aYUTccTaZ XdXXT c XdXXT pXZcUUYT XUTbXTTUc cpZY cdacX aYdcUdXap pYppbaTUa X YpdXpdd X aYdcUdXap ZpXZ dTba aYUTccTaZ pTZpTTYY a Xc a Xc Zcb dTUbY ddZ bTaUdba ddZ YpXX YXT ZdUpdX YXT bTd aXXbpY Ycbdbdacc bca YXT ZdUpdX pdpcZ bYbU paabTU ZdUpdX cXpUY Ycbdbdacc paUUc caUY paabTU Xpc bdcXXX cbYbYZba ZdUpdX acUp dTp dTpaadXXXT d dZppTapa dZppTapa aT dYpXab TZcaTTdac b TdpcZUY TT YpcaUpTdY aabYcZZd aT XdTUd cTUa d XbbZYZT abddZYcbX YcacpZUdTXUccY adXpUddTU UY dXdXU dXdXU XZbYXU bcTbYpp UY Tp UY aYZpYddTb U bcTbYpp UZ dpUX dXXT UZ dUZUZYXp dp ZUdTXUccY Tp aYYcTYcT UbpXTUUY abUpUadXT TZcaaYaZd XY dpXX UY dp YUZUc ZUc dYc dbaZYb apXdpcX dX U dbcpX pUUba UY dTcbTUbYY UY Tp cZZUZbc a UY YaUU pZZc Tp cTYU aYbpYXTaY UYTYTZbbdca ZZcc ZZcc ZZcc ZZ ZTbYTXcZa dYc dYc T bUabb Y UY ZZcc addbUppaX UpaU TYTZbbdca XT TUZpX bUabb TT ZU XU TcZp abp Zd dZaZbZpXU ZddpcZX adTTTTba bcbdaaT XTdU ZZccXdpaY aaTbZc aaTbZc XdpaY bdXp dYbYYbTda aaTbZc aaTbZc dYbYYbTda Ud TZUpTaa XdpaY dc aaTbZc aaUZcTTa ZUa pUbYdZXbc XdpaYdTZY aTadY bpbpT aTadY aadTUda YYpc bpXTZb dXXYcbYX aTpXpdacU bUcYp Y UXTXUpdU cpX aTpXpdacU Xadd TUdbZZabZ YYpc YU T YYcTZbXa aTpXpdacU YYpc bbU ZUbUd TUdZ Up YYpc bXXbpcTc TUdZ UcbUbpX dXZZ YpXUZd c UTcUa UcbbTYdp TTUpUc XYpbbXd ZdTpaZTUT aTadY Xd T aacZUXY dXZZ YaappUb X b aapbbddbX aapbbddbXTdXXdXZp c c UTTaZpca cdZbYUZcc X UbUad aYYcZYU YUba X YddTdapU cbTU XYaUdcZYZ cpdXaU X pcYpcT XUpXUa aZbaUpaaU cpdXaU ZcppY aYYcZYU c cpdXaU YUcbaZUZXdYUd ad cZT cZT b bZXp ZYdTbc bZXp cdcbXaYaT bTaYadcdUdb X pX X X ZXd U aUTZTUY X bcU Ud aUTZTUY Ud X paTabaUd aUTZTUY
    




    str




```python
words = words.lower().split()
print(words)
```

    ['xdcxxtdtu', 'tyxx', 'ztduybpu', 'bbu', 'apuxtdb', 'yatcx', 'xdcxxtdtu', 'yd', 'ztduybpu', 'uzbyupxp', 'zttypbyyb', 'zbaxxdpcy', 'ttdzubu', 'utaydtp', 'utaydtp', 'zbaxxdpcy', 'azycytu', 'utcudbua', 'bx', 'uatub', 'bbu', 'xdcxptdxb', 'uzbyupxp', 'zbaxxdpcy', 'xyzztp', 'caypdu', 'cut', 'bx', 'xypubapdd', 'zdtd', 'putdz', 'azycytu', 'utaydtp', 'utcudbua', 'uz', 'uzxat', 'du', 'dddzadc', 'xypubapdd', 'adbz', 'uypytyayt', 'uypytyayt', 'dab', 'uypytyayt', 'dab', 'dab', 'yxbtcz', 'bcdbbbd', 'cayp', 'ypca', 'uypytyayt', 'bcc', 'ypca', 'bcc', 'dab', 'czpzt', 'zzctzuc', 'x', 'tcx', 'xyya', 'cbbucbdzb', 'ucx', 'dudtyz', 'dab', 'apapdbxtt', 'apapdbxtt', 'ydzb', 'bz', 'tz', 'uypytyayt', 'uypytyayt', 'apapdbxtt', 'a', 'uty', 'baduz', 'adt', 'btxbux', 'uybazuxd', 'axbbtutzu', 'adt', 'ypca', 'ydaubupuc', 'ypca', 'bccucd', 'ucd', 'typtdxzbx', 'zxcud', 'zxcud', 'uybza', 'tuxdcx', 'yauux', 'y', 'p', 'ucd', 'dp', 'uybza', 'ztua', 'ccybtxx', 'ucdz', 'c', 'c', 'c', 'a', 'txpxucdtz', 'tyzz', 'c', 'z', 'yddyap', 'yupd', 'c', 'c', 'txpxucdtzcx', 'cx', 'u', 'txduu', 'u', 'c', 'tzap', 'yacdza', 't', 'tt', 'dyt', 'dayudcbctbxpxta', 'bctbxpxta', 'pat', 'tpzaut', 'c', 'zxztzy', 'cxp', 'auxy', 'ccxuppu', 'auxy', 'cxayczy', 'bctbxpxta', 'zztdu', 'tcb', 'tydxxpy', 'xxcac', 'bctbxpxta', 'c', 'bctbxpxta', 'pat', 'yyx', 'audza', 'tcb', 'c', 'attdyyuyx', 'dybtd', 'bctbxpxta', 'udb', 'ydcxucab', 'bxdbcuzy', 'z', 'at', 'bctbxpxta', 'bctbxpxta', 'auxy', 'ca', 'xztx', 'bctbxpxta', 'b', 'bctbxpxta', 'dx', 'btzapcdzb', 'atbb', 'tctbypuad', 'xutuu', 'bctbxpxta', 'yacyxdyuc', 'bxyxauuza', 'zatdcupb', 'bdzzzux', 'yzd', 'tydxxpy', 'axbdazd', 'tyxtyyuducctpd', 'apux', 'ayzbc', 'uducctpd', 'azyzx', 'apux', 'u', 'uducctpd', 'ttytacbxt', 'ayzbc', 'apux', 'uducctpd', 'uducctpd', 'atytc', 'apux', 'tbxbzp', 'uducctpd', 'cpapxztax', 'ac', 'xzatycxzb', 'ydtdyubdd', 'baxxxtyp', 'yazxyb', 'paaa', 'dbuc', 'dx', 'ddzztpaba', 'uducctpd', 'uducctpd', 'bbyyutbb', 'tdtca', 'puz', 'cb', 'ptcdud', 'dpbpy', 'baxxxtyp', 'ppttztu', 'zy', 'ptb', 'atdtb', 'uyt', 'c', 'ubpbtyppx', 'uyt', 'uyt', 'axtabcyya', 'ddztxp', 'cdzzxzp', 'ubpbtyppx', 'dzpatttu', 'ub', 'c', 'ubpbtyppx', 'ubpbtyppx', 'axtabcyya', 'c', 'ubpbtyppx', 'ppbxt', 'apd', 'czcbztut', 'ubpbtyppx', 'xcaztb', 'bxbyzxxt', 'au', 'xcaztb', 'axtabcyya', 'pbzxpyzp', 'au', 'tzpytdxt', 'tz', 'txyzuduzz', 'yyuaxutx', 'c', 'zbpy', 'zbuauu', 'cubyud', 'xbuzxay', 'ba', 'dzpatttu', 'yxxtzxtz', 'zbbdub', 'xbp', 'aayutdtuu', 'dzpatttu', 'xbuzxay', 'yb', 'p', 'uya', 'ytttpt', 'cdzzxzp', 'yxxtzxtz', 'b', 'xuzpztayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'x', 'acaaxuy', 'yppbdbuxy', 'ytcdyxzdu', 'yppbdbuxy', 'zbaup', 'a', 'xzuyccbux', 'uctz', 'aydcudxap', 'ayutcctaz', 'xdxxt', 'c', 'xdxxt', 'pxzcuuyt', 'xutbxttuc', 'cpzy', 'cdacx', 'aydcudxap', 'pyppbatua', 'x', 'ypdxpdd', 'x', 'aydcudxap', 'zpxz', 'dtba', 'ayutcctaz', 'ptzpttyy', 'a', 'xc', 'a', 'xc', 'zcb', 'dtuby', 'ddz', 'btaudba', 'ddz', 'ypxx', 'yxt', 'zdupdx', 'yxt', 'btd', 'axxbpy', 'ycbdbdacc', 'bca', 'yxt', 'zdupdx', 'pdpcz', 'bybu', 'paabtu', 'zdupdx', 'cxpuy', 'ycbdbdacc', 'pauuc', 'cauy', 'paabtu', 'xpc', 'bdcxxx', 'cbybyzba', 'zdupdx', 'acup', 'dtp', 'dtpaadxxxt', 'd', 'dzpptapa', 'dzpptapa', 'at', 'dypxab', 'tzcattdac', 'b', 'tdpczuy', 'tt', 'ypcauptdy', 'aabyczzd', 'at', 'xdtud', 'ctua', 'd', 'xbbzyzt', 'abddzycbx', 'ycacpzudtxuccy', 'adxpuddtu', 'uy', 'dxdxu', 'dxdxu', 'xzbyxu', 'bctbypp', 'uy', 'tp', 'uy', 'ayzpyddtb', 'u', 'bctbypp', 'uz', 'dpux', 'dxxt', 'uz', 'duzuzyxp', 'dp', 'zudtxuccy', 'tp', 'ayyctyct', 'ubpxtuuy', 'abupuadxt', 'tzcaayazd', 'xy', 'dpxx', 'uy', 'dp', 'yuzuc', 'zuc', 'dyc', 'dbazyb', 'apxdpcx', 'dx', 'u', 'dbcpx', 'puuba', 'uy', 'dtcbtubyy', 'uy', 'tp', 'czzuzbc', 'a', 'uy', 'yauu', 'pzzc', 'tp', 'ctyu', 'aybpyxtay', 'uytytzbbdca', 'zzcc', 'zzcc', 'zzcc', 'zz', 'ztbytxcza', 'dyc', 'dyc', 't', 'buabb', 'y', 'uy', 'zzcc', 'addbuppax', 'upau', 'tytzbbdca', 'xt', 'tuzpx', 'buabb', 'tt', 'zu', 'xu', 'tczp', 'abp', 'zd', 'dzazbzpxu', 'zddpczx', 'adttttba', 'bcbdaat', 'xtdu', 'zzccxdpay', 'aatbzc', 'aatbzc', 'xdpay', 'bdxp', 'dybyybtda', 'aatbzc', 'aatbzc', 'dybyybtda', 'ud', 'tzuptaa', 'xdpay', 'dc', 'aatbzc', 'aauzctta', 'zua', 'pubydzxbc', 'xdpaydtzy', 'atady', 'bpbpt', 'atady', 'aadtuda', 'yypc', 'bpxtzb', 'dxxycbyx', 'atpxpdacu', 'bucyp', 'y', 'uxtxupdu', 'cpx', 'atpxpdacu', 'xadd', 'tudbzzabz', 'yypc', 'yu', 't', 'yyctzbxa', 'atpxpdacu', 'yypc', 'bbu', 'zubud', 'tudz', 'up', 'yypc', 'bxxbpctc', 'tudz', 'ucbubpx', 'dxzz', 'ypxuzd', 'c', 'utcua', 'ucbbtydp', 'ttupuc', 'xypbbxd', 'zdtpaztut', 'atady', 'xd', 't', 'aaczuxy', 'dxzz', 'yaappub', 'x', 'b', 'aapbbddbx', 'aapbbddbxtdxxdxzp', 'c', 'c', 'uttazpca', 'cdzbyuzcc', 'x', 'ubuad', 'ayyczyu', 'yuba', 'x', 'yddtdapu', 'cbtu', 'xyaudczyz', 'cpdxau', 'x', 'pcypct', 'xupxua', 'azbaupaau', 'cpdxau', 'zcppy', 'ayyczyu', 'c', 'cpdxau', 'yucbazuzxdyud', 'ad', 'czt', 'czt', 'b', 'bzxp', 'zydtbc', 'bzxp', 'cdcbxayat', 'btayadcdudb', 'x', 'px', 'x', 'x', 'zxd', 'u', 'autztuy', 'x', 'bcu', 'ud', 'autztuy', 'ud', 'x', 'patabaud', 'autztuy']
    


```python
words.sort()
```


```python
print(words)
```

    ['a', 'a', 'a', 'a', 'a', 'a', 'aabyczzd', 'aaczuxy', 'aadtuda', 'aapbbddbx', 'aapbbddbxtdxxdxzp', 'aatbzc', 'aatbzc', 'aatbzc', 'aatbzc', 'aatbzc', 'aauzctta', 'aayutdtuu', 'abddzycbx', 'abp', 'abupuadxt', 'ac', 'acaaxuy', 'acup', 'ad', 'adbz', 'addbuppax', 'adt', 'adt', 'adttttba', 'adxpuddtu', 'apapdbxtt', 'apapdbxtt', 'apapdbxtt', 'apd', 'apux', 'apux', 'apux', 'apux', 'apuxtdb', 'apxdpcx', 'at', 'at', 'at', 'atady', 'atady', 'atady', 'atbb', 'atdtb', 'atpxpdacu', 'atpxpdacu', 'atpxpdacu', 'attdyyuyx', 'atytc', 'au', 'au', 'audza', 'autztuy', 'autztuy', 'autztuy', 'auxy', 'auxy', 'auxy', 'axbbtutzu', 'axbdazd', 'axtabcyya', 'axtabcyya', 'axtabcyya', 'axxbpy', 'aybpyxtay', 'aydcudxap', 'aydcudxap', 'aydcudxap', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayutcctaz', 'ayyctyct', 'ayyczyu', 'ayyczyu', 'ayzbc', 'ayzbc', 'ayzpyddtb', 'azbaupaau', 'azycytu', 'azycytu', 'azyzx', 'b', 'b', 'b', 'b', 'b', 'ba', 'baduz', 'baxxxtyp', 'baxxxtyp', 'bbu', 'bbu', 'bbu', 'bbyyutbb', 'bca', 'bcbdaat', 'bcc', 'bcc', 'bccucd', 'bcdbbbd', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbxpxta', 'bctbypp', 'bctbypp', 'bcu', 'bdcxxx', 'bdxp', 'bdzzzux', 'bpbpt', 'bpxtzb', 'btaudba', 'btayadcdudb', 'btd', 'btxbux', 'btzapcdzb', 'buabb', 'buabb', 'bucyp', 'bx', 'bx', 'bxbyzxxt', 'bxdbcuzy', 'bxxbpctc', 'bxyxauuza', 'bybu', 'bz', 'bzxp', 'bzxp', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'ca', 'cauy', 'cayp', 'caypdu', 'cb', 'cbbucbdzb', 'cbtu', 'cbybyzba', 'ccxuppu', 'ccybtxx', 'cdacx', 'cdcbxayat', 'cdzbyuzcc', 'cdzzxzp', 'cdzzxzp', 'cpapxztax', 'cpdxau', 'cpdxau', 'cpdxau', 'cpx', 'cpzy', 'ctua', 'ctyu', 'cubyud', 'cut', 'cx', 'cxayczy', 'cxp', 'cxpuy', 'czcbztut', 'czpzt', 'czt', 'czt', 'czzuzbc', 'd', 'd', 'dab', 'dab', 'dab', 'dab', 'dab', 'dayudcbctbxpxta', 'dbazyb', 'dbcpx', 'dbuc', 'dc', 'dddzadc', 'ddz', 'ddz', 'ddztxp', 'ddzztpaba', 'dp', 'dp', 'dp', 'dpbpy', 'dpux', 'dpxx', 'dtba', 'dtcbtubyy', 'dtp', 'dtpaadxxxt', 'dtuby', 'du', 'dudtyz', 'duzuzyxp', 'dx', 'dx', 'dx', 'dxdxu', 'dxdxu', 'dxxt', 'dxxycbyx', 'dxzz', 'dxzz', 'dybtd', 'dybyybtda', 'dybyybtda', 'dyc', 'dyc', 'dyc', 'dypxab', 'dyt', 'dzazbzpxu', 'dzpatttu', 'dzpatttu', 'dzpatttu', 'dzpptapa', 'dzpptapa', 'p', 'p', 'paaa', 'paabtu', 'paabtu', 'pat', 'pat', 'patabaud', 'pauuc', 'pbzxpyzp', 'pcypct', 'pdpcz', 'ppbxt', 'ppttztu', 'ptb', 'ptcdud', 'ptzpttyy', 'pubydzxbc', 'putdz', 'puuba', 'puz', 'px', 'pxzcuuyt', 'pyppbatua', 'pzzc', 't', 't', 't', 't', 'tbxbzp', 'tcb', 'tcb', 'tctbypuad', 'tcx', 'tczp', 'tdpczuy', 'tdtca', 'tp', 'tp', 'tp', 'tp', 'tpzaut', 'tt', 'tt', 'tt', 'ttdzubu', 'ttupuc', 'ttytacbxt', 'tudbzzabz', 'tudz', 'tudz', 'tuxdcx', 'tuzpx', 'txduu', 'txpxucdtz', 'txpxucdtzcx', 'txyzuduzz', 'tydxxpy', 'tydxxpy', 'typtdxzbx', 'tytzbbdca', 'tyxtyyuducctpd', 'tyxx', 'tyzz', 'tz', 'tz', 'tzap', 'tzcaayazd', 'tzcattdac', 'tzpytdxt', 'tzuptaa', 'u', 'u', 'u', 'u', 'u', 'u', 'uatub', 'ub', 'ubpbtyppx', 'ubpbtyppx', 'ubpbtyppx', 'ubpbtyppx', 'ubpbtyppx', 'ubpbtyppx', 'ubpxtuuy', 'ubuad', 'ucbbtydp', 'ucbubpx', 'ucd', 'ucd', 'ucdz', 'uctz', 'ucx', 'ud', 'ud', 'ud', 'udb', 'uducctpd', 'uducctpd', 'uducctpd', 'uducctpd', 'uducctpd', 'uducctpd', 'uducctpd', 'up', 'upau', 'utaydtp', 'utaydtp', 'utaydtp', 'utcua', 'utcudbua', 'utcudbua', 'uttazpca', 'uty', 'uxtxupdu', 'uy', 'uy', 'uy', 'uy', 'uy', 'uy', 'uy', 'uy', 'uya', 'uybazuxd', 'uybza', 'uybza', 'uypytyayt', 'uypytyayt', 'uypytyayt', 'uypytyayt', 'uypytyayt', 'uypytyayt', 'uyt', 'uyt', 'uyt', 'uytytzbbdca', 'uz', 'uz', 'uz', 'uzbyupxp', 'uzbyupxp', 'uzxat', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'xadd', 'xbbzyzt', 'xbp', 'xbuzxay', 'xbuzxay', 'xc', 'xc', 'xcaztb', 'xcaztb', 'xd', 'xdcxptdxb', 'xdcxxtdtu', 'xdcxxtdtu', 'xdpay', 'xdpay', 'xdpaydtzy', 'xdtud', 'xdxxt', 'xdxxt', 'xpc', 'xt', 'xtdu', 'xu', 'xupxua', 'xutbxttuc', 'xutuu', 'xuzpztayutcctaz', 'xxcac', 'xy', 'xyaudczyz', 'xypbbxd', 'xypubapdd', 'xypubapdd', 'xyya', 'xyzztp', 'xzatycxzb', 'xzbyxu', 'xztx', 'xzuyccbux', 'y', 'y', 'y', 'yaappub', 'yacdza', 'yacyxdyuc', 'yatcx', 'yauu', 'yauux', 'yazxyb', 'yb', 'ycacpzudtxuccy', 'ycbdbdacc', 'ycbdbdacc', 'yd', 'ydaubupuc', 'ydcxucab', 'yddtdapu', 'yddyap', 'ydtdyubdd', 'ydzb', 'ypca', 'ypca', 'ypca', 'ypca', 'ypcauptdy', 'ypdxpdd', 'yppbdbuxy', 'yppbdbuxy', 'ypxuzd', 'ypxx', 'ytcdyxzdu', 'ytttpt', 'yu', 'yuba', 'yucbazuzxdyud', 'yupd', 'yuzuc', 'yxbtcz', 'yxt', 'yxt', 'yxt', 'yxxtzxtz', 'yxxtzxtz', 'yyctzbxa', 'yypc', 'yypc', 'yypc', 'yypc', 'yyuaxutx', 'yyx', 'yzd', 'z', 'z', 'zatdcupb', 'zbaup', 'zbaxxdpcy', 'zbaxxdpcy', 'zbaxxdpcy', 'zbbdub', 'zbpy', 'zbuauu', 'zcb', 'zcppy', 'zd', 'zddpczx', 'zdtd', 'zdtpaztut', 'zdupdx', 'zdupdx', 'zdupdx', 'zdupdx', 'zpxz', 'ztbytxcza', 'ztduybpu', 'ztduybpu', 'zttypbyyb', 'ztua', 'zu', 'zua', 'zubud', 'zuc', 'zudtxuccy', 'zxcud', 'zxcud', 'zxd', 'zxztzy', 'zy', 'zydtbc', 'zz', 'zzcc', 'zzcc', 'zzcc', 'zzcc', 'zzccxdpay', 'zzctzuc', 'zztdu']
    


```python
def key_assign(words, lib):
    unique = list(set(words))
    for i in unique:
        lib[i] = 1
```


```python
def counter(words, lib): 
    i = 0
    if len(words) > 1:
        for j in words:
            if words[i] == words[i+1]:
                lib[words[i]] +=1
            i+=1
            if len(words) - 1 == i:
                break 
```


```python
key_assign(words, lib)
counter(words, lib)
sorted_tuple = dict(reversed(sorted(lib.items(), key=lambda x: (x[1]))))
print(sorted_tuple)

```

    {'c': 19, 'x': 13, 'bctbxpxta': 10, 'ayutcctaz': 9, 'uy': 8, 'uducctpd': 7, 'ubpbtyppx': 6, 'u': 6, 'a': 6, 'uypytyayt': 6, 'dab': 5, 'aatbzc': 5, 'b': 5, 'zzcc': 4, 'ypca': 4, 'zdupdx': 4, 'tp': 4, 'yypc': 4, 't': 4, 'apux': 4, 'axtabcyya': 3, 'dzpatttu': 3, 'dx': 3, 'yxt': 3, 'utaydtp': 3, 'apapdbxtt': 3, 'atpxpdacu': 3, 'auxy': 3, 'dyc': 3, 'ud': 3, 'zbaxxdpcy': 3, 'uz': 3, 'atady': 3, 'at': 3, 'bbu': 3, 'cpdxau': 3, 'dp': 3, 'autztuy': 3, 'uyt': 3, 'aydcudxap': 3, 'tt': 3, 'y': 3, 'ayyczyu': 2, 'xdxxt': 2, 'adt': 2, 'xcaztb': 2, 'xbuzxay': 2, 'xypubapdd': 2, 'cdzzxzp': 2, 'xc': 2, 'bzxp': 2, 'xdcxxtdtu': 2, 'ztduybpu': 2, 'pat': 2, 'utcudbua': 2, 'bcc': 2, 'yxxtzxtz': 2, 'uybza': 2, 'tudz': 2, 'z': 2, 'ucd': 2, 'buabb': 2, 'xdpay': 2, 'p': 2, 'ddz': 2, 'ayzbc': 2, 'uzbyupxp': 2, 'tz': 2, 'ycbdbdacc': 2, 'dybyybtda': 2, 'czt': 2, 'dxdxu': 2, 'tydxxpy': 2, 'au': 2, 'zxcud': 2, 'dzpptapa': 2, 'dxzz': 2, 'baxxxtyp': 2, 'paabtu': 2, 'yppbdbuxy': 2, 'azycytu': 2, 'tcb': 2, 'bctbypp': 2, 'bx': 2, 'd': 2, 'ad': 1, 'xdcxptdxb': 1, 'zz': 1, 'bcbdaat': 1, 'pcypct': 1, 'ydaubupuc': 1, 'btayadcdudb': 1, 'aauzctta': 1, 'adbz': 1, 'xztx': 1, 'ztbytxcza': 1, 'dc': 1, 'ccxuppu': 1, 'ttdzubu': 1, 'dbuc': 1, 'zua': 1, 'ydcxucab': 1, 'bxbyzxxt': 1, 'yauux': 1, 'dbcpx': 1, 'xutuu': 1, 'dtuby': 1, 'ddztxp': 1, 'xyaudczyz': 1, 'uxtxupdu': 1, 'tdpczuy': 1, 'xtdu': 1, 'aabyczzd': 1, 'zu': 1, 'zudtxuccy': 1, 'axxbpy': 1, 'tyxx': 1, 'uytytzbbdca': 1, 'yzd': 1, 'bz': 1, 'tbxbzp': 1, 'utcua': 1, 'zbpy': 1, 'cxp': 1, 'patabaud': 1, 'upau': 1, 'acup': 1, 'acaaxuy': 1, 'puuba': 1, 'tdtca': 1, 'apxdpcx': 1, 'ucx': 1, 'yddyap': 1, 'yuzuc': 1, 'pxzcuuyt': 1, 'ptb': 1, 'bcu': 1, 'pzzc': 1, 'zdtpaztut': 1, 'yatcx': 1, 'dtba': 1, 'yucbazuzxdyud': 1, 'tzcattdac': 1, 'dpux': 1, 'uatub': 1, 'dpxx': 1, 'ytcdyxzdu': 1, 'pyppbatua': 1, 'xyzztp': 1, 'txduu': 1, 'ubpxtuuy': 1, 'aapbbddbxtdxxdxzp': 1, 'yauu': 1, 'zd': 1, 'xy': 1, 'uybazuxd': 1, 'cbbucbdzb': 1, 'xzuyccbux': 1, 'axbbtutzu': 1, 'yaappub': 1, 'yacdza': 1, 'txpxucdtz': 1, 'tzap': 1, 'atbb': 1, 'xuzpztayutcctaz': 1, 'tudbzzabz': 1, 'xypbbxd': 1, 'bpbpt': 1, 'yxbtcz': 1, 'bca': 1, 'xt': 1, 'cbybyzba': 1, 'btzapcdzb': 1, 'zxztzy': 1, 'ptcdud': 1, 'udb': 1, 'uzxat': 1, 'bdxp': 1, 'bpxtzb': 1, 'ac': 1, 'baduz': 1, 'xadd': 1, 'xd': 1, 'yyctzbxa': 1, 'xzatycxzb': 1, 'yyuaxutx': 1, 'ttupuc': 1, 'uttazpca': 1, 'ptzpttyy': 1, 'abupuadxt': 1, 'ucbbtydp': 1, 'zztdu': 1, 'ydtdyubdd': 1, 'atdtb': 1, 'apuxtdb': 1, 'zubud': 1, 'yb': 1, 'paaa': 1, 'aadtuda': 1, 'pbzxpyzp': 1, 'zbbdub': 1, 'bbyyutbb': 1, 'aayutdtuu': 1, 'ucdz': 1, 'xpc': 1, 'ypdxpdd': 1, 'xutbxttuc': 1, 'zcppy': 1, 'tzcaayazd': 1, 'dpbpy': 1, 'dtcbtubyy': 1, 'ypcauptdy': 1, 'xzbyxu': 1, 'btd': 1, 'ba': 1, 'xdpaydtzy': 1, 'typtdxzbx': 1, 'ub': 1, 'ayzpyddtb': 1, 'ydzb': 1, 'ytttpt': 1, 'tctbypuad': 1, 'tzuptaa': 1, 'cauy': 1, 'up': 1, 'cpx': 1, 'bdzzzux': 1, 'dypxab': 1, 'tuxdcx': 1, 'tytzbbdca': 1, 'yyx': 1, 'ayyctyct': 1, 'abddzycbx': 1, 'du': 1, 'ccybtxx': 1, 'cut': 1, 'txyzuduzz': 1, 'zy': 1, 'ca': 1, 'ttytacbxt': 1, 'pubydzxbc': 1, 'caypdu': 1, 'cubyud': 1, 'ypxuzd': 1, 'zdtd': 1, 'bxdbcuzy': 1, 'dxxt': 1, 'tcx': 1, 'cxpuy': 1, 'pdpcz': 1, 'bybu': 1, 'dbazyb': 1, 'bcdbbbd': 1, 'zpxz': 1, 'aapbbddbx': 1, 'tpzaut': 1, 'azyzx': 1, 'yupd': 1, 'zbuauu': 1, 'btxbux': 1, 'ycacpzudtxuccy': 1, 'bucyp': 1, 'yazxyb': 1, 'tyzz': 1, 'cdcbxayat': 1, 'zzccxdpay': 1, 'dxxycbyx': 1, 'tuzpx': 1, 'yacyxdyuc': 1, 'ppttztu': 1, 'xu': 1, 'pauuc': 1, 'zxd': 1, 'czcbztut': 1, 'audza': 1, 'abp': 1, 'ubuad': 1, 'zcb': 1, 'attdyyuyx': 1, 'zuc': 1, 'putdz': 1, 'zzctzuc': 1, 'cdzbyuzcc': 1, 'zttypbyyb': 1, 'addbuppax': 1, 'ypxx': 1, 'adttttba': 1, 'dudtyz': 1, 'aaczuxy': 1, 'ctua': 1, 'axbdazd': 1, 'cxayczy': 1, 'uctz': 1, 'ucbubpx': 1, 'ddzztpaba': 1, 'tzpytdxt': 1, 'ztua': 1, 'cb': 1, 'bxxbpctc': 1, 'dddzadc': 1, 'zydtbc': 1, 'atytc': 1, 'uty': 1, 'cayp': 1, 'cpapxztax': 1, 'yd': 1, 'czpzt': 1, 'yu': 1, 'txpxucdtzcx': 1, 'xdtud': 1, 'dtpaadxxxt': 1, 'cdacx': 1, 'xyya': 1, 'xupxua': 1, 'btaudba': 1, 'zbaup': 1, 'xbp': 1, 'uya': 1, 'duzuzyxp': 1, 'dtp': 1, 'bdcxxx': 1, 'xxcac': 1, 'ppbxt': 1, 'aybpyxtay': 1, 'adxpuddtu': 1, 'czzuzbc': 1, 'cx': 1, 'px': 1, 'ctyu': 1, 'xbbzyzt': 1, 'cpzy': 1, 'apd': 1, 'tczp': 1, 'bccucd': 1, 'azbaupaau': 1, 'dzazbzpxu': 1, 'cbtu': 1, 'zddpczx': 1, 'yddtdapu': 1, 'dayudcbctbxpxta': 1, 'yuba': 1, 'bxyxauuza': 1, 'tyxtyyuducctpd': 1, 'dyt': 1, 'puz': 1, 'zatdcupb': 1, 'dybtd': 1}
    


```python
max_val = max(sorted_tuple.values())
kk = ''
for key, value in sorted_tuple.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
    if value == max_val:
        kk += str(key) + str(' ')
kk = kk.split()
kk.sort()
print(kk[0], max_val)
```


```python
with open('out.txt', 'w') as f:
    print('Filename:', file=f)  # Python 3.x

import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
print(kk[0], max_val)
sys.stdout = orig_stdout
f.close()

```


```python

```
