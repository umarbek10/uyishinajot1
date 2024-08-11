class Kitob:
    def __init__(self, nomi, mualliflari, narxi, nashriyoti):
        self.nomi = nomi
        self.mualliflari = mualliflari
        self.narxi = narxi
        self.nashriyoti = nashriyoti
    
    def info(self):
        return f"Kitob nomi: {self.nomi}, Mualliflari: {', '.join(self.mualliflari)}, Narxi: {self.narxi}, Nashriyoti: {self.nashriyoti}"

def filter_books_by_publisher(books):
    filtered_books = [book for book in books if 'A' <= book.nashriyoti[0] <= 'H']
    return filtered_books

kitob1 = Kitob("Kitob A", ["Muallif 1", "Muallif 2"], 50000, "Barcha Nashriyot")
kitob2 = Kitob("Kitob B", ["Muallif 3"], 75000, "Zamonaviy Nashriyot")
kitob3 = Kitob("Kitob C", ["Muallif 4"], 60000, "Guliston Nashriyot")
kitob4 = Kitob("Kitob D", ["Muallif 5"], 45000, "Hamsa Nashriyot")

kitoblar = [kitob1, kitob2, kitob3, kitob4]


filtered_kitoblar = filter_books_by_publisher(kitoblar)


for kitob in filtered_kitoblar:
    print(kitob.info())
