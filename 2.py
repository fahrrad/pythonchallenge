from_a = 'abcdefghijklmnopqrstuvwxyz'
to_a ='cdefghijklmnopqrstuvwxyzab'

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

d = str.maketrans(from_a, to_a)
print (str.translate(s,d))
print (str.translate('map', d))