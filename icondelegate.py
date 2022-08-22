from PyQt5 import QtWidgets

def maxpid(self,result,alt):
    result = str(result[0])
    print("result from maxpid redit",result)
    if result == None or result == 'None':
        result = alt
    pres = result[1:]
    result = int(pres)
    result = result+1
    result = str(result)
    return result

def maxpidint(self,result):
    result = str(result[0])
    print("result from maxpid redit",result)
    if result == None or result == 'None':
        result = 0
    result = int(result) + 1
    return str(result)
    pres = result[1:]
    result = int(pres)
    result = result+1
    result = str(result)
    return result

class IconDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(IconDelegate, self).initStyleOption(option, index)
        if option.features & QtWidgets.QStyleOptionViewItem.HasDecoration:
            s = option.decorationSize
            s.setWidth(option.rect.width())
            option.decorationSize = s