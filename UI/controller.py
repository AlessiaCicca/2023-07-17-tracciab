import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        brand = self._view.dd_brand.value
        if brand is None:
            self._view.create_alert("Selezionare un brand")
            return
        anno = self._view.dd_anno.value
        if anno is None:
            self._view.create_alert("Selezionare un Anno")
            return

        grafo = self._model.creaGrafo(brand, int(anno))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        prodottipresenti,lista=self._model.analisi()

        self._view.txt_result.controls.append(ft.Text("Top 3 archi"))
        for (p1,p2,peso) in lista:
         self._view.txt_result.controls.append(ft.Text(f"Arco da {p1.Product_number} a {p2.Product_number}, peso= {peso}"))
        self._view.txt_result.controls.append(ft.Text("Nodi che compaiono almeno due volte"))
        for prodotto in prodottipresenti:
         self._view.txt_result.controls.append(ft.Text(f"Product ID:{prodotto.Product_number}"))
        self._view.update_page()
    def fillDD(self):
        ann="201"
        for i in range(5,9):
            anno=ann+str(i)
            self._view.dd_anno.options.append(ft.dropdown.Option(
                               text=anno))
        brand=self._model.getBrand
        for b in brand:
            self._view.dd_brand.options.append(ft.dropdown.Option(
                text=b))
