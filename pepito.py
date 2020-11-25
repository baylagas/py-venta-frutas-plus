from dx_logic import Logic


class PepitoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "product"

    def getAllPepitos(self):
        listaPepitos = super().getAllRows(self.tableName)
        print(listaPepitos)

    def deleteRowById(self, id):
        super().deleteRowById(id, self.tableName)
