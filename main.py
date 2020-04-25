from BookList import BookList
from dotenv import load_dotenv
import os


class Main:
    def __init__(self):
        load_dotenv()
        key = os.getenv('KEY')
        self.list = BookList(key)
        self.cmds = {
            'help': self.help,
            'list': self.view,
            'search': self.search,
            'add': self.add,
            'exit': self.exit,
            'save': self.list.save,
        }

    @staticmethod
    def help():
        print('Welcome to the Reading List helper!\n'
              'Available commands:\n'
              '\thelp\tview this help dialogue\n'
              '\tlist\tview the current reading list\n'
              '\tsearch\tsearch for a book\n'
              '\tadd\tadd a book to the reading list\n'
              '\tsave\tsave your list for later\n\n')
        return False

    @staticmethod
    def get_cmd():
        print('Welcome to the reading list! Try "help" for options!\n')
        return input('> ')

    @staticmethod
    def exit():
        print('Good bye!\n\n')
        return True

    def view(self):
        print(self.list.view(), '\n\n')

    def search(self):
        query = input('What do you want to search for?\n> ')
        self.list.gather(query)
        print(self.list.display_search_results(), '\n\n')
        return False

    def add(self):
        index = int(input('Which did you want to add? [0-4]\n> '))
        self.list.add(index)
        print('Done!')
        return False

    def main(self):
        done = false
        while not done:
            try:
                done = self.cmds[self.get_cmd()]()
            except keyerror:
                print("i didn't recognize that, please try again!\n\n")


if __name__ == '__main__':
    prog = Main()
    prog.main()
