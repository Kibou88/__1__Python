
from formate_extract_datas.test.test_dico_user import add_seance


class Formate_datas():

    def __init__(self, dico_user):
        self.dico_user = dico_user

    def formate_date(self):
        """
        Fonctionne
        si d/m/yy ==> dd/mm/yyyy
        :return:
        """
        self.valid_date = self.dico_user['date']
        print(len(self.valid_date))
        if not (self.valid_date.count('/') == 2):
            print("Date invalide")
        elif not (len(self.valid_date) == 10):
            self.valid_date = self.valid_date.split('/')
            for i in range(len(self.valid_date)):
                if len(self.valid_date[i]) == 1:
                    self.valid_date[i] = '0' + self.valid_date[i]
                if (len(self.valid_date[i]) == 2) and i == 2:
                    self.valid_date[i] = '20' + self.valid_date[i]
            self.valid_date = "/".join(self.valid_date)
        print(self.valid_date)


if __name__ == '__main__':
    date_seance = add_seance["date"] # Affiche la date
    exercice1 = add_seance["exercices"][0] # Affiche tout les renseignements du 1er exercice
    exercice2 = add_seance["exercices"][1]
    # print(exercice1)
    # print(exercice2)
    test = Formate_datas(add_seance)
    test.formate_date()