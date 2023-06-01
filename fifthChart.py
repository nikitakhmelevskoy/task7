import matplotlib.pyplot as plt


def create_fifth_chart(df):
    male = df[df['Пол'] == 'мужской']
    female = df[df['Пол'] == 'женский']
    married_men = male[male['Состоит в браке'] == 'Да'].count()['Состоит в браке']
    married_women = female[female['Состоит в браке'] == 'Да'].count()['Состоит в браке']
    percent_married_men = married_men / len(male) * 100
    percent_married_women = married_women / len(female) * 100
    labels = ['Мужчины', 'Женщины']
    sizes = [percent_married_men, percent_married_women]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Состоят ли в браке')
    plt.show()


def create_sixth_chart(df):
    male = df[df['Пол'] == 'мужской']
    female = df[df['Пол'] == 'женский']
    mean_male = male['Срок проживания'].mean()
    mean_female = female['Срок проживания'].mean()
    labels = ['Мужчины', 'Женщины']
    means = [mean_male, mean_female]

    plt.bar(labels, means)
    plt.xlabel('Пол')
    plt.ylabel('Средний срок проживания')
    plt.title('Средний срок проживания для мужчин и женщин')
    plt.show()


def create_seventh_chart(df):
    male = df[df['Пол'] == 'мужской']
    female = df[df['Пол'] == 'женский']
    bullying_male = male['Иждивенцы'].sum()
    bullying_female = female['Иждивенцы'].sum()
    labels = ['Мужчины', 'Женщины']
    bullying = [bullying_male, bullying_female]

    plt.bar(labels, bullying)
    plt.xlabel('Пол')
    plt.ylabel('Количество иждивенцов')
    plt.title('Соотношение иждивенцов')
    plt.show()
