class Book:
    """书籍类，包含书名、作者、ISBN等属性，以及可借状态"""
    def __init__(self, book_name, author, isbn):
        self.book_name = book_name  # 书名
        self.author = author        # 作者
        self.isbn = isbn            # ISBN编号
        self.is_borrowed = False    # 借阅状态，默认未借出

    def __str__(self):
        """返回书籍的字符串描述"""
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"《{self.book_name}》- {self.author} (ISBN:{self.isbn}) - {status}"


class User:
    """用户类，包含姓名、借书卡号，以及已借书籍列表"""
    def __init__(self, name, card_id):
        self.name = name        # 姓名
        self.card_id = card_id  # 借书卡号
        self.borrowed_books = []  # 已借书籍列表

    def __str__(self):
        """返回用户的字符串描述"""
        borrowed_book_names = [book.book_name for book in self.borrowed_books]
        books_str = "、".join(borrowed_book_names) if borrowed_book_names else "无"
        return f"用户：{self.name} (借书卡：{self.card_id})，已借书籍：{books_str}"


class LibrarySystem:
    """图书馆系统类，实现借书、还书、查询书籍状态的功能"""
    def __init__(self):
        self.books = []  # 图书馆藏书列表
        self.users = []  # 图书馆注册用户列表

    def add_book(self, book):
        """添加书籍到图书馆"""
        self.books.append(book)
        print(f"书籍《{book.book_name}》已加入图书馆！")

    def add_user(self, user):
        """添加用户到图书馆"""
        self.users.append(user)
        print(f"用户{user.name}（卡号：{user.card_id}）已注册！")

    def check_book_available(self, isbn):
        """根据ISBN查询书籍是否可借，返回书籍对象或None"""
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print(f"书籍《{book.book_name}》当前已借出，不可借阅！")
                else:
                    print(f"书籍《{book.book_name}》可借阅！")
                return book
        print("未找到该ISBN对应的书籍！")
        return None

    def borrow_book(self, user_card_id, book_isbn):
        """用户借书功能"""
        # 查找用户
        user = None
        for u in self.users:
            if u.card_id == user_card_id:
                user = u
                break
        if not user:
            print("未找到该借书卡对应的用户！")
            return

        # 查找书籍并判断是否可借
        book = self.check_book_available(book_isbn)
        if not book or book.is_borrowed:
            return

        # 执行借书操作
        book.is_borrowed = True
        user.borrowed_books.append(book)
        print(f"{user.name}成功借阅《{book.book_name}》！")

    def return_book(self, user_card_id, book_isbn):
        """用户还书功能"""
        # 查找用户
        user = None
        for u in self.users:
            if u.card_id == user_card_id:
                user = u
                break
        if not user:
            print("未找到该借书卡对应的用户！")
            return

        # 查找用户已借的该书籍
        target_book = None
        for book in user.borrowed_books:
            if book.isbn == book_isbn:
                target_book = book
                break
        if not target_book:
            print(f"{user.name}未借阅该ISBN对应的书籍！")
            return

        # 执行还书操作
        target_book.is_borrowed = False
        user.borrowed_books.remove(target_book)
        print(f"{user.name}成功归还《{target_book.book_name}》！")


# 测试图书馆系统
if __name__ == "__main__":
    # 初始化图书馆系统
    lib = LibrarySystem()

    # 添加书籍
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787115546926")
    book3 = Book("深入理解计算机系统", "兰德尔·E·布莱恩特", "9787111641247")
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)

    # 添加用户
    user1 = User("张三", "C001")
    user2 = User("李四", "C002")
    lib.add_user(user1)
    lib.add_user(user2)

    print("\n----- 查询书籍可借状态 -----")
    lib.check_book_available("9787115428028")

    print("\n----- 张三借阅Python编程书籍 -----")
    lib.borrow_book("C001", "9787115428028")

    print("\n----- 再次查询Python编程书籍状态 -----")
    lib.check_book_available("9787115428028")

    print("\n----- 张三归还Python编程书籍 -----")
    lib.return_book("C001", "9787115428028")

    print("\n----- 最终用户信息 -----")
    print(user1)
    print(user2)
