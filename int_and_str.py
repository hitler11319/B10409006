def deal_strandint(a): 
    number=[str(i) for i in range(0,10)] #判斷是否為數字字元（用字串分別來看）
    rr=["+","-",".","$"] #有些人會將這些打入金額中
    number+=rr
    for letter in a :
        if  not letter  in number: #有沒有在數字字串number中
            return False #回傳d為false，如沒有d自已為跑到else去
            break
#其實也可以用try和except來處理，只要在try項下打上int(變數)，是的話就執行，不是就用例外


#這是用來改變字串中特定一項的內容，text為字串,bagin為起始值,end為結束值,change_str為改變的值
def changestr(text, bagin, end, change_str):
    text = text[:bagin] + change_str + text[end+1:]
    return text


#這是把一個串列中的所有字串相加
def strsum(sum_list):
    test = ""
    for item in sum_list:
        test += item

    return test


#這是尋找字串的東西，因為re有點難用（begin_str是起始字元，end_str是結束用元, text是傳進來的用串）
def search(begin_str, end_str, text):
    str_list = []
    text = text.replace(begin_str, '** +++', 1000).replace(end_str, '+++** ', 1000).split('** ')

    for item in text:
        if item[0:3] == '+++' and item[len(item)-3:len(item)] == '+++':
            str_list.append(item[3:len(item)-3])

    return str_list
