#Цель работы: На данной практической работе необходимо использовать датасет с прошлой практической работы и визуализировать данные в виде графиков.

import matplotlib.pyplot as plt
import pandas as pd

starwars = pd.read_csv("star_wars_character_dataset.csv")
print(starwars)

# Для начала был создан линейный график с выводом массы.

#plt.plot(starwars.index[:20], starwars["mass"].head(20), color="pink", label="Продолжительность")
#plt.xlabel('Фильм')
#plt.ylabel("Продолжительность")
#plt.title('Продолжительность фильмов Звездных Войн')
#plt.grid()
#plt.show()


#Затем был создан линейный график с ростом персонажей star wars.

#plt.plot(starwars.index[:20], starwars["height"].head(20), color="blue", label="Рост")
#plt.xlabel ('Index')
#plt.ylabel("Рост персонажа")
#plt.title('Рост')
#plt.grid()
#plt.show()


#После чего был создан линейный график который показывает, сколько существует цвет глаз и количество.

#plt.plot(starwars.index[:20], starwars["eye_color"].head(20), color="purple", label="Тип")
#plt.xlabel ('Index')
#plt.ylabel("Цвета глаз")
#plt.title('Тип глаз ')
#plt.grid()
#plt.show()

#Далее был создан столбчатый график который показывает, Гендер персонажей.

#plt.bar(starwars.index[:20], starwars["sex"].head(20), color="black", label="пол")
#plt.xlabel('Index')
#plt.ylabel('Виды полов')
#plt.title('Пол')
#plt.legend()
#plt.show()

#Затем был создан столбчатый график, показывающий Пол.

#plt.bar(starwars.index[:20], starwars["gender"].head(20), color="green", label="Гендер")
#plt.xlabel('Index')
#plt.ylabel('Гендеры')
#plt.title('Гендер')
#plt.legend()
#plt.show()

#После чего, был создан столбчатый график, показывающий вид персонажей.

#plt.bar(starwars.index[:20], starwars["species"].head(20), color="yellow", label="Виды персонажей")
#plt.xlabel('Index')
#plt.ylabel('Вид')
#plt.title('Виды персонажей')
#plt.legend()
#plt.show()

#Затем была создана диаграмма, которая показывает страны откуда они родом.

# data = starwars["homeworld"].value_counts().head()
# plt.pie(data, labels = data.index, colors = ["blue", "red"],autopct="%1.1f%%")
# plt.legend()
# plt.show()

#Далее была создана круговая диаграмма, указывающая транспортные средства персонажей.

#data = starwars["vehicles"].value_counts().head()
#plt.pie(data, labels = data.index, colors = ["blue", "red"],autopct="%1.1f%%")
#plt.legend()
#plt.show()

#После чего, был создан график рассеивания, который показывает, день рождения персонажей star wars и рост.

#plt.scatter(starwars["birth_year"].head(20), starwars["height"].head(20))
#plt.show()

#Потом был создан график рассеивания, который показывает массу или возраст.

#plt.scatter(starwars["mass"].tail(20), starwars["birth_year"].tail(20))
#plt.show()

#Была представлена гистограмма, показывающая цвет глаз.

#plt.hist(starwars["eye_color"].head(20), bins=30, edgecolor="black")
#plt.xlabel('Цвет')
#plt.ylabel('Количество')
#plt.title('Цвета глаз')
#plt.legend()
#plt.show()

#Была представлена гистограмма, показывающая массу персонажей.

#plt.hist(starwars["mass"].head(20), bins=30, edgecolor="black")
#plt.xlabel('Масса')
#plt.ylabel('Количество')
#plt.title('Вес персонажей')
#plt.legend()
#plt.show()

#Была представлена гистограмма, показывающая какеи есть цвета кожи персонажей.


#plt.hist(starwars["skin_color"].head(20), bins=30, edgecolor="black")
#plt.xlabel('Цвет кожи')
#plt.ylabel('Количество')
#plt.title('Цвета кож')
#plt.legend()
#plt.show()


#Вывод: В данной практической работе использована датасет с прошлой практической работы и выполнина визуализированние данных в виде графиков.
