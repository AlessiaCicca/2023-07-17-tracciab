import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getBrand=DAO.getBrand()
        self.grafo = nx.Graph()
        self._idMap={}

    def creaGrafo(self, brand,anno):
        self.nodi = DAO.getNodi(brand)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges(anno)
        for v in self.nodi:
            self._idMap[v.Product_number] = v
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, anno):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                   peso=DAO.getPeso(anno,nodo1.Product_number, nodo2.Product_number)
                   if peso>0:
                        self.grafo.add_edge(nodo1, nodo2, weight=peso)


    def analisi(self):
        lista=[]
        for arco in self.grafo.edges:
            lista.append((arco[0],arco[1],self.grafo[arco[0]][arco[1]]["weight"]))
        listaOrdinata=sorted(lista, key=lambda x:x[2],reverse=True)
        listaOrdinata=listaOrdinata[:3]
        prodottiPresenti=set()
        prodottiDaStampare=set()
        for (p1,p2,peso) in listaOrdinata:
            if p1 in prodottiPresenti:
                prodottiDaStampare.add(p1)
            else:
                prodottiPresenti.add(p1)
            if p2 in prodottiPresenti:
                prodottiDaStampare.add(p2)
            else:
                prodottiPresenti.add(p2)
        return prodottiDaStampare,listaOrdinata
