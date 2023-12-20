# Class Note, Notebook
# Class Note


class Note(object):
    ## variable
    # content
    def __init__(self, content=None):
        self.content = content

    ## method
    # write content
    def write_content(self, content):
        self.content = content
    # remove all
    def remove_all(self):
        self.content = ""
    # note를 하나로 합친다.     
    def __add__(self, other):
        return self.content + other.content
    
    def __str__(self):
        return "노트에 적힌 내용입니다."+self.content
         
class Notebook():
    ## variable
    # title
    # page_number
    # notes
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}
    
    ## method
    # add note
    def add_note(self, note, page=0):
        if self.page_number < 300 :
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
                # print(self.notes)
            else : # 2번째 페이지 삽입 실행 시 초기화가되는데..(page_number 1)
                # self.notes = {page : note}  --이렇게 사용하면 실행 시 마다 초기화가 되버림. 디버깅 완료
                self.notes[page] = note
                self.page_number += 1
                # print(self.notes)
        else : 
            print("Page가 모두 채워졌습니다.")

    # remove note
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당페이지는 존재하지 않습니다.")
    # get number of note
    def get_number_of_note(self):
        return len(self.notes.keys())
    