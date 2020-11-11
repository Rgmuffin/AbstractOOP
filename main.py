from Cat import Cat
from Dog import Dog
# Кошки едят только молоко, а собаки только мясо
# Реализовал 2 абстрактных метода и два обычных. 
#Есть вариант, где реализовал абстрактными все методы 

cat = Cat()
cat.set_size("small") 
cat.get_size()
cat.feed("milk") 
cat.need_to_feed()

dog = Dog()
dog.set_size("Big")
dog.get_size()
dog.feed("milk") 
dog.need_to_feed()
